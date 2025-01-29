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

API_ID = "17131033"
API_HASH = "7768488c115ac09684bb38e608c47997"
BOT_TOKEN = "8150264707:AAHjeNNF3PHeql98L_yM0v71zDujiJmCZvY"

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
                text="💸 Pembayaran",
                callback_data="terms_conditions",
            )
        ],
        [
            InlineKeyboardButton(
                text="🗒 Prediksi",
                callback_data="price_list",
            ),
            InlineKeyboardButton(
                text="🆘 Testimoni", url="https://t.me/+i-KmRABwFzk5N2I1"
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
                text="Kembali",
                callback_data="home_intro",
            ),
        ],
    ]
)

button_k1 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="🛒 Order", url="https://t.me/BacodTele"),
        ],
        [
            InlineKeyboardButton(
                text="❌ Batalkan",
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

Selamat Datang Di Bot Prediksi Spaceman 🚀🚀 

🔴 Hati Hati Banyak Bot Palsu Yang Meniru @SPACEMANPREDIKSIBYLANGBOT
💭 Berikut dibawah ini opsi yang berisi petunjuk untuk menggunakan bot!
        """
        button = button_a1
    elif update.from_user.id not in []:
        #       text = "BELUM JOIN KALO MAU JOIN YA KE https://t.me/+i-KmRABwFzk5N2I1"
        text = "GRUP PREDIKSI HANYA DI https://t.me/+n96_Y5vc_aY2MzFl"
        button = None
    else:
        text = f"Hey {update.from_user.first_name}. Please browse through the options"
        button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Bantuan",
                        callback_data="help_back",
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
    inpurchase = """
• <u>Untuk Melanjutkan Transaksi langsung melakukan pembayaran ke <b>Admin Vip yang tersedia di tombol Order</b></u>

• <b>Metode Pembayaran</b>
• OVO
• Gopay
• DANA
• Shopee Pay
• M-BANKING

• <b>Cara Pembayaran</b>
1. Click tombol Order di bawah.
2. Pilih Admin Vip.
3. Ketik Bayar Vip.
4. Kirim pembayaran sesuai metode pembayaran yang admin sediakan.
5. Setelah melakukan transfer pembayaran, customer wajib mengirim bukti pembayaran sesuai format di bawah ini.

<code>VIP / VVIP:
Total Pembayaran:
Bukti Transfer & Nama Pengirim: "Screenshot"
</code>
    """
    await cq.edit_message_text(inpurchase, reply_markup=button_k1)


@bot.on_callback_query(filters.regex("^price_list$"))
async def d_price(_, cq: CallbackQuery):
    await cq.answer("berikut daftar harga yang tersedia")
    pricelist = """
PREDIKSI BOT SPACEMAN 🚀

PREDIKSI HARI INI : 👇
15:00 = min x9/=====>  up
15:05 = min x3/=====>  up
15:06 = min x2/=====>  up
15:12 = min x1/=====>  up
15:14 = min x1/=====>  up
15:18 = min x3/=====>  up
15:23 = min x1/=====>  up
15:27 = min x2/=====>  up
15:31 = min x28/====>  up
15:34 = min x2/=====>  up
15:38 = min x1/=====>  up
15:42 = min x1/=====>  up
15:45 = min x5/=====>  up
15:50 = min x1/=====>  up
15:57 = min x2/=====>  up
16:01 = min x1/=====>  up
16:08 = min x1/=====>  up
16:14 = min x9/=====>  up
16:16 = min x2/=====>  up
16:26 = min x1/=====>  up
16:28 = min x1/=====>  up
16:32 = min x3/=====>  up
16:39 = min x8/=====>  up
16:45 = min x3/=====>  up
16:49 = min x21/====>  up
16:56 = min x1/=====>  up
16:58 = min x1/=====>  up
17:01 = min x1/=====>  up
17:05 = min x4/=====>  up 
17:12 = min x1/=====>  up
17:16 = min x2/=====>  up
17:21 = min x1/=====>  up
17:26 = min x2/=====>  up
17:28 = min x42/====>  up
17:32 = min x1/=====>  up
17:35 = min x2/=====>  up
17:41 = min x1/=====>  up
17:45 = min x2/=====>  up
17:47 = min x3/=====>  up 
17:51 = min x1/=====>  up
17:53 = min x2/=====>  up
17:57 = min x1/=====>  up
17:59 = min x9/=====>  up


NOTE : Tidak ada jaminan 100% akurat !!!

LINK MAIN DI: 👇
https://suara89.info/biqz

jangan paksakan pola apabila tebakan kurang tepat feeling lebih di utamakan dalam spaceman

main di link yang gua kirim dan mengacu zona waktu WIB yang lain bisa mengikuti

JANGAN GEGEBAH FULL AMBIL KALI GEDE , SEKIRA NYA UDAH CUKUP LANGSUNG CAIRIN JANGAN SAMPE LO NYESEL KALO DIA TIBA TIBA NABRAK !!
    """
    await cq.edit_message_text(pricelist, reply_markup=button_b1)


@bot.on_callback_query(filters.regex("^terms_conditions$"))
async def d_provision(_, cq: CallbackQuery):
    await cq.answer("syarat dan ketentuan pembayaran")
    tecom = """
🧸 <u><b>GRUP VIP / VVIP</b></u>

↪️ <b>Kebijakan pengembalian</b>
Setelah melakukan pembayaran, dan jika anda belum mendapatkan respon dari pesanan yang anda buat,
anda akan memiliki <b>1 hari</b> untuk menggunakan <b>hak penggantian/pengembalian</b>, kegagalan transaksi
kemungkinan akan mengaktifkan layanan yang diminta.

🆘 <b>Dukungan</b>
Untuk menerima dukungan, anda dapat:
• Hubungi @BacodTele di Telegram
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
