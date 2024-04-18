import helpfull_stuff
import game as gm
import requests
import datetime
import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

BD = {}
gms = []

KEY = 'bed4363a34565fc32ca5bc2e78d2ed25'
TOKEN = " "
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def help_mes(msg: types.Message):
    await msg.reply(f'{msg.from_user.first_name}, ' +
                    helpfull_stuff.help_str_1)
    print(msg.from_user.id)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Хочу поиграть в Виселицу")],
        [types.KeyboardButton(text="Хочу узнать погоду")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        input_field_placeholder="Выберите возможную активность"
    )
    await message.answer("Что вы хотите сделать?", reply_markup=keyboard)
    print(message.from_user.id)


@dp.message_handler(lambda message: message.text in helpfull_stuff.help_arr_5)
async def handle_location(message: types.Message):
    city = helpfull_stuff.help_dict_3[message.text]
    URL = helpfull_stuff.help_str_4 + city + f"&appid={KEY}&units=metric"
    response = requests.get(URL).json()
    temp_aver = response["main"]["temp"]
    temp_high = response["main"]["temp_max"]
    temp_low_ = response["main"]["temp_min"]
    rise = datetime.datetime.fromtimestamp(response["sys"]["sunrise"])
    set_ = datetime.datetime.fromtimestamp(response["sys"]["sunset"])
    description = response["weather"][0]["description"]
    help_1 = f"Сейчас в городе {message.text}: {description}\n"
    help_2 = f"Средняя температура: {temp_aver}°C\n"
    help_3 = f"Максимальная температура: {temp_high}°C\n"
    help_4 = f"Минимальная температура: {temp_low_}°C\n"
    help_3 = f"Максимальная температура: {temp_high}°C\n"
    help_4 = f"Минимальная температура: {temp_low_}°C\n"
    help_5 = f"Время восхода: {rise}\n"
    help_6 = f"Время заката: {set_}\n"
    help_7 = f"Продолжительность светого дня: {set_ - rise}\n"
    help_ = help_1 + help_2 + help_3 + help_4 + help_5 + help_6 + help_7
    await bot.send_message(chat_id=message.chat.id, text=help_)
    print(message.from_user.id, message.text)


