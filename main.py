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

print(f'Slack Token: {slack_api_token}')
print(f'Slack Channel: {slack_channel}')




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
            channel=slack_channel,
            text= _text
        )
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")

if __name__ == "__main__":
    app.run(port=3000 , debug=True)