
import logging
import os

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import gpt_3_5 as gpt



btnHlp = KeyboardButton('Help')


help_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).row(btnHlp)

token = os.environ['GPT_TG_BOT_TOKEN']

bot = Bot(token=token)  # Токен моего  бота gpt_textai_bot

dp: Dispatcher = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)

boss_id = 799592984

ban_users = ['5895827248']
@dp.message_handler(commands='start')
async def start_using(message: types.Message):
    ban_users = []
    with open("ban.txt", "r") as file:
        banned_users = file.readlines()
        for i in banned_users:
            ban_users.append(i.replace('\n', '').replace(" ", ""))
    file.close()

    if str(message.from_user.id) in ban_users:
        await message.answer("You have banned.")

    elif message.from_user.id == 799592984:
        await message.answer(' Работает c 19.03.2023')
        await message.answer(' Чтобы задать вопрос нейросети Chat-GPT просто напиши в чат!', reply_markup=help_kb)

    else:
        await message.answer('Приветствую. Чтобы задать вопрос нейросети Chat-GPT просто напиши в чат!', reply_markup=help_kb)
        await bot.send_message(799592984, f'Кто-то нажал старт user_id - {message.from_user.id}, \n'
                                          f'user_name - {message.from_user.username}')



@dp.message_handler()
async def help_command(message: types.Message):
    ban_users = []
    with open("ban.txt", "r") as file:
        banned_users = file.readlines()
        for i in banned_users:
            ban_users.append(i.replace('\n', '').replace(" ", ""))
    file.close()

    if str(message.from_user.id) in ban_users:
        await message.answer("You have banned.")

    elif message.from_user.id == 799592984:
        if message.text == 'Help':
            await message.answer('Работает несмотря ни на что!!')
            await message.answer('Чтобы задать вопрос нейросети Chat-GPT просто напиши в чат!',
                                 reply_markup=help_kb)

        elif "ban" in message.text:
            id_user_banned = str(message.text).replace(" ", "").replace("\n", "").replace("ban")
            ban_users.append(id_user_banned)
            with open("ban.txt", "w") as file:
                for i in ban_users:
                    file.write(i + "\n")
            file.close()

            await message.answer(f"User id - {id_user_banned} - added in ban-list.")

        elif "unb" in message.text:
            id_user_unbanned = str(message.text).replace(" ", "").replace("\n", "")
            ban_users.remove(id_user_unbanned)
            with open("ban.txt", "w") as file:
                for i in ban_users:
                    file.write(i + "\n")
            file.close()
            await message.answer(f"User id - {id_user_unbanned} - removed from ban-list.")


        elif "b-list" == message.text:
            ban_list = ""
            with open("ban.txt", "r") as file:
                banned_users = file.readlines()
                for i in banned_users:
                    ban_list = ban_list + i + "\n"
            file.close()
            await message.answer(f"Список заблокированных ID:\n {ban_list}")


        else:
            try:
                answer = gpt.gpt_try(message.text)
                await message.answer(answer[0])
            except Exception as exc:
                await message.answer(str(exc))

    else:
        if message.text == 'Help':
            await message.answer('Чтобы задать вопрос нейросети Chat-GPT просто напиши в чат!',
                                 reply_markup=help_kb)
        else:
            try:
                answer = gpt.gpt_try(message.text)
                await message.answer(answer[0])
                await bot.send_message(boss_id, f"запрос от {message.from_user.id}\n\n {answer[1]} \n\n "
                                                f"ответ - \n\n {answer[0]}")
            except Exception as exc:
                await message.answer(str(exc))
                await bot.send_message(boss_id, f"{str(exc)}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)