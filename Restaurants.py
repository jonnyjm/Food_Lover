from tkinter import filedialog
from PIL import Image, ImageTk
import customtkinter

root = customtkinter.CTk()
root.geometry("1080x720")
root.title("Food Lover")
root.minsize(1080,720)
root.maxsize(1080,720)
root.iconphoto(False,ImageTk.PhotoImage(Image.open("Images/food_lover.ico")))
root.config(bg="white")

btn = customtkinter.CTkButton(master=root, text="Order Food", bg_color="white", text_color="white", fg_color="grey", width= 540)
btn.grid(row=0, column=0, sticky=customtkinter.W)
btn_2 = customtkinter.CTkButton(master=root, text="Account", bg_color="white", text_color="white", fg_color="black", width= 540)
btn_2.grid(row=0, column=1)

restaurant1_img = ImageTk.PhotoImage(Image.open("Images/mcD.png").resize((200,200), Image.Resampling.LANCZOS))
restaurant1 = customtkinter.CTkLabel(root, image=restaurant1_img, text="", bg_color="white", justify="left").grid(row=1,column=0, pady=20)
customtkinter.CTkLabel(root, text="Mcdonald's: 2.4 miles away ORDER NOW", text_color= "black", bg_color="white").grid(row=1, column=1)

root.mainloop()
