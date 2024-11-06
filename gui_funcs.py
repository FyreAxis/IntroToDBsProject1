import tkinter as tk
import gui_assets

#user will either create account or log into existing acc
def startLogin():
    gui_assets.loginPrompt.pack(side='top')
    gui_assets.usernameField.pack()
    gui_assets.passwordField.pack()
    gui_assets.loginButton.pack(side='right')
    gui_assets.signupButton.pack(side='left')

