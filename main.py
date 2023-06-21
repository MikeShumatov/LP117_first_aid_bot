from mysql.connector import Error  # pip install mysql-connector-python
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton  # pip install aiogram 2.25.1
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # pip install aiogram
# pip install aiomysql
from sqlalchemy import Column, Integer, BigInteger, DateTime, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy import select, update, delete  # pip install sqlalchemy
from sqlalchemy.dialects.mysql import insert
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # Для хранения данных в ОЗУ для машины состояний
from aiogram.dispatcher import FSMContext
import states as st

import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine, DateTime, BigInteger
from sqlalchemy.orm import sessionmaker
from aiogram.dispatcher.middlewares import BaseMiddleware
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine  # pip install aiomysql
from datetime import datetime
# -------------------
import keybord as kb
import call_bakc_query as cc
from states import profile, class_good_work, class_good_relationships, class_sociophobia
from admin import *

# важен порядок в коде
# Создание БД
# этот кусок кода не менять ни в коем случае до main_menu
Base = declarative_base()
metadata = Base.metadata

main_menu = kb.menu.create(0)


# Модели - таблица
class T_User(Base):
    __tablename__ = 't_user'
    # user_id = Column(BigInteger, unique=True, nullable=False, primary_key=True)
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, unique=False, nullable=False)
    s_username = Column(String, unique=False, nullable=False)
    s_first_name = Column(String, unique=False, nullable=False)
    s_last_name = Column(String, unique=False, nullable=False)
    s_language_code = Column(String, unique=False, nullable=False)
    s_is_premium = Column(String, unique=False, nullable=False)
    dt_dateupd = Column(DateTime, unique=False, nullable=False)


class T_Log(Base):
    __tablename__ = 't_log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, unique=False, nullable=False)
    s_username = Column(String, unique=False, nullable=False)
    s_first_name = Column(String, unique=False, nullable=False)
    s_last_name = Column(String, unique=False, nullable=False)
    s_language_code = Column(String, unique=False, nullable=False)
    s_is_premium = Column(String, unique=False, nullable=False)
    s_text = Column(String, unique=False, nullable=False)
    dt_dateupd = Column(DateTime, unique=False, nullable=False)


# class T_Test(Base):
#     __tablename__ = 't_test'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(BigInteger, unique=False, nullable=False)
#     s_username = Column(String, unique=False, nullable=False)
#     s_first_name = Column(String, unique=False, nullable=False)
#     s_last_name = Column(String, unique=False, nullable=False)
#     s_language_code = Column(String, unique=False, nullable=False)
#     s_is_premium = Column(String, unique=False, nullable=False)
#     s_text = Column(String, unique=False, nullable=False)
#     dt_dateupd = Column(DateTime, unique=False, nullable=False)
#     s_state1 = Column(String, unique=False, nullable=False)
#     s_state2 = Column(String, unique=False, nullable=False)
#     s_state3 = Column(String, unique=False, nullable=False)
#     s_state4 = Column(String, unique=False, nullable=False)
#     s_state5 = Column(String, unique=False, nullable=False)
#     s_state6 = Column(String, unique=False, nullable=False)
#
#
# class T_Test_good_work(Base):
#     __tablename__ = 't_test_good_work'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(BigInteger, unique=False, nullable=False)
#     s_username = Column(String, unique=False, nullable=False)
#     s_first_name = Column(String, unique=False, nullable=False)
#     s_last_name = Column(String, unique=False, nullable=False)
#     s_language_code = Column(String, unique=False, nullable=False)
#     s_is_premium = Column(String, unique=False, nullable=False)
#     s_text = Column(String, unique=False, nullable=False)
#     dt_dateupd = Column(DateTime, unique=False, nullable=False)
#     s_good_work_states1 = Column(String, unique=False, nullable=False)
#     s_good_work_states2 = Column(String, unique=False, nullable=False)
#     s_good_work_states3 = Column(String, unique=False, nullable=False)
#     s_good_work_states4 = Column(String, unique=False, nullable=False)
#     s_good_work_states5 = Column(String, unique=False, nullable=False)
#     s_good_work_states6 = Column(String, unique=False, nullable=False)
#     s_good_work_states7 = Column(String, unique=False, nullable=False)


