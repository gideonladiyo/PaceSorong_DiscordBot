import os
import discord
from discord.ext import commands, tasks
import datetime
import google.generativeai as genai
from dotenv import load_dotenv
from zoneinfo import ZoneInfo
from utils.read_save_data import *
from utils.filepath import file_path

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

KONTEN_KONTEXTUAL = """
Kamu adalah Pace Papua Bot, seorang laki-laki asli Papua dari Sorong, Papua Barat Daya. Kamu selalu berbicara dengan logat Papua yang khas. Saat menjawab, jangan gunakan awalan seperti 'Pace:' — langsung saja berikan responsnya.

Pastikan setiap jawaban tidak melebihi 1700 karakter. Gunakan gaya bicara yang santai dan khas orang Papua, tapi tetap sopan dan ramah.
"""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

channel_histories = {}

@bot.event
async def on_ready():
    print(f"{bot.user} su online dan su siap menjawab!")
    renungan.start()

# renungan
@tasks.loop(seconds=60)
async def renungan():
    now = datetime.datetime.now(ZoneInfo("Asia/Jakarta"))
    current_time = now.strftime("%H:%M")

    if current_time in ["06:00", "21:00"]:
        renungan_ids = read_data(filepath=file_path.RENUNGAN_PATH) or []
        for channel_id in renungan_ids:
            channel = bot.get_channel(channel_id)
            if channel:
                waktu = ""
                if current_time == "06:00":
                    waktu = "pagi"
                elif current_time == "21:00":
                    waktu = "malam"

                prompt = f"Buatkan renungan {waktu} ini untuk tanggal {now.day} {now.month} {now.year} dari Alkitab. Pastikan response tidak lebih dari 2000 karakter. Jangan berikan response seperti 'Tentu, ini renungan malam untuk tanggal ..., berdasarkan Alkitab:', tetapi langsung saja kasih tanpa memberikan response seolaholah response dari AI. Struktur dari renungan harus terdapat judul, ayat, isi renungan, dan apa yang harus didoakan hari ini. Responsnya jangan ada 'Pace:', langsung responsenya"
                
                try:
                    response = model.generate_content(prompt)
                    await channel.send(
                        f"We kam pace @everyone, baca tong pu renungan {waktu} dulu ini."
                    )
                    await channel.send(response.text.strip())
                except Exception as e:
                    print("Error:", e)
                    await channel.send("❌ Gagal kirim pesan otomatis.")

@bot.command()
async def setrenunganchannel(ctx):
    new_renungan_channel = ctx.channel.id
    renungan_ids = read_data(filepath=file_path.RENUNGAN_PATH)
    if new_renungan_channel not in renungan_ids:
        renungan_ids.append(new_renungan_channel)
        save_data(filepath=file_path.RENUNGAN_PATH, data=renungan_ids)
        await ctx.send("✅ Channel ini su jadi tempat kirim renungan e! Kalo mau kasi batal tinggal pake command `/cancelrenunganchannel` saja.")
    else:
        await ctx.send(
            "Aduh kaka channel ini su jadi tempat kirim renungan, jadi ko tinggal tunggu saja👌"
        )

@bot.command()
async def cancelrenunganchannel(ctx):
    channel_id = ctx.channel.id
    renungan_ids = read_data(filepath=file_path.RENUNGAN_PATH)
    if channel_id in renungan_ids:
        renungan_ids.remove(channel_id)
        save_data(filepath=file_path.RENUNGAN_PATH, data=renungan_ids)
        await ctx.send("✅ Ko su batalkan channel ini jadi tempat kirim renungan, jadi sa tra kirim lagi. Tapi kalo ko mau kirim tinggal kasi command `/setrenunganchannel` di channel yang mau ko tempati e!")


@bot.command()
async def renunganmanual(ctx, waktu: str):
    if waktu.lower() not in ["pagi", "malam"]:
        await ctx.send("⚠️ Waktu harus 'pagi' atau 'malam'.")
        return

    now = datetime.datetime.now(ZoneInfo("Asia/Jakarta"))
    prompt = f"Buatkan renungan {waktu} ini untuk tanggal {now.day} {now.month} {now.year} dari Alkitab. Pastikan response tidak lebih dari 2000 karakter. Jangan berikan response seperti 'Tentu, ini renungan malam untuk tanggal ..., berdasarkan Alkitab:', tetapi langsung saja kasih tanpa memberikan response seolaholah response dari AI. Struktur dari renungan harus terdapat judul, ayat, isi renungan, dan apa yang harus didoakan hari ini. Responsnya jangan ada 'Pace:', langsung responsenya"

    response = model.generate_content(prompt)
    await ctx.send(f"We kam pace @everyone, baca tong pu renungan {waktu} dulu ini.")
    await ctx.send(response.text.strip())


# chatbot
MAX_LENGTH = 1700
@bot.command()
async def pace(ctx, *, pertanyaan):
    try:
        channel_id = ctx.channel.id
        if channel_id not in channel_histories:
            channel_histories[channel_id] = [f"{KONTEN_KONTEXTUAL}"]

        # Tambahkan pertanyaan user ke riwayat
        channel_histories[channel_id].append(f"User: {pertanyaan}")

        # Gabung riwayat untuk prompt
        prompt = "\n".join(channel_histories[channel_id])

        # Panggil model untuk menghasilkan konten
        response = model.generate_content(prompt)

        # Pastikan response memiliki atribut 'text'
        if not hasattr(response, "text"):
            await ctx.send("❌ Tidak ada teks yang dikembalikan.")
            return

        # Membatasi panjang teks agar tidak lebih dari 1700 karakter
        response_text = response.text.strip()
        if response_text.startswith("Pace:"):
            response_text = response_text.replace("Pace:", "")
        if len(response_text) > MAX_LENGTH:
            response_text = response_text[:MAX_LENGTH]
            next_response = response_text[MAX_LENGTH:]

        # Masukkan response ke riwayat
        channel_histories[channel_id].append(f"Pace: {response_text}")

        await ctx.send(response_text)
        if len(response_text) > MAX_LENGTH:
            await ctx.send(next_response)

        # Kalau konteks > 6
        if len(channel_histories[channel_id]) > 8:
            channel_histories[channel_id] = [
                channel_histories[channel_id][0]
            ] + channel_histories[channel_id][-6:]

    except Exception as e:
        await ctx.send(f"❌ Terjadi kesalahan saat menjawab. {e}")
        print("Error:", e)

        # Tangani error karena limit API
        if "quota" in str(e).lower() or "rate limit" in str(e).lower():
            admin_id = 533104933168480286
            await ctx.send(
                f"❌ Pace su capek, sa pu kuota API su habis ni😔\n<@{admin_id}>, bantu cek dulu!"
            )
        else:
            await ctx.send(f"❌ Terjadi kesalahan saat menjawab. {e}")

# reset riwayat
@bot.command()
async def reset(ctx):
    channel_id = ctx.channel.id
    if channel_id in channel_histories:
        del channel_histories[channel_id]
        await ctx.send("🔄 Konteks percakapan su direset. Pace mulai baru lagi e!")
    else:
        await ctx.send(
            "⚠️ Belum ada konteks di channel ini. Pace belum ada bicara apa-apa."
        )


bot.run(DISCORD_TOKEN)
