from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from utils.configs_logic import ru_button


def select_lang():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Русский 🇷🇺", callback_data="selectlang:ru"),
                InlineKeyboardButton(text="English 🇬🇧", callback_data="selectlang:gb"),
            ]
    ])
    return keyboard

def settings_menu(lang):
    if lang == "ru":
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=ru_button.settings.gender, callback_data="select_settings:gender"),
                ],
                [
                    InlineKeyboardButton(text=ru_button.settings.age, callback_data="select_settings:age"),
                ],
                [
                    InlineKeyboardButton(text=ru_button.settings.privat_photo_video, callback_data="select_settings:privat_photo_video"),
                ],
                [
                    InlineKeyboardButton(text=ru_button.settings.alerts,callback_data="select_settings:alerts"),
                ]
        ])
    else:
        #TODO поменять на узбек.
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=ru_button.settings.gender, callback_data="select_settings:gender"),
                ],
                [
                    InlineKeyboardButton(text=ru_button.settings.age, callback_data="select_settings:age"),
                ],
                [
                    InlineKeyboardButton(text=ru_button.settings.privat_photo_video, callback_data="select_settings:privat_photo_video"),
                ],
                [
                    InlineKeyboardButton(text=ru_button.settings.alerts,callback_data="select_settings:alerts"),
                ]
        ])
    return keyboard


def edit_gender(lang):
    if lang == "ru":
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=ru_button.settingsgender.man, callback_data="edit_gender:man"),
                    InlineKeyboardButton(text=ru_button.settingsgender.women, callback_data="edit_gender:women"),
                ],
                [
                    InlineKeyboardButton(text=ru_button.settingsgender.delete_gender, callback_data="edit_gender:none"),
                ],
                [
                    InlineKeyboardButton(text=ru_button.common.back, callback_data="settings"),
                ],

        ])
    else:
        #TODO поменять на узбек.
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=ru_button.settingsgender.man, callback_data="edit_gender:man"),
                    InlineKeyboardButton(text=ru_button.settingsgender.women, callback_data="edit_gender:women"),
                ],
                [
                    InlineKeyboardButton(text=ru_button.settingsgender.delete_gender, callback_data="edit_gender:none"),
                ],
                [
                    InlineKeyboardButton(text=ru_button.common.back, callback_data="settings"),
                ],

        ])
    return keyboard


def edit_ages(lang):
    if lang == "ru":
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=ru_button.settingsages.delete_age, callback_data="age_delete"),

                ],
                [
                    InlineKeyboardButton(text=ru_button.common.back, callback_data="settings"),
                ],

        ])
    else:
        #TODO поменять на узбек.
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=ru_button.settingsages.delete_age, callback_data="age_delete"),

                ],
                [
                    InlineKeyboardButton(text=ru_button.common.back, callback_data="settings"),
                ],

        ])
    return keyboard


def error_age(lang):
    if lang == "ru":
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=ru_button.settingsages.error_age, callback_data="error_age"),

                ],
        ])
    else:
        #TODO поменять на узбек.
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=ru_button.settingsages.error_age, callback_data="error_age"),

                ],
        ])
    return keyboard


def privat_video_photo(lang, result):
    if lang == "ru":
        if result == 0:
            button_text = ru_button.settingprivatphoto.off_button
        else:
            button_text = ru_button.settingprivatphoto.on_button
    else:
        #Переделать под узбек #TODO
        if result == 0:
            button_text = ru_button.settingprivatphoto.off_button
        else:
            button_text = ru_button.settingprivatphoto.on_button
    if lang == "ru":
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=button_text, callback_data="change_privat_photo"),

                ],
                [
                    InlineKeyboardButton(text=ru_button.common.back, callback_data="settings"),
                ],
        ])
    else:
        #TODO поменять на узбек.
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=button_text, callback_data="change_privat_photo"),
                ],
                [
                    InlineKeyboardButton(text=ru_button.common.back, callback_data="settings"),
                ],
        ])
    return keyboard


def alert_change(lang, result):
    if lang == "ru":
        if result == 0:
            button_text = ru_button.settingsalerts.off_button
        else:
            button_text = ru_button.settingsalerts.on_button
    else:
        #Переделать под узбек #TODO
        if result == 0:
            button_text = ru_button.settingsalerts.off_button
        else:
            button_text = ru_button.settingsalerts.on_button
    if lang == "ru":
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=button_text, callback_data="change_alert"),

                ],
                [
                    InlineKeyboardButton(text=ru_button.common.back, callback_data="settings"),
                ],
        ])
    else:
        #TODO поменять на узбек.
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=button_text, callback_data="change_alert"),
                ],
                [
                    InlineKeyboardButton(text=ru_button.common.back, callback_data="settings"),
                ],
        ])
    return keyboard


