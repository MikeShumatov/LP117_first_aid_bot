from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from aiogram.dispatcher import FSMContext
from aiogram import types
from main import add_log, add_test  # , add_test_good_work, add_test_good_relationships, add_test_sociophobia
import keybord as kb
from states import profile, class_good_work, class_good_relationships, class_sociophobia


async def f_menu_main(message: types.Message, bot, main_menu, session: AsyncSession):
    if message.text == "⭐Начать обучение":
        await bot.send_video(message.from_user.id,
                             "BAACAgIAAxkBAAIBeWSEV0yLQ9qbS3lhLeggibwlfF9sAAJeLQACM_EhSO4gnK00zbBbLwQ",
                             protect_content=True)
        await message.answer(f"Пройдите тест", reply_markup=kb.menu_change_test)
    elif message.text == "ℹ️ О проекте":
        await about_project(message, bot, main_menu, session)
    elif message.text == "Донат \n помощь проекту🙏":
        await donat(message, bot, main_menu, session)


async def about_project(message: types.Message, bot, main_menu, session: AsyncSession):
    await message.answer(f"О проекте: \n" +
                         f" Создатель Михаил - мега крутой парень \n" +
                         f" напиши ему в личку: @Mike_shumatov"
                         , reply_markup=main_menu)
    await add_log(session, message)


async def donat(message: types.Message, bot, main_menu, session: AsyncSession):
    await message.answer(f"Поддержи проект: \n" +
                         f"Переведи любую сумму на сбер по номеру телефона: "
                         , reply_markup=main_menu)
    await message.answer(f"89272360355")
    await add_log(session, message)


# вставить перед вопросами
# await bot.send_video(message.from_user.id, BAACAgIAAxkBAAIBeWSEV0yLQ9qbS3lhLeggibwlfF9sAAJeLQACM_EhSO4gnK00zbBbLwQ, protect_content=True)

async def f_start_test_sash(message: types.Message, bot, main_menu, session: AsyncSession):
    # print(message.message.text)
    await add_log(session, message)
    menu_test_step_1 = kb.menu.menu_stap1(0)
    await bot.send_message(message.from_user.id, f"Первый вопрос: Клиническая смерть - это:",
                           reply_markup=menu_test_step_1)
    await bot.send_message(message.from_user.id, f"Варианты ответов:"
                                                 f"\n А: Обратимый этап умирания"
                                                 f"\n Б: Необратимый этап умирания",
                           reply_markup=menu_test_step_1)
    await profile.s_states1.set()


async def profile_s_states1(message: types.Message, session: AsyncSession, bot, state: FSMContext, main_menu):
    await add_log(session, message)
    answer = message.text
    if answer == "Отменить ввод":
        await bot.send_message(message.from_user.id, f"Ввод прекращен, данные не запоминались \n",
                               reply_markup=main_menu)
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, f"Ваш ответ - {answer}")
        await state.update_data(s_states1=answer)
        if answer == "Б":  # or "Б": or "В": - or не работает, поэтому использую elif
            await bot.send_message(message.from_user.id, f"Неверный ответ, попробуйте ещё раз")
            menu_test_step_1 = kb.menu.menu_stap1(0)
            await bot.send_message(message.from_user.id, f"Первый вопрос: Клиническая смерть - это:",
                                       reply_markup=menu_test_step_1)
            await bot.send_message(message.from_user.id, f"Варианты ответов:"
                                                             f"\n А: Обратимый этап умирания"
                                                             f"\n Б: Необратимый этап умирания",
                                       reply_markup=menu_test_step_1)
            await profile.s_states1.set()

        else:

            menu_test_step_2 = kb.menu.menu_stap2(0)
            await bot.send_message(message.from_user.id,
                                       f"Второй вопрос: Сколько вдохов и сколько нажатий делают при реанимации?\n",
                                       reply_markup=menu_test_step_2)
            await bot.send_message(message.from_user.id, f"Варианты ответов:"
                                                             f"\n А: 30 х 2"
                                                             f"\n Б: 20 х 2",
                                       reply_markup=menu_test_step_2)
            await profile.s_states2.set()


