import tkinter as tk

#creates and populates a "label"
#a label cannot be changed
loginPrompt = tk.Label(text="Please Log In Below",
    foreground = "black", #shorthand is fg
    background = "thistle", #shorthand is bg
    width = 50, #remember, these are "text units" not pixels
    height = 7 
    )
usernameLabel = tk.Label(text="Username",
    foreground = "black", #shorthand is fg
    background = "thistle", #shorthand is bg
    width = 25, #remember, these are "text units" not pixels
    height = 7 
    )
passwordLabel = tk.Label(text="Password",
    foreground = "black", #shorthand is fg
    background = "thistle", #shorthand is bg
    width = 25, #remember, these are "text units" not pixels
    height = 7 
    )
#entries let Users type
usernameField = tk.Entry(fg = "black",
    bg = "white",
    width = 30)
passwordField = tk.Entry(fg = "black",
    bg = "white",
    width = 30)
emailField = tk.Entry(fg = "black",
    bg = "white",
    width = 30)
#actually "packs" the label into the window, otherwise it does nothing

loginButton = tk.Button(text= "Log In", #add authentication
    fg = "black",
    bg = "thistle",
    width = 5,
    height = 1)
signupButton = tk.Button(text= "Sign Up", #add into db, pack emailField
    fg = "black",
    bg = "thistle",
    width = 5,
    height = 1)