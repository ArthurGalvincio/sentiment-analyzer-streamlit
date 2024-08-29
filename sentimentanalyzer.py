import streamlit as st
from pysentimiento import create_analyzer

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def analyze_sentiment(user_input):
    sentiment_analyzer = create_analyzer(task="sentiment", lang="pt")
    result = sentiment_analyzer.predict(user_input)
    label = result.output.capitalize()
    score = result.probas[result.output]
    
    return label, score

def main():
    st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

    load_css('dark_theme.css')

    st.title("Sentiment Analyzer")
    st.write("Enter the text below to analyze the sentiment.")

    user_input = st.text_area("Text for analysis:", "")

    # When the user clicks the "Analyze Sentiment" button
    if st.button("Analyze Sentiment"):
        if user_input:
            # Perform sentiment analysis
            label, score = analyze_sentiment(user_input)
            
            # Display the result in the interface
            st.success("Analysis completed!")
            st.subheader("Analysis Result:")
            st.write(f"Sentiment: **{label}**")
            st.write(f"Confidence: **{score:.2f}**")
            
            # Visualize the result
            st.progress(score)
        else:
            st.warning("Please enter text for analysis.")

    st.markdown("---")
    
    with st.expander("About the Model"):
        st.write("""
            This sentiment analyzer uses the **bertweet-pt-sentiment** model from Hugging Face, specifically trained to interpret and classify sentiments in Portuguese texts.
        """)
    
    st.markdown("Developed by **Arthur Galvíncio, Isaac Medeiros, and Rodrigo Andrade**")

if __name__ == "__main__":
    main()
