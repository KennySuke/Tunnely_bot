class Locator:

    def __init__(self):
        self._config = None
        self._kp = None
        self._tg = None
        self._master = None

    def config(self):
        if self._config is None:
            from src.domain.config import Config
            self._config = Config()
        return self._config

    def kp(self):
        if self._kp is None:
          from src.managers.kp.kp import Kp
          self._kp = Kp(self)
        return self._kp

    def tg(self):
        if self._tg is None:
          from src.managers.tg.tg import Tg
          self._tg = Tg(self)
        return self._tg

    def master(self):
        if self._master is None:
          from src.managers.master import Master
          self._master = Master(self)
        return self._master
class LocatorStorage:
  def __init__(self, locator: Locator = None):
    self.locator = locator or Locator


_global_locator = Locator()


def glob():
  return _global_locator

#END