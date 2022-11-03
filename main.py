from asyncio import get_event_loop_policy

from pyrogram import Client, filters
from pyrogram.errors import MessageNotModified, QueryIdInvalid
from pyrogram.methods.utilities.idle import idle
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

API_ID = "3487995"
API_HASH = "7b9f1868c1e90b7408d48445f1e89603"
BOT_TOKEN = "5459903932:AAG4HFZtrQuEWLHvVGaAR9FlJce5FzlzcZM"

bot = Client(
    name="bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
)


button_a1 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="💸 Buat pembayaran",
                callback_data="terms_conditions",
            )
        ],
        [
            InlineKeyboardButton(
                text="🗒 Daftar harga",
                callback_data="price_list",
            ),
            InlineKeyboardButton(
                text="🆘 Dukungan", url="https://t.me/tedeubot_support_bot"
            ),
        ],
    ]
)


button_a2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="✅ Setuju & Lanjutkan",
                callback_data="in_purchase",
            )
        ],
        [
            InlineKeyboardButton(
                text="❌ Batalkan",
                callback_data="home_intro",
            ),
        ],
    ]
)


button_b1 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="home_intro",
            ),
        ],
    ]
)


@bot.on_message(filters.command("start") & filters.private)
@bot.on_callback_query(filters.regex("^home_intro$"))
async def intro_msg(_, update: Message | CallbackQuery):
    if isinstance(update, CallbackQuery):
        try:
            await update.answer()
        except QueryIdInvalid:
            pass
        method = update.edit_message_text
    else:
        method = update.reply_text

    user_prem = False
    if not user_prem:
        text = f"""
👋🏻 Halo {update.from_user.first_name}!

Dengan bot ini, anda dapat melakukan pembayaran untuk userbot premium Tede-Userbot.

💭 Berikut dibawah ini opsi yang berisi petunjuk untuk melakukan pembayaran!
        """
        button = button_a1
    elif update.from_user.id not in []:
        text = "lo dah premium tapi lo belum bikin userbot premium kamu akan abis pada senin 0 sep 1999"
        button = None
    else:
        text = f"Hey {update.from_user.first_name}. Please browse through the options"
        button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "help",
                        callback_data="help_back",
                    ),
                    InlineKeyboardButton(
                        "restart bot",
                        callback_data=f"restartTedeUb_{update.from_user.id}",
                    ),
                ]
            ]
        )

    try:
        await method(text, reply_markup=button)
    except MessageNotModified:
        pass


@bot.on_callback_query(filters.regex("^in_purchase$"))
async def d_purchase(_, cq: CallbackQuery):
    await cq.answer("lakukan pembayaran melalui platform yang tersedia")
    await cq.edit_message_text(
        "coming-soon !\n\nbot is still under development, payment method are coming very soon.",
        reply_markup=button_b1,
    )


@bot.on_callback_query(filters.regex("^price_list$"))
async def d_price(_, cq: CallbackQuery):
    await cq.answer("berikut daftar harga yang tersedia")
    await cq.edit_message_text(
        "coming-soon !\n\nbot is still under development, price list are coming very soon.",
        reply_markup=button_b1,
    )


@bot.on_callback_query(filters.regex("^terms_conditions$"))
async def d_provision(_, cq: CallbackQuery):
    await cq.answer("syarat dan ketentuan pembayaran")
    tecom = """
🧸 <u><b>TedeUserbot premium</b></u>

↪️ <b>Kebijakan pengembalian</b>
Setelah melakukan pembayaran, dan jika anda belum mendapatkan produk dari pesanan yang anda buat,
anda akan memiliki <b>2 hari</b> untuk menggunakan <b>hak penggantian/pengembalian</b>, kegagalan transaksi/malfungsi
produk kemungkinan akan mengaktifkan layanan yang diminta.

<i>Oleh karena itu, jika anda sudah menggunakan produk yang anda pesan dan tidak terdapat cacat dalam produk tersebut
(termasuk akses penuh dalam pamakaian nya), anda akan kehilangan hak atas pengembalian uang</i>

🔐 <b>Kebijakan privasi</b>
Anda dapat berkonsultasi dengan Kebijakan Privasi kami dengan mengklik <a href=\"https://\">di sini</a>.

🆘 <b>Dukungan</b>
Untuk menerima dukungan, anda dapat:
• Hubungi @tofik_dn di Telegram
• Hubungi tim kami di @tedeubot_support_bot
⚠️ <b>JANGAN hubungi</b> Dukungan Telegram atau Dukungan Bot Telegram perihal pembayaran yang anda buat di bot ini.

👉🏻 Tekan <b>tombol hijau</b> untuk menyatakan bahwa anda telah <b>membaca dan menerima ketentuan</b> ini dan untuk melanjutkan pembayaran,
jika tidak, batalkan.
    """
    await cq.edit_message_text(tecom, reply_markup=button_a2)


async def main():
    async with bot:
        await idle()


if __name__ == "__main__":
    get_event_loop_policy().get_event_loop().run_until_complete(main())