@dp.message_handler(lambda message: message.text in helpfull_stuff.help_arr_2)
async def get_text_messages(msg: types.Message):
    kb = [
        [types.KeyboardButton(text="Легкий")],
        [types.KeyboardButton(text="Средний")],
        [types.KeyboardButton(text="Сложный")],
        [types.KeyboardButton(text="Начать сначала")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        input_field_placeholder="Какой уровень сложности вы хотите?"
    )
    await msg.reply(helpfull_stuff.help_str_2, reply_markup=keyboard)
    print(msg.from_user.id, msg.text)


@dp.message_handler(lambda message: message.text == "Хочу узнать погоду")
async def weather(msg: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True, row_width=3,
        input_field_placeholder="Погоду в каком месты вы хотите узнать?"
    )
    keyboard.row(types.KeyboardButton(text="Начать сначала"))
    keyboard.row(
        types.KeyboardButton(text="Каир"),
        types.KeyboardButton(text="Дубай"),
        types.KeyboardButton(text="Эр-Рияд"),
        types.KeyboardButton(text="Рим")
    )
    keyboard.row(
        types.KeyboardButton(text="Лондон"),
        types.KeyboardButton(text="Сингапур"),
        types.KeyboardButton(text="Мадрид")
    )
    keyboard.row(
        types.KeyboardButton(text="Барселона"),
        types.KeyboardButton(text="Вашингтон"),
        types.KeyboardButton(text="Берлин")
    )
    keyboard.row(
        types.KeyboardButton(text="Нью-Йорк"),
        types.KeyboardButton(text="Лос-Анжелес"),
        types.KeyboardButton(text="Маями")
    )
    keyboard.row(
        types.KeyboardButton(text="Неаполь"),
        types.KeyboardButton(text="Мехико"),
        types.KeyboardButton(text="Буэнос-Айрес")
    )
    keyboard.row(
        types.KeyboardButton(text="Мельбурн"),
        types.KeyboardButton(text="Москва"),
        types.KeyboardButton(text="Париж")
    )
    keyboard.row(
        types.KeyboardButton(text="Токио"),
        types.KeyboardButton(text="Пекин"),
        types.KeyboardButton(text="Сеул")
    )
    keyboard.row(
        types.KeyboardButton(text="Сантьяго-де-Чили"),
        types.KeyboardButton(text="Санкт-Петербург")
    )
    await msg.reply("Выберите место, в котором вы хотите узнать погоду",
                    reply_markup=keyboard)
    print(msg.from_user.id, msg.text)


@dp.message_handler(lambda message: message.text == "Начать сначала")
async def from_beginning(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Хочу поиграть в Виселицу")],
        [types.KeyboardButton(text="Хочу узнать погоду")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        input_field_placeholder="Выберите возможную активность"
    )
    await message.answer("Что вы хотите сделать?", reply_markup=keyboard)
    print(message.from_user.id, "начало")


@dp.message_handler(lambda message: message.text in helpfull_stuff.help_arr_1)
async def mode_type(message: types.Message):
    kb = [
        [types.KeyboardButton(text="1-2 буквы")],
        [types.KeyboardButton(text="3-5 букв")],
        [types.KeyboardButton(text="Хочу хардкор (0 букв)")],
        [types.KeyboardButton(text="Начать сначала")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        input_field_placeholder="Сколько букв вы хотите открыть заранее?"
    )
    game = gm.Game()
    game.at = helpfull_stuff.help_dict_2[message.text]
    BD[message.from_user.id] = game
    # gms.append(game)
    await message.reply(f'Отлично, Вы выбрали {message.text.lower()} режим. '
                        + helpfull_stuff.help_str_3, reply_markup=keyboard)
    print(message.from_user.id, message.text)


@dp.message_handler(lambda message: message.text in helpfull_stuff.help_arr_3)
async def amount_of_letters(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Давай же начнем!")],
        [types.KeyboardButton(text="Начать сначала")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        input_field_placeholder="Скорее начинаем!"
    )
    await message.reply('Отлично, Вы выбрали режим и количество открытых букв.'
                        + ' Давай-те же начнем игру', reply_markup=keyboard)
    print(message.from_user.id, message.text)
    BD[message.from_user.id].amount_letters = random.choice(
        helpfull_stuff.help_dict_1[message.text])
    BD[message.from_user.id].create()
    # gms[len(gms) - 1].amount_letters = random.choice(
    #     helpfull_stuff.help_dict_1[message.text])
    # gms[len(gms) - 1].create()


@dp.message_handler(lambda message: message.text == "Давай же начнем!")
async def the_game(message: types.Message):
    key = types.ReplyKeyboardMarkup(
        input_field_placeholder="Введите одну букву"
    )
    # i = len(gms) - 1
    i = message.from_user.id
    help_str = "Отгадайте это слово. У вас " + f'{BD[i].at} попыток' + "\n"
    await message.reply(help_str + f'{BD[i].out()}', reply_markup=key)


@dp.message_handler(lambda message: message.text in helpfull_stuff.help_arr_4)
async def check_letter(message: types.Message):
    # i = len(gms) - 1
    i = message.from_user.id
    letter = message.text.lower()
    if letter in helpfull_stuff.help_arr_4:
        if letter in BD[i].already_open:
            await message.reply("Эта буква уже была. Попробуйте другую. " +
                                f'У Вас все еще {BD[i].at} жизней' +
                                f'\n{BD[i].out()}',
                                reply_markup=types.ReplyKeyboardRemove())
        elif letter in BD[i].exist:
            for j in range(len(BD[i].word)):
                if letter == BD[i].word[j]:
                    BD[i].pat[j] = letter
                    BD[i].number_letters += 1
            if BD[i].number_letters == len(BD[i].word):
                await message.reply("Вы отгадали слово!\n" +
                                    f'{BD[i].word}')
                kb = [
                    [types.KeyboardButton(text="Хочу снова " +
                                          "поиграть в Виселицу")],
                    [types.KeyboardButton(text="Хочу узнать погоду")]
                ]
                keyboard = types.ReplyKeyboardMarkup(
                    keyboard=kb,
                    input_field_placeholder="Выберите возможную активность"
                )
                await message.answer("Что вы хотите сделать теперь?",
                                     reply_markup=keyboard)
            else:
                # print(BD[i].number_letters, )
                BD[i].already_open.append(letter)
                await message.reply("Вы отгадали букву!\nУ Вас еще " +
                                    f'{BD[i].at} жизней!\n{BD[i].out()}')
        else:
            BD[i].at -= 1
            if BD[i].at == 0:
                await message.reply("Вы не отгадали слово!\nЭто было " +
                                    f'слово {BD[i].word}')
                kb = [
                    [types.KeyboardButton(text="Хочу снова " +
                                          "поиграть в Виселицу")],
                    [types.KeyboardButton(text="Хочу узнать погоду")]
                ]
                keyboard = types.ReplyKeyboardMarkup(
                    keyboard=kb,
                    input_field_placeholder="Выберите возможную активность"
                )
                await message.answer("Что вы хотите сделать теперь?",
                                     reply_markup=keyboard)
            else:
                BD[i].already_open.append(letter)
                await message.reply("Вы не отгадали букву!\nУ Вас еще " +
                                    f'{BD[i].at} жизней!\n{BD[i].out()}')
    print(i, BD[i].word, BD[i].out(), letter, BD[i].number_letters)

if __name__ == '__main__':
    executor.start_polling(dp)
