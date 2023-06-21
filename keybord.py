from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton #pip install aiogram 2.25.1

menu_change_test = InlineKeyboardMarkup(row_width=1)
menu_change_test_btn1 = InlineKeyboardButton(text="Начать тест по сердечно-лёгочной реанимации", callback_data="test_1")
menu_change_test.add(menu_change_test_btn1)

menu_change_test_obmorok = InlineKeyboardMarkup(row_width=1)
menu_change_test_btn_obmorok = InlineKeyboardButton(text="Начать тест по обмороку", callback_data="test_obmorok")
menu_change_test_obmorok.add(menu_change_test_btn_obmorok)


menu_change_test_utop = InlineKeyboardMarkup(row_width=1)
menu_change_test_btn_utop = InlineKeyboardButton(text="Начать тест по утоплению", callback_data="test_utop")
menu_change_test_utop.add(menu_change_test_btn_utop)

# menu_change_test_btn1 = InlineKeyboardButton(text="Тест на астению ШАС", callback_data="1_asthenia")
# menu_change_test_btn2 = InlineKeyboardButton(text="Тест на работу по призванию", callback_data="2_good_work")
# menu_change_test_btn3 = InlineKeyboardButton(text="Тест на гармоничные отношения", callback_data="3_good_relationships")
# menu_change_test_btn4 = InlineKeyboardButton(text="Тест на социофобию", callback_data="4_sociophobia")
# menu_change_test.add(menu_change_test_btn1, menu_change_test_btn2, menu_change_test_btn3, menu_change_test_btn4)

keyboard = InlineKeyboardMarkup()
# button = InlineKeyboardButton('Переходи по ссылке', url='https://google.com')
#keyboard.add(button)

class menu:
    def create(self):
        # Создание клавиатуры
        btn_start = KeyboardButton("⭐Начать обучение")
        btn_about = KeyboardButton("ℹ️ О проекте")
        btn_donat = KeyboardButton("Донат \n помощь проекту🙏")
        #btn_instructions = KeyboardButton("⚙Инструкции")  # "🔷 Инструкции"
        main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_start, btn_about, btn_donat)
        return (main_menu)

    def menu_stap1(self):
        menu_test_step_1_Button1 = KeyboardButton("А")
        menu_test_step_1_Button2 = KeyboardButton("Б")
        menu_test_step_1_Button3 = KeyboardButton("Отменить ввод")
        menu_test_step_1 = ReplyKeyboardMarkup(resize_keyboard=True).add(menu_test_step_1_Button1,
                                                                         menu_test_step_1_Button2,
                                                                         menu_test_step_1_Button3)

        return (menu_test_step_1)

    def menu_stap2(self):
        menu_test_step_2_Button1 = KeyboardButton("А")
        menu_test_step_2_Button2 = KeyboardButton("Б")

        menu_test_step_2_Button3 = KeyboardButton("Отменить ввод")
        menu_test_step_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(menu_test_step_2_Button1,
                                                                         menu_test_step_2_Button2,
                                                                         menu_test_step_2_Button3)

        return (menu_test_step_2)


   # кнопки ответов на второй тест на обморок


    def menu_good_work_stap1(self):
        menu_test_good_work_step_1_Button1 = KeyboardButton("А")
        menu_test_good_work_step_1_Button2 = KeyboardButton("Б")

        menu_test_good_work_step_1_Button3 = KeyboardButton("Отменить ввод")
        menu_test_good_work_step_1 = ReplyKeyboardMarkup(resize_keyboard=True).add(menu_test_good_work_step_1_Button1,
                                                                         menu_test_good_work_step_1_Button2,
                                                                         menu_test_good_work_step_1_Button3)


        return (menu_test_good_work_step_1)

    def menu_good_work_stap2(self):
        menu_test_good_work_step_2_Button1 = KeyboardButton("А")
        menu_test_good_work_step_2_Button2 = KeyboardButton("Б")
        menu_test_good_work_step_2_Button3 = KeyboardButton("В")
        menu_test_good_work_step_2_Button4 = KeyboardButton("Отменить ввод")
        menu_test_good_work_step_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(menu_test_good_work_step_2_Button1,
                                                                         menu_test_good_work_step_2_Button2,
                                                                         menu_test_good_work_step_2_Button3,
                                                                         menu_test_good_work_step_2_Button4)

        return (menu_test_good_work_step_2)



   # кнопки ответов на третий тест на утопление

    def menu_good_relationships_stap1(self):
        menu_test_good_relationships_step_1_Button1 = KeyboardButton("А")
        menu_test_good_relationships_step_1_Button2 = KeyboardButton("Б")
        menu_test_good_relationships_step_1_Button3 = KeyboardButton("В")

        menu_test_good_relationships_step_1_Button4 = KeyboardButton("Отменить ввод")
        menu_test_good_relationships_step_1 = ReplyKeyboardMarkup(resize_keyboard=True).add(menu_test_good_relationships_step_1_Button1,
                                                                                            menu_test_good_relationships_step_1_Button2,
                                                                                            menu_test_good_relationships_step_1_Button3,
                                                                                            menu_test_good_relationships_step_1_Button4)


        return (menu_test_good_relationships_step_1)

    def menu_good_relationships_stap2(self):
        menu_test_good_relationships_step_2_Button1 = KeyboardButton("А")
        menu_test_good_relationships_step_2_Button2 = KeyboardButton("Б")
        menu_test_good_relationships_step_2_Button3 = KeyboardButton("В")

        menu_test_good_relationships_step_2_Button4 = KeyboardButton("Отменить ввод")
        menu_test_good_relationships_step_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(menu_test_good_relationships_step_2_Button1,
                                                                                            menu_test_good_relationships_step_2_Button2,
                                                                                            menu_test_good_relationships_step_2_Button3,
                                                                                            menu_test_good_relationships_step_2_Button4)


        return (menu_test_good_relationships_step_2)

    def menu_good_relationships_stap3(self):
        menu_test_good_relationships_step_3_Button1 = KeyboardButton("А")
        menu_test_good_relationships_step_3_Button2 = KeyboardButton("Б")
        menu_test_good_relationships_step_3_Button3 = KeyboardButton("В")

        menu_test_good_relationships_step_3_Button4 = KeyboardButton("Отменить ввод")
        menu_test_good_relationships_step_3 = ReplyKeyboardMarkup(resize_keyboard=True).add(menu_test_good_relationships_step_3_Button1,
                                                                                            menu_test_good_relationships_step_3_Button2,
                                                                                            menu_test_good_relationships_step_3_Button3,
                                                                                            menu_test_good_relationships_step_3_Button4)


        return (menu_test_good_relationships_step_3)
