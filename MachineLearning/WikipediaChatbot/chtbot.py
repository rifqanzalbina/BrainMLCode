import wikipediaapi

# Inisialisasi objek Wikipedia
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent='CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org) generic-library/0.0'
)

# Minta pengguna memasukkan judul halaman yang ingin dicari
input_title = input("Masukkan judul halaman Wikipedia: ")

# Dapatkan halaman Wikipedia berdasarkan input pengguna
page = wiki_wiki.page(input_title)

if page.exists():
    print("Judul artikel:", page.title)
    print("Isi artikel:\n", page.text)
else:
    print("Halaman tidak ditemukan.")

print("Daftar bahasa yang tersedia:")
for lang in page.langlinks:
    print(f"- {lang}: {page.langlinks[lang].title}")
