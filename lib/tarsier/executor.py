from .plugins.tarsier_checker_base import TarsierCheckerPlugin
from .plugins.tarsier_input_base import TarsierInputPlugin
from .plugins.tarsier_output_base import TarsierOutputPlugin


class Executor:
    def __init__(self, input_plugin: TarsierInputPlugin, checker_plugin: TarsierCheckerPlugin,
                 output_plugin: TarsierOutputPlugin):
        self._input = input_plugin
        self._checker = checker_plugin
        self._output = output_plugin

    def exec(self):
        pipe_data = self._input.load()
        matched, params = self._checker.check(pipe_data)
        if matched:
            self._output.publish(params)
