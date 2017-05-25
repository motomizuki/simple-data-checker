class OutputPlugin(object):
    def __init__(self, config):
        self.__config = config

    def init(self):
        self.init_plugin(**self.parse_config(self.__config))
        return self

    def parse_config(self, config: dict) -> dict:
        return config

    def init_plugin(self, **kwargs):
        pass

    def publish(self, params: dict):
        pass