# class T_Test_good_relationships(Base):
#     __tablename__ = 't_test_good_relationships'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(BigInteger, unique=False, nullable=False)
#     s_username = Column(String, unique=False, nullable=False)
#     s_first_name = Column(String, unique=False, nullable=False)
#     s_last_name = Column(String, unique=False, nullable=False)
#     s_language_code = Column(String, unique=False, nullable=False)
#     s_is_premium = Column(String, unique=False, nullable=False)
#     s_text = Column(String, unique=False, nullable=False)
#     dt_dateupd = Column(DateTime, unique=False, nullable=False)
#     s_good_relationships_states1 = Column(String, unique=False, nullable=False)
#     s_good_relationships_states2 = Column(String, unique=False, nullable=False)
#     s_good_relationships_states3 = Column(String, unique=False, nullable=False)
#     s_good_relationships_states4 = Column(String, unique=False, nullable=False)
#     s_good_relationships_states5 = Column(String, unique=False, nullable=False)
#     s_good_relationships_states6 = Column(String, unique=False, nullable=False)
#     s_good_relationships_states7 = Column(String, unique=False, nullable=False)


# class T_Test_sociophobia(Base):
#     __tablename__ = 't_test_sociophobia'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(BigInteger, unique=False, nullable=False)
#     s_username = Column(String, unique=False, nullable=False)
#     s_first_name = Column(String, unique=False, nullable=False)
#     s_last_name = Column(String, unique=False, nullable=False)
#     s_language_code = Column(String, unique=False, nullable=False)
#     s_is_premium = Column(String, unique=False, nullable=False)
#     s_text = Column(String, unique=False, nullable=False)
#     dt_dateupd = Column(DateTime, unique=False, nullable=False)
#     s_sociophobia_states1 = Column(String, unique=False, nullable=False)
#     s_sociophobia_states2 = Column(String, unique=False, nullable=False)
#     s_sociophobia_states3 = Column(String, unique=False, nullable=False)
#     s_sociophobia_states4 = Column(String, unique=False, nullable=False)
#     s_sociophobia_states5 = Column(String, unique=False, nullable=False)
#     s_sociophobia_states6 = Column(String, unique=False, nullable=False)
#     s_sociophobia_states7 = Column(String, unique=False, nullable=False)
#     s_sociophobia_states8 = Column(String, unique=False, nullable=False)


class T_General_test(Base):
    __tablename__ = 't_general_test'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, unique=False, nullable=False)
    s_username = Column(String, unique=False, nullable=False)
    s_first_name = Column(String, unique=False, nullable=False)
    s_last_name = Column(String, unique=False, nullable=False)
    s_language_code = Column(String, unique=False, nullable=False)
    s_is_premium = Column(String, unique=False, nullable=False)
    s_text = Column(String, unique=False, nullable=False)
    dt_dateupd = Column(DateTime, unique=False, nullable=False)
    s_states1 = Column(String, unique=False, nullable=False)
    s_states2 = Column(String, unique=False, nullable=False)
    s_states3 = Column(String, unique=False, nullable=False)
    s_states4 = Column(String, unique=False, nullable=False)
    s_states5 = Column(String, unique=False, nullable=False)
    s_states6 = Column(String, unique=False, nullable=False)
    s_states7 = Column(String, unique=False, nullable=False)
    s_states8 = Column(String, unique=False, nullable=False)
    s_states9 = Column(String, unique=False, nullable=False)
    s_states10 = Column(String, unique=False, nullable=False)
    i_type_test_id = Column(Integer, unique=False, nullable=False)
    s_type_test = Column(String, unique=False, nullable=False)