async def profile_s_states2(message: types.Message, session: AsyncSession, bot, state: FSMContext, main_menu):
    await add_log(session, message)
    answer = message.text
    if answer == "Отменить ввод":
        await bot.send_message(message.from_user.id, f"Ввод прекращен, данные не запоминались \n",
                               reply_markup=main_menu)
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, f"Ваш ответ - {answer}")
        await state.update_data(s_states2=answer)
        if answer == "Б":  # or "Б": or "В": - or не работает, поэтому использую elif
            await bot.send_message(message.from_user.id, f"Неверный ответ, попробуйте ещё раз")
            menu_test_step_2 = kb.menu.menu_stap2(0)
            await bot.send_message(message.from_user.id,
                                       f"Второй вопрос: Сколько вдохов и сколько нажатий делают при реанимации?\n",
                                       reply_markup=menu_test_step_2)
            await bot.send_message(message.from_user.id, f"Варианты ответов:"
                                                             f"\n А: 30 х 2"
                                                             f"\n Б: 20 х 2",
                                       reply_markup=menu_test_step_2)
            await profile.s_states2.set()


        else:

            await bot.send_message(message.from_user.id, f'Тест окончен \n Можно переходить к следующему видео.'
                                       , reply_markup=kb.keyboard)

            await bot.send_video(message.from_user.id,
                                     "BAACAgIAAxkBAAICBWSGN1wBotEHIGhwVg4eL4RHMEGQAAL9NAAC4qUxSGYEBRfTIiTWLwQ",
                                     protect_content=True)
            await message.answer(f"Пройдите тест", reply_markup=kb.menu_change_test_obmorok)
            await state.update_data(s_states3=None)
            await state.update_data(s_states4=None)
            await state.update_data(s_states5=None)
            await state.update_data(s_states6=None)

            await state.update_data(s_states7=None)
            await state.update_data(s_states8=None)
            await state.update_data(s_states9=None)
            await state.update_data(s_states10=None)

            data = await state.get_data()
            print(f"data: {data}")
            await add_test(session, message, 1, 'asthenia', data['s_states1'],
                           data['s_states2'],
                           data['s_states3'],
                           data['s_states4'],
                           data['s_states5'],
                           data['s_states6'],
                           data['s_states7'],
                           data['s_states8'],
                           data['s_states9'],
                           data['s_states10'])
            await state.finish()


# второй тест - на обморок

async def f_start_test_good_work(message: types.Message, bot, main_menu, session: AsyncSession):
    # print(message.message.text)
    await add_log(session, message)
    menu_test_good_work_step_1 = kb.menu.menu_good_work_stap1(0)
    await bot.send_message(message.from_user.id, f"Первый вопрос: обморок - это:",
                           reply_markup=menu_test_good_work_step_1)
    await bot.send_message(message.from_user.id, f"Варианты ответов: "
                                                 f"\n А: Потеря сознания не более 5 минут"
                                                 f"\n Б: Потеря сознания более 5 минут",
                           reply_markup=menu_test_good_work_step_1)
    await class_good_work.s_good_work_states1.set()


async def f_good_work_states1(message: types.Message, session: AsyncSession, bot, state: FSMContext, main_menu):
    await add_log(session, message)
    answer = message.text
    if answer == "Отменить ввод":
        await bot.send_message(message.from_user.id, f"Ввод прекращен, данные не запоминались \n",
                               reply_markup=main_menu)
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, f"Ваш ответ - {answer}")
        await state.update_data(s_good_work_states1=answer)
        if answer == "Б":
            await bot.send_message(message.from_user.id, f"Неверный ответ, попробуйте ещё раз")
            menu_test_good_work_step_1 = kb.menu.menu_good_work_stap1(0)
            await bot.send_message(message.from_user.id, f"Первый вопрос: обморок - это:",
                                       reply_markup=menu_test_good_work_step_1)
            await bot.send_message(message.from_user.id, f"Варианты ответов: "
                                                             f"\n А: Потеря сознания не более 5 минут"
                                                             f"\n Б: Потеря сознания более 5 минут",
                                       reply_markup=menu_test_good_work_step_1)
            await class_good_work.s_good_work_states1.set()
        else:
            menu_test_good_work_step_2 = kb.menu.menu_good_work_stap2(0)
            await bot.send_message(message.from_user.id,
                                       f"Второй вопрос: какое положение следует придать пострадавшему  при остановке дыхания? \n"
                                       , reply_markup=menu_test_good_work_step_2)
            await bot.send_message(message.from_user.id, f"Варианты ответов: \n А: Полулежа"
                                                             f"\n Б: Полусидя"
                                                             f"\n В: Горизонтальное, ноги выше уровня головы",
                                       reply_markup=menu_test_good_work_step_2)
            await class_good_work.s_good_work_states2.set()


