import os
import discord
from discord.ext import commands, tasks
import datetime
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
# Load API Keys dari environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

KONTEN_KONTEXTUAL = """
Kamu adalah Pace Papua Bot, kamu berperan sebagai orang papua dengan logat papua. Kamu berasal dari Sorong, Papua Barat Daya. Pastikan kamu selalu menggunakan logat papua dan melakukan jokes2 papua atau mop papua jika diminta. Kalau kasih jawaban, usahakan jangan lebih dari 1500 karakter.
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
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")

    if current_time in ["06:00", "21:00"]:
        print("Waktunya renungan!")
        channel = bot.get_channel(1371476522036105387)

        if channel:
            waktu = ""
            if current_time == "06:00":
                waktu = "pagi"
            elif current_time == "21:00":
                waktu = "malam"
            prompt = f"Buatkan renungan {waktu} ini untuk tanggal {now.day} {now.month} {now.year} dari Alkitab. Pastikan response tidak lebih dari 2000 karakter. Jangan berikan response seperti 'Tentu, ini renungan malam untuk tanggal ..., berdasarkan Alkitab:', tetapi langsung saja kasih tanpa memberikan response seolaholah response dari AI. Struktur dari renungan harus terdapat judul, ayat, isi renungan, dan apa yang harus didoakan hari ini."

            try:
                response = model.generate_content(prompt)
                await channel.send(
                    f"We kam pace <@{591159912881586183}> <@{533104933168480286}> <@{450509161210314752}> <@{460678478988312606}>, baca tong pu renungan {waktu} dulu ini."
                )
                await channel.send(response.text.strip())
            except Exception as e:
                print("Error:", e)
                await channel.send("❌ Gagal kirim pesan otomatis.")


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

        response = model.generate_content(prompt)

        # Masukkan response ke riwayat
        channel_histories[channel_id].append(f"Pace: {response.text.strip()}")

        await ctx.send(response.text.strip())

        # Kalau konteks > 20
        if len(channel_histories[channel_id]) > 22:
            channel_histories[channel_id] = [
                channel_histories[channel_id][0]
            ] + channel_histories[channel_id][-20:]

        print(channel_histories)

    except Exception as e:
        await ctx.send("❌ Terjadi kesalahan saat menjawab.")
        print("Error:", e)

        # Tangani error karena limit API
        if "quota" in str(e).lower() or "rate limit" in str(e).lower():
            admin_id = 533104933168480286
            await ctx.send(
                f"❌ Pace su capek, sa pu kuota API su habis ni😔\n<@{admin_id}>, bantu cek dulu!"
            )
        else:
            await ctx.send("❌ Terjadi kesalahan saat menjawab.")


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
