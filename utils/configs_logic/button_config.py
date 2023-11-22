from utils.configs_logic.config_creater import CreatingConfig


class RuButton(CreatingConfig):
    def __init__(self) -> None:
        super().__init__(path = 'data/button_config.json')
        self.settings = self.Settings(config = self)

        self.settingsgender  = self.SettingsGender(config = self)
        self.settingsages = self.SettingsAges(config = self)
        self.settingprivatphoto = self.SettingsPrivatPhoto(config = self)
        self.settingsalerts = self.SettingsAlerts(config = self)

        self.interests = self.Interests(config = self)

        self.common = self.Common(config = self)
        self.searchingparther = self.SearchingParther(config = self)


    class Settings:
        def __init__(self, config : CreatingConfig) -> None:
            self.gender = config.config_field(key = 'gender', layer = 'settings', default = '🧑 Пол 👧')
            self.age = config.config_field(key = 'age', layer = 'settings', default = '📅 Возраст')
            self.privat_photo_video = config.config_field(key = 'privat_photo_video', layer = 'settings', default = '🔐 Скрытие фото/видео')
            self.alerts = config.config_field(key = 'alerts', layer = 'settings', default = '🗣 Уведомления')

    class SettingsGender:
        def __init__(self, config : CreatingConfig) -> None:
            self.man = config.config_field(key = 'man', layer = 'settingsgender', default = 'Я парень 🧑')
            self.women = config.config_field(key = 'women', layer = 'settingsgender', default = 'Я девушка 👧')
            self.delete_gender = config.config_field(key = 'delete_gender', layer = 'settingsgender', default = 'Удалить мой пол')

    class SettingsAges:
        def __init__(self, config: CreatingConfig) -> None:
            self.delete_age = config.config_field(key='delete_age', layer='settingsgender', default='❌ Удалить возраст')
            self.error_age = config.config_field(key='error_age', layer='settingsgender', default='🚫 Не сейчас')

    class SettingsPrivatPhoto:
        def __init__(self, config: CreatingConfig) -> None:
            self.off_button = config.config_field(key='off_button', layer='settingsprivatphoto', default='❌  Отключить скрытие фото/видео')
            self.on_button = config.config_field(key='on_button', layer='settingsprivatphoto', default='✅ Включить скрытие фото/видео')

    class SettingsAlerts:
        def __init__(self, config: CreatingConfig) -> None:
            self.off_button = config.config_field(key='off_button', layer='settingsalerts', default='❌  Отключить уведомления')
            self.on_button = config.config_field(key='on_button', layer='settingsalerts', default='✅ Включить уведомления')

    class Interests:
        def __init__(self, config: CreatingConfig) -> None:
            self.role_game = config.config_field(key='role_game', layer='interests', default='Ролевые игры')
            self.mems = config.config_field(key='mems', layer='interests', default='Мемы')
            self.loneliness = config.config_field(key='loneliness', layer='interests', default='Одиночество')
            self.flirting = config.config_field(key='flirting', layer='interests', default='Флирт')
            self.games = config.config_field(key='games', layer='interests', default='Игры')
            self.music = config.config_field(key='music', layer='interests', default='Музыка')
            self.travels = config.config_field(key='travels', layer='interests', default='Пушествия')
            self.anime = config.config_field(key='anime', layer='interests', default='Аниме')
            self.movies = config.config_field(key='movies', layer='interests', default='Фильмы')
            self.pets = config.config_field(key='pets', layer='interests', default='Фильмы')
            self.books = config.config_field(key='books', layer='interests', default='Книги')
            self.sport = config.config_field(key='sport', layer='interests', default='Спорт')
            self.reset_interests = config.config_field(key='reset_interests', layer='interests', default='❌ Сбросить интересы')

    class Common:
        def __init__(self, config : CreatingConfig) -> None:
            self.back = config.config_field(key = 'back', layer = 'common', default = '← Назад')

    class SearchingParther:
        def __init__(self, config : CreatingConfig) -> None:
            self.stop = config.config_field(key = 'stop', layer = 'searchingparther', default = 'Остановить поиск')
            self.stop_message = config.config_field(key = 'stop_message', layer = 'searchingparther', default = 'Остановить диалог')
