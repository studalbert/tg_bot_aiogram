from random import randint

from aiogram import F, Router
from aiogram.types import CallbackQuery

from keyboards.inline_keyboards.actions_kb import random_num_updated_cb_data, build_actions_kb, FixedRandonNumCbData

router = Router(name=__name__)


@router.callback_query(F.data == random_num_updated_cb_data)
async def handle_random_number_edited(callback_query: CallbackQuery):
    # await callback_query.bot.answer_callback_query(
    #     callback_query_id=callback_query.id,
    # )
    await callback_query.answer()
    await callback_query.message.edit_text(
        text=f"Random number: {randint(1,100)}",
        reply_markup=build_actions_kb("Generate again")
    )

@router.callback_query(
    FixedRandonNumCbData.filter(F.number == 71),
)
async def handle_target_random_number_callback(
        callback_query: CallbackQuery,
):
    await callback_query.answer(
        text="Jackpot!!!",
        cache_time=30,
    )


@router.callback_query(
    FixedRandonNumCbData.filter()
)
async def handle_fixed_random_number_callback(
        callback_query: CallbackQuery,
        callback_data: FixedRandonNumCbData,
):
    await callback_query.answer(
        text=(
            f"Your fixed random number is {callback_data.number}\n"
              f"Callback data: {callback_query.data!r}"
        ),
        show_alert=True,
        cache_time=30,
    )


