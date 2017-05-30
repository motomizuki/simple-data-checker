import json

import requests

from .tarsier_output_base import TarsierOutputPlugin


class TarsierOutputSlack(TarsierOutputPlugin):
    def init_plugin(self, webhook_url: str, channel="#random", text=""):
        self._webhook_url = webhook_url
        self._text = text
        self._channel = channel

    def publish(self, params: dict):
        headers = {'content-type': 'application/json'}
        text = self._text.format(**params.get("matched_data")[0])
        requests.post(self._webhook_url, data=json.dumps({"text": text, "channel": self._channel}), headers=headers)
