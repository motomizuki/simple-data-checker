from plugins.checker_base import CheckerPlugin
from plugins.input_base import InputPlugin
from plugins.output_base import OutputPlugin


class Executor:
    def __init__(self, input_plugin: InputPlugin, checker_plugin: CheckerPlugin, output_plugin: OutputPlugin):
        self._input = input_plugin
        self._checker = checker_plugin
        self._output = output_plugin

    def exec(self):
        pipe_data = self._input.load()
        matched, params = self._checker.check(pipe_data)
        if matched:
            self._output.publish(params)

