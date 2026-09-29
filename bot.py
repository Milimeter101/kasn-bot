import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiohttp import web

# Render ရဲ့ Environment ထဲက Token ယူသုံးခြင်း
TOKEN = os.getenv("TOKEN")

# သင့်ရဲ့ Telegram Admin ID
ADMIN_ID = 1861529838

# ချန်နယ် ID များ
VIP_CHANNEL_ID = "-1002535791299"
ONLINE_CLASS_CHANNEL_ID = "-1002667237249"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ပင်မ Menu ခလုတ်များ
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


# --- ခလုတ်များ နှိပ်လိုက်သည့်အခါ အချက်အလက်များ ပြသခြင်း ---

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
        "မင်္ဂလာပါခင်ဗျာ။ စိတ်ဝင်စားပေးလို့ ကျေးဇူးပါဗျ။\n\n"
        "ဒီသင်တန်းလေးကတော့ Telegram မှာ Movie Channel ထောင်ပြီး TikTok ကနေ လူခေါ်တာ၊ ကြော်ငြာလက်ခံပြီး ဝင်ငွေရှာတဲ့အထိ အစအဆုံး သင်ပေးထားတဲ့ Video Class လေးပါဗျ။\n\n"
        "သင်တန်းကြေးကတော့ **၃၅,၀၀၀ ကျပ်** ဖြစ်ပြီး အချိန်အကန့်အသတ်မရှိ လေ့လာနိုင်ပါတယ်။\n\n"
        "🤩 **Wave** - 09448835260 (Kaung Si Thu)\n"
        "🤩 **Kpay** - 09752828949 (Aye Sandar Moe)\n\n"
        "📌 ငွေလွဲပြီးပါက **ပြေစာပုံကို Bot ချတ်ထဲသို့ တိုက်ရိုက် ပို့ပေးပါခင်ဗျာ**။ Admin စစ်ဆေးပြီးပါက သင်တန်းချန်နယ် ဝင်ခွင့်လင့်ခ် ပို့ပေးပါမည်။\n\n"
        "**ဆက်သွယ်ရန်** 👇\n"
        "@milimeterz"
    )
    await callback.message.answer(class_text)
    await callback.answer()

@dp.callback_query(F.data == "vip_channel")
async def process_vip_channel(callback: CallbackQuery):
    vip_text = (
        "မန်ဘာဝင်ရတာပါအကို series တွေက ကျန်တာတွေက မလိုပါဘူးဗျ မန်ဘာကြေးကသတ်မှတ်ထားတာမရှိဘဲ...\n\n"
        "5000 က စလို့ စေတနာရှိသလောက် အက်မင်ကို Support ပေးလို့ရပါတယ်..တစ်ခါသွင်းထားရုံနဲ့ ချန်နယ်မပျက်မချင်း အကျုံးဝင်ပါတယ်...\n\n"
        "🤩 **Wave** - 09448835260\n"
        "🤩 **Name** - Kaung Si Thu\n\n"
        "🤩 **Kpay** - 09752828949\n"
        "🤩 **Name** - Aye Sandar Moe\n\n"
        "Note မှာ Shop တစ်ခုတည်းသာရေးပေးပါ ✅\n\n"
        "📌 ဒီ Ph no တွေသာ သုံးပါတယ်။\n"
        "📌 ငွေလွဲပြီး ပြေစာ တစ်ခါတည်း ပို့ထားပေးပါခင်ဗျာ ။\n\n"
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
        "@pornworldkasn1\n"
        "@kasnmoviewworld\n"
        "@kasnreviews1\n"
        "@kasnreviews3\n\n"
        "💎 **One Sub 3.5 ကျပ် ပါ**\n"
        "📌 **One day one post pin ပါ**\n"
        "💬 **ဆက်သွယ်ရန် =@milimeterz**"
    )
    await callback.message.answer(ads_text)
    await callback.answer()


# --- 📸 User တွေ ငွေလွဲပြေစာပို့ရင် Admin ဆီကို VIP လား၊ Class လား ခွဲခြားပြီး ပို့ပေးခြင်း ---
@dp.message(F.photo)
async def handle_payment_screenshot(message: Message):
    user = message.from_user
    user_info = f"📩 **ငွေလွဲပြေစာ အသစ်ရောက်ရှိပါပြီ!**\n\n" \
                f"👤 **အမည်:** {user.full_name}\n" \
                f"🔗 **Username:** @{user.username if user.username else 'None'}\n" \
                f"🆔 **User ID:** `{user.id}`"

    # ခလုတ်နှစ်ခု (VIP အတွက် တစ်ခု၊ Online Class အတွက် တစ်ခု)
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💎 VIP Channel သို့ ထည့်ရန်", callback_data=f"approve_vip_{user.id}")],
            [InlineKeyboardButton(text="📚 Online Class သို့ ထည့်ရန်", callback_data=f"approve_class_{user.id}")]
        ]
    )

    try:
        await bot.send_photo(
            chat_id=ADMIN_ID,
            photo=message.photo[-1].file_id,
            caption=user_info,
            reply_markup=keyboard,
            parse_mode="Markdown"
        )
        await message.answer("ကျေးဇူးတင်ပါတယ်ခင်ဗျာ 🙏 ငွေလွဲပြေစာကို Admin ထံသို့ ပို့ပေးလိုက်ပါပြီ။ Admin မှ စစ်ဆေးပြီးပါက ချန်နယ်လင့်ခ် ပို့ပေးပါမည်။")
    except Exception as e:
        print(f"ERROR: Failed to handle photo from user {user.id} ({user.full_name}): {e}")
        await message.answer("ပြေစာပို့ရာတွင် အခက်အခဲရှိနေပါသည်။ ကျေးဇူးပြု၍ Admin ကို တိုက်ရိုက်ဆက်သွယ်ပေးပါ (@milimeterz)။")


