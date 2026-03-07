from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main_menu = ReplyKeyboardBuilder()
main_menu.button(text="Ariza berish")
main_menu.adjust(1)
main_menu = main_menu.as_markup(resize_keyboard=True)

def vote_btn(report_id: int, yes_count: int = 0, no_count: int = 0):
    builder = InlineKeyboardBuilder()
    builder.button(text=f"✅ Ha ({yes_count})", callback_data=f"vote_yes_{report_id}")
    builder.button(text=f"❌ Yo'q ({no_count})", callback_data=f"vote_no_{report_id}")
    builder.adjust(2)
    return builder.as_markup()

def more_view_btn(report_id: int):
    builder = InlineKeyboardBuilder()
    builder.button(text="Batafsil", callback_data=f"more_{report_id}")
    builder.adjust(1)
    return builder.as_markup()