# это генератор сессий, этот кусок кода не менять ни в коем случае
class DbSessionMiddleware(BaseMiddleware):
    def __init__(self, session_pool):
        self.session_pool = session_pool
        super(DbSessionMiddleware, self).__init__()

    async def on_pre_process_message(self, message: types.Message, data: dict):
        session = self.session_pool()
        data['session'] = session

    async def on_pre_process_callback_query(self, callback: types.CallbackQuery, data: dict):
        session = self.session_pool()
        data['session'] = session

    # Важно оставить этот код что бы закрывать сессии
    async def on_post_process_message(self, message: types.Message, data_from_filter: list, data: dict):
        session = data['session']
        await session.close()

    async def on_post_process_callback_query(self, callback: types.CallbackQuery, data_from_filter: list, data: dict):
        session = data['session']
        await session.close()


# Если у нас пользователь_ид не уникален, то мы не реагируем(обработка через - .on_conflict_do_nothing(index_elements=['user_id']) )
# Для MySQL
async def add_user(session: AsyncSession, message: types.Message):
    stmt = insert(T_User).values(user_id=message.from_id,
                                 s_username=message.from_user.username,
                                 s_first_name=message.from_user.first_name,
                                 s_last_name=message.from_user.last_name,
                                 s_language_code=message.from_user.language_code,
                                 s_is_premium=message.from_user.is_premium,
                                 dt_dateupd=datetime.now()
                                 ).prefix_with('IGNORE')
    await session.execute(stmt)
    await session.commit()

async def add_test(session: AsyncSession, message: types.Message, i_type_test_id, s_type_test, s_states1, s_states2, s_states3, s_states4, s_states5, s_states6, s_states7, s_states8, s_states9, s_states10):
    stmt = insert(T_General_test).values(user_id=message.from_id,
                                 s_username=message.from_user.username,
                                 s_first_name=message.from_user.first_name,
                                 s_last_name=message.from_user.last_name,
                                 s_language_code=message.from_user.language_code,
                                 s_is_premium=message.from_user.is_premium,
                                 s_text=message.text,
                                 dt_dateupd=datetime.now(),
                                 s_states1=s_states1,
                                 s_states2=s_states2,
                                 s_states3=s_states3,
                                 s_states4=s_states4,
                                 s_states5=s_states5,
                                 s_states6=s_states6,
                                 s_states7=s_states7,
                                 s_states8=s_states8,
                                 s_states9=s_states9,
                                 s_states10=s_states10,
                                 i_type_test_id=i_type_test_id,
                                 s_type_test=s_type_test
                                 ).prefix_with('IGNORE')
    await session.execute(stmt)
    await session.commit()
    print(f"::: message ::: {message}")


