import os
from dotenv import load_dotenv
from slack import WebClient
from slack.errors import SlackApiError

load_dotenv()  # Load environment variables from .env file

slack_token = os.getenv('SLACK_API_TOKEN')
print(f'Slack Token: {slack_token}')



client = WebClient(token=slack_token)

try:
    response = client.chat_postMessage(
        channel='#test',
        text="Hello world!")
    assert response["message"]["text"] == "Hello world!"
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
