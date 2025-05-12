# Bot Pace Sorong 1.1.0

## Daftar Isi/Table of Contents

- [Pendahuluan](#pendahuluan)
- [Cara Membuat Bot](#cara-membuat-bot)
- [Cara Menggunakan Bot](#cara-menggunakan-bot)

## Pendahuluan

Selamat datang di bot Pace Sorong! Bot ini hanya seperti bot lainnya, tetapi mempunyai fitur chating dengan bantuan Gemini API dengan konteks bot sebagai orang Sorong. Bot ini akan berbicara dengan bahasa Indonesia tetapi dengan logat Papua.

## Cara Membuat Bot

Untuk membuat bot ini, cukup clone repository ini, kemudian buat file `.env` yang berisi variabel `GOOGLE_API_KEY` dan `DISCORD_TOKEN` dengan nilai yang sesuai. Di bawah adalah langkah-langkah lengkapnya:

- Clone Repositori

Jalankan perintah berikut di terminal:

```bash

git clone https://github.com/gideonladiyo/PaceSorong_DiscordBot.git

```

lalu:

```bash

cd PaceSorong_DiscordBot
code .

```

- Install library/depedencies dengan memasukkan command berikut di terminal:

```bash
pip install -r requirements.txt
```

- Buat file `.env` pada direktoru proyek dengan isi sebagai berikut:

```dotenv
GOOGLE_API_KEY=YOUR_GEMINI_KEY
DISCORD_TOKEN=YOUR_DISCORD_KEY
```

- Dapatkan Gemini API Key di link [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
- Dapatkan Discord Token di link [https://discord.com/developers/applications](https://discord.com/developers/applications)
- Jalankan bot dengan memasukkan command berikut di terminal:

```bash
python bot.py
```

## Cara Menggunakan Bot

Untuk menggunakan bot, buka discord developer lalu pilih bot yang akan ditambahkan ke server discord. Setelah itu, buka menu OAuth2. Untuk `Scopes` pilih:

- ✅Bot

Untuk `Bot Permission` pilih:

- ✅Send Messages
- ✅View Channels
- ✅Read Messages History

Copy Link yang dihasilkan lalu buka di browser dan pilih lokasi server bot akan ditambahkan. Untuk memanggil bot di chat, cukup awali dengan command `/pace` pada chat. Contoh:

```bash
/pace halo pace
```

Command `/reset` untuk mereset konteks dari channel jika response bot mulai tidak sesuai atau nguawuor.

Terdapat fitur renungan harian setiap jam 6 pagi dan jam 9 malam yang otomatis dikirimkan ketika bot sedang dijalankan
