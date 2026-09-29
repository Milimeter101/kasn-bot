import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiohttp import web

# Render ရဲ့ Environment ထဲက Token ကို ယူသုံးခြင်း
TOKEN = os.getenv("TOKEN")

# သင့်ရဲ့ Telegram Admin ID
ADMIN_ID = 1861529838

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ပင်မ Menu ခလုတ် ၅ ခု
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


# --- ၁။ ခလုတ်များ နှိပ်လိုက်သည့်အခါ အချက်အလက်များ ပြသခြင်း ---

@dp.callback_query(F.data == "free_movies")
async def process_free_movies(callback: CallbackQuery):
    text = (
        "🎬 **Free Movie Channels များ:**\n\n"
        "ကျွန်ုပ်တို့ရဲ့ အခမဲ့ ရုပ်ရှင်ချန်နယ်တွေထဲကို အောက်ပါလင့်ခ်ကနေ ဝင်ရောက်နိုင်ပါတယ် -\n"
        "👉 https://t.me/kasnreviews"
    )
    await callback.message.answer(text, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "online_class")
async def process_online_class(callback: CallbackQuery):
    class_text = (
        "မင်္ဂလာပါခင်ဗျာ။ စိတ်ဝင်စားပေးလို့ ကျေးဇူးပါဗျ။ "
        "ဒီသင်တန်းလေးကတော့ Telegram မှာ Movie Channel ထောင်ပြီး TikTok ကနေ လူခေါ်တာ၊ ကြော်ငြာလက်ခံပြီး ဝင်ငွေရှာတဲ့အထိ အစအဆုံး သင်ပေးထားတဲ့ Video Class လေးပါဗျ။\n\n"
        "သင်တန်းကြေးကတော့ ၃၅,၀၀၀ ကျပ် ပဲ ကျသင့်မှာဖြစ်ပြီး အချိန်အကန့်အသတ်မရှိ လေ့လာနိုင်ပါတယ်။\n\n"
        "သင်တန်းအပ်နှံလိုပါက Admin သို့ ဆက်သွယ်နိုင်ပါသည် -\n"
        "👉 @milimeterz"
    )
    await callback.message.answer(class_text)
    await callback.answer()

@dp.callback_query(F.data == "vip_channel")
async def process_vip_channel(callback: CallbackQuery):
    vip_text = (
        "မန်ဘာဝင်ရတာပါအကို series တေက ကျန်တာတေက မလိုပါဘူးဗျ မန်ဘာကြေးကသတ်မှတ်ထားတာမရှိဘဲ...\n\n"
        "5000 က စလို့ စေတနာရှိသလောက် အက်မင်ကို Support ပေးလို့ရပါတယ်..တစ်ခါသွင်းထားရုံနဲ့ ချန်နယ်မပျက်မချင်း အကျုံးဝင်ပါတယ်...\n\n"
        "🤩 **Wave** - 09448835260\n"
        "🤩 **Name** - Kaung Si Thu\n\n"
        "🤩 **Kpay** - 09752828949\n"
        "🤩 **Name** - Aye Sandar Moe\n\n"
        "Note မှာ Shop တစ်ခုထည်းသာရေးပေးပါ ✅\n\n"
        "📌 ဒီ Ph no တွေသာ သုံးပါတယ်။\n"
        "📌 ငွေလွဲးပီး ပြေစာ တစ်ခါထည်း ပို့ထားပေးပါခင်ဗျာ ။\n\n"
        "**ဆက်သွယ်ရန်** 👇👇\n"
        "@milimeterz\n"
        "@AS273152\n\n"
        "**လက်ရှိတင်ထားပြီးသား ဇာတ်လမ်းတွဲစာရင်းကြည့်ရန်**👇👇👇\n"
        "https://t.me/kasnseries/711"
    )
    await callback.message.answer(vip_text)
    await callback.answer()