# async def add_test(session: AsyncSession, message: types.Message,
#                    data):  # s_state1,s_state2,s_state3,s_state4, s_state5, s_state5):
#     stmt = insert(T_Test).values(user_id=message.from_id,
#                                  s_username=message.from_user.username,
#                                  s_first_name=message.from_user.first_name,
#                                  s_last_name=message.from_user.last_name,
#                                  s_language_code=message.from_user.language_code,
#                                  s_is_premium=message.from_user.is_premium,
#                                  s_text=message.text,
#                                  dt_dateupd=datetime.now(),
#                                  s_state1=data['s_states1'],
#                                  s_state2=data['s_states2'],
#                                  s_state3=data['s_states3'],
#                                  s_state4=data['s_states4'],
#                                  s_state5=data['s_states5'],
#                                  s_state6=data['s_states6']
#                                  ).prefix_with('IGNORE')
#     await session.execute(stmt)
#     await session.commit()
#     print(f"::: message ::: {message}")
#
#
# async def add_test_good_work(session: AsyncSession, message: types.Message,
#                    data):
#     stmt = insert(T_Test_good_work).values(user_id=message.from_id,
#                                  s_username=message.from_user.username,
#                                  s_first_name=message.from_user.first_name,
#                                  s_last_name=message.from_user.last_name,
#                                  s_language_code=message.from_user.language_code,
#                                  s_is_premium=message.from_user.is_premium,
#                                  s_text=message.text,
#                                  dt_dateupd=datetime.now(),
#                                  s_good_work_states1=data['s_good_work_states1'],
#                                  s_good_work_states2=data['s_good_work_states2'],
#                                  s_good_work_states3=data['s_good_work_states3'],
#                                  s_good_work_states4=data['s_good_work_states4'],
#                                  s_good_work_states5=data['s_good_work_states5'],
#                                  s_good_work_states6=data['s_good_work_states6'],
#                                  s_good_work_states7=data['s_good_work_states7']
#                                  ).prefix_with('IGNORE')
#     await session.execute(stmt)
#     await session.commit()
#     print(f"::: message ::: {message}")
#
# async def add_test_good_relationships(session: AsyncSession, message: types.Message,
#                    data):
#     stmt = insert(T_Test_good_relationships).values(user_id=message.from_id,
#                                  s_username=message.from_user.username,
#                                  s_first_name=message.from_user.first_name,
#                                  s_last_name=message.from_user.last_name,
#                                  s_language_code=message.from_user.language_code,
#                                  s_is_premium=message.from_user.is_premium,
#                                  s_text=message.text,
#                                  dt_dateupd=datetime.now(),
#                                  s_good_relationships_states1=data['s_good_relationships_states1'],
#                                  s_good_relationships_states2=data['s_good_relationships_states2'],
#                                  s_good_relationships_states3=data['s_good_relationships_states3'],
#                                  s_good_relationships_states4=data['s_good_relationships_states4'],
#                                  s_good_relationships_states5=data['s_good_relationships_states5'],
#                                  s_good_relationships_states6=data['s_good_relationships_states6'],
#                                  s_good_relationships_states7=data['s_good_relationships_states7']
#                                  ).prefix_with('IGNORE')
#     await session.execute(stmt)
#     await session.commit()
#     print(f"::: message ::: {message}")
#
#
# async def add_test_sociophobia(session: AsyncSession, message: types.Message,
#                    data):
#     stmt = insert(T_Test_sociophobia).values(user_id=message.from_id,
#                                  s_username=message.from_user.username,
#                                  s_first_name=message.from_user.first_name,
#                                  s_last_name=message.from_user.last_name,
#                                  s_language_code=message.from_user.language_code,
#                                  s_is_premium=message.from_user.is_premium,
#                                  s_text=message.text,
#                                  dt_dateupd=datetime.now(),
#                                  s_sociophobia_states1=data['s_sociophobia_states1'],
#                                  s_sociophobia_states2=data['s_sociophobia_states2'],
#                                  s_sociophobia_states3=data['s_sociophobia_states3'],
#                                  s_sociophobia_states4=data['s_sociophobia_states4'],
#                                  s_sociophobia_states5=data['s_sociophobia_states5'],
#                                  s_sociophobia_states6=data['s_sociophobia_states6'],
#                                  s_sociophobia_states7=data['s_sociophobia_states7'],
#                                  s_sociophobia_states8=data['s_sociophobia_states8']
#                                  ).prefix_with('IGNORE')
#     await session.execute(stmt)
#     await session.commit()
#     print(f"::: message ::: {message}")


async def add_log(session: AsyncSession, message: types.Message):
    try:
        stmt = insert(T_Log).values(user_id=message.from_id,
                                s_username=message.from_user.username,
                                s_first_name=message.from_user.first_name,
                                s_last_name=message.from_user.last_name,
                                s_language_code=message.from_user.language_code,
                                s_is_premium=message.from_user.is_premium,
                                s_text=message.text,
                                dt_dateupd=datetime.now()
                                ).prefix_with('IGNORE')
    except:
        stmt = insert(T_Log).values(user_id=message.from_user.id,
                                    s_username=message.from_user.username,
                                    s_first_name=message.from_user.first_name,
                                    s_last_name=message.from_user.last_name,
                                    s_language_code=message.from_user.language_code,
                                    s_is_premium=message.from_user.is_premium,
                                    s_text=message.message.text,
                                    dt_dateupd=datetime.now()
                                    ).prefix_with('IGNORE')
    await session.execute(stmt)
    await session.commit()
    print(f"::: message ::: {message}")


# async def delete_user(session: AsyncSession, user_id: int):
# на основе этих трёх функций можно реализовывать КРУДы с пользователями
async def delete_user(session: AsyncSession, user_id):
    await session.execute(
        delete(T_User)
        .where(T_User.user_id == user_id)
    )
    await session.commit()


