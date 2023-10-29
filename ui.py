import tkinter as tk
from tkinter import *
from tkinter import filedialog # thu vien SUB-LIB tkinter = Hop thoai ho tro Mo file
from tkinter import messagebox as msg # thu vien SUB-LIB tkinter = Hop thong bao = messagebox
from PIL import Image, ImageTk
#B2: THIET LAP & KHOI TAO DOI TUONG FORM
wf = tk.Tk()
wf.title("N19DCPT064")
wf.geometry("600x500")
wf.resizable(tk.FALSE, tk.FALSE)

def OpenTextFile():
    global filepath
    filepath = filedialog.askopenfilename(title = "File to translate",
    filetypes = (("Audio file (*.mp3)", "*.mp3"),))
    f1 = open(filepath, "r", encoding="utf-8")
    print("filepath", filepath)
    f1.close()

# Left side
# tk.Label(wf,text="Check Valid Video",relief = tk.SUNKEN, width = 25).place(x=5, y=5)
# tk.Frame(wf, width = 380, height = 600, relief = tk.SUNKEN, borderwidth = 3).place(x=5, y=40)
# # Right side
# tk.Label(wf,text="SKU Available",relief = tk.SUNKEN, width = 25).place(x=700, y=5)
# tk.Frame(wf, width = 380, height = 600, relief = tk.SUNKEN, borderwidth = 3).place(x=520, y=40)
image_path = 'Logo_PTIT_University.png'
img= Image.open(image_path)

#Resize the Image using resize method
resized_image= img.resize((100,100), Image.ANTIALIAS)
image = ImageTk.PhotoImage(resized_image)

canvas= Canvas(wf, width= 300, height= 300)
canvas.pack()
canvas.create_image(110,40, anchor=NW, image=image)

btnCheckReview = tk.Button(wf,text = "Review")
btnCheckReview.place(x=250, y=200, width=100)

btnSku = tk.Button(wf,text = "Inventory")
btnSku.place(x=250, y=250, width=100)

# frame = tk.Frame(wf, width = 380, height = 300, relief = tk.SUNKEN, borderwidth = 3)
# frame.place(x=5,y=40)
# lblFileText = tk.Text(frame, width = 50, state=tk.DISABLED)
# scroll_y = tk.Scrollbar(frame, command = lblFileText.yview, orient = tk.VERTICAL)
# lblFileText.configure(yscrollcommand = scroll_y.set)
# scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
# lblFileText.pack(side=tk.LEFT, fill=tk.BOTH)
# btnXuLy = tk.Button(wf,text = "Xử lý", command=XuLy)
# btnXuLy.place(x=450, y=5)
# frame2 = tk.Frame(wf, width = 380, height = 300, relief = tk.SUNKEN, borderwidth = 3)
# frame2.place(x=450,y=40)
# lblXuLy = tk.Text(frame2, width = 50, state=tk.DISABLED)
# scroll_y = tk.Scrollbar(frame2, command = lblXuLy.yview, orient = tk.VERTICAL)
# lblXuLy.configure(yscrollcommand = scroll_y.set)
# scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
# lblXuLy.pack(side=tk.LEFT, fill=tk.BOTH)
# lblCount = tk.Label(wf,text="Số lượng SV: 0",relief = tk.SUNKEN, width = 25)
# lblCount.place(x=700, y=470)
wf.mainloop()