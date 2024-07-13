

word_index=imdb.get_word_index()
reverse_word_index={value: key for key, value in word_index.items()}

model = load_model('simple_rnn_imdb.h5')

def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3,'?') for i in encoded_review])

def preprocessor_text(text):
    words=text.lower().split()
    encoded_review= [word_index.get(word, 2) + 3 for word in words]
    padded_review =sequence.pad_sequences([encoded_review],maxlen=500)
    return padded_review   


## designing streamlit 
import streamlit as st
st.title('Review Analysis System')
st.write('Enter a movie review to classify it as positive or negative')

user_input= st.text_area('Movie Reviews')

if st.button('Classify'):

    preprocessed_input=preprocessor_text(user_input)

    prediction=model.predict(preprocessed_input)
    sentiment= "positive" if prediction[0][0]>0.5 else "Negative"


    st.write(f"Sentiment: {sentiment}")
    st.write(f"Prediction Score: {prediction[0][0]}")
else:
    st.write("Please Enter a Movie Review")