async def update_user(session: AsyncSession, user_id: int, input_name: str):
    await session.execute(
        update(T_User)
        .where(T_User.user_id == user_id)  # фильтр
        .values(user_name=input_name)  # пользовательское поле для апдейта
    )
    await session.commit()


async def select_users(session: AsyncSession):
    all_users = await session.execute(
        select(T_User)
    )
    # print(f"all_users.scalars().all() - ",all_users.scalars().all())
    return all_users.scalars().all()  # чтобы не выводились беспорядочные тюплы, а выводилось все грамотно, не выведет ошибку если ничего не возвращено(вернет None)


async def select_users2(session: AsyncSession):  # другой вариант выведения кода сверху
    all_user = await session.scalars(
        select(T_User)
    )
    return all_user.all()


async def on_startup(dispatcher):
    engine = create_async_engine("mysql+aiomysql://usr:12345@localhost/db_bot", echo=False)
    db_pool = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
    dp.middleware.setup(DbSessionMiddleware(db_pool))


bot = Bot(token='6010018100:AAFVYpKOIBo4nVGDbxiFB_qQrYZOcGdBv-o'
          , parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Дальше идут наши хендлеры и обработчики
@dp.message_handler(commands=['start'])
async def start_com(message: types.Message, session: AsyncSession):
    print(datetime.now())
    await add_user(session, message)  # Добавление пользователя
    print("message: ", message)
    print("message: ", message.from_id, message.from_user.username, message.from_user.first_name,
          message.from_user.last_name, message.from_user.is_premium)
    await message.answer(f"Добро пожаловать, {message.from_user.first_name}", reply_markup=main_menu)
    await message.answer(f"Это бот «Успей спасти жизнь». Он - ваш личный интерактивный ассистент. Под его руководством вы узнаете, как оказывать помощь пострадавшим, получите инструкции по оказанию экстренной помощи.", reply_markup=main_menu)


@dp.callback_query_handler(text='delete_user')
async def delete_user_callback(callback: types.CallbackQuery, session: AsyncSession):
    await delete_user(session, callback.message.from_id)
    await callback.message.edit_text('Вы были удалены из базы данных')


@dp.message_handler()
async def messages(message: types.Message, session: AsyncSession):
    await cc.f_menu_main(message, bot, main_menu, session)
    print(message)


@dp.message_handler(state=profile.s_states1)
async def s_states1(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.profile_s_states1(message, session, bot, state, main_menu)


@dp.message_handler(state=profile.s_states2)
async def s_states2(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.profile_s_states2(message, session, bot, state, main_menu)


@dp.message_handler(state=profile.s_states3)
async def s_states3(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.profile_s_states3(message, session, bot, state, main_menu)


@dp.message_handler(state=profile.s_states4)
async def s_states4(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.profile_s_states4(message, session, bot, state, main_menu)


@dp.message_handler(state=profile.s_states5)
async def s_states5(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.profile_s_states5(message, session, bot, state, main_menu)

@dp.message_handler(state=profile.s_states6)
async def s_states6(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.profile_s_states6(message, session, bot, state, main_menu)





@dp.callback_query_handler(text="test_1")
async def start_test_sash(message: types.Message, session: AsyncSession):
    await cc.f_start_test_sash(message, bot, main_menu, session)



#хендлеры для второго теста - на работу по призванию


@dp.message_handler(state=class_good_work.s_good_work_states1)
async def s_good_work_states1(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_good_work_states1(message, session, bot, state, main_menu)


@dp.message_handler(state=class_good_work.s_good_work_states2)
async def s_good_work_states2(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_good_work_states2(message, session, bot, state, main_menu)


@dp.message_handler(state=class_good_work.s_good_work_states3)
async def s_good_work_states3(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_good_work_states3(message, session, bot, state, main_menu)


@dp.message_handler(state=class_good_work.s_good_work_states4)
async def s_good_work_states4(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_good_work_states4(message, session, bot, state, main_menu)


@dp.message_handler(state=class_good_work.s_good_work_states5)
async def s_good_work_states5(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_good_work_states5(message, session, bot, state, main_menu)

@dp.message_handler(state=class_good_work.s_good_work_states6)
async def s_good_work_states6(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_good_work_states6(message, session, bot, state, main_menu)

@dp.message_handler(state=class_good_work.s_good_work_states7)
async def s_good_work_states7(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_good_work_states7(message, session, bot, state, main_menu)


@dp.callback_query_handler(text="test_obmorok")
async def start_test_good_work(message: types.Message, session: AsyncSession):
    await cc.f_start_test_good_work(message, bot, main_menu, session)

#хендлеры для третьего теста - на гармоничные отношения


@dp.message_handler(state=class_good_relationships.s_good_relationships_states1)
async def s_good_relationships_states1(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_good_relationships_states1(message, session, bot, state, main_menu)


@dp.message_handler(state=class_good_relationships.s_good_relationships_states2)
async def s_good_relationships_states2(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_good_relationships_states2(message, session, bot, state, main_menu)


@dp.message_handler(state=class_good_relationships.s_good_relationships_states3)
async def s_good_relationships_states3(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_good_relationships_states3(message, session, bot, state, main_menu)


@dp.message_handler(state=class_good_relationships.s_good_relationships_states4)
async def s_good_relationships_states4(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_good_relationships_states4(message, session, bot, state, main_menu)


@dp.message_handler(state=class_good_relationships.s_good_relationships_states5)
async def s_good_relationships_states5(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_good_relationships_states5(message, session, bot, state, main_menu)

@dp.message_handler(state=class_good_relationships.s_good_relationships_states6)
async def s_good_relationships_states6(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_good_relationships_states6(message, session, bot, state, main_menu)

@dp.message_handler(state=class_good_relationships.s_good_relationships_states7)
async def s_good_relationships_states7(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_good_relationships_states7(message, session, bot, state, main_menu)


@dp.callback_query_handler(text="test_utop")
async def start_test_good_relationships(message: types.Message, session: AsyncSession):
    await cc.f_start_test_good_relationships(message, bot, main_menu, session)


#хендлеры для четвёртого теста - на социофобию


@dp.message_handler(state=class_sociophobia.s_sociophobia_states1)
async def s_sociophobia_states1(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_sociophobia_states1(message, session, bot, state, main_menu)


@dp.message_handler(state=class_sociophobia.s_sociophobia_states2)
async def s_sociophobia_states2(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_sociophobia_states2(message, session, bot, state, main_menu)


@dp.message_handler(state=class_sociophobia.s_sociophobia_states3)
async def s_sociophobia_states3(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_sociophobia_states3(message, session, bot, state, main_menu)


@dp.message_handler(state=class_sociophobia.s_sociophobia_states4)
async def s_sociophobia_states4(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_sociophobia_states4(message, session, bot, state, main_menu)


@dp.message_handler(state=class_sociophobia.s_sociophobia_states5)
async def s_sociophobia_states5(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_sociophobia_states5(message, session, bot, state, main_menu)

@dp.message_handler(state=class_sociophobia.s_sociophobia_states6)
async def s_sociophobia_states6(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_sociophobia_states6(message, session, bot, state, main_menu)

@dp.message_handler(state=class_sociophobia.s_sociophobia_states7)
async def s_sociophobia_states7(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_sociophobia_states7(message, session, bot, state, main_menu)

@dp.message_handler(state=class_sociophobia.s_sociophobia_states8)
async def s_sociophobia_states8(message: types.Message, state: FSMContext, session: AsyncSession):
    await cc.f_sociophobia_states8(message, session, bot, state, main_menu)


@dp.callback_query_handler(text="4_sociophobia")
async def start_test_sociophobia(message: types.Message, session: AsyncSession):
    await cc.f_start_test_sociophobia(message, bot, main_menu, session)


@dp.message_handler(content_types="video")
async def get_file_id_p(message: types.Message):
    print (f"::: message ::: {message}")
    if str(message.from_id) in str(ADMIN_ID):
        await bot.send_message(message.from_user.id, message.video.file_id)



# Стоит вконце программы, просто что бы программа все время работала
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup,
                           skip_updates=True)  # Updates were skipped successfully. - бот пропускает все что ему отправили пока он был выключен
