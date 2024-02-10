# Filename : FrmView.py
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,E, W, font, ttk,messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from Penjualan import Penjualan
from Penjualan_detail import Penjualan_detail
from Barang import Barang
import random
import string

class FrmDetail:
    def __init__(self, parent, title, update_main_window=None, extra_data=None):
        self.parent = parent      
        self.parent.geometry("490x400")
        self.parent.title(title)
        self.update_main_window = update_main_window 
        self.extra_data=extra_data
        self.nomor = self.extra_data[0]
        self.uraian = self.extra_data[1]
        self.tanggal = self.extra_data[2]
        self.totalbayar = 0
        self.lunas = 0
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.resized_img = None 
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        self.txtDisplay=Label(mainFrame)
        self.txtDisplay.place(x=290, y=0)
        self.txtDisplay.configure(text=self.custom_format(self.totalbayar),font=('Arial', 20, 'bold'))

        Label(mainFrame, text='NOMOR_BUKTI:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NOMOR_BUKTI
        self.txtNOMOR_BUKTI = Label(mainFrame, text=self.nomor) 
        self.txtNOMOR_BUKTI.grid(row=0, column=1, sticky=W, padx=5, pady=5) 

        Label(mainFrame, text='URAIAN:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox URAIAN
        self.txtURAIAN = Label(mainFrame, text=self.uraian) 
        self.txtURAIAN.grid(row=1, column=1, sticky=W, padx=5, pady=5) 

        Label(mainFrame, text='TANGGAL:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL
        self.txtTANGGAL = Label(mainFrame, text=self.tanggal)
        self.txtTANGGAL.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        # Specify the desired width and height
        Label(mainFrame, text='KODE_BARANG:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtKODE_BARANG = Entry(mainFrame, width=10) 
        self.txtKODE_BARANG.grid(row=4, column=0,sticky=W, padx=5, pady=5) 
        self.txtKODE_BARANG.bind("<Return>",self.onCariBarang)
        
        Label(mainFrame, text='NAMA_BARANG:').grid(row=3, column=1, sticky=W, padx=5, pady=5)
        # Textbox NAMA_BARANG
        self.txtNAMA_BARANG = Entry(mainFrame) 
        self.txtNAMA_BARANG.grid(row=4, column=1, padx=5, pady=5)

        Label(mainFrame, text='QTY:').grid(row=3, column=3, sticky=W, padx=5, pady=5)
        # Textbox QTY
        self.txtQTY = Entry(mainFrame, width=5) 
        self.txtQTY.grid(row=4, column=3, padx=5, pady=5)
        self.txtQTY.delete(0,END)
        self.txtQTY.insert(END,"1")

        Label(mainFrame, text='HARGA:').grid(row=3, column=4, sticky=W, padx=5, pady=5)
        # Textbox HARGA
        self.txtHARGA = Entry(mainFrame) 
        self.txtHARGA.grid(row=4, column=4, padx=5, pady=5)

        self.btnSimpan = Button(mainFrame, text='+', bg='orange', fg='black', font=('Arial', 10, 'bold'),width=5, command=self.onSimpan)
        self.btnSimpan.grid(row=4, column=5, padx=5, pady=5)

        self.btnLunas = Button(mainFrame, text='Set Lunas', bg='green', fg='white', font=('Arial', 10, 'bold'),width=10, command=self.onSetLunas)
        self.btnLunas.place(x=0, y=350)

        self.LabelTotalBayar = Label(mainFrame, text='Total Bayar:').place(x=280, y=350)
        self.txtTotalBayar = Label(mainFrame)
        self.txtTotalBayar.place(x=380, y=350)
        # define columns
        columns = ('id','kode_barang','nama_barang','harga', 'qty', 'subtotal')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings', height=7)
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('kode_barang', text='kode_barang')
        self.tree.column('kode_barang', width="100")
        self.tree.heading('nama_barang', text='nama_barang')
        self.tree.column('nama_barang', width="100")
        self.tree.heading('harga', text='harga')
        self.tree.column('harga', width="100")
        self.tree.heading('qty', text='qty')
        self.tree.column('qty', width="30")
        self.tree.heading('subtotal', text='subtotal')
        self.tree.column('subtotal', width="100")
        # set tree position
        self.tree.place(x=0, y=175)
    
    def custom_format(self,number):
        formatted_number = "{:,.2f}".format(number)
        formatted_number = formatted_number.replace(',', 'temp').replace('.', ',').replace('temp', '.')
        return formatted_number

    def generate_random_string(self,length):
        characters = string.ascii_letters + string.digits + string.punctuation
        # Remove unwanted characters
        characters = ''.join(char for char in characters if char not in 'iIoO0')
        return ''.join(random.choice(characters) for _ in range(length))

    def onCariBarang(self, event=None):
        kode_barang = self.txtKODE_BARANG.get()
        obj = Barang()
        res = obj.getByKODE_BARANG(kode_barang)
        rec = obj.affected
        if(rec>0):
            self.TampilBarang()
            self.ditemukan=False
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan=None
        return res
    
    def TampilBarang(self):
        kode_barang = self.txtKODE_BARANG.get()
        obj = Barang()
        res = obj.getByKODE_BARANG(kode_barang)
        self.txtNAMA_BARANG.delete(0,END)
        self.txtNAMA_BARANG.insert(END,obj.nama_barang)
        self.txtHARGA.delete(0,END)
        self.txtHARGA.insert(END,obj.harga)

    def onReload(self, nomor):
        # get data penjualan_detail
        obj = Penjualan_detail()
        result = obj.getAllData(nomor)
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)

        for row in mylist:
            self.tree.insert('',END, values=row)

    def onSetLunas(self):
        pj = Penjualan()
        val = pj.setLunas(self.nomor)
        if(val==1):
            messagebox.showinfo("showinfo", "Data Berhasil di set LUNAS")
            self.btnSimpan.destroy()
            self.btnLunas.destroy()

        else:
            messagebox.showwarning("showwarning", "Data Gagal di set LUNAS")


    def onClear(self, event=None):                          
        self.txtKODE_BARANG.delete(0,END)
        self.txtKODE_BARANG.insert(END,"")

        self.txtNAMA_BARANG.delete(0,END)
        self.txtNAMA_BARANG.insert(END,"")
                                
        self.txtQTY.delete(0,END)
        self.txtQTY.insert(END,"1")

        self.txtHARGA.delete(0,END)
        self.txtHARGA.insert(END,"")
                                                                
        self.btnSimpan.config(text="+")
        self.onReload(self.nomor)
        self.ditemukan = False

    def onSimpan(self, event=None):
        kode = self.generate_random_string(5)
        nomor_bukti = self.nomor
        kode_barang = self.txtKODE_BARANG.get()
        qty = self.txtQTY.get()
        harga = self.txtHARGA.get()
        subtotal = int(qty) * float(harga)        
        obj = Penjualan_detail()
        pj = Penjualan()
        tb = pj.getTotalbayar(nomor_bukti)
        obj.kode = kode
        obj.nomor_bukti = nomor_bukti
        obj.kode_barang = kode_barang
        obj.qty = qty
        obj.harga = harga
        obj.subtotal = subtotal

        res = obj.simpan()
        ket = 'Disimpan'
            
        rec = obj.affected
        if(rec>0):
            total = int(tb) + int(subtotal)
            self.totalbayar = total
            pj.updateTotalbayar(total, nomor_bukti)
            self.onReload(nomor_bukti)
            self.txtDisplay.configure(text=self.custom_format(self.totalbayar),font=('Arial', 20, 'bold'))
            self.txtTotalBayar.configure(text=self.custom_format(self.totalbayar))
            self.onClear()
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        
        return rec

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    def update_main_window(result):
        print(result)
        
    root = Tk()  
    aplikasi = FrmDetail(root, "Windows Detail Penjualan")
    root.mainloop() 