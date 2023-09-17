from aiogram.filters import BaseFilter
from aiogram.types import Message

from utils.configs_logic import config_manager


class ModeratorCheck(BaseFilter): #Фильтр на проверку, является ль пользователем модератором
    def __init__(self, moderators_id: list):
        self.moderators_id = moderators_id

    async def __call__(self, message: Message) -> bool:
        main_admin = config_manager.get_value("main_admin")
        if  message.from_user.id == main_admin:
            return True
        else:
            return message.from_user.id in self.moderators_id


class StreamerCheck(BaseFilter):  #Фильтр на проверку, является ль пользователем стримером
    def __init__(self, streamers_id: list):
        self.streamers_id = streamers_id

    async def __call__(self, message: Message) -> bool:
        main_admin = config_manager.get_value("main_admin")
        if  message.from_user.id == main_admin:
            return True
        else:
            return message.from_user.id in self.streamers_id