import os
from dotenv import load_dotenv
from slack import WebClient
from slack.errors import SlackApiError
from slackeventsapi import SlackEventAdapter
from flask import Flask

from ai_manager.model import QroqModel

load_dotenv()  # Load environment variables from .env file

## Load environment variables
groq_api_token = os.getenv("GROQ_API_TOKEN")
slack_api_token = os.getenv('SLACK_API_TOKEN')
slack_signing_secret = os.getenv('SLACK_SIGNING_SECRET')
slack_channel = os.getenv('SLACK_CHANNEL')
flask_debug = os.getenv('FLASK_DEBUG') == 'True'

# Check for missing environment variables and throw an exception if any are missing
if not groq_api_token:
    raise EnvironmentError("Missing environment variable: GROQ_API_TOKEN")
if not slack_api_token:
    raise EnvironmentError("Missing environment variable: SLACK_API_TOKEN")
if not slack_signing_secret:
    raise EnvironmentError("Missing environment variable: SLACK_SIGNING_SECRET")
if not slack_channel:
    raise EnvironmentError("Missing environment variable: SLACK_CHANNEL")

## Initialize the Flask app
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events", app)
client = WebClient(token=slack_api_token)

## Initialize the QroqModel
groq_model = QroqModel(groq_api_token)



@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]

    # Ignore messages from the bot itself
    if '?' not in message["text"] or message.get("subtype") == "bot_message" or message.get("user") == client.auth_test()["user_id"]:
        return
    

    try:
        _text = groq_model.get_response(message['text'])

        response = client.chat_postMessage(
            channel=message['channel'],
            text= _text
        )
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0" , debug=flask_debug)