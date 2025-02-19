
# Slack Sensei Bot

## Introduction
Slack Sensei is a bot designed to interact with Slack channels. This guide will help you set up the bot by creating a Slack app, configuring necessary scopes, and setting up a Flask server.

## Setup Instructions

### 1. Create a Slack App
1. Go to [Slack API](https://api.slack.com/apps) and click on "Create New App".
2. Choose "From scratch" and provide a name for your app.
3. Select the workspace where you want to develop your app.

### 2. Add Scopes
1. Navigate to "OAuth & Permissions" under "Features".
2. Scroll down to "Scopes" and add the following Bot Token Scopes:
   - `channels:history`
   - `channels:read`
   - `channels:write`

### 3. Install the App
1. Go to "Install App" under "Settings".
2. Click on "Install App to Workspace".
3. Authorize the app to get the OAuth token. Note down the OAuth token for later use.

### 4. Enable Events
1. Navigate to "Event Subscriptions" under "Features".
2. Enable "Event Subscriptions".
3. Enter the Request URL of your Flask server (e.g., `https://your-flask-server.com/slack/events`).
4. Subscribe to bot events as needed.

### 5. Get the Signing Secret
1. Go to "Basic Information" under "Settings".
2. Scroll down to "App Credentials" and note down the Signing Secret.

### 6. Configure Flask Server
1. Set up a Flask server to handle Slack events.
2. Use the OAuth token and Signing Secret in your Flask application to verify requests and interact with Slack.



## Environment Variables
Make sure to set the following environment variables in your Flask server:
- `SLACK_BOT_TOKEN`
- `SLACK_SIGNING_SECRET`
- `SLACK_CHANNEL`
## Conclusion
You have successfully set up the Slack Sensei bot. You can now extend its functionality by handling different Slack events and adding more features.