async def f_good_work_states2(message: types.Message, session: AsyncSession, bot, state: FSMContext, main_menu):
    await add_log(session, message)
    answer = message.text
    if answer == "Отменить ввод":
        await bot.send_message(message.from_user.id, f"Ввод прекращен, данные не запоминались \n",
                               reply_markup=main_menu)
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, f"Ваш ответ - {answer}")
        await state.update_data(s_good_work_states2=answer)
        if answer == "А":
            await bot.send_message(message.from_user.id, f"Неверный ответ, попробуйте ещё раз")
            menu_test_good_work_step_2 = kb.menu.menu_good_work_stap2(0)
            await bot.send_message(message.from_user.id,
                                       f"Второй вопрос: какое положение следует придать пострадавшему  при остановке дыхания? \n"
                                       , reply_markup=menu_test_good_work_step_2)
            await bot.send_message(message.from_user.id, f"Варианты ответов: \n А: Полулежа"
                                                             f"\n Б: Полусидя"
                                                             f"\n В: Горизонтальное, ноги выше уровня головы",
                                       reply_markup=menu_test_good_work_step_2)
            await class_good_work.s_good_work_states2.set()

        elif answer == "Б":
            await bot.send_message(message.from_user.id, f"Неверный ответ, попробуйте ещё раз")
            menu_test_good_work_step_2 = kb.menu.menu_good_work_stap2(0)
            await bot.send_message(message.from_user.id,
                                       f"Второй вопрос: какое положение следует придать пострадавшему  при остановке дыхания? \n"
                                       , reply_markup=menu_test_good_work_step_2)
            await bot.send_message(message.from_user.id, f"Варианты ответов: \n А: Полулежа"
                                                             f"\n Б: Полусидя"
                                                             f"\n В: Горизонтальное, ноги выше уровня головы",
                                       reply_markup=menu_test_good_work_step_2)
            await class_good_work.s_good_work_states2.set()

        else:

                # await bot.send_message(message.from_user.id, f"Ваш ответ - {answer}", reply_markup=main_menu)
            await state.update_data(s_good_work_states2=answer)
            await bot.send_message(message.from_user.id, f'Тест окончен \n Можно переходить к следующему видео.'
                                       , reply_markup=kb.keyboard)
            await bot.send_video(message.from_user.id,
                                     "BAACAgIAAxkBAAICB2SGOt7Aa7OZVkSphEXTVCLdKtXCAAIINQAC4qUxSN1RrUTF5eAtLwQ",
                                     protect_content=True)
            await message.answer(f"Пройдите тест", reply_markup=kb.menu_change_test_utop)

            await state.update_data(s_good_work_states3=None)
            await state.update_data(s_good_work_states4=None)
            await state.update_data(s_good_work_states5=None)
            await state.update_data(s_good_work_states6=None)
            await state.update_data(s_good_work_states7=None)

            await state.update_data(s_good_work_states8=None)
            await state.update_data(s_good_work_states9=None)
            await state.update_data(s_good_work_states10=None)

            data = await state.get_data()
            print(f"data: {data}")
            await add_test(session, message, 2, 'good_work', data['s_good_work_states1'],
                           data['s_good_work_states2'],
                           data['s_good_work_states3'],
                           data['s_good_work_states4'],
                           data['s_good_work_states5'],
                           data['s_good_work_states6'],
                           data['s_good_work_states7'],
                           data['s_good_work_states8'],
                           data['s_good_work_states9'],
                           data['s_good_work_states10'])
            await state.finish()


# третий тест - на утопление

async def f_start_test_good_relationships(message: types.Message, bot, main_menu, session: AsyncSession):
    # print(message.message.text)
    await add_log(session, message)
    menu_test_good_relationships_step_1 = kb.menu.menu_good_relationships_stap1(0)
    await bot.send_message(message.from_user.id, f"Вопрос 1: утопление бывает:",
                           reply_markup=menu_test_good_relationships_step_1)
    await bot.send_message(message.from_user.id, f"Варианты ответов: "
                                                 f"\n А: Истинное"
                                                 f"\n Б: Ложное"
                                                 f"\n В: Истинное и ложное"
                           ,
                           reply_markup=menu_test_good_relationships_step_1)
    await class_good_relationships.s_good_relationships_states1.set()


