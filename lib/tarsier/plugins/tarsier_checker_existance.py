from .tarsier_checker_base import TarsierCheckerPlugin


def str2bool(s):
    return s.lower() in ['true', 'yes', 'y', 't', '1']


class TarsierCheckerExistance(TarsierCheckerPlugin):
    def init_plugin(self, filter=None, filter_condition="all", exist=True):
        self._filter = filter
        self._filter_condition = filter_condition
        self._exist = exist

    def check(self, data):
        if self._filter:
            if self._filter_condition == "all":
                data = list(filter(lambda x: all([x.get(k) in v for k, v in self._filter.items()]), data))
            else:
                data = list(filter(lambda x: any([x.get(k) in v for k, v in self._filter.items()]), data))
        b = len(data) > 0
        r = b if self._exist else not b

        return r, {"msg": "{}data exists.".format("" if self._exist else "no ").title(), "matched_data": data}
