import importlib

import yaml
import sys
from .executor import Executor

template = "..plugins.tarsier_{type_}_{name}"


def get_plugin_class(type_, name):
    try:
        # check plugin that installed via pip
        _module = importlib.import_module("tarsier_{type_}_{name}".format(type_=type_, name=name))
    except:
        # check default plugin
        _module = importlib.import_module(template.format(type_=type_, name=name), package=__name__)
    return getattr(_module, "Tarsier{}{}".format(type_.title(), name.title()))


class Builder:
    def __init__(self, path):
        with open(path, "r") as f:
            self._config = yaml.load(f)

    def build(self):
        # init input plugin instance

        if "in" in self._config and "checker" in self._config and "out" in self._config:
            input_conf = self._config["in"]
            __cls = get_plugin_class("input", input_conf["type"])
            del input_conf["type"]
            input_plugin = __cls(input_conf).init()

            checker_conf = self._config["checker"]
            __cls = get_plugin_class("checker", checker_conf["type"])
            del checker_conf["type"]
            checker_plugin = __cls(checker_conf).init()

            output_conf = self._config["out"]
            __cls = get_plugin_class("output", output_conf["type"])
            del output_conf["type"]
            output_plugin = __cls(output_conf).init()
            return Executor(input_plugin=input_plugin, checker_plugin=checker_plugin, output_plugin=output_plugin)
        else:
            raise ValueError("in, checker, out field is required in configuration yaml file.")
