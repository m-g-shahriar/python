from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


class DemoSplashScreen:
    def __init__(self, parent):
        self.parent = parent

        self.aturSplash()
        self.aturWindow()

    def aturSplash(self):
        # import image menggunakan Pillow
        self.gambar = Image.open('py.jpg')
        self.imgSplash = ImageTk.PhotoImage(self.gambar)

    def aturWindow(self):
        # ambil ukuran dari file image
        lebar, tinggi = self.gambar.size

        setengahLebar = (self.parent.winfo_screenwidth() - lebar) // 2
        setengahTinggi = (self.parent.winfo_screenheight() - tinggi) // 2

        # atur posisi window di tengah-tengah layar
        self.parent.geometry("%ix%i+%i+%i" % (lebar, tinggi,
                                              setengahLebar, setengahTinggi))

        # atur Image via Komponen Label
        Label(self.parent, image=self.imgSplash).pack()


if __name__ == '__main__':
    root = Tk()

    # menghilangkan judul dan batas frame Window
    root.overrideredirect(True)
    progressbar = ttk.Progressbar(orient=HORIZONTAL, length=10000, mode='determinate')
    progressbar.pack(side="bottom")
    app = DemoSplashScreen(root)
    progressbar.start()

    # menutup window setelah 5 detik
    root.after(6010, root.destroy)

    root.mainloop()