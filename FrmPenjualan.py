# filename : FrmPenjualan.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W, SW, NW,StringVar,messagebox
from Penjualan import Penjualan
from FrmDetail import *
from FrmViewDetail import *
from bs4 import BeautifulSoup 
import time

# pip install tkcalendar
from tkcalendar import Calendar, DateEntry

class FormPenjualan:   
    def __init__(self, parent, title, update_main_window=None):
        self.parent = parent       
        self.parent.geometry("500x370")
        self.parent.title(title)
        self.update_main_window = update_main_window
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.__data = []    
        self.ditemukan = None
        self.totalbayar = None
        self.lunas = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='NOMOR_BUKTI:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NOMOR_BUKTI
        self.txtNOMOR_BUKTI = Entry(mainFrame) 
        self.txtNOMOR_BUKTI.grid(row=0, column=1, sticky=W, padx=5, pady=5) 
        self.txtNOMOR_BUKTI.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # text 

        Label(mainFrame, text='URAIAN:').grid(row=1, column=0, sticky=NW, padx=5, pady=5)
        # Text Area Box
        
        self.txtURAIAN = tk.Text(mainFrame, height=5, width=30) 
        self.txtURAIAN.grid(row=1, column=1, padx=5, pady=5)
        
        
         # date 

        Label(mainFrame, text='TANGGAL:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL
        self.txtTANGGAL = DateEntry(mainFrame, width= 12, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL.grid(row=2, column=1, sticky=W, padx=5, pady=5)
                    
        
            
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=5, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=5,sticky=NW, padx=5, pady=5)
        
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=1, column=5, padx=5, pady=5)
        self.btnView = Button(mainFrame, text='View Detail', command=self.onView, width=10)
        
        # define columns
        columns = ('id','nomor_bukti','uraian','tanggal','total_bayar','lunas')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings', height=7)
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('nomor_bukti', text='nomor_bukti')
        self.tree.column('nomor_bukti', width="50")
        self.tree.heading('uraian', text='uraian')
        self.tree.column('uraian', width="150")
        self.tree.heading('tanggal', text='tanggal')
        self.tree.column('tanggal', width="100")
        self.tree.heading('total_bayar', text='total_bayar')
        self.tree.column('total_bayar', width="100")
        self.tree.heading('lunas', text='lunas')
        self.tree.column('lunas', width="50")
        # set tree position
        self.tree.place(x=0, y=175)
        # Create a Vertical Scrollbar
        
        self.onReload()

    def onView(self):
        if(self.ditemukan==True):
            self.new_window("View Detail", FrmViewDetail, self.__data)

    def on_treeview_scroll(self,*args):
        self.tree.yview(*args)

    def clean_html_tags(self,html_text):
        soup = BeautifulSoup(html_text, 'html.parser')
        cleaned_text = soup.get_text()
        return cleaned_text

    def onClear(self, event=None):
        self.__data = [] 
        self.ditemukan = None
        self.totalbayar = None
        self.lunas = None
        self.txtNOMOR_BUKTI.delete(0,END)
        self.txtNOMOR_BUKTI.insert(END,"")

        self.txtURAIAN.delete("1.0",END)
        self.txtURAIAN.insert("1.0","")
                                    
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        self.btnView.destroy()

    def onReload(self, event=None):
        # get data penjualan
        obj = Penjualan()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)

        for row in mylist:
            self.tree.insert('',END, values=row)
            


    def onCari(self, event=None):
        nomor_bukti = self.txtNOMOR_BUKTI.get()
        obj = Penjualan()
        res = obj.getByNOMOR_BUKTI(nomor_bukti)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        nomor_bukti = self.txtNOMOR_BUKTI.get()
        obj = Penjualan()
        res = obj.getByNOMOR_BUKTI(nomor_bukti)
        self.txtURAIAN.delete("1.0",END)
        self.txtURAIAN.insert("1.0",self.clean_html_tags(obj.uraian))
        self.txtTANGGAL.delete(0,END)
        self.txtTANGGAL.insert(END,obj.tanggal)
        self.btnSimpan.config(text="Update")
        nomor_bukti = self.txtNOMOR_BUKTI.get()
        uraian = self.txtURAIAN.get("1.0", "end-1c")
        tanggal = self.txtTANGGAL.get()
        self.totalbayar = obj.total_bayar
        self.lunas = obj.lunas
        self.__data.append(nomor_bukti)
        self.__data.append(uraian)
        self.__data.append(tanggal)
        self.__data.append(self.totalbayar)
        self.__data.append(self.lunas)
        self.btnView.grid(row=1, column=5, sticky=SW ,padx=5, pady=5)

    def onSimpan(self):
        nomor_bukti = self.txtNOMOR_BUKTI.get()
        uraian = self.txtURAIAN.get("1.0", "end-1c")
        tanggal = self.txtTANGGAL.get()
           
        obj = Penjualan()

        obj.nomor_bukti = nomor_bukti
        obj.uraian = uraian
        obj.tanggal = tanggal
        self.__data.append(nomor_bukti)
        self.__data.append(uraian)
        self.__data.append(tanggal)

        if(self.ditemukan==True):
            res = obj.updateByNOMOR_BUKTI(nomor_bukti)
            ket = 'Diperbarui'
            
        else:
            obj.total_bayar = 0
            obj.lunas = 0
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
            self.onReload()
            if(self.ditemukan == False):  # jika data baru
                time.sleep(2)
                self.new_window("Entry Detail", FrmDetail, self.__data)

        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec


 
    def onDelete(self, event=None):
        nomor_bukti = self.txtNOMOR_BUKTI.get()
        obj = Penjualan()
        obj.nomor_bukti = nomor_bukti
        if(self.ditemukan==True):
            res = obj.deleteByNOMOR_BUKTI(nomor_bukti)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
    def new_window(self, number, _class, extra_data):
        new = tk.Toplevel(self.parent)
        new.transient()
        new.grab_set()
        _class(new, number, self.update_main_window, extra_data)

    def update_main_window(self, data):
        # Method to receive data from child windows
        self.__data = data
        level = self.__data[0]
        loginvalid = self.__data[1]
        if(loginvalid==True):
            index = self.file_menu.index('Login')
            # hapus menu login
            self.file_menu.delete(index)
            self.file_menu.add_command(label='Logout', command=self.Logout)

            # tambahkan menu sesuai level
            if(level=='admin'): 
                self.menubar.add_cascade(label="Admin", menu=self.admin_menu)
                self.__level = 'Admin'
            else:
                pass

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()


if __name__ == '__main__':
    def update_main_window(result):
        print(result)

    root = tk.Tk()
    aplikasi = FormPenjualan(root, "Aplikasi Data Penjualan")
    root.mainloop() 
    
