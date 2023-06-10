from typing import Optional, List
from src.domain.locator import LocatorStorage, Locator

class Master(LocatorStorage):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        #self.tg = self.locator.tg()
        self.kp = self.locator.kp()

    def findMovies(self, query: str) -> str:
        return self.kp.getMovies(query)

#END