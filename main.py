#game secret number

secret_number = 111
tebakan = int (input("Tebak Angka:"))

while secret_number != tebakan:
    print("Haha.. kamu terjebak dalam looping selamanya")
    print("Coba tebal lagi")
    tebakan = int(input("Tebak Angka:"))

    print("Selamat anda benar!!")