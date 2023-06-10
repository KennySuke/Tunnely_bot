from src.domain.locator import LocatorStorage, Locator
import requests
class Kp(LocatorStorage):
    def __init__(self, locator: Locator):
        super().__init__(locator)
        self.config = self.locator.config()

    def getMovies(self, query: str) -> str:
        request = 'https://api.kinopoisk.dev/v1.2/movie/search?limit=50&query='+query
        #request = 'https://api.kinopoisk.dev/v1.3/movie?name='+query
        #print(request)
        response = requests.get(url=request, headers={'X-API-KEY': self.config.kpToken()})
        return response.text

#END