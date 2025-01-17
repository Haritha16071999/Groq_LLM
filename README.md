# Groq_LLM
Sentiment Analysis with Flask and Groq LLM API


Overview

This project is a Flask-based web application that allows users to analyze the sentiment (Positive, Negative, or Neutral) of input text. It integrates with the Groq LLM API to provide accurate sentiment analysis using techniques like few-shot prompting.

Features
Accepts text input via a POST request.
Uses the Groq LLM API to process text and analyze sentiment.
Returns sentiment results in real-time.
Implements robust logging for inputs, API responses, and errors.
Handles invalid inputs and errors gracefully.


Enter the text you want to analyze in the input field.
Click the "Submit" button.
View the sentiment result (Positive, Negative, or Neutral) on the page.
Logging
Logs all incoming requests and responses for debugging and monitoring.
Captures and logs errors during API calls or invalid input handling.
Error Handling
Empty Input: If the input text is empty, the application displays a user-friendly error message and logs the issue.
API Errors: If the Groq API call fails, the application catches the error, logs it, and displays an error message.
