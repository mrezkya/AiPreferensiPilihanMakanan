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
#enkapsulasi
class password:
    def __init__(self,username,password):
        self.__user = username
        self.__pass = password
    def TampilInfo(self):
        print(f'halo {self.__user} anda punya password {self.__pass}')
#contoh error mengakses enkapsulasi
# class error(password):
#     def test(self):
#         print(f'halo {self.__user}')
        
#polymorphism
class poly:
    def __init__(self,prodi,univ):
        self.prodi = prodi
        self.univ = univ

    def TampilkanPesan(self):
        print(f'prodi kamu adalah {self.prodi}, dan universitas kami adalah {self.univ}')
#class objek di panggil
Objek('panini',12).TampilkanPesan()
poly('Teknik Informatika','UHO').TampilkanPesan()
#class Pegawai di panggil
Pegawai('panini',12).TampilNamaPegawai()
#class Passowrd di panggil
password('panini123',123123123).TampilInfo()
# error('panini123',1111).test()