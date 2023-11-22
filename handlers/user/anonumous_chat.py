from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from utils.services import db
from keyboards.user.inline_kb import stop_searching, stop_message
from utils.filters.chat_type import ChatTypeFilter

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type="private"))  # Все обработчики в данном коде будут попадать только в личные диалоги


class SelectFirstLang(StatesGroup):
    select_lang = State()

@router.message(Command("search"))
async def start_user(message: Message, state: FSMContext, bot:Bot):
    await state.clear()

    parther = db.get_queue()
    print(parther)

    if db.create_chat(message.from_user.id, parther) is False:
        db.add_queue(message.from_user.id)

        await message.answer("Идет поиск собеседника", reply_markup=stop_searching("ru"))

    else:
        db.delete_queue(message.from_user.id)
        db.delete_queue(parther)

        await message.answer("Ты подключился в этот чат!", reply_markup=stop_message("ru"))
        await bot.send_message(parther,"Ты подключился в этот чат!", reply_markup=stop_message("ru") )


@router.message(F.text)
async def message_text(message: Message, state: FSMContext, bot:Bot):
    chat = db.get_chat(message.from_user.id)


    if chat:
        await bot.send_message(chat[1], message.text)


@router.message(F.photo)
async def message_photo(message: Message, bot:Bot):
    chat = db.get_chat(message.from_user.id)

    photo = message.photo[-1].file_id

    if chat:
        await bot.send_photo(chat[1], photo)

@router.message(F.video)
async def message_video(message: Message, bot:Bot):
    chat = db.get_chat(message.from_user.id)

    video = message.video.file_id

    if chat:
        await bot.send_video(chat[1], video)

@router.message(F.voice)
async def message_voice(message: Message, bot:Bot):
    chat = db.get_chat(message.from_user.id)

    voice = message.voice.file_id

    if chat:
        await bot.send_voice(chat[1], voice)

@router.message(F.animation)
async def message_animation(message: Message, bot:Bot):
    chat = db.get_chat(message.from_user.id)

    animation = message.animation.file_id

    if chat:
        await bot.send_animation(chat[1], animation)

@router.message(F.audio)
async def message_audio(message: Message, bot:Bot):
    chat = db.get_chat(message.from_user.id)

    audio = message.audio.file_id

    if chat:
        await bot.send_audio(chat[1], audio)