from random import randint

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

random_num_updated_cb_data = "random_num_updated_cb_data"


class FixedRandonNumCbData(CallbackData, prefix="fixed-random-num"):
    number: int


def build_actions_kb(random_number_button_text="random number") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=random_number_button_text, callback_data=random_num_updated_cb_data)
    cb_data_1 = FixedRandonNumCbData(number=randint(1,100))
    builder.button(
        text=f"Random number: {cb_data_1.number}",
        callback_data=cb_data_1.pack(),
    )
    builder.button(
        text="Random number: [HIDDEN]",
        callback_data=FixedRandonNumCbData(number=randint(1,100)).pack(),
    )
    builder.adjust(1)
    return builder.as_markup()
