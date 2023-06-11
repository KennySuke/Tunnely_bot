import json
from typing import Optional, List
from src.domain.locator import LocatorStorage, Locator

class Master(LocatorStorage):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        #self.tg = self.locator.tg()
        self.kp = self.locator.kp()

    def findMovies(self, request: str) -> list[str]:
        response = json.loads(self.kp.getMovies(request))['docs']
        films = [x for x in response if request.lower() in x['name'].lower()]
        films.sort(key=lambda x: x['year'])
        return films

#END