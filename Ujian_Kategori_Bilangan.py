import math

def kategori(angka):
    jawaban=[]
    if(math.isnan(angka)):
        return "Input bukan angka"
    else:
        if (isinstance(angka,int)):
            jawaban.append('Bulat')
        if (angka>=0):
            jawaban.append('Cacah')
        if (angka < 0):
            jawaban.append('Negatif')
        if (angka == 0):
            jawaban.append('Nol')
        if (angka > 0):
            jawaban.append('Asli')
        if (angka % 2 == 1):
            jawaban.append('Ganjil')
        if (angka % 2 == 0):
            jawaban.append('Genap')
            
        if (primaAtauKomposit(angka)=="prima"):
            jawaban.append('Prima')
        elif (primaAtauKomposit(angka)=="komposit"):
            jawaban.append('Komposit')
    return jawaban

def primaAtauKomposit(angka):
    if angka < 2:
        return "Bukan Prima atau Komposit"
    elif angka == 2:
        return "prima"

    i = 2
    batas = int(math.sqrt(angka))

    while i <= batas:
        if angka % i == 0:
            return "komposit"
        i += 1

    return "prima"

try:
    userinputchecker=input("Masukkan angka ")
    if(userinputchecker.__contains__('.')):
        inputasli=float(userinputchecker)
    else:
        inputasli=int(userinputchecker)
    print(kategori(inputasli))
except:
    print("Input Bukan Angka")
