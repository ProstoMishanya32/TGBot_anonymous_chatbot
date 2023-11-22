from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.user import inline_kb
from utils.configs_logic import ru_text
from utils.filters.chat_type import ChatTypeFilter
from utils.services import db

router = Router()
router.message.filter(ChatTypeFilter(chat_type="private")) #Все обработчики в данном коде будут попадать только в личные диалоги

class GetAge(StatesGroup):
    age = State()


@router.message(Command("interests"))
async def start_interests_menu(message: Message, state: FSMContext):
    await state.clear()

    data = db.get_user_by_id(message.from_user.id)
    lang = data['language']

    interests = db.get_interests_by_id(message.from_user.id)

    if lang == "ru":
        await message.answer(ru_text.interests.menu, disable_web_page_preview=True, reply_markup=inline_kb.interests_menu(lang, interests))
    else:
        # TODO поменять на узбек.
        await message.answer(ru_text.interests.menu, disable_web_page_preview=True, reply_markup=inline_kb.interests_menu(lang, interests))


@router.callback_query(Text(startswith="change_interests:"))
async def change_interests(call: CallbackQuery, state: FSMContext):
    interes = call.data.split(":")[1]

    user_id = call.from_user.id

    data = db.get_user_by_id(user_id)
    lang = data['language']


    if interes == "reset_interests":
        db.update_all_interests(user_id, 0)

    else:
        interests = db.get_interests_by_id(user_id)
        if interests[interes] == 1:
            result = 0
        else:
            result = 1

        db.update_interests_column(user_id, interes, result)

    interests = db.get_interests_by_id(user_id)


    if lang == "ru":
        await call.message.edit_text(ru_text.interests.menu, disable_web_page_preview=True, reply_markup=inline_kb.interests_menu(lang, interests))
    else:
        # TODO поменять на узбек.
        await call.message.edit_text(ru_text.interests.menu, disable_web_page_preview=True, reply_markup=inline_kb.interests_menu(lang, interests))

