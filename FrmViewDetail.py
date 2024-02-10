# Filename : FrmView.py
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,E, W, font, ttk,messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from Penjualan import Penjualan
from Penjualan_detail import Penjualan_detail
from Barang import Barang
from datetime import datetime

class FrmViewDetail:
    def __init__(self, parent, title, update_main_window=None, extra_data=None):
        self.parent = parent      
        self.parent.geometry("490x400")
        self.parent.title(title)
        self.update_main_window = update_main_window 
        self.extra_data=extra_data
        self.nomor = self.extra_data[0]
        self.uraian = self.extra_data[1]
        self.tanggal = self.extra_data[2]
        self.totalbayar = self.extra_data[3]
        self.lunas = self.extra_data[4]
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.resized_img = None 
        self.aturKomponen()
        self.onReload(self.nomor)
        
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
        self.txtTANGGAL = Label(mainFrame, text=self.flip_date(self.tanggal))
        self.txtTANGGAL.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        Label(mainFrame, text='TOTAL BAYAR:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Date Input TOTAL BAYAR
        self.txtTOTALBAYAR = Label(mainFrame, text=self.custom_format(self.totalbayar))
        self.txtTOTALBAYAR.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        Label(mainFrame, text='LUNAS:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Date Input LUNAS
        self.txtLUNAS = Label(mainFrame, text=self.getStatusLunas(self.lunas))
        self.txtLUNAS.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        Label(mainFrame, text='Total Bayar:').place(x=280, y=350)
        Label(mainFrame, text=self.custom_format(self.totalbayar)).place(x=380, y=350)
        if(self.lunas==0):
            self.btnLunas = Button(mainFrame, text='Set Lunas', bg='green', fg='white', font=('Arial', 10, 'bold'),width=10, command=self.onSetLunas)
            self.btnLunas.place(x=0, y=350)

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
        self.tree.column('harga', width="100", anchor='e')
        self.tree.heading('qty', text='qty')
        self.tree.column('qty', width="30")
        self.tree.heading('subtotal', text='subtotal')
        self.tree.column('subtotal', width="100", anchor='e')
        # set tree position
        self.tree.place(x=0, y=175)

    def getStatusLunas(self, statuslunas):
        if(statuslunas==1):
            val = "Telah Lunas"
        else:
            val = "Belum Lunas"
        return val
    
    def onSetLunas(self):
        pj = Penjualan()
        val = pj.setLunas(self.nomor)
        if(val==1):
            messagebox.showinfo("showinfo", "Data Berhasil di set LUNAS")
            self.lunas = 1
            self.txtLUNAS.configure(text=self.getStatusLunas(self.lunas))
            self.btnLunas.destroy()

        else:
            messagebox.showwarning("showwarning", "Data Gagal di set LUNAS")

    
    def custom_format(self,number):
        formatted_number = "{:,.2f}".format(int(number))
        formatted_number = formatted_number.replace(',', 'temp').replace('.', ',').replace('temp', '.')
        return formatted_number

    def flip_date(self,input_date):
        # Parse the input string as a date
        date_object = datetime.strptime(input_date, '%Y-%m-%d')
        # Format the date in the desired way
        flipped_date = date_object.strftime('%d-%m-%Y')
        return flipped_date

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

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    def update_main_window(result):
        print(result)
        
    root = Tk()  
    aplikasi = FrmViewDetail(root, "Windows Detail Penjualan")
    root.mainloop() 