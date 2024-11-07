import tkinter as tk
import sqlite3
from tkinter import ttk
from hashlib import md5

class GUI:
    #first group is login

    def loginAuthentication(): #TODO: needs manager case
        username = GUI.ent_username.get()
        username_tuple = (username,)
        password = GUI.ent_password.get()
        password_hash = md5(password.encode())
        password_hash_tuple = (password_hash,)

        res = cur.execute("SELECT Username FROM Accounts WHERE Username = ?", username_tuple )
        correct_username = res.fetchone()

        if username_tuple == correct_username:
            res = cur.execute("SELECT PasswordHash FROM Accounts WHERE Username = ?", username_tuple)
            correct_password_hash = res.fetchone()
            if password_hash_tuple == correct_password_hash:
                GUI.closeLogin()
                GUI.openDefaultScreen()
            else:
                print("Incorrect Password")
        else:
            print("Incorrect Username")

    def signupAuthentication(): #needs manager case
        username = GUI.ent_username.get()
        username_tuple = (username,)
        password = GUI.ent_password.get()
        password_hash = md5(password.encode()).hexdigest()
        email = GUI.ent_email.get()
        email_tuple = (email,)

        if username == "" or email == "" or password == "": #empty fields check
            print("One or more fields is empty")
        else:
            res = cur.execute("SELECT Username FROM Accounts WHERE Username = ?", username_tuple)
            taken_username = res.fetchone()

            if username_tuple == taken_username: #valid username check
                print("This username is already taken")
            else:
                res = cur.execute("SELECT Email FROM Accounts WHERE Email = ?", email_tuple)
                taken_email = res.fetchone()

                if email_tuple == taken_email: #valid email check (duplicates only)
                    print("This email is already taken")
                else:
                    GUI.createAccount(username, email, password_hash)
                    GUI.closeSignup()

    def openLogin(): #opens login gui
        GUI.lbl_login.pack(side='top')
        GUI.ent_username.pack()
        GUI.ent_username.insert(0, "Username")
        GUI.ent_password.pack()
        GUI.ent_password.insert(0, "Password")
        GUI.btn_login.pack(side='right')
        GUI.btn_signup_navigate.pack(side='left')

    username_save = "" #used for saving user input when typing into log in before switching to sign up
    password_save = ""

    def closeLogin(): #closes gui and saves input to restore if necessary
        GUI.lbl_login.pack_forget()
        GUI.username_save = GUI.ent_username.get()
        GUI.ent_username.pack_forget()
        GUI.password_save = GUI.ent_password.get()
        GUI.ent_password.pack_forget()
        GUI.btn_login.pack_forget()
        GUI.btn_signup_navigate.pack_forget()

    def openSignup():
        GUI.closeLogin()
        GUI.lbl_login.pack(side='top')
        GUI.ent_username.pack()

        if GUI.username_save != "": #save case for user (currently prints twice)
            GUI.ent_username.insert(0, GUI.username_save)
        else:
            GUI.ent_username.insert(0, "Username")
        GUI.ent_password.pack()
        if GUI.password_save != "": #save case for user (currently prints twice)
            GUI.ent_password.insert(0, GUI.password_save)
        else:
            GUI.ent_password.insert(0, "Password")
        
        GUI.ent_email.pack()
        GUI.ent_email.insert(0, "Email")
        GUI.btn_signup.pack(side='bottom')

    def closeSignup(): #closes signup gui
        GUI.lbl_login.pack_forget()
        GUI.ent_username.pack_forget()
        GUI.ent_email.pack_forget()
        GUI.ent_password.pack_forget()
        GUI.btn_signup.pack_forget()
        GUI.showProfileCreate()

    def createAccount(username, email, password_hash): #add manager case
        account_info = (username, email, password_hash)
        create_cur = con.cursor()
        create_cur.execute("INSERT INTO Accounts (Username, Email, PasswordHash) VALUES(?, ?, ?)", account_info )
        con.commit()

    def createOrg():
        pass

    def searchOrgs():
        table = ttk.Treeview(root, columns = ("Org Name"), show = "headings")
        table.heading("Org Name", text = "Name")
        for row in cur.execute("SELECT Name FROM Orgs WHERE LookingForApplicants = 1"):
            table.insert("", tk.END, values=row)
        table.pack(fill="both", expand=True)
   
    def openDefaultScreen(): #may want manager case
        GUI.btn_search.pack()

    #creates and populates a "label"
    #a label cannot be changed
    lbl_login = tk.Label(text="Please Log In Below",
        foreground = "black", #shorthand is fg
        background = "thistle", #shorthand is bg
        width = 50, #remember, these are "text units" not pixels
        height = 7 
        )

    lbl_is_manager = tk.Label(text = "Our records indicate you are a manager",
        fg = "black",
        bg = "thistle",
        width = 50,
        height = 7)

    lbl_ask_manager = tk.Label(text = "If you would like to create a manager account, press M",
        fg = "black",
        bg = "thistle",
        width = 50,
        height = 7)

    lbl_make_manager = tk.Label(text = "You will be making a manager account",
        fg = "black",
        bg = "thistle",
        width = 50,
        height = 7)

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

    btn_login = tk.Button(text = "Log In", #add authentication
        fg = "black",
        bg = "thistle",
        width = 5,
        height = 1,
        command = loginAuthentication)
    
    btn_signup_navigate = tk.Button(text = "Sign Up", #leads to signup screen
        fg = "black",
        bg = "thistle",
        width = 5,
        height = 1,
        command = openSignup)

    btn_signup = tk.Button(text = "Sign Up", #add into db, pack ent_email, forget login
        fg = "black",
        bg = "thistle",
        width = 5,
        height = 1,
        command = signupAuthentication)

    btn_search = tk.Button(text = "Search",
        fg = "black",
        bg = "thistle",
        width = 5,
        height = 1,
        command = searchOrgs)

    #create profile

    def showProfileCreate():
        #TODO: needs label
        GUI.ent_first_name.pack()
        GUI.ent_first_name.insert(0, "First Name")
        GUI.ent_last_name.pack()
        GUI.ent_last_name.insert(0, "Last Name")
        GUI.ent_suffix.pack()
        GUI.ent_suffix.insert(0, "Suffix (Erase if N/A)")
        GUI.ent_department.pack()
        GUI.ent_department.insert(0, "Department")
        GUI.ent_job_title.pack()
        GUI.ent_job_title.insert(0, "Job Title")
        GUI.ent_years_of_experience.pack()
        GUI.ent_years_of_experience.insert(0, "Years of Experience")
        GUI.ent_bachelors_from.pack()
        GUI.ent_bachelors_from.insert(0, "Bachelors From (Erase if N/A)")
        #TODO: needs button, and that button needs createProfile as command

    def createProfile(): 
        #TODO: write to various tables
        GUI.openDefaultScreen()
        pass

    lbl_create_profile = tk.Label(text="Create Profile by filling out the fields below")

    lbl_hiree_id = tk.Label(text = "HireeID is: ") #TODO: needs database connection

    ent_first_name = tk.Entry(fg = "black",
        bg = "white",
        width = 30)
    
    ent_last_name = tk.Entry(fg = "black",
        bg = "white",
        width = 30)
    
    ent_suffix = tk.Entry(fg = "black",
        bg = "white",
        width = 30)

    ent_department = tk.Entry(fg = "black",
        bg = "white",
        width = 30)

    ent_job_title = tk.Entry(fg = "black",
        bg = "white",
        width = 30)
    
    ent_years_of_experience = tk.Entry(fg = "black",
        bg = "white",
        width = 30)
    
    ent_bachelors_from = tk.Entry(fg = "black",
        bg = "white",
        width = 30)

#create org

ent_org_name = tk.Entry(fg = "black",
        bg = "white",
        width = 30)

ent_industry = tk.Entry(fg = "black",
        bg = "white",
        width = 30)

ent_looking_for_applicants = tk.Entry(fg = "black",
        bg = "white",
        width = 30)

#creates our initial login (main)

root = tk.Tk() #creates window
root.title("CRUD Corp")
root.minsize(500,500)
con = sqlite3.connect("CRUD_Corp_Copy.db") #connects to db
cur = con.cursor() #creates our cursor
#example SELECT
# for row in cur.execute("SELECT PasswordHash FROM Accounts"):
#     print(row)
GUI.openLogin()
root.mainloop() #prevents actions until window closed





