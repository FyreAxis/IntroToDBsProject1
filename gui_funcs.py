import tkinter as tk
import gui_assets

#user will either create account or log into existing acc
def bootstrap():
    root = tk.Tk() #creates window
    root.minsize(500,500)

    LoginSignup.openLogin()

    root.mainloop() #prevents actions until window closed

class LoginSignup:
    username_save = "" #used for saving user input when typing into log in before switching to sign up
    password_save = ""

    def openLogin(): #opens login gui
        gui_assets.lbl_login.pack(side='top')
        gui_assets.ent_username.pack()
        gui_assets.ent_username.insert(0, "Username")
        gui_assets.ent_password.pack()
        gui_assets.ent_password.insert(0, "Password")
        gui_assets.btn_login.pack(side='right')
        gui_assets.btn_signup_navigate.pack(side='left')
    def closeLogin(): #closes gui and saves input to restore if necessary
        gui_assets.lbl_login.pack_forget()
        LoginSignup.username_save = gui_assets.ent_username.get()
        gui_assets.ent_username.pack_forget()
        LoginSignup.password_save = gui_assets.ent_password.get()
        gui_assets.ent_password.pack_forget()
        gui_assets.btn_login.pack_forget()
        gui_assets.btn_signup_navigate.pack_forget()

    def loginAuthentication(): #sample, obvi not final
        username = gui_assets.ent_username.get()
        password = gui_assets.ent_password.get()
        if username == "CORRECT" and password == "CORRECT":
            print("Logged In")
            LoginSignup.closeLogin()
        else:
            print("Incorrect Input")

    def openSignup():
        LoginSignup.closeLogin()
        gui_assets.lbl_login.pack(side='top')
        gui_assets.ent_username.pack()

        if LoginSignup.username_save != "": #save case for user (currently prints twice)
            gui_assets.ent_username.insert(0, LoginSignup.username_save)
        else:
            gui_assets.ent_username.insert(0, "Username")
        gui_assets.ent_password.pack()
        if LoginSignup.password_save != "": #save case for user (currently prints twice)
            gui_assets.ent_password.insert(0, LoginSignup.password_save)
        else:
            gui_assets.ent_password.insert(0, "Password")
        
        gui_assets.ent_email.pack()
        gui_assets.ent_email.insert(0, "Email")
        gui_assets.btn_signup.pack(side='right')
        
    def closeSignup(): #closes signup gui
        gui_assets.lbl_login.pack_forget()
        gui_assets.ent_username.pack_forget()
        gui_assets.ent_email.pack_forget()
        gui_assets.ent_password.pack_forget()
        gui_assets.btn_signup.pack_forget()

    def signupAuthentication():
        username = gui_assets.ent_username.get()
        email = gui_assets.ent_email.get()
        password = gui_assets.ent_password.get()
        email = gui_assets.ent_email.get()
        if username == "CORRECT" and password == "CORRECT" and email == "CORRECT":
            print("Signed Up")
            LoginSignup.closeSignup()
        else:
            print("Incorrect Input")


