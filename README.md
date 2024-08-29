# Sentiment Analyzer 🎉

Welcome to the **Sentiment Analyzer** project! This project is developed as part of the "Special Topics in Bioinformatics" course and aims to create an easy-to-use web application for sentiment analysis using artificial intelligence. The application is designed specifically for processing and analyzing texts in Portuguese.

## 📋 Project Description

This project consists of a sentiment analysis application that uses AI to determine the sentiment (positive, negative, or neutral) of user-provided text. The system is implemented in Python and leverages a pre-trained model from the Hugging Face platform. The application is hosted in the cloud via Streamlit, providing an interactive and user-friendly interface.

## 🎯 Objective

The main objective of this application is to offer an accessible and intuitive tool for sentiment analysis. It can be used in various contexts such as social media monitoring, customer feedback analysis, or opinion studies. The application showcases how AI models can be seamlessly integrated into cloud-based solutions, making data analysis more efficient and practical.

## 🚀 How It Works

- **Data Collection**: Users input text via the interface.
- **Data Processing**: The text is pre-processed to fit the AI model.
- **Sentiment Analysis**: A pre-trained model from Hugging Face is applied to classify the text's sentiment.
- **Results Display**: The results are shown in real-time on the Streamlit interface.

## 🛠️ Technologies Used

- **Python**: The primary language used for development.
- **Hugging Face**: Platform for utilizing pre-trained AI models.
- **Streamlit**: Framework for building the web interface and deploying the application in the cloud.

## 💻 Installation

To run this project locally, you'll need to clone the repository and install the necessary dependencies. Follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/sentiment-analyzer.git
   cd sentiment-analyzer

   ```
2. Install the required packages:
   ```bash
   pip install streamlit torch==2.3.1 pysentimiento
   ```
3. Run the application:
   ```bash
   streamlit run sentimentanalisys.py
   ```

## ✨ Features
Real-time Sentiment Analysis: Get instant feedback on the sentiment of your text input.
User-Friendly Interface: Easily interact with the application through a clean and simple web interface.
Cloud Deployment: Accessible from anywhere, thanks to the power of Streamlit.

## 👩‍💻 Project Structure
app.py: The main application script.
dark_theme.css: Custom CSS for the dark theme interface.
requirements.txt: List of dependencies required for the project.
🤝 Contributors
Developed by Arthur Galvíncio, Isaac Medeiros, and Rodrigo Andrade as part of their coursework.

## 📚 Additional Information
This project utilizes the bertweet-pt-sentiment model from Hugging Face, specifically trained to interpret and classify sentiments in Portuguese texts.


