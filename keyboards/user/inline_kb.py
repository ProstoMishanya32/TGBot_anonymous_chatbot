from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from utils.configs_logic import ru_button


def select_lang():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Русский 🇷🇺", callback_data="selectlang:ru"),
                InlineKeyboardButton(text="o'zbek tili 🇺🇿", callback_data="selectlang:uz"),
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