async def f_good_relationships_states1(message: types.Message, session: AsyncSession, bot, state: FSMContext,
                                       main_menu):
    await add_log(session, message)
    answer = message.text
    if answer == "Отменить ввод":
        await bot.send_message(message.from_user.id, f"Ввод прекращен, данные не запоминались \n",
                               reply_markup=main_menu)
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, f"Ваш ответ - {answer}")
        await state.update_data(s_good_relationships_states1=answer)
        if answer == "А":
            await bot.send_message(message.from_user.id, f"Неверный ответ, попробуйте ещё раз")
            menu_test_good_relationships_step_1 = kb.menu.menu_good_relationships_stap1(0)
            await bot.send_message(message.from_user.id, f"Вопрос 1: утопление бывает:",
                                       reply_markup=menu_test_good_relationships_step_1)
            await bot.send_message(message.from_user.id, f"Варианты ответов: "
                                                             f"\n А: Истинное"
                                                             f"\n Б: Ложное"
                                                             f"\n В: Истинное и ложное"
                                       ,
                                       reply_markup=menu_test_good_relationships_step_1)
            await class_good_relationships.s_good_relationships_states1.set()
        elif answer == "Б":
            await bot.send_message(message.from_user.id, f"Неверный ответ, попробуйте ещё раз")
            menu_test_good_relationships_step_1 = kb.menu.menu_good_relationships_stap1(0)
            await bot.send_message(message.from_user.id, f"Вопрос 1: утопление бывает:",
                                       reply_markup=menu_test_good_relationships_step_1)
            await bot.send_message(message.from_user.id, f"Варианты ответов: "
                                                             f"\n А: Истинное"
                                                             f"\n Б: Ложное"
                                                             f"\n В: Истинное и ложное"
                                       ,
                                       reply_markup=menu_test_good_relationships_step_1)
            await class_good_relationships.s_good_relationships_states1.set()
        else:
            menu_test_good_relationships_step_2 = kb.menu.menu_good_relationships_stap2(0)
            await bot.send_message(message.from_user.id, f"Вопрос 2: Подплывать к пострадавшему нужно: \n",
                                       reply_markup=menu_test_good_relationships_step_2)
            await bot.send_message(message.from_user.id, f"Варианты ответов: "
                                                             f"\n А: Со спины"
                                                             f"\n Б: Спереди"
                                                             f"\n В: Со спины и сбоку"
                                       ,
                                       reply_markup=menu_test_good_relationships_step_2)
            await class_good_relationships.s_good_relationships_states2.set()


async def f_good_relationships_states2(message: types.Message, session: AsyncSession, bot, state: FSMContext,
                                       main_menu):
    await add_log(session, message)
    answer = message.text
    if answer == "Отменить ввод":
        await bot.send_message(message.from_user.id, f"Ввод прекращен, данные не запоминались \n",
                               reply_markup=main_menu)
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, f"Ваш ответ - {answer}")
        await state.update_data(s_good_relationships_states2=answer)
        if answer == "А":
            await bot.send_message(message.from_user.id, f"Неверный ответ, попробуйте ещё раз")
            menu_test_good_relationships_step_2 = kb.menu.menu_good_relationships_stap2(0)
            await bot.send_message(message.from_user.id, f"Вопрос 2: Подплывать к пострадавшему нужно: \n",
                                       reply_markup=menu_test_good_relationships_step_2)
            await bot.send_message(message.from_user.id, f"Варианты ответов: "
                                                             f"\n А: Со спины"
                                                             f"\n Б: Спереди"
                                                             f"\n В: Со спины и сбоку"
                                       ,
                                       reply_markup=menu_test_good_relationships_step_2)
            await class_good_relationships.s_good_relationships_states2.set()
        elif answer == "Б":
            await bot.send_message(message.from_user.id, f"Неверный ответ, попробуйте ещё раз")
            menu_test_good_relationships_step_2 = kb.menu.menu_good_relationships_stap2(0)
            await bot.send_message(message.from_user.id, f"Вопрос 2: Подплывать к пострадавшему нужно: \n",
                                       reply_markup=menu_test_good_relationships_step_2)
            await bot.send_message(message.from_user.id, f"Варианты ответов: "
                                                             f"\n А: Со спины"
                                                             f"\n Б: Спереди"
                                                             f"\n В: Со спины и сбоку"
                                       ,
                                       reply_markup=menu_test_good_relationships_step_2)
            await class_good_relationships.s_good_relationships_states2.set()
        else:

            menu_test_good_relationships_step_3 = kb.menu.menu_good_relationships_stap3(0)
            await bot.send_message(message.from_user.id, f"Вопрос 3: Пострадавшего нужно уложить: \n",
                                       reply_markup=menu_test_good_relationships_step_3)
            await bot.send_message(message.from_user.id, f"Варианты ответов:"
                                                             f"\n А: На спину"
                                                             f"\n Б: На бок"
                                                             f"\n В: Полулежа"
                                       ,
                                       reply_markup=menu_test_good_relationships_step_3)
            await class_good_relationships.s_good_relationships_states3.set()


