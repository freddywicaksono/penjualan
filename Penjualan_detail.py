
# filename : Penjualan_detail.py
from db import DBConnection as mydb

class Penjualan_detail:

    def __init__(self):
        self.__id=None
        self.__kode=None
        self.__nomor_bukti=None
        self.__kode_barang=None
        self.__qty=None
        self.__harga=None
        self.__subtotal=None

        self.conn = None
        self.affected = None
        self.result = None


    @property
    def id(self):
        return self.__id

    @property
    def kode(self):
        return self.__kode
        
    @kode.setter
    def kode(self, value):
        self.__kode = value

    @property
    def nomor_bukti(self):
        return self.__nomor_bukti
        
    @nomor_bukti.setter
    def nomor_bukti(self, value):
        self.__nomor_bukti = value

    @property
    def kode_barang(self):
        return self.__kode_barang
        
    @kode_barang.setter
    def kode_barang(self, value):
        self.__kode_barang = value

    @property
    def qty(self):
        return self.__qty
        
    @qty.setter
    def qty(self, value):
        self.__qty = value

    @property
    def harga(self):
        return self.__harga
        
    @harga.setter
    def harga(self, value):
        self.__harga = value

    @property
    def subtotal(self):
        return self.__subtotal
        
    @subtotal.setter
    def subtotal(self, value):
        self.__subtotal = value





    def simpan(self):
        self.conn = mydb()
        val = (self.__kode,self.__nomor_bukti,self.__kode_barang,self.__qty,self.__harga,self.__subtotal)
        sql="INSERT INTO Penjualan_detail (kode,nomor_bukti,kode_barang,qty,harga,subtotal) VALUES " + str(val)

        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kode,self.__nomor_bukti,self.__kode_barang,self.__qty,self.__harga,self.__subtotal, id)
        sql="UPDATE penjualan_detail SET kode = %s,nomor_bukti = %s,kode_barang = %s,qty = %s,harga = %s,subtotal = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByKODE(self, kode):
        self.conn = mydb()
        val = (self.__nomor_bukti,self.__kode_barang,self.__qty,self.__harga,self.__subtotal, kode)
        sql="UPDATE penjualan_detail SET nomor_bukti = %s,kode_barang = %s,qty = %s,harga = %s,subtotal = %s WHERE kode=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM penjualan_detail WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByKODE(self, kode):
        self.conn = mydb()
        sql="DELETE FROM penjualan_detail WHERE kode='" + str(kode) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM penjualan_detail WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)

        self.__id = self.result[0]
        self.__kode = self.result[1]
        self.__nomor_bukti = self.result[2]
        self.__kode_barang = self.result[3]
        self.__qty = self.result[4]
        self.__harga = self.result[5]
        self.__subtotal = self.result[6]
        self.conn.disconnect
        return self.result

    def getByKODE(self, kode):
        a=str(kode)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM penjualan_detail WHERE kode='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__kode = self.result[1]
           self.__nomor_bukti = self.result[2]
           self.__kode_barang = self.result[3]
           self.__qty = self.result[4]
           self.__harga = self.result[5]
           self.__subtotal = self.result[6]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__kode = ''
           self.__nomor_bukti = ''
           self.__kode_barang = ''
           self.__qty = ''
           self.__harga = ''
           self.__subtotal = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self, nomor):
        # id, kode_barang, nama_barang, harga, qty, subtotal
        self.conn = mydb()
        sql="SELECT a.id, a.kode_barang, b.nama_barang, CONCAT(FORMAT(a.harga, 2), '') AS harga, a.qty, CONCAT(FORMAT(a.subtotal, 2), '') AS subtotal FROM penjualan_detail AS a JOIN barang AS b ON a.kode_barang = b.kode_barang WHERE a.nomor_bukti = '" + nomor + "'"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,nomor_bukti FROM penjualan_detail"
        self.result = self.conn.findAll(sql)
        return self.result        
        