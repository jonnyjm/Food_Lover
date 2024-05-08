from pymongo import MongoClient
from tkinter import filedialog
from PIL import Image, ImageTk
import customtkinter

# Connects the db to the app
client = MongoClient("mongodb+srv://foodlover:CDOG2CI3GApYWkJv@foodlover.xagchl4.mongodb.net/")
db = client['users']

# cleans screen and loads new window once prompted
def newwin(): 
    for widget in root.winfo_children():
        widget.destroy()


#main screen where users can sign up or register
def mainscreen(): 
    newwin()
    fl_logo = ImageTk.PhotoImage(Image.open("Images/food_lover.ico").resize((100,100), Image.Resampling.LANCZOS))
    customtkinter.CTkLabel(root, image=fl_logo, text="", bg_color="white").place(relx=0.47, rely= 0.32)
    customtkinter.CTkLabel(root, text=" Welcome to Food Lover", compound="left",font=("Futura", 20, "bold"),justify="center", text_color="black", bg_color="white").place(relx=0.40, rely= 0.5)
    register_btn = customtkinter.CTkButton(root, text="Register", command= register, fg_color="black", text_color="white", hover_color="grey", font=("Futura",15), border_color='white')
    register_btn.place(anchor='center', relx=0.52, rely=0.66)

    login_btn = customtkinter.CTkButton(root, command= login,text="Login", fg_color="black", text_color="white", hover_color="grey", font=("Futura",15), corner_radius=10)
    login_btn.place(anchor='center', relx=0.52, rely=0.6)

    customtkinter.CTkLabel(root, text="Copyright: Team F", font=("Futura", 10, "bold"), text_color="black", bg_color="white").place(relx= .48, rely=0.95)



#login window
def login(): 
    newwin()
    btn = customtkinter.CTkImage(Image.open("Images/arrow.png"),size=(26, 26))
    register_btn = customtkinter.CTkButton(master=root, image=btn, command=mainscreen, text="", fg_color="white", hover=False)
    register_btn.place(relx=0, rely=0.01)

    customtkinter.CTkLabel(root, text=" Welcome back", compound="left",font=("Futura", 25, "bold"), text_color="black", bg_color="white").place(relx=0.43, rely= 0.3)

    email_entry = customtkinter.CTkEntry(root, placeholder_text="Email", width=250, placeholder_text_color="grey", text_color="black", fg_color="white")
    email_entry.place(relx=0.4, rely=0.4)

    pw_entry = customtkinter.CTkEntry(root, placeholder_text="Password", show="*", width=250, placeholder_text_color="grey", text_color="black", fg_color="white")
    pw_entry.place(relx=0.4, rely=0.46)
    error_label = customtkinter.CTkLabel(root, text="", compound="left",font=("Futura", 15, "bold"), text_color="#BB2100", bg_color="white")
    customtkinter.CTkButton(root, command= lambda:login_check(email_entry.get(), pw_entry.get(), error_label), text="Enter", fg_color='black', text_color="white").place(rely=0.52, relx=0.45)
    

def login_check(email, pw, error_label):

    error_label.configure(text="")
    if email == "" or pw == "":
        error_label.configure(text="Please enter a valid email and password")
        error_label.place(relx=0.38, rely=0.6)
        return
    
    user_data = db['login_data']
    user = user_data.find_one({"email": email})

    if user:
        if user["password"] == pw:
            print(user)
            return user

        else:
            error_label.configure(text="The password does not match the email entered")
            error_label.place(relx=0.38, rely=0.6)
        
    else:
        error_label.configure(text="Email not found")
        error_label.place(relx=0.47, rely=0.6)




def register():
    newwin()
    btn = customtkinter.CTkImage(Image.open("Images/arrow.png"),size=(26, 26))
    register_btn = customtkinter.CTkButton(master=root, image=btn, command=mainscreen, text="", fg_color="white", hover=False)
    register_btn.place(relx=0, rely=0.01)
    customtkinter.CTkLabel(root, text="Hello new user !!!", compound="left",font=("Futura", 25, "bold"), text_color="black", bg_color="white").place(relx=0.40, rely= 0.32)

    name_entry = customtkinter.CTkEntry(root, placeholder_text="Name", width=250, placeholder_text_color="grey", text_color="black", fg_color="white")
    name_entry.place(relx=0.4, rely=0.4)

    email_entry = customtkinter.CTkEntry(root, placeholder_text="Email", width=250, placeholder_text_color="grey", text_color="black", fg_color="white")
    email_entry.place(relx=0.4, rely=0.45)

    password_entry = customtkinter.CTkEntry(root, placeholder_text="Password", width=250, placeholder_text_color="grey", text_color="black", fg_color="white")
    password_entry.place(relx=0.4, rely=0.5)

    customtkinter.CTkButton(root, text="Enter", fg_color='black', text_color="white").place(relx=0.45, rely=0.55)


    




# attributes of app
root = customtkinter.CTk()
root.geometry("1080x720")
root.title("Food Lover")
root.minsize(1080,720)
root.iconphoto(False,ImageTk.PhotoImage(Image.open("Images/food_lover.ico")))
root.config(bg="white")

mainscreen()

root.mainloop()
