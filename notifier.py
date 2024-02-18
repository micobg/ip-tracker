import os
import slack_sdk
from slack_sdk.errors import SlackApiError


class Notifier:

    _client = None

    def __init__(self):
        if self._client is None:
            self._client_initialize()

    def message(self, text: str):
        try:
            self._client.chat_postMessage(channel=os.environ['SLACK_CHANNEL'], text=text)
        except SlackApiError as e:
            print(f'Error on sending message ({text}) to Slack: {e.response}')

    def _client_initialize(self):
        self._client = slack_sdk.WebClient(token=os.environ['SLACK_TOKEN'])
