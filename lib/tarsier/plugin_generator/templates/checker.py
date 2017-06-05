CHECKER = """from tarsier import TarsierCheckerPlugin


class {}(TarsierCheckerPlugin):
    def parse_config(self, config: dict) -> dict:
        # Please implement this function if you need additional yaml field parsing or validation or type casting.
        return config

    def init_plugin(self, hoge):
        # recieve yaml config and set instance variables
        self.hoge = hoge
        
    def check(self, data) -> [bool, dict]:
        # Implement here
        return True, {{"message": "", "matched_event": data}}
        
"""