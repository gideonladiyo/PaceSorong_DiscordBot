# Bot Pace Sorong 1.2.0

## Daftar Isi/Table of Contents

- [Pendahuluan](#pendahuluan)
- [Cara Membuat Bot](#cara-membuat-bot)
- [Cara Menggunakan Bot](#cara-menggunakan-bot)
- [Fitur Pace Sorong Bot](#fitur-pace-sorong-bot)

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

Copy Link yang dihasilkan lalu buka di browser dan pilih lokasi server bot akan ditambahkan.

## Fitur Pace Sorong Bot

- **Chatbot**: Pengguna dapat melakukan percakapan dengan bot ini di channel apa saja dengan memanggil command `/pace`. Bot ini dapat menjawab pertanyaan, memberikan informasi, dan melakukan tugas lainnya dengan menggunakan dialeg yang berasal dari Papua. Bot ini masih kurang dalam pemahaman konteks pada percakapan yang dilakukan dengan bot. Contoh penggunaan command:

    ```bash
    /pace halo pace!
    ```

- **Renungan pagi dan malam**: Pengguna dapat menyetel server di mana bot akan mengirim renungan pagi dan malam setiap jam 6 pagi dan 9 malam. Pengguna dapat memanggil command `/setrenunganchannel` pada channel tertentu agar bot dapat mengetahui channel mana saja yang akan dikirim renungan harian. Untuk membatalkan channel yang dipilih, pengguna bisa menggunakan command `/cancelrenunganchannel`. Jika pengguna ingin bot mengirim renungan secara manual, cukup panggil bot dengan command `/renunganmanual` diikuti dengan teks `pagi` atau `malam` setelah command agar bot mengetahui jenis renungan yang akan dikirim. Contoh penggunaan command:

    ```bash
    /setrenunganchannel
    /cancelrenunganchannel
    /renunganmanual pagi
    ```
