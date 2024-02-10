
# filename : Penjualan.py
from db import DBConnection as mydb

class Penjualan:

    def __init__(self):
        self.__id=None
        self.__nomor_bukti=None
        self.__uraian=None
        self.__tanggal=None
        self.__total_bayar=None
        self.__lunas=None

        self.conn = None
        self.affected = None
        self.result = None


    @property
    def id(self):
        return self.__id

    @property
    def nomor_bukti(self):
        return self.__nomor_bukti
        
    @nomor_bukti.setter
    def nomor_bukti(self, value):
        self.__nomor_bukti = value

    @property
    def uraian(self):
        return self.__uraian
        
    @uraian.setter
    def uraian(self, value):
        self.__uraian = value

    @property
    def tanggal(self):
        return self.__tanggal
        
    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value

    @property
    def total_bayar(self):
        return self.__total_bayar
        
    @total_bayar.setter
    def total_bayar(self, value):
        self.__total_bayar = value

    @property
    def lunas(self):
        return self.__lunas
        
    @lunas.setter
    def lunas(self, value):
        self.__lunas = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nomor_bukti,self.__uraian,self.__tanggal,self.__total_bayar,self.__lunas)
        sql="INSERT INTO Penjualan (nomor_bukti,uraian,tanggal,total_bayar,lunas) VALUES " + str(val)

        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nomor_bukti,self.__uraian,self.__tanggal,self.__total_bayar,self.__lunas, id)
        sql="UPDATE penjualan SET nomor_bukti = %s,uraian = %s,tanggal = %s,total_bayar = %s,lunas = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNOMOR_BUKTI(self, nomor_bukti):
        self.conn = mydb()
        val = (self.__uraian,self.__tanggal,self.__total_bayar,self.__lunas, nomor_bukti)
        sql="UPDATE penjualan SET uraian = %s,tanggal = %s,total_bayar = %s,lunas = %s WHERE nomor_bukti=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def getTotalbayar(self, nomor):
        self.conn = mydb()
        sql="SELECT total_bayar FROM penjualan WHERE nomor_bukti='" + str(nomor) + "'"
        self.result = self.conn.findOne(sql)
        self.__total_bayar = self.result[0]
        self.conn.disconnect
        return self.__total_bayar
     
    def updateTotalbayar(self, nominal, nomor_bukti):
        self.conn = mydb()
        val = (nominal, nomor_bukti)
        sql="UPDATE penjualan SET total_bayar = %s WHERE nomor_bukti=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def setLunas(self, nomor_bukti):
        self.conn = mydb()
        val = (nomor_bukti,)
        sql="UPDATE penjualan SET lunas = '1' WHERE nomor_bukti=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM penjualan WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNOMOR_BUKTI(self, nomor_bukti):
        self.conn = mydb()
        sql="DELETE FROM penjualan WHERE nomor_bukti='" + str(nomor_bukti) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM penjualan WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)

        self.__id = self.result[0]
        self.__nomor_bukti = self.result[1]
        self.__uraian = self.result[2]
        self.__tanggal = self.result[3]
        self.__total_bayar = self.result[4]
        self.__lunas = self.result[5]
        self.conn.disconnect
        return self.result

    def getByNOMOR_BUKTI(self, nomor_bukti):
        a=str(nomor_bukti)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM penjualan WHERE nomor_bukti='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__nomor_bukti = self.result[1]
           self.__uraian = self.result[2]
           self.__tanggal = self.result[3]
           self.__total_bayar = self.result[4]
           self.__lunas = self.result[5]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__nomor_bukti = ''
           self.__uraian = ''
           self.__tanggal = ''
           self.__total_bayar = ''
           self.__lunas = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM penjualan"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,uraian FROM penjualan"
        self.result = self.conn.findAll(sql)
        return self.result        
        