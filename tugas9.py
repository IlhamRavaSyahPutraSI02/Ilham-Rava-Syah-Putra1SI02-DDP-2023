def say(nama,alamat,gender,umur,hooby):
    print("nama saya adalah",nama)
    print("saya tinggal di",alamat)
    print("gender saya adalah",gender)
    print("saat ini saya berusia",umur)
    print("saya menyukai",hooby)
#panggil
say("Rava","cikeas","laki-laki","18","masak")

print()
def cek_nilai_kelulusan(nilai):
    if nilai<60:
        print("gagal")
    elif 61 <= nilai <= 70:
        print("baik")
    elif 71<= nilai <=80:
        print("sangat baik")
    elif 81 <= nilai<= 100:
        print("istimewa")
    else:
        print("tidak lulus")
#panggil
cek_nilai_kelulusan(90)

print()
def ganjil(angka):
    for x in range(1, angka + 1, 2):
        print(x)
ganjil(100)