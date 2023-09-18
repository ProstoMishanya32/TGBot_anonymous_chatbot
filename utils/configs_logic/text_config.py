from utils.configs_logic.config_creater import CreatingConfig


class CommonText(CreatingConfig):
    def __init__(self) -> None:
        super().__init__(path = 'data/text_config.json')
        self.welcome = self.Welcome(config = self)
        self.settings = self.Settings(config = self)


    class Welcome:
        def __init__(self, config : CreatingConfig) -> None:
            self.first_welcome = config.config_field(key = 'first_welcome', layer = 'welcome', default = 'Привет дорогой <b>{username}</b>.Рады впервые видеть тебя тут.\n\n{select_lang}')
            self.welcome = config.config_field(key = 'welcome', layer = 'welcome', default = 'Привет дорогой <b>{username}</b>.Мы тебя помним).\nВот тебе главное меню 😁')

    class Settings:
        def __init__(self, config : CreatingConfig) -> None:
            self.select_lang = config.config_field(key = 'select_lang', layer = 'settings', default = 'Выберите язык 🇷🇺 // Tilni tanlang 🇺🇿')

class RuText(CreatingConfig):
    def __init__(self) -> None:
        super().__init__(path = 'data/text_config.json')
        self.menu = self.Menu(config = self)
        self.settings = self.Settings(config = self)

    class Menu:
        def __init__(self, config : CreatingConfig) -> None:
            self.menu = config.config_field(key = 'menu', layer = 'menu', default = '👋 Привет! Это Анонимный чат Телеграма.\nТут можно общаться 1 на 1 со случайными собеседниками.\n\n📖 В чате есть правила поведения, которые нужно соблюдать.\nНельзя спамить, продвигать свои услуги, оскорблять собеседников.\n\n📋 Подробнее правила можно прочитать тут:\nhttps://telegra.ph/anonrubot-rules-07-03\n\n🔎 Работает бот очень просто: вы жмете кнопку поиска или используете команду /search и бот находит вам собеседника.\nУдачного общения! Будьте вежливы к собеседникам.')
    class Settings:
        def __init__(self, config : CreatingConfig) -> None:
            self.menu = config.config_field(key = 'menu', layer = 'settings', default = '<i>Выберите настройки, которые вы бы хотели изменить:</i>')
            self.not_gender = config.config_field(key = 'not_gender', layer = 'settings', default = '<i>Пол не установлен. Укажите ваш пол:</i>')
            self.gender_man = config.config_field(key = 'gender_man', layer = 'settings', default = '<i>У вас установлен мужской пол\nЧтобы изменить или удалить пол, нажмите на кнопки ниже</i>')
            self.gender_women = config.config_field(key = 'gender_women', layer = 'settings', default = '<i>У вас установлен женский пол\nЧтобы изменить или удалить пол, нажмите на кнопки ниже</i>')
            self.successfully_edit_gender = config.config_field(key = 'successfully_edit_gender', layer = 'settings', default = '<i>Спасибо, что указали свой пол.\n\nЧтобы искать нового собеседника, нажмите /search</i>')
            self.aged_start = config.config_field(key = 'aged_start', layer = 'settings', default = 'Введите ваш возраст цифрами (от 9 до 99), чтобы мы могли находить вам наиболее подходящих собеседников.\n\nНапример, если вам 21 год, напишите 21:')
            self.delete_age = config.config_field(key = 'delete_age', layer = 'settings', default = '<i>Ваш возраст был удален</i>')
            self.finish_age = config.config_field(key = 'finish_age', layer = 'settings', default = '<i>Спасибо, что указали свой возраст</i>')
            self.error_age = config.config_field(key = 'error_age', layer = 'settings', default = 'Вы ввели неправильный возраст\n\nВведите ваш возраст цифрами (от 9 до 99), чтобы мы могли находить вам наиболее подходящих собеседников.\n\nНапример, если вам 21 год, напишите 21:')
            self.age_cancel = config.config_field(key = 'age_cancel', layer = 'settings', default = '<i>Хорошо, спрашивать больше не буду</i>')
            self.privat_photo_video = config.config_field(key = 'privat_photo_video', layer = 'settings', default = '<i>В режиме скрытия все фотографии, видео, документы и GIF, которые присылает вам собеседник, будут видны только после нажатия вами кнопки "Показать"</i>')
            self.alerts = config.config_field(key = 'alerts', layer = 'settings', default = '<i>Если вы включите уведомления, то раз в сутки мы будем уведомлять вас о количестве забаненных пользователей по вашим жалобам</i>')