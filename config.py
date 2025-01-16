
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import logging
from groq import Groq


load_dotenv()

app = Flask(__name__)


api_key = os.getenv("GROQ_API_KEY")


if not api_key:
    raise ValueError("GROQ_API_KEY is not set. Please check your .env file.")

client = Groq(api_key=api_key)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment_result = None
    user_input = None
    error_message = None

    if request.method == "POST":
        try:
       
            user_input = request.form["user_input"]

       
            logger.info(f"Received input: {user_input}")

            if not user_input:
                error_message = "Input text cannot be empty!"
                logger.error(error_message)
                return render_template("index.html", error_message=error_message)

           
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"What is the sentiment of the following text: '{user_input}'"
                    }
                ],
                model="mixtral-8x7b-32768"
            )

          
            logger.info(f"API Response: {chat_completion.choices[0].message.content}")

           
            sentiment_result = chat_completion.choices[0].message.content

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            logger.error(error_message)
            return render_template("index.html", error_message=error_message)

    return render_template("index.html", sentiment_result=sentiment_result, user_input=user_input, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)


