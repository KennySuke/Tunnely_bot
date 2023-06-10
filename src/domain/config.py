import json

class Config:
    CONFIG_FILE_NAME = 'config.json'

    def __init__(self):
        self.data = dict()
        with open(Config.CONFIG_FILE_NAME) as file:
            self.data = json.load(file)

    def kpToken(self) -> str:
        return self._paramOrNone('kinopoisk_token', str)

    def tgToken(self) -> str:
        return self._paramOrNone('tg_token', str)

    def locale(self) -> str:
        return self._paramOrNone('locale', str)

    def _paramOrNone(self, name: str, tp):
        return Config._valueOrNone(self.data.get(name), tp)

    @staticmethod
    def _valueOrNone(value, tp):
        return value if type(value) is tp else None

#END