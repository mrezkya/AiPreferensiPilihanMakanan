#Objek 
#Inheritance
class Objek:
    def __init__(self,nama,umur):
        self.name = nama
        self.age  = umur

    def TampilkanPesan(self):
        print('halo {} umur kamu {}'.format(self.name, self.age))
#Inheritance
class Pegawai(Objek):
    def TampilNamaPegawai(self):
        print(f'halo {self.name} anda adalah seorang staf di sini')

#class objek di panggil
Objek('panini',12).TampilkanPesan()
#class Pegawai di panggil
Pegawai('panini',12).TampilNamaPegawai()