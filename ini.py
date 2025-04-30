#Manipulasi filel
handle = open('mbox-short.txt') 
count = 0 
for line in handle: 
  count = count + 1 
print('Line Count:', count)

#menampilkan ukuran file teks dalam bytes
handle = open('mbox-short.txt') 
hasil = handle.read() 
print("Ukuran: " + len(hasil) + "bytes") 
print("Huruf dari belakang sendiri mundur 16 huruf adalah: " + hasil[-16::1])

#Selama dilakukan looping kita juga dapat melakukan manipulasi terhadap file tersebut, seperti misalnya menangkap / menampilkan bagian dari string.
handle = open('mbox-short.txt') 
count = 1 
for line in handle: 
  if line.startswith("Date:") and count <= 10: 
    count += 1 
    print(line)

#penyimpanan file
handle = open('output.txt','w') 
tulisan = "teks ini akan dituliskan ke file\n" 
handle.write(tulisan) 
handle.close()

#digunakan perintah find(). Untuk menampilkan jumlah baris digunakan counter untuk setiap baris yang ditemukan.
filename = input("nama file: ") 
handle = open(filename) 
c = 0 
for line in handle: 
  if line.find("ac.uk") !=-1: 
    c += 1 
    print("Web domain 'ac.uk' ditemukan di \"" + line.strip() + "\"") 
print("Jumlah: ",c)

#tampilkanlah berapa baris string pada file yang diawali kata "Subject"
filename = input("nama file: ") 
handle = open(filename) 
c = 0 
for line in handle: 
  if line.startswith("Subject:"): 
    c += 1 
    line = line.strip().title() 
    print(line) 
print("Jumlah: ",c)

#Program harus mampu menampilkan ukuran file dalam KB dari sebuah file teks dan menghandle error jika file yang diinputkan tidak ditemukan.
filename = input("nama file: ") 
try: 
  handle = open(filename) 
  total = 0 
  for line in handle: 
    total += len(line) 
    kb = total / 1000 
    print("Ukuran: " + str(mb) + " KB") 
except: 
  print("File tiidak ditemukan!")

