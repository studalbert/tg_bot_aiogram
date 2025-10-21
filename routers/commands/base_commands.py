from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram import F

from keyboards.common_keyboards import ButtonText, get_on_start_kb, get_on_help_kb, get_actions_kb
from keyboards.inline_keyboards.info_kb import build_info_kb

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://avatars.mds.yandex.net/get-shedevrum/12445758/img_3db98cc12ff211efa2a4922ae52888c4/orig"
    markup = get_on_start_kb()
    await message.answer(
        text=f"{markdown.hide_link(url)}Hello, {markdown.hbold(message.from_user.full_name)}!",
        parse_mode=ParseMode.HTML,
        reply_markup=markup,
    )

@router.message(F.text == ButtonText.WHATS_NEXT)
@router.message(Command(commands=["help"], prefix="/!%"))
async def handle_help(message: types.Message):
    text = "I'm an echo bot\\.\nSend me *any* message\\!"
    text = markdown.text(
        markdown.markdown_decoration.quote("I'm an echo bot."),
        markdown.text(
            "Send me",
            markdown.markdown_decoration.bold(
                markdown.text(
                    markdown.underline("literally"),
                    "any",
                ),
            ),
            markdown.markdown_decoration.quote("message!"),
        ),
        sep="\n",
    )
    await message.answer(
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=get_on_help_kb()
    )

@router.message(Command('more', prefix="/!"))
async def handle_more(message: types.Message):
    markup = get_actions_kb()
    await message.answer(text="Choose action:", reply_markup=markup)



@router.message(Command('info',prefix="/!"))
async def handle_info(message: types.Message):
    markup = build_info_kb()
    await message.answer(text="Ссылки и прочие ресурсы:", reply_markup=markup)



