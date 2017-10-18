nim= int(input("masukan nim yang sesuai (tidak menggunakan 0 di depan : "))
loop=int(input("berapa banyak yang ingin di tampilkan : "))
K = 0

print("jumlah angka NIM yang di tampilkan dalam bilangan genap ")
while (K < loop):
            if (nim % 2) ==0:
                print(nim)
            K += 1
            nim += 1
print ("TERIMAKASIH")
