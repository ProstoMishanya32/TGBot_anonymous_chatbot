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


@router.message(Command("settings"))
async def start_settings(message: Message, state: FSMContext):
    await state.clear()

    data = db.get_user_by_id(message.from_user.id)
    lang = data['language']

    if lang == "ru":
        await message.answer(ru_text.settings.menu, disable_web_page_preview=True, reply_markup=inline_kb.settings_menu(lang))
    else:
        # TODO поменять на узбек.
        await message.answer(ru_text.settings.menu, disable_web_page_preview=True, reply_markup=inline_kb.settings_menu(lang))


@router.callback_query(Text("settings"))
async def settings_menu(call: CallbackQuery, state: FSMContext):
    await state.clear()

    data = db.get_user_by_id(call.from_user.id)
    lang = data['language']

    if lang == "ru":
        await call.message.edit_text(ru_text.settings.menu, disable_web_page_preview=True, reply_markup=inline_kb.settings_menu(lang))
    else:
        # TODO поменять на узбек.
        await call.message.edit_text(ru_text.settings.menu, disable_web_page_preview=True, reply_markup=inline_kb.settings_menu(lang))


@router.callback_query(Text(startswith="select_settings"))
async def select_settings(call: CallbackQuery, state: FSMContext):
    settings = call.data.split(":")[1]

    data = db.get_user_by_id(call.from_user.id)
    lang = data['language']
    gender = data['gender']

    if settings == "gender":
        if lang == "ru":
            if gender == None:
                await call.message.edit_text(ru_text.settings.not_gender, reply_markup=inline_kb.edit_gender(lang))
            elif gender == "man":
                await call.message.edit_text(ru_text.settings.gender_man, reply_markup=inline_kb.edit_gender(lang))
            elif gender == "women":
                await call.message.edit_text(ru_text.settings.gender_women, reply_markup=inline_kb.edit_gender(lang))
        else:
            #TODO поменять на узбек.

            if gender == None:
                await call.message.edit_text(ru_text.settings.not_gender, reply_markup=inline_kb.edit_gender(lang))
            elif gender == "man":
                await call.message.edit_text(ru_text.settings.gender_man, reply_markup=inline_kb.edit_gender(lang))
            elif gender == "women":
                await call.message.edit_text(ru_text.settings.gender_women, reply_markup=inline_kb.edit_gender(lang))

    elif settings == "age":
        await state.set_state(GetAge.age)
        if lang == "ru":
            await call.message.edit_text(ru_text.settings.aged_start, reply_markup=inline_kb.edit_ages(lang))
        else:
            await call.message.edit_text(ru_text.settings.aged_start, reply_markup=inline_kb.edit_ages(lang))


@router.callback_query(Text(startswith="edit_gender:"))
async def edit_gender(call: CallbackQuery, state: FSMContext):
    gender = call.data.split(":")[1]

    user_id = call.from_user.id

    data = db.get_user_by_id(user_id)
    lang = data['language']
    if gender == "none":
        gender = None

    db.update_users_column(user_id, "gender", gender)

    if lang == "ru":
        await call.message.edit_text(ru_text.settings.successfully_edit_gender)
    else:
        # TODO поменять на узбек.
        await call.message.edit_text(ru_text.settings.successfully_edit_gender)


@router.callback_query(Text("age_delete"), GetAge.age)
async def delete_age(call: CallbackQuery, state: FSMContext):
    await state.clear()

    data = db.get_user_by_id(call.from_user.id)
    lang = data['language']


    db.update_users_column(call.from_user.id, "age", None)

    if lang == "ru":
        await call.message.edit_text(ru_text.settings.delete_age)
    else:
        # TODO поменять на узбек.
        await call.message.edit_text(ru_text.settings.delete_age)


@router.message(GetAge.age)
async def get_age(message: Message, state: FSMContext):
    data = db.get_user_by_id(message.from_user.id)
    lang = data['language']
    try:
        age = int(message.text)
        if age > 0 and age < 99:
            await state.clear()

            db.update_users_column(message.from_user.id, "age", age)
            if lang == "ru":
                await message.answer(ru_text.settings.finish_age)
            else:
                #TODO поменять на узбек.
                await message.answer(ru_text.settings.finish_age)
        else:
            if lang == "ru":
                await message.answer(ru_text.settings.error_age, reply_markup=inline_kb.error_age(lang))
            else:
                #TODO поменять на узбек.
                await message.answer(ru_text.settings.error_age, reply_markup=inline_kb.error_age(lang))
    except ValueError:
        if lang == "ru":
            await message.answer(ru_text.settings.error_age, reply_markup=inline_kb.error_age(lang))
        else:
            # TODO поменять на узбек.
            await message.answer(ru_text.settings.error_age, reply_markup=inline_kb.error_age(lang))



@router.callback_query(Text("error_age"), GetAge.age)
async def age_cancel(call: CallbackQuery, state: FSMContext):
    await state.clear()

    await call.message.edit_text(ru_text.settings.age_cancel)