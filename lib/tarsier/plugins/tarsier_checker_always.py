from .tarsier_checker_base import TarsierCheckerPlugin


class TarsierCheckerAlways(TarsierCheckerPlugin):
    def check(self, data) -> [bool, dict]:
        return True, {"message": "this checker always return true", "matched_event": {}}

