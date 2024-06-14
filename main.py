import logging
import asyncio
import random

from aiogram import Bot, Dispatcher, types, F
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command

# Bot token
BOT_TOKEN = "7368091530:AAHOVRq-Zzin_vptGGybXpwYZ_BfAhIB8XY"

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Lists for films
Action_List = ["https://www.kinopoisk.ru/film/807682/", "https://www.kinopoisk.ru/film/1318972/dates/"]
Fantasy_List = ["https://www.kinopoisk.ru/film/4370148/", "https://www.kinopoisk.ru/film/505966/"]
Horror_List = ["https://www.kinopoisk.ru/film/808062/", "https://www.kinopoisk.ru/film/1122138/"]
Humor_List = ["https://www.kinopoisk.ru/film/490323/", "https://www.kinopoisk.ru/film/472105/"]

# Lists for snacks
Chipsy_List = [
    ("Чипсы с сыром", "https://simg.marwin.kz/media/catalog/product/9/b/chipsy_lays_syr_90g.jpeg"),
    ("Чипсы нежный сыр с зеленью", "https://imgproxy.sbermarket.ru/imgproxy/width-auto/czM6Ly9jb250ZW50LWltYWdlcy1wcm9kL3Byb2R1Y3RzLzE1MTExNTUwL29yaWdpbmFsLzEvMjAyNC0wMS0xOFQxMyUzQTA1JTNBMDguMzA1MTU2JTJCMDAlM0EwMC8xNTExMTU1MF8xLmpwZw==.jpg"),
    ("Чипсы классические", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvXb05ixsKIn0w8xGCJK9GbD_DwLlo2v-mXw&s")
]

Napitki_List = [
    ("Вода", "https://elitalco.kz/upload/images/47516_473484_04.jpg"),
    ("Фьюс чай с персиком", "https://resources.cdn-kaspi.kz/img/m/p/hb5/h36/84657525227550.png?format=gallery-large"),
    ("Кока кола", "https://elitalco.kz/upload/images/32864_310426_09.jpeg")
]

Suhariki_List = [
    ("Сухарики телятина на гриле", "https://kokshetau.avokado.kz/upload/iblock/9a2/9a2299382e5812dcf3500264971b988f.png"),
    ("Сухарики сметана", "https://avatars.mds.yandex.net/get-mpic/5234126/img_id7739811888363590965.jpeg/orig"),
    ("Сухарики багет сырное ассорти", "https://resources.cdn-kaspi.kz/img/m/p/h0f/ha2/84708866359326.jpg?format=gallery-large")
]

Popkorn_List = [
    ("Сырный попкорн", "https://shuba.life/static/content/thumbs/1905x884/a/8a/6iwmtb---c1905x884x50px50p-up--8af6472aeeb72660a090e1d1ce1198aa.jpg"),
    ("Соленый попкорн", "https://www.vsegdavkusno.ru/assets/images/recipes/2941/popcorn-solenyi2.jpg"),
    ("Карамельный попкорн", "https://the-challenger.ru/wp-content/uploads/2018/05/shutterstock_750535642-800x536.jpg")
]

# Start command handler
@dp.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://images.satu.kz/174559357_robot-talkbo-mini.jpg"
    await message.answer(
        text=f"{markdown.hide_link(url)}Привет, я бот который найдёт тебе фильм по твоим хотелкам!{markdown.hbold(message.from_user.full_name)} \n У меня есть команда /help которая покажет какие у меня есть команды",
        parse_mode=ParseMode.HTML,
    )

# Help command handler
@dp.message(Command("help"))
async def handle_help(message: types.Message):
    await message.answer(
        text="Привет! У меня есть такие команды как:\n/films - Дает возможность выбрать жанр фильмов\n/zakuski - Показывает случайную еду.",
        parse_mode=ParseMode.HTML
    )

# Zakuski command handler
@dp.message(Command("zakuski"))
async def zakuski_type(message: types.Message):
    kb = [
        [types.KeyboardButton(text="чипсы")],
        [types.KeyboardButton(text="напитки")],
        [types.KeyboardButton(text="сухарики")],
        [types.KeyboardButton(text="попкорн")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Вот ваше меню!", reply_markup=keyboard)

@dp.message(Command("yes"))
async def yes_type(message: types.Message):
    await message.answer(
        text="Хорошо с вас 800 тенге",
        parse_mode=ParseMode.HTML
    )
@dp.message(Command("no"))
async def no_type(message: types.Message):
    await message.answer(
        text="Хорошо, тогда верните товар на полку",
        parse_mode=ParseMode.HTML
    )

@dp.message(F.text.lower() == "попкорн")
async def show_chipsy(message: types.Message):
    popkorn = random.choice(Popkorn_List)
    await message.answer_photo(photo=popkorn[1],caption=f"{message.from_user.full_name}, Вот ваш попкорн будете покупать? Если да то напишите /yes, а если нет то /no - {popkorn[0]}")

@dp.message(F.text.lower() == "чипсы")
async def show_chipsy(message: types.Message):
    chipsy = random.choice(Chipsy_List)
    await message.answer_photo(photo=chipsy[1], caption=f"{message.from_user.full_name}, Вот ваши чипсы будете покупать? Если да то напишите /yes, а если нет то /no - {chipsy[0]}")

@dp.message(F.text.lower() == "напитки")
async def show_napitok(message: types.Message):
    napitok = random.choice(Napitki_List)
    await message.answer_photo(photo=napitok[1], caption=f"{message.from_user.full_name}, Вот ваш напиток будете покупать? Если да то напишите /yes, а если нет то /no - {napitok[0]}")

@dp.message(F.text.lower() == "сухарики")
async def show_suhariki(message: types.Message):
    suhariki = random.choice(Suhariki_List)
    await message.answer_photo(photo=suhariki[1], caption=f"{message.from_user.full_name}, Вот ваши сухарики будете покупать? Если да то напишите /yes, а если нет то /no - {suhariki[0]}")

# Films command handler
@dp.message(Command("films"))
async def films_type(message: types.Message):
    kb = [
        [types.KeyboardButton(text="экшн")],
        [types.KeyboardButton(text="фантастика")],
        [types.KeyboardButton(text="ужасы")],
        [types.KeyboardButton(text="комедия")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Выберите желаемый жанр, и бот выберет вам фильм!", reply_markup=keyboard)

# Handlers for film genres
@dp.message(F.text.lower() == "экшн")
async def show_action_film(message: types.Message):
    await message.answer(
        text=f"{message.from_user.full_name}, Твой фильм это - {random.choice(Action_List)}"
    )

@dp.message(F.text.lower() == "фантастика")
async def show_fantasy_film(message: types.Message):
    await message.answer(
        text=f"{message.from_user.full_name}, Твой фильм это - {random.choice(Fantasy_List)}"
    )

@dp.message(F.text.lower() == "ужасы")
async def show_horror_film(message: types.Message):
    await message.answer(
        text=f"{message.from_user.full_name}, Твой фильм это - {random.choice(Horror_List)}"
    )
@dp.message(F.text.lower() == "комедия")
async def show_comedy_film(message: types.Message):
    await message.answer(
        text=f"{message.from_user.full_name}, Твой фильм это - {random.choice(Humor_List)}"
    )

# Main function
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())