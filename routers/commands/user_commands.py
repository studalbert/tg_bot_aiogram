import csv
import io

import aiohttp
from aiogram import Router, types
from aiogram.enums import ParseMode, ChatAction
from aiogram.filters import Command
from aiogram.utils import markdown
from aiogram.utils.chat_action import ChatActionSender

router = Router(name=__name__)

@router.message(Command(commands=["code"], prefix="/!%"))
async def handle_command_code(message: types.Message):
    text = markdown.text(
        "Here's Python code:",
        "",
        markdown.markdown_decoration.pre_language(
            markdown.text(
                "print('Hello World!')",
                "\n",
                "def foo():\n    return 'bar'",
                sep="\n",
            ),
            language="python",
        ),
        "And here's some JS:",
        "",
        markdown.markdown_decoration.pre_language(
            markdown.text(
                "console.log('Hello world!')",
                "\n",
                "function foo() {\n  return 'bar'\n}",
                sep="\n",
            ),
            language="javascript",
        ),
        sep="\n",
    )
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)


@router.message(Command("pic"))
async def handle_command_pic_by_url(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    url = "https://pic.rutubelist.ru/video/2025-08-01/13/51/13514ca887092c87ca87636896bdc6ea.jpg"
    await message.reply_photo(
        photo=url,
    )



@router.message(Command("file"))
async def handle_command_pic(message: types.Message):
    file_path = "/home/user/Pictures/1.jpg"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    await message.reply_document(
        document=types.FSInputFile(
            path=file_path,
            filename="cat-photo.jpeg"
        ),
    )


@router.message(Command("text"))
async def send_txt_file(message: types.Message):
    file = io.StringIO()
    file.write("Hello, world!\n")
    file.write("This is a text file.\n")
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue().encode("utf-8"),
            filename="text.txt",
        ),
    )


@router.message(Command("csv"))
async def send_csv_file(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    )
    file = io.StringIO()
    csv_writer = csv.writer(file)
    csv_writer.writerows([
        ["Name", "Age", "City"],
        ["john Smith", "28", "New York"],
        ["jane Doe", "32", "Los Angeles"],
        ["Mike Johnson", "40", "Chicago"],
    ])
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue().encode("utf-8"),
            filename="people.csv",
        ),
    )


async def send_big_file(message: types.Message):
    url = "https://pic.rutubelist.ru/video/2025-08-01/13/51/13514ca887092c87ca87636896bdc6ea.jpg"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result_bytes = await response.read()

    await message.reply_document(
        document=types.BufferedInputFile(
            file=result_bytes,
            filename="cat-pic.jpeg",
        ),
    )


@router.message(Command("pic_file"))
async def send_pic_file_buffered(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    async with ChatActionSender.upload_document(
        bot=message.bot,
        chat_id=message.chat.id,
    ):
        await send_big_file(message)
