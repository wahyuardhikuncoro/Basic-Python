### SOAL 3 ###
## PROGRAM PENILAIAN UJIAN TEORI DAN UJIAN ###

nilaiteori = float(input("Masukan Nilai Teori: "))
nilaipraktek = float(input("Masukan Nilai Praktek: "))

if nilaiteori < 70 and nilaipraktek < 70:
    print("Anda harus mengulang ujian teori dan praktek.")
elif nilaiteori < 70 and nilaipraktek >= 70:
    print("Anda harus mengulang ujian teori.")
elif nilaiteori >= 70 and nilaipraktek < 70:
    print("Anda harus mengulang ujian praktek.")
else:
    print("Selamat, anda lulus!")