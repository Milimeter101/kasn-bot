import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

TOKEN = os.getenv("TOKEN")
ADMIN_ID = 1861529838

VIP_CHANNEL_ID = "-1002535791299"
ONLINE_CLASS_CHANNEL_ID = "-1002667237249"

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEBHOOK_PATH = f"/bot/{TOKEN}"
BASE_WEBHOOK_URL = f"{WEBHOOK_URL}{WEBHOOK_PATH}" if WEBHOOK_URL else ""

bot = Bot(token=TOKEN)
dp = Dispatcher()

class UserState(StatesGroup):
    waiting_for_vip_slip = State()
    waiting_for_class_slip = State()

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
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    welcome_text = (
        "မင်္ဂလာပါခင်ဗျာ 👋\n"
        "KASN Movie Platform မှ ကြိုဆိုပါတယ်။\n\n"
        "📌 အသုံးပြုပုံ လမ်းညွှန်ချက် (FAQ):\n"
        "• VIP Channel ဝင်လိုပါက နှိပ်ပြီး ငွေလွဲကာ ပြေစာပုံ ပို့ပေးပါ။\n"
        "• Online Class တက်လိုပါက အချက်အလက်ကြည့်ပြီး ပြေစာပုံ ပို့ပေးပါ။\n"
        "• ငွေလွဲပြေစာ ပို့လိုက်သည်နှင့် Admin စစ်ဆေးပြီး ချန်နယ် Join Request လင့်ခ် ပို့ပေးပါမည်။\n\n"
        "အောက်ပါတို့အနက်မှ လိုအပ်ရာကို ရွေးချယ်နိုင်ပါတယ် -"
    )
    await message.answer(text=welcome_text, reply_markup=get_main_menu())

