from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.user import inline_kb
from utils.configs_logic import common_text, ru_text
from utils.filters.chat_type import ChatTypeFilter
from utils.miscellaneous.get_info import get_real_time
from utils.services import db

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type="private"))  # Все обработчики в данном коде будут попадать только в личные диалоги


class SelectFirstLang(StatesGroup):
    select_lang = State()

@router.message(Command("start"))
async def start_user(message: Message, state: FSMContext):
    await state.clear()

    user = message.from_user

    if user.username:
        username = user.username
    else:
        username = user.first_name or user.last_name or "Пользователь"

    if db.user_exists(user.id):
        data = db.get_user_by_id(user.id)
        lang = data['language']

        if lang == "ru":
            await message.answer(ru_text.menu.menu, disable_web_page_preview=True)
        else:
            # TODO change on english.
            await message.answer(ru_text.menu.menu, disable_web_page_preview=True)

    else:
        select_lang = common_text.settings.select_lang

        await state.set_state(SelectFirstLang.select_lang)
        await state.update_data(username=username)

        await message.answer(select_lang, reply_markup=inline_kb.select_lang())


@router.callback_query(Text(startswith="selectlang"), SelectFirstLang.select_lang)
async def fist_select_lang(call: CallbackQuery, state: FSMContext):
    lang = call.data.split(":")[1]

    data = await state.get_data()
    username = data['username']
    await state.clear()

    db.add_user(call.from_user.id, username, lang, get_real_time())

    if lang == "ru":
        await call.message.edit_text(ru_text.menu.menu, disable_web_page_preview=True)
        # TODO change on english.
        await call.message.edit_text(ru_text.menu.menu, disable_web_page_preview=True)