@dp.callback_query(F.data == "contact_admin")
async def process_contact_admin(callback: CallbackQuery):
    text = (
        "💬 **Admin သို့ တိုက်ရိုက်ဆက်သွယ်ရန်:**\n\n"
        "အဆင်မပြေတာလေးများရှိပါက Admin ကို တိုက်ရိုက်ဆက်သွယ်နိုင်ပါသည် -\n"
        "👉 @milimeterz"
    )
    await callback.message.answer(text, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(F.data == "ads_inquiry")
async def process_ads_inquiry(callback: CallbackQuery):
    ads_text = (
        "📢 **ကြော်ငြာလက်ခံမည့် ချန်နယ်များ**\n\n"
        "@kasnreviews\n"
        "@movieblablabla\n"
        "@kasnactions\n"
        "@indiamovieslovers\n"
        "@kasnseries\n"
        "@kasncartoon\n"
        "@horrorcrazymalay\n"
        "@myintmyatkar\n"
        "@romanticloverkasn\n"
        "@japankaronlykasn\n"
        "@onlyin18kasn\n"
        "@fullkarkyichilar\n"
        "@allkarkyimalar\n"
        "@pornworldkasn1\n\n"
        "https://t.me/+jS8kwg4rG1ZkYWU1\n"
        "https://t.me/+ngM9sYGvAU44NDA1\n"
        "https://t.me/+laf6oHxHWklmMzE1\n"
        "https://t.me/+GsVFKMJiHjJjMzE9\n"
        "https://t.me/+xK8FCmgVEd5kZWNl\n"
        "https://t.me/+e0g781rHsso0MWM1\n"
        "https://t.me/+O10ofdYJRiNkOGU1\n\n"
        "**ကြော်ငြာလက်ခံမည့် ချန်နယ်များ**\n\n"
        "https://t.me/moviewreviews\n"
        "https://t.me/mwzkarsones\n"
        "https://t.me/mwaction\n"
        "https://t.me/mwromantic\n"
        "https://t.me/mvonlyin18\n"
        "https://t.me/vivamaxmw\n"
        "https://t.me/mwjapankar\n"
        "https://t.me/mvloecar\n"
        "https://t.me/+Z_5OIp2otRI3YTE1\n"
        "https://t.me/+GK1Vd9PJWpRjNmZl\n"
        "https://t.me/+-VzQ3zcPb1c1YzJl\n"
        "https://t.me/+vAybu6lgjNdhMTdl\n\n"
        "💎 **One Sub 3.5 ကျပ် ပါ**\n"
        "📌 **One day one post pin ပါ**\n"
        "💬 **ဆက်သွယ်ရန် =@milimeterz**"
    )
    await callback.message.answer(ads_text)
    await callback.answer()


# --- ၂။ User တွေက ငွေလွဲပြေစာ (Photo) ပို့လိုက်ရင် Admin (1861529838) ဆီ အလိုအလျောက် ပို့ပေးမည့်စနစ် ---
@dp.message(F.photo)
async def handle_payment_screenshot(message: Message):
    user = message.from_user
    user_info = f"📩 **ငွေလွဲပြေစာ အသစ်ရောက်ရှိပါပြီ!**\n\n" \
                f"👤 **အမည်:** {user.full_name}\n" \
                f"🔗 **Username:** @{user.username if user.username else 'None'}\n" \
                f"🆔 **User ID:** `{user.id}`"

    try:
        await bot.send_photo(
            chat_id=ADMIN_ID,
            photo=message.photo[-1].file_id,
            caption=user_info,
            parse_mode="Markdown"
        )
        await message.answer("ကျေးဇူးတင်ပါတယ်ခင်ဗျာ 🙏 ငွေလွဲပြေစာကို Admin ထံသို့ ပို့ပေးလိုက်ပါပြီ။ Admin မှ စစ်ဆေးပြီး လိုအပ်တာတွေကို ဆက်လက်ဆောင်ရွက်ပေးပါမည်။")
    except Exception as e:
        await message.answer("ပြေစာပို့ရာတွင် အခက်အခဲရှိနေပါသည်။ ကျေးဇူးပြု၍ Admin ကို တိုက်ရိုက်ဆက်သွယ်ပေးပါ (@milimeterz)။")


# --- ၃။ စာနဲ့ လာမေးရင် အလိုအလျောက် ပြန်ဖြေမည့် စနစ် (Auto-Reply / FAQ) ---

@dp.message(F.text.lower().contains("price") | F.text.lower().contains("ဈေး") | F.text.lower().contains("သင်တန်း") | F.text.lower().contains("ဖိုး"))
async def reply_price(message: Message):
    await message.answer("💰 Online Class သို့မဟုတ် VIP Channel နှင့် ပတ်သက်သော အချက်အလက်များကို သိရှိလိုပါက Menu ထဲမှ သက်ဆိုင်ရာ ခလုတ်ကို နှိပ်၍ ကြည့်ရှုနိုင်ပါတယ်ခင်ဗျာ။")

@dp.message(F.text.lower().contains("admin") | F.text.lower().contains("ဆက်သွယ်") | F.text.lower().contains("လူကြီးမင်း"))
async def reply_contact(message: Message):
    await message.answer("💬 Admin ကို ဆက်သွယ်လိုပါက @milimeterz သို့ တိုက်ရိုက် စာပို့နိုင်ပါတယ်။")


# --- Render အတွက် Fake Web Server (Port 10000) ---
async def handle(request):
    return web.Response(text="Bot is running!")

app = web.Application()
app.router.add_get("/", handle)

async def web_server():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 10000)
    await site.start()


# --- Main Function ---
async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot and Web Server are running...")
    
    await web_server()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
