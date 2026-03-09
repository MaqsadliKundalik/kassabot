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

admin_menu = ReplyKeyboardBuilder()
admin_menu.button(text="Kassaga pul qo'shish")
admin_menu.button(text="Kassa hisoboti")
admin_menu.adjust(1)
admin_menu = admin_menu.as_markup(resize_keyboard=True)


def confirm_btn(report_id: int):
    confirm_btn = InlineKeyboardBuilder()
    confirm_btn.button(text="Tasdiqlash", callback_data=f"confirm_{report_id}")
    confirm_btn.button(text="Bekor qilish", callback_data=f"cancel_{report_id}")
    confirm_btn.adjust(2)
    return confirm_btn.as_markup()