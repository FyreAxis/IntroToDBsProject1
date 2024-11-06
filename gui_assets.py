import tkinter as tk
import gui_funcs

#creates and populates a "label"
#a label cannot be changed
lbl_login = tk.Label(text="Please Log In Below",
    foreground = "black", #shorthand is fg
    background = "thistle", #shorthand is bg
    width = 50, #remember, these are "text units" not pixels
    height = 7 
    )
#entries let Users type
ent_username = tk.Entry(fg = "black",
    bg = "white",
    width = 30)
ent_password = tk.Entry(fg = "black",
    bg = "white",
    width = 30)
ent_email = tk.Entry(fg = "black",
    bg = "white",
    width = 30)
#actually "packs" the label into the window, otherwise it does nothing

btn_login = tk.Button(text= "Log In", #add authentication
    fg = "black",
    bg = "thistle",
    width = 5,
    height = 1,
    command = gui_funcs.LoginSignup.loginAuthentication)

btn_signup_navigate = tk.Button(text= "Sign Up", #add into db, pack ent_email
    fg = "black",
    bg = "thistle",
    width = 5,
    height = 1,
    command = gui_funcs.LoginSignup.openSignup)

btn_signup = tk.Button(text= "Sign Up", #add into db, pack ent_email
    fg = "black",
    bg = "thistle",
    width = 5,
    height = 1,
    command = gui_funcs.LoginSignup.signupAuthentication)