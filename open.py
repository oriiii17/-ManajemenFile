# mbox = open("mbox.txt")
inputan = input("Masukkan nama buku yang ingin dicari : ")
ini = open("daftarbuku.txt")
# print(mbox)

hasil = ini.readlines()
count = 1
state = True

for i in hasil :
    lineTemp = i.split(",")
    if lineTemp[0].lower() == inputan.lower() :

        print('Buku ditemukan')
        print('Nama : ', lineTemp[0])
        print('Kode :', lineTemp[1])
        print('Tahun rilis :', lineTemp[2])
        print('Deskripsi :', lineTemp[3])

        state = True
        break

    elif inputan is not state :
        print("Buku tidak ditemukan")


    # spasi = i.strip('')
    # a = i.split(',')
    # if inputan.lower() in i.lower():
    #     print(Hasil)
    #     print(a)
    # if inputan == "Pengenalan Java untuk Pemula"  :
    #     print("BUKU DITEMUKAN ----")
    #     print("Nama : ", inputan)



# count = 0
# for line in mbox :
#     count = count + 1
# print('Line count : ', count)

# hasil = mbox.read()
# ini = 'X-DSPAM-Result:'
# count = 0
# if ini in hasil :
#     for i in ini :
#         count = count + 1
#     print(count)