@dp.callback_query(F.data == "free_movies")
async def process_free_movies(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    text = (
        "🎬 Free Movie Channels များ:\n\n"
        "ကျွန်ုပ်တို့ရဲ့ အခမဲ့ ရုပ်ရှင်ချန်နယ်တွေထဲကို အောက်ပါလင့်ခ်ကနေ ဝင်ရောက်နိုင်ပါတယ် -\n"
        "👉 https://t.me/kasnreviews"
    )
    await callback.message.answer(text)
    await callback.answer()

@dp.callback_query(F.data == "online_class")
async def process_online_class(callback: CallbackQuery, state: FSMContext):
    await state.set_state(UserState.waiting_for_class_slip)
    
    class_text = (
        "မင်္ဂလာပါခင်ဗျာ။ စိတ်ဝင်စားပေးလို့ ကျေးဇူးပါဗျ။\n\n"
        "ဒီသင်တန်းလေးကတော့ Telegram မှာ Movie Channel ထောင်ပြီး TikTok ကနေ လူခေါ်တာ၊ ကြော်ငြာလက်ခံပြီး ဝင်ငွေရှာတဲ့အထိ အစအဆုံး သင်ပေးထားတဲ့ Video Class လေးပါဗျ။\n\n"
        "သင်တန်းကြေးကတော့ ၃၅,၀၀၀ ကျပ် ဖြစ်ပြီး အချိန်အကန့်အသတ်မရှိ လေ့လာနိုင်ပါတယ်။\n\n"
        "🤩 Wave - 09448835260 (Kaung Si Thu)\n"
        "🤩 Kpay - 09752828949 (Aye Sandar Moe)\n\n"
        "📌 [Online Class အတွက် ရွေးချယ်ထားပါသည်]\n"
        "ငွေလွဲပြီးပါက ပြေစာပုံကို ယခုချတ်ထဲသို့ တိုက်ရိုက် ပို့ပေးပါခင်ဗျာ။ Admin စစ်ဆေးပြီးပါက သင်တန်းချန်နယ် ဝင်ခွင့်လင့်ခ် ပို့ပေးပါမည်။\n\n"
        "ဆက်သွယ်ရန် 👇\n"
        "@milimeterz"
    )
    await callback.message.answer(class_text)
    await callback.answer()

@dp.callback_query(F.data == "vip_channel")
async def process_vip_channel(callback: CallbackQuery, state: FSMContext):
    await state.set_state(UserState.waiting_for_vip_slip)
    
    vip_text = (
        "မန်ဘာဝင်ရတာပါအကို series တွေက ကျန်တာတွေက မလိုပါဘူးဗျ မန်ဘာကြေးကသတ်မှတ်ထားတာမရှိဘဲ...\n\n"
        "5000 က စလို့ စေတနာရှိသလောက် အက်မင်ကို Support ပေးလို့ရပါတယ်..တစ်ခါသွင်းထားရုံနဲ့ ချန်နယ်မပျက်မချင်း အကျုံးဝင်ပါတယ်...\n\n"
        "🤩 Wave - 09448835260\n"
        "🤩 Name - Kaung Si Thu\n\n"
        "🤩 Kpay - 09752828949\n"
        "🤩 Name - Aye Sandar Moe\n\n"
        "Note မှာ Shop တစ်ခုတည်းသာရေးပေးပါ ✅\n\n"
        "📌 [VIP Channel အတွက် ရွေးချယ်ထားပါသည်]\n"
        "📌 ဒီ Ph no တွေသာ သုံးပါတယ်။\n"
        "📌 ငွေလွဲပြီး ပြေစာပုံ ပို့ထားပေးပါခင်ဗျာ ။\n\n"
        "ဆက်သွယ်ရန် 👇👇\n"
        "@milimeterz\n"
        "@AS273152\n\n"
        "လက်ရှိတင်ထားပြီးသား ဇာတ်လမ်းတွဲစာရင်းကြည့်ရန်👇👇👇\n"
        "https://t.me/kasnseries/711"
    )
    await callback.message.answer(vip_text)
    await callback.answer()

@dp.callback_query(F.data == "contact_admin")
async def process_contact_admin(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    text = (
        "💬 Admin သို့ တိုက်ရိုက်ဆက်သွယ်ရန်:\n\n"
        "အဆင်မပြေတာလေးများရှိပါက Admin ကို တိုက်ရိုက်ဆက်သွယ်နိုင်ပါသည် -\n"
        "👉 @milimeterz"
    )
    await callback.message.answer(text)
    await callback.answer()

@dp.callback_query(F.data == "ads_inquiry")
async def process_ads_inquiry(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    ads_text = (
        "📢 ကြော်ငြာလက်ခံမည့် ချန်နယ်များ\n\n"
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
        "https://t.me/+jS8kwg4rG1ZkYWU1\n"
        "https://t.me/+ngM9sYGvAU44NDA1\n"
        "https://t.me/+CN0BI4DqMPsyNDk1\n"
        "https://t.me/+laf6oHxHWklmMzE1\n"
        "https://t.me/+GsVFKMJiHjJjMzE9\n"
        "https://t.me/+xK8FCmgVEd5kZWNl\n"
        "https://t.me/+e0g781rHsso0MWM1\n"
        "https://t.me/+O10ofdYJRiNkOGU1\n\n"
        "ကြော်ငြာလက်ခံမည့် ချန်နယ်များ\n\n"
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
        "💎 One Sub 3.5 ကျပ် ပါ\n"
        "📌 One day one post pin ပါ\n"
        "💬 ဆက်သွယ်ရန် = @milimeterz"
    )
    # parse_mode ကို Markdown သို့မဟုတ် HTML မသုံးဘဲ ရိုးရိုးစာသားအတိုင်း ပို့ပေးခြင်းဖြင့် စာများ မပြတ်တောက်ဘဲ အကုန်ပေါ်စေရန်
    await callback.message.answer(ads_text)
    await callback.answer()

@dp.message(F.photo)
async def handle_payment_screenshot(message: Message, state: FSMContext):
    user = message.from_user
    current_state = await state.get_state()
    
    if current_state == UserState.waiting_for_vip_slip.state:
        purpose = "💎 ဝယ်ယူသည့်အမျိုးအစား: VIP Channel"
    elif current_state == UserState.waiting_for_class_slip.state:
        purpose = "📚 ဝယ်ယူသည့်အမျိုးအစား: Online Class"
    else:
        purpose = "❓ ဝယ်ယူသည့်အမျိုးအစား: မသတ်မှတ်ရသေးပါ (သို့မဟုတ် /start မနှိပ်ဘဲ ပို့ထားခြင်း)"

    user_info = f"📩 ငွေလွဲပြေစာ အသစ်ရောက်ရှိပါပြီ!\n\n" \
                f"{purpose}\n" \
                f"👤 အမည်: {user.full_name}\n" \
                f"🔗 Username: @{user.username if user.username else 'None'}\n" \
                f"🆔 User ID: {user.id}"

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
            reply_markup=keyboard
        )
        await message.answer("ကျေးဇူးတင်ပါတယ်ခင်ဗျာ 🙏 ငွေလွဲပြေစာကို Admin ထံသို့ ပို့ပေးလိုက်ပါပြီ။ Admin မှ စစ်ဆေးပြီးပါက ချန်နယ်လင့်ခ် ပို့ပေးပါမည်။")
        await state.clear()
    except Exception as e:
        print(f"ERROR: Failed to handle photo from user {user.id}: {e}")
        await message.answer("ပြေစာပို့ရာတွင် အခက်အခဲရှိနေပါသည်၊ ကျေးဇူးပြု၍ Admin ကို တိုက်ရိုက်ဆက်သွယ်ပါ (@milimeterz)။")

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
            text=f"🎉 သင်၏ VIP Channel ငွေလွဲပြေစာ အတည်ပြုပြီးပါပြီ!\n\n"
                 f"VIP Channel သို့ ဝင်ရောက်ရန် အောက်ပါလင့်ခ်ကို နှိပ်ပြီး Join Request တင်ပေးပါ -\n"
                 f"👉 {invite_link.invite_link}"
        )

        await callback.message.edit_caption(
            caption=callback.message.caption + "\n\n✅ [VIP Channel လင့်ခ် ပို့ပြီးပါပြီ]"
        )
        await callback.answer("✅ VIP လင့်ခ် ပို့ပြီးပါပြီ။")

    except Exception as e:
        print(f"ERROR: Failed to approve VIP for user {target_user_id}: {e}")
        await callback.answer(f"❌ အမှားဖြစ်ပေါ်နေပါသည်: {e}", show_alert=True)

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
            text=f"🎉 သင်၏ Online Class ငွေလွဲပြေစာ အတည်ပြုပြီးပါပြီ!\n\n"
                 f"Online Class ချန်နယ်သို့ ဝင်ရောက်ရန် အောက်ပါလင့်ခ်ကို နှိပ်ပြီး Join Request တင်ပေးပါ -\n"
                 f"👉 {invite_link.invite_link}"
        )

        await callback.message.edit_caption(
            caption=callback.message.caption + "\n\n✅ [Online Class လင့်ခ် ပို့ပြီးပါပြီ]"
        )
        await callback.answer("✅ Online Class လင့်ခ် ပို့ပြီးပါပြီ။")

    except Exception as e:
        print(f"ERROR: Failed to approve Online Class for user {target_user_id}: {e}")
        await callback.answer(f"❌ အမှားဖြစ်ပေါ်နေပါသည်: {e}", show_alert=True)

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
                        target_user_id = line.split("User ID:")[1].strip()
                        break
                
                if target_user_id:
                    target_id = int(target_user_id)
                    
                    if message.photo:
                        await bot.send_photo(
                            chat_id=target_id,
                            photo=message.photo[-1].file_id,
                            caption=f"💬 Admin မှ ပေးပို့သော မက်ဆေ့ချ်:\n\n{message.caption}" if message.caption else "💬 Admin မှ ပေးပို့သော ပုံ:"
                        )
                    elif message.text:
                        await bot.send_message(
                            chat_id=target_id,
                            text=f"💬 Admin မှ ပြောကြားချက်:\n\n{message.text}"
                        )
                        
                    await message.reply("✅ User ထံသို့ အောင်မြင်စွာ ပို့ပြီးပါပြီ။")
                    return
        except Exception as e:
            print(f"ERROR: Admin reply failed: {e}")
            await message.reply(f"❌ ပို့၍မရပါ။ အမှားအယွင်းရှိနေပါသည်: {e}")
            return
            
    await message.reply("💡 User ဆီ စာပြန်လိုပါက ပုံကို Reply လုပ်၍ စာ/ပုံ ပို့ပါ။")

async def on_startup(bot: Bot):
    await bot.set_webhook(BASE_WEBHOOK_URL)

async def main():
    logging.basicConfig(level=logging.INFO)
    
    app = web.Application()
    
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    
    setup_application(app, dp, bot=bot)
    
    dp.startup.register(on_startup)
    
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.getenv("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    
    print(f"Webhook Bot started on port {port}...")
    
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