def interests_menu(lang, interests):
    if lang == "ru":
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"{'✅ ' if interests['role_game'] == 1 else ''}{ru_button.interests.role_game}", callback_data="change_interests:role_game"),
                    InlineKeyboardButton(text=f"{'✅ ' if interests['mems'] == 1 else ''}{ru_button.interests.mems}", callback_data="change_interests:mems"),
                ],
                [
                    InlineKeyboardButton(text=f"{'✅ ' if interests['loneliness'] == 1 else ''}{ru_button.interests.loneliness}", callback_data="change_interests:loneliness"),
                    InlineKeyboardButton(text=f"{'✅ ' if interests['flirting'] == 1 else ''}{ru_button.interests.flirting}", callback_data="change_interests:flirting"),
                ],
                [
                    InlineKeyboardButton(text=f"{'✅ ' if interests['games'] == 1 else ''}{ru_button.interests.games}", callback_data="change_interests:games"),
                    InlineKeyboardButton(text=f"{'✅ ' if interests['music'] == 1 else ''}{ru_button.interests.music}", callback_data="change_interests:music"),
                ],
                [
                    InlineKeyboardButton(text=f"{'✅ ' if interests['travels'] == 1 else ''}{ru_button.interests.travels}", callback_data="change_interests:travels"),
                    InlineKeyboardButton(text=f"{'✅ ' if interests['anime'] == 1 else ''}{ru_button.interests.anime}", callback_data="change_interests:anime"),
                ],
                [
                    InlineKeyboardButton(text=f"{'✅ ' if interests['movies'] == 1 else ''}{ru_button.interests.movies}", callback_data="change_interests:movies"),
                    InlineKeyboardButton(text=f"{'✅ ' if interests['pets'] == 1 else ''}{ru_button.interests.pets}", callback_data="change_interests:pets"),
                ],
                [
                    InlineKeyboardButton(text=f"{'✅ ' if interests['books'] == 1 else ''}{ru_button.interests.books}", callback_data="change_interests:books"),
                    InlineKeyboardButton(text=f"{'✅ ' if interests['sport'] == 1 else ''}{ru_button.interests.sport}", callback_data="change_interests:sport"),
                ],
                [
                    InlineKeyboardButton(text=ru_button.interests.reset_interests, callback_data="change_interests:reset_interests"),
                ]
        ])
    else:
        #TODO поменять на узбек.
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"{'✅ ' if interests['role_game'] == 1 else ''}{ru_button.interests.role_game}", callback_data="change_interests:role_game"),
                    InlineKeyboardButton(text=f"{'✅ ' if interests['mems'] == 1 else ''}{ru_button.interests.mems}", callback_data="change_interests:mems"),
                ],
                [
                    InlineKeyboardButton(text=f"{'✅ ' if interests['loneliness'] == 1 else ''}{ru_button.interests.loneliness}", callback_data="change_interests:loneliness"),
                    InlineKeyboardButton(text=f"{'✅ ' if interests['flirting'] == 1 else ''}{ru_button.interests.flirting}", callback_data="change_interests:flirting"),
                ],
                [
                    InlineKeyboardButton(text=f"{'✅ ' if interests['games'] == 1 else ''}{ru_button.interests.games}", callback_data="change_interests:games"),
                    InlineKeyboardButton(text=f"{'✅ ' if interests['music'] == 1 else ''}{ru_button.interests.music}", callback_data="change_interests:music"),
                ],
                [
                    InlineKeyboardButton(text=f"{'✅ ' if interests['travels'] == 1 else ''}{ru_button.interests.travels}", callback_data="change_interests:travels"),
                    InlineKeyboardButton(text=f"{'✅ ' if interests['anime'] == 1 else ''}{ru_button.interests.anime}", callback_data="change_interests:anime"),
                ],
                [
                    InlineKeyboardButton(text=f"{'✅ ' if interests['movies'] == 1 else ''}{ru_button.interests.movies}", callback_data="change_interests:movies"),
                    InlineKeyboardButton(text=f"{'✅ ' if interests['pets'] == 1 else ''}{ru_button.interests.pets}", callback_data="change_interests:pets"),
                ],
                [
                    InlineKeyboardButton(text=f"{'✅ ' if interests['books'] == 1 else ''}{ru_button.interests.books}", callback_data="change_interests:books"),
                    InlineKeyboardButton(text=f"{'✅ ' if interests['sport'] == 1 else ''}{ru_button.interests.sport}", callback_data="change_interests:sport"),
                ],
                [
                    InlineKeyboardButton(text=ru_button.interests.reset_interests, callback_data="change_interests:reset_interests"),
                ]
        ])
    return keyboard



def stop_searching(lang):
    if lang == "ru":
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=ru_button.searchingparther.stop, callback_data="stop_searching"),

                ],
        ])
    else:
        #TODO поменять на англ..
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=ru_button.searchingparther.stop, callback_data="stop_searching"),

                ],
        ])
    return keyboard


def stop_message(lang):
    if lang == "ru":
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=ru_button.searchingparther.stop_message, callback_data="stop_message"),

                ],
        ])
    else:
        #TODO поменять на англ..
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=ru_button.searchingparther.stop_message, callback_data="stop_message"),

                ],
        ])
    return keyboard