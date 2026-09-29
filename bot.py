import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# Render ရဲ့ Environment ထဲက Token ကို ယူသုံးခြင်း
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎬 Free Movie Channels များကို ဝင်ရန်", callback_data="free_movies")],
            [InlineKeyboardButton(text="📚 Online Class တက်ရောက်ရန်", callback_data="online_class")],
            [InlineKeyboardButton(text="💎 VIP Channel သို့ ဝင်ရောက်ရန်", callback_data="vip_channel")],
            [InlineKeyboardButton(text="💬 ဆက်သွယ်ရန် / Admin သို့ စကားပြောရန်", callback_data="contact_admin")],
            [InlineKeyboardButton(text="📢 ကြော်ငြာကိစ္စဆွေးနွေးရန်", callback_data="ads_inquiry")]
        ]
    )
    return keyboard

@dp.message(Command("start"))
async def cmd_start(message: Message):
    welcome_text = (
        f"မင်္ဂလာပါခင်ဗျာ 👋\n"
        f"KASN Movie Platform မှ ကြိုဆိုပါတယ်။\n\n"
        f"အောက်ပါတို့အနက်မှ လိုအပ်ရာကို ရွေးချယ်နိုင်ပါတယ် -"
    )
    await message.answer(text=welcome_text, reply_markup=get_main_menu())

@dp.callback_query(F.data == "free_movies")
async def process_free_movies(callback: callback_query):
    await callback.message.answer("🎬 Free Movie Channels တွေထဲကို ဝင်ဖို့ ဒီလင့်ခ်ကို နှိပ်ပါ - [သင့်ရဲ့ ချန်နယ်လင့်ခ်များ]")
    await callback.answer()

@dp.callback_query(F.data == "online_class")
async def process_online_class(callback: callback_query):
    await callback.message.answer("📚 Online Class တက်ရောက်လိုပါက ငွေလွှဲရမည့်စာရင်းနှင့် အသေးစိတ်ကို ဤနေရာတွင် ကြည့်ပါ - [Class Details / Admin Contact]")
    await callback.answer()

@dp.callback_query(F.data == "vip_channel")
async def process_vip_channel(callback: callback_query):
    await callback.message.answer("💎 VIP Channel ဝင်ရောက်ရန် နှုန်းထားများနှင့် ငွေလွှဲပုံစံ - [VIP Info & Payment]")
    await callback.answer()

@dp.callback_query(F.data == "contact_admin")
async def process_contact_admin(callback: callback_query):
    await callback.message.answer("💬 Admin ကို တိုက်ရိုက်ဆက်သွယ်ရန် - @YourAdminUsername ကို ဆက်သွယ်နိုင်ပါတယ်။")
    await callback.answer()

@dp.callback_query(F.data == "ads_inquiry")
async def process_ads_inquiry(callback: callback_query):
    await callback.message.answer("📢 ကြော်ငြာလက်ခံခြင်းဆိုင်ရာ နှုန်းထားများနှင့် စည်းကမ်းချက်များ - [Ads Rates & Rules]")
    await callback.answer()

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
