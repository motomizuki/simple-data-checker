from .tarsier_checker_base import TarsierCheckerPlugin


class TarsierCheckerThreshold(TarsierCheckerPlugin):
    def init_plugin(self, field, lower=None, upper=None):
        if lower is None and upper is None:
            raise ValueError("Either lower or upper is necessary")

        self._lower = float(lower)
        self._upper = float(upper)
        self._field = field

    def check(self, data):
        def f(x):
            value = float(x[self._field])
            lower = self._lower is not None and self._lower > value
            upper = self._upper is not None and self._upper < value
            return lower or upper
        matched = list(filter(f, data))
        return len(matched) > 0, {"msg": "matched threshold data", "matched_data": matched}