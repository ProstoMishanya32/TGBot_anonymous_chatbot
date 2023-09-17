from aiogram.types import FSInputFile

from utils.configs_logic import config_manager
from utils.services import db


async def send_moderator_admin(message, bot, type_content=None, content=None, reply_kb=None,):
    main_admin =  config_manager.get_value("main_admin")
    moderators = db.get_users_by_moderator()
    if content != None:
        content = FSInputFile(content)

    if type_content == "video":
        for user in moderators:
            await bot.send_video(chat_id=user['user_id'], video=content, caption=message, reply_markup=reply_kb)
        await bot.send_video(chat_id=main_admin, video=content, caption=message, reply_markup=reply_kb)
    elif type_content == "photo":
        for user in moderators:
            await bot.send_photo(chat_id=user['user_id'], photo=content, caption=message, reply_markup=reply_kb)
        await bot.send_photo(chat_id=main_admin, photo=content, caption=message, reply_markup=reply_kb)
    elif type_content == "audio":
        for user in moderators:
            await bot.send_audio(chat_id=user['user_id'], audio=content, caption=message, reply_markup=reply_kb)
        await bot.send_audio(chat_id=main_admin, audio=content, caption=message, reply_markup=reply_kb)
    elif type_content == "animation":
        for user in moderators:
            await bot.send_audio(chat_id=user['user_id'], audio=content, caption=message, reply_markup=reply_kb)
        await bot.send_animation(chat_id=main_admin, animation=content, caption=message, reply_markup=reply_kb)
    elif type_content == "document":
        for user in moderators:
            await bot.send_document(chat_id=user['user_id'], document=content, caption=message, reply_markup=reply_kb)
        await bot.send_animation(chat_id=main_admin, animation=content, caption=message, reply_markup=reply_kb)
    else:
        for user in moderators:
            await bot.send_message(chat_id=user['user_id'], text=message, reply_markup=reply_kb)
        await bot.send_message(chat_id=main_admin, text=message, reply_markup=reply_kb)


def ded(get_text: str):
    if get_text is not None:
        split_text = get_text.split("\n")
        if split_text[0] == "": split_text.pop(0)
        if split_text[-1] == "": split_text.pop(-1)
        save_text = []

        for text in split_text:
            while text.startswith(" "):
                text = text[1:]

            save_text.append(text)
        get_text = "\n".join(save_text)

    return get_text
