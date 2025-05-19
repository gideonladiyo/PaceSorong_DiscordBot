def generate_prompt(type: str, time=None, waktu=None):
    if type == "renungan" and (time is not None and waktu is not None):
        return f"Buatkan renungan {waktu} ini untuk tanggal {time.day} {time.month} {time.year} dari Alkitab. Pastikan response tidak lebih dari 2000 karakter. Jangan berikan response seperti 'Tentu, ini renungan malam untuk tanggal ..., berdasarkan Alkitab:', tetapi langsung saja kasih tanpa memberikan response seolaholah response dari AI. Struktur dari renungan harus terdapat judul, ayat, isi renungan, dan apa yang harus didoakan hari ini. Responsnya jangan ada 'Pace:', langsung responsenya"
    else:
        return "Maaf, saya tidak mengerti perintah Anda. Silakan periksa"
