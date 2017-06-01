from .tarsier_output_base import TarsierOutputPlugin


class TarsierOutputStd(TarsierOutputPlugin):
    def publish(self, params: dict):
        print(params)
