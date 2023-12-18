from customtkinter import *
from PIL import Image
from pytube import YouTube
from tkinter import messagebox
import requests
import sys
import os

def get_image_path(filename):
    if hasattr(sys,"_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename
def atualizar_thumb():
    url = entry.get()

    try:
        yt = YouTube(url)
        thumb = yt.thumbnail_url

        img_vid2 = Image.open(requests.get(thumb, stream=True).raw)
        thumb_interface.configure(dark_image=img_vid2)
        titulo_vid = yt.title
        thumb_texto.configure(text=titulo_vid)

    except Exception as e:
        print("Erro", f"Ocorreu um erro ao atualizar a thumbnail: {str(e)}")
def download(): 
    link = entry.get()
    qualidade = options.get()
    atualizar_thumb()
    try:    
        yt = YouTube(link)
        if qualidade == "Máx. Qualidade":
            video = yt.streams.get_highest_resolution()
            video.download()
            messagebox.showinfo("Download Concluído", "O vídeo foi baixado com sucesso!")
        elif qualidade =="720p":
            video = yt.streams.get_by_resolution("720p")
            video.download()
            messagebox.showinfo("Download Concluído", "O vídeo foi baixado com sucesso!")
        elif qualidade =="360p":
            video = yt.streams.get_by_resolution("360p")
            video.download()
            messagebox.showinfo("Download Concluído", "O vídeo foi baixado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

app = CTk()
app.geometry("900x600") # Tamanho
app.title("Youtube Downloader") # Título
app.resizable(width=False, height=False)
set_appearance_mode("dark") # Tema

# Imagens
img_banner = Image.open(get_image_path("imagens/banner.png"))
img = Image.open(get_image_path("imagens/botao.png"))
img_vid = Image.open(get_image_path("imagens/thumb.png"))

# Adicione também a linha para o ícone do aplicativo
app_icon_path = get_image_path("imagens/app.ico")
app.iconbitmap(app_icon_path)

titulo_vid = ("O título do seu vídeo aparecerá aqui.")

# Interface
banner = CTkImage(dark_image=img_banner, size=(900,127)) # Abre a imagem do banner
CTkLabel(app, text=None, image=banner, anchor="n").pack()

entry = CTkEntry(app, placeholder_text="Insira uma URL...", # Entrada do usuário (url_link)
                 fg_color="white", 
                 width=291, height=44, 
                 text_color="black", 
                 corner_radius=8,                
                ) 
entry.place(relx=0.25, rely=0.35, anchor="center") 

options = CTkComboBox(app, values=["360p","720p","Máx. Qualidade"], # Caixa de opções
                      width=207,height=51, 
                      fg_color="white", 
                      text_color="black", corner_radius=15,button_color="#bfbfbf",
                      border_color="#bfbfbf",                                     
                      )
options.place(relx=0.20, rely=0.5, anchor="center")

btn = CTkButton(app, text="Download", # Botão de download
                fg_color="white", 
                image=CTkImage(dark_image=img),
                width=185,height=68, 
                text_color="black", 
                hover_color="#e04436",
                command=download
                )
btn.place(relx=0.19,rely=0.95, anchor="s")


# Thumbnail
thumb_interface = CTkImage(dark_image=img_vid, size=(416,230))  # Imagem da thumb do video
thumb_label = CTkLabel(app, text=None, image=thumb_interface, anchor="s")
thumb_label.place(relx=0.72, rely=0.53, anchor="center")  # Posicionamento da imagem

thumb_texto = CTkLabel(app, text=titulo_vid, font=("Arial",11), text_color="white") # Título do vídeo
thumb_texto.place(relx=0.72, rely=0.75, anchor="center")

app.mainloop()
