# Data list dari Kegiatan 1 Modul 1
data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari & jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

# Menggunakan filter dan lambda untuk mengambil nilai integer dari setiap string dalam data
filtered_data = list(map(lambda s: [x for x in s.split() if x.isdigit()], data))

# Menampilkan output
for item in filtered_data:
    print(item)
