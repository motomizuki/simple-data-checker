from .checker_base import CheckerPlugin


class CheckerAlways(CheckerPlugin):
    def check(self, data) -> [bool, dict]:
        return True, {"message": "this checker always return true", "matched_event": {}}