# --- ✅ VIP Channel အတွက် အတည်ပြုပေးသောအခါ ---
@dp.callback_query(F.data.startswith("approve_vip_"))
async def process_approve_vip(callback: CallbackQuery):
    target_user_id = int(callback.data.split("_")[2])

    try:
        invite_link = await bot.create_chat_invite_link(
            chat_id=VIP_CHANNEL_ID,
            creates_join_request=True
        )

        await bot.send_message(
            chat_id=target_user_id,
            text=f"🎉 **သင်၏ VIP Channel ငွေလွဲပြေစာ အတည်ပြုပြီးပါပြီ!**\n\n"
                 f"VIP Channel သို့ ဝင်ရောက်ရန် အောက်ပါလင့်ခ်ကို နှိပ်ပြီး Join Request တင်ပေးပါ (Admin မှ စစ်ဆေးအတည်ပြုပေးပါမည်) -\n"
                 f"👉 {invite_link.invite_link}"
        )

        await callback.message.edit_caption(
            caption=callback.message.caption + "\n\n✅ **[VIP Channel လင့်ခ် ပို့ပြီးပါပြီ]**",
            parse_mode="Markdown"
        )
        await callback.answer("✅ VIP လင့်ခ် ပို့ပြီးပါပြီ။")

    except Exception as e:
        print(f"ERROR: Failed to approve VIP for user {target_user_id}: {e}")
        await callback.answer(f"❌ အမှားဖြစ်ပေါ်နေပါသည်: {e}", show_alert=True)


# --- ✅ Online Class အတွက် အတည်ပြုပေးသောအခါ ---
@dp.callback_query(F.data.startswith("approve_class_"))
async def process_approve_class(callback: CallbackQuery):
    target_user_id = int(callback.data.split("_")[2])

    try:
        invite_link = await bot.create_chat_invite_link(
            chat_id=ONLINE_CLASS_CHANNEL_ID,
            creates_join_request=True
        )

        await bot.send_message(
            chat_id=target_user_id,
            text=f"🎉 **သင်၏ Online Class ငွေလွဲပြေစာ အတည်ပြုပြီးပါပြီ!**\n\n"
                 f"Online Class ချန်နယ်သို့ ဝင်ရောက်ရန် အောက်ပါလင့်ခ်ကို နှိပ်ပြီး Join Request တင်ပေးပါ (Admin မှ စစ်ဆေးအတည်ပြုပေးပါမည်) -\n"
                 f"👉 {invite_link.invite_link}"
        )

        await callback.message.edit_caption(
            caption=callback.message.caption + "\n\n✅ **[Online Class လင့်ခ် ပို့ပြီးပါပြီ]**",
            parse_mode="Markdown"
        )
        await callback.answer("✅ Online Class လင့်ခ် ပို့ပြီးပါပြီ။")

    except Exception as e:
        print(f"ERROR: Failed to approve Online Class for user {target_user_id}: {e}")
        await callback.answer(f"❌ အမှားဖြစ်ပေါ်နေပါသည်: {e}", show_alert=True)


# --- 🔄 Admin ဘက်ကနေ ရိုးရိုး Reply လုပ်ပြီး စာပြန်ချင်ရင် သုံးရန် ---
@dp.message(F.from_user.id == ADMIN_ID)
async def admin_reply_handler(message: Message):
    if message.reply_to_message and message.reply_to_message.caption:
        caption = message.reply_to_message.caption
        try:
            if "User ID:" in caption:
                lines = caption.split("\n")
                target_user_id = None
                for line in lines:
                    if "User ID:" in line:
                        target_user_id = line.split("`")[1]
                        break
                
                if target_user_id:
                    await bot.send_message(
                        chat_id=int(target_user_id),
                        text=f"💬 **Admin မှ ပြောကြားချက်:**\n\n{message.text}"
                    )
                    await message.reply("✅ User ထံသို့ စာပို့ပြီးပါပြီ။")
                    return
        except Exception as e:
            print(f"ERROR: Admin reply failed: {e}")
            await message.reply(f"❌ ပို့၍မရပါ။ အမှားအယွင်းရှိနေပါသည်: {e}")
            return
            
    await message.reply("💡 User ဆီ စာပြန်လိုပါက ပုံအောက်ပါ ခလုတ်များကို နှိပ်ပါ (သို့မဟုတ်) ပုံကို Reply လုပ်၍ စာပို့ပါ။")


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
    await dp.start_polling(bot, drop_pending_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
