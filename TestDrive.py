import sqlite3

class koneksi:
    def __init__(self,database,user,komen) -> str:
        self.database = database
        self.user = user
        self.komen = komen
    def Database(self):
        return sqlite3.connect(self.database)
    def TampilkanKomen(self):
        koneksi = self.Database()
        print(koneksi.execute('select * from komen').fetchall())
    def TambahKomen(self):
        koneksi = self.Database()
        sql = f"insert into komen values('{self.user}','{self.komen}')"
        koneksi.execute(sql)
        koneksi.commit()
koneksi('FinalAI.db','dion','hebat sekali').TampilkanKomen()
# koneksi('FinalAI.db','dion','hebat sekali').TambahKomen()