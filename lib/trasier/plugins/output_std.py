from .output_base import OutputPlugin


class OutputStd(OutputPlugin):
    def publish(self, params: dict):
        print(params)