async def f_good_relationships_states3(message: types.Message, session: AsyncSession, bot, state: FSMContext,
                                       main_menu):
    await add_log(session, message)
    answer = message.text
    if answer == "Отменить ввод":
        await bot.send_message(message.from_user.id, f"Ввод прекращен, данные не запоминались \n",
                               reply_markup=main_menu)
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, f"Ваш ответ - {answer}")
        await state.update_data(s_good_relationships_states3=answer)
        if answer == "Б":
            await bot.send_message(message.from_user.id, f"Неверный ответ, попробуйте ещё раз")
            menu_test_good_relationships_step_3 = kb.menu.menu_good_relationships_stap3(0)
            await bot.send_message(message.from_user.id, f"Вопрос 3: Пострадавшего нужно уложить: \n",
                                       reply_markup=menu_test_good_relationships_step_3)
            await bot.send_message(message.from_user.id, f"Варианты ответов:"
                                                             f"\n А: На спину"
                                                             f"\n Б: На бок"
                                                             f"\n В: Полулежа"
                                       ,
                                       reply_markup=menu_test_good_relationships_step_3)
            await class_good_relationships.s_good_relationships_states3.set()
        elif answer == "В":
            await bot.send_message(message.from_user.id, f"Неверный ответ, попробуйте ещё раз")
            menu_test_good_relationships_step_3 = kb.menu.menu_good_relationships_stap3(0)
            await bot.send_message(message.from_user.id, f"Вопрос 3: Пострадавшего нужно уложить: \n",
                                       reply_markup=menu_test_good_relationships_step_3)
            await bot.send_message(message.from_user.id, f"Варианты ответов:"
                                                             f"\n А: На спину"
                                                             f"\n Б: На бок"
                                                             f"\n В: Полулежа"
                                       ,
                                       reply_markup=menu_test_good_relationships_step_3)
            await class_good_relationships.s_good_relationships_states3.set()

        else:
                # await bot.send_message(message.from_user.id, f"Ваш ответ - {answer}", reply_markup=main_menu)
            await state.update_data(s_good_relationships_states3=answer)
            await bot.send_message(message.from_user.id, f'Тест окончен \n Поздравляем! Вы прошли три теста!:'
                                       #,reply_markup=kb.keyboard)
                                       ,reply_markup=main_menu)
            await state.update_data(s_good_relationships_states4=None)
            await state.update_data(s_good_relationships_states5=None)
            await state.update_data(s_good_relationships_states6=None)
            await state.update_data(s_good_relationships_states7=None)
            await state.update_data(s_good_relationships_states8=None)
            await state.update_data(s_good_relationships_states9=None)
            await state.update_data(s_good_relationships_states10=None)

            data = await state.get_data()
            print(f"data: {data}")
            await add_test(session, message, 3, 'good_relationships', data['s_good_relationships_states1'],
                               data['s_good_relationships_states2'],
                               data['s_good_relationships_states3'],
                               data['s_good_relationships_states4'],
                               data['s_good_relationships_states5'],
                               data['s_good_relationships_states6'],
                               data['s_good_relationships_states7'],
                               data['s_good_relationships_states8'],
                               data['s_good_relationships_states9'],
                               data['s_good_relationships_states10'])
            await state.finish()
