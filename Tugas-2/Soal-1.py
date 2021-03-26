### SOAL 1 ###
## PROGRAM MENYIMPAN DAN MENAMPILKAN KONTAK ###

# dictionary list_contact
list_contact = []

# fungsi add_contact
def add_contact():
    print("")
    name = input("Nama: ")
    phone = input("No Telepon: ")
    contact = {
        "nama": name,
        "telepon": phone
    }
    return contact

# fungsi contact_list
def contact_list(list_contact):
    for contact in list_contact:
        print("")
        print(f"Nama: {contact['nama']}")
        print(f"No Telepon: {contact['telepon']}")

# while condition menu
# if choice 1 maka masuk ke contact_list
# elif chioce 2 maka masuk ke add_contact
# elif choice 3 maka break print("Program selesai, sampai jumpa!")
# else choice != 1,2,3 maka print("Menu tidak tersedia!")
while True:
    print("")
    print("Selamat Datang!")
    print("--MENU--")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

    choice = input("Pilih Menu: ")
    if choice == "1":
        print("Daftar Kontak:")
        contact_list(list_contact)
    elif choice == "2":
        contact = add_contact()
        list_contact.append(contact)
        print("Kontak berhasil ditambahkan.")
    elif choice == "3":
        print("Program selesai, sampai jumpa!")
        print("")
        break
    else:
        print("Menu tidak tersedia!")