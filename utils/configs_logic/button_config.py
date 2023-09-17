from utils.configs_logic.config_creater import CreatingConfig


class RuButton(CreatingConfig):
    def __init__(self) -> None:
        super().__init__(path = 'data/text_config.json')
        self.settings = self.Settings(config = self)
        self.settingsgender  = self.SettingsGender(config = self)
        self.settingsages = self.SettingsAges(config = self)
        self.common = self.Common(config = self)


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

    class Common:
        def __init__(self, config : CreatingConfig) -> None:
            self.back = config.config_field(key = 'back', layer = 'common', default = '← Назад')