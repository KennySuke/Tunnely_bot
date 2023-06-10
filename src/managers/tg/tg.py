import telebot
from telebot.types import Message
from src.domain.locator import LocatorStorage, Locator
import json

class Tg(LocatorStorage):

    def __init__(self, locator: Locator):
        super().__init__(locator)
        self.config = self.locator.config()
        self.tg = telebot.TeleBot(token=self.config.tgToken())
        self.master = self.locator.master()

        @self.tg.message_handler(commands=['start'])
        def cmd_start(m: Message, _=False):
            self.tg.send_message(chat_id=m.chat.id, text='Зачем ты меня породил?')

        @self.tg.message_handler(content_types=['text'])
        def cmd_find(m: Message, _=False):
            split = m.text.split('"')
            for i in range(1, len(split), 2):
                query = split[i]
                response = json.loads(self.master.findMovies(query))['docs']
                films = [x for x in response if query.lower() in x['name'].lower()]
                lines = map(lambda x: f"[{x['name']} ({str(x['year'])})]"+
                                      f"(https://www.kinopoisk.ru/film/{str(x['id'])})", films)
                text = '\n'.join(lines)

                self.tg.send_message(chat_id=m.chat.id,
                                     parse_mode="Markdown",
                                     text=text,
                                     disable_web_page_preview=(len(films)>1))


#END



