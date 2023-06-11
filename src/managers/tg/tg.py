import telebot
from telebot.types import Message
from src.domain.locator import LocatorStorage, Locator
import json
import re

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
            requests = list(map(lambda x: x.split('"')[1], re.findall(r'\"[^"]+\"', m.text)))
            for request in requests:
                response = json.loads(self.master.findMovies(request))['docs']
                films = [x for x in response if request.lower() in x['name'].lower()]
                films.sort(key=lambda x: x['year'])
                lines = list(map(lambda x: f"[{x['name']} ({str(x['year'])})]" +
                                      f"(https://www.kinopoisk.ru/film/{str(x['id'])})", films))
                text = f'Ваш запрос: "{request}"\n\n'
                text += "Найдено:\n"+'\n'.join(lines) if lines else "Фильмов с таким названием не найдено."
                self.tg.send_message(chat_id=m.chat.id,
                                     parse_mode="Markdown",
                                     text=text,
                                     reply_to_message_id=m.id,
                                     disable_web_page_preview=(len(films) > 1)
                                     )

#END



