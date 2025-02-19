import os
from dotenv import load_dotenv
from slack import WebClient
from slack.errors import SlackApiError
from slackeventsapi import SlackEventAdapter
from flask import Flask

load_dotenv()  # Load environment variables from .env file

slack_token = os.getenv('SLACK_API_TOKEN')
slack_signing_secret = os.getenv('SLACK_SIGNING_SECRET')
slack_channel = os.getenv('SLACK_CHANNEL')
print(f'Slack Token: {slack_token}')
print(f'Slack Channel: {slack_channel}')

app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events", app)
client = WebClient(token=slack_token)

@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    
    # Ignore messages from the bot itself
    if message.get("subtype") == "bot_message" or message.get("user") == client.auth_test()["user_id"]:
        return
    
    try:
        response = client.chat_postMessage(
            channel=slack_channel,
            text=f"Received your message: {message['text']}"
        )
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")

if __name__ == "__main__":
    app.run(port=3000 , debug=True)