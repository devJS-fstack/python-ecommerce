import tkinter as tk
from tkinter import *
from tkinter import filedialog, font
from PIL import Image, ImageTk
from googletrans import Translator as Translator_07_nvt


wf = tk.Tk()


def on_select(value, selected_option):
    selected_option.set(value)


def translate(txt, in_selected, out_selected):
    in_lang = in_selected.get()
    out_lang = out_selected.get()
    # result = translate_text_07_nvt(txt, in_lang, out_lang)
    # print(result)


def translate_text_07_nvt(text_07_nvt, input_lang_07_nvt, output_lang_07_nvt):
    translator_07_nvt = Translator_07_nvt()
    translated_07_nvt = translator_07_nvt.translate(
        "How are you", src="vi", dest="en")
    return translated_07_nvt.text


def complain_render(root):
    # wf = tk.Toplevel(root)
    wf.title("Complain")
    wf.geometry("800x600")
    wf.resizable(tk.FALSE, tk.FALSE)
    complaint_txt = Text(wf, width=60, height=15, borderwidth=3)
    complaint_txt.place(x=5, y=40)

    in_lang_options = ["vi", "en"]
    in_lang_selected_option = StringVar()
    in_lang_selected_option.set(in_lang_options[0])

    in_lang_option_menu = OptionMenu(
        wf, in_lang_selected_option, *in_lang_options, command=lambda value, s=in_lang_selected_option: on_select(value, s))
    in_lang_option_menu.place(x=610, y=40)

    out_lang_options = ["vi", "en"]
    out_lang_selected_option = StringVar()
    out_lang_selected_option.set(out_lang_options[0])

    out_lang_option_menu = OptionMenu(
        wf, out_lang_selected_option, *out_lang_options, command=lambda value, s=out_lang_selected_option: on_select(value, s))
    out_lang_option_menu.place(x=680, y=40)

    complaint__translate_txt = Text(wf, width=60, height=5, borderwidth=3)
    complaint__translate_txt.place(x=5, y=285)
    complaint__translate_txt.config(state="disabled")

    translate_radio = Button(
        wf, text="Translate", font=font.Font(size=11), command=lambda: translate(complaint_txt.get("1.0", "end-1c"), in_lang_selected_option, out_lang_selected_option))
    translate_radio.place(x=500, y=40, width=100)

    voice_btn = Button(wf, text="Voice", font=font.Font(size=11))
    voice_btn.place(x=500, y=75, width=100)

    upload_img_btn = Button(wf, text="Upload", font=font.Font(size=11))
    upload_img_btn.place(x=500, y=110, width=100)

    clear_btn = Button(wf, text="Clear", font=font.Font(size=11))
    clear_btn.place(x=280, y=380, width=100)

    submit_btn = Button(wf, text="Submit", font=font.Font(size=11))
    submit_btn.place(x=390, y=380, width=100)


# complain_render(1)
# wf.mainloop()


translate_text_07_nvt("how are you", "en", "vi")
