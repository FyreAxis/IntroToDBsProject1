import tkinter as tk
import sqlite3
from tkinter import ttk
from hashlib import md5

class GUI:
    #first group is login
    
    username_save = "" #used for saving user input when typing into log in before switching to sign up
    password_save = ""
    is_hired = False
    is_manager = False

    freshHireeID = 0 #used for making new accs
    freshOrgID = 0

    def getHireeID(username) -> int:
        username_tuple = (username,)
        cur = con.cursor()
        cur.execute("SELECT HireeID FROM Accounts WHERE Username = ?", username_tuple)
        id = cur.fetchone()
        return id[0]

    def openLogin(): #opens login gui
        GUI.lbl_login.pack(side='top')
        GUI.ent_username.pack()
        GUI.ent_username.insert(0, "Username")
        GUI.ent_password.pack()
        GUI.ent_password.insert(0, "Password")
        GUI.btn_login.pack(side='bottom')
        GUI.btn_signup_navigate.pack(side='right')
        GUI.btn_org_navigate.pack(side='left')

    def loginAuthentication():
        username = GUI.ent_username.get()
        username_tuple = (username,)
        password = GUI.ent_password.get()
        password_hash = md5(password.encode()).hexdigest()

        res = cur.execute("SELECT Username FROM Accounts WHERE Username = ?", username_tuple )
        correct_username = res.fetchone()

        if username_tuple == correct_username:
            res = cur.execute("SELECT PasswordHash FROM Accounts WHERE Username = ?", username_tuple)
            password_hash_object_grab = res.fetchone()
            correct_password_hash = password_hash_object_grab[0]
            if password_hash == correct_password_hash:
                GUI.closeLogin()
                GUI.openDefaultScreen()
            else:
                alert = tk.Tk()

                lbl_empty_fields_alert = tk.Label(alert, text = "This password is incorrect",
                fg = "black",
                bg = "thistle",
                width = 50,
                height = 7)

                lbl_empty_fields_alert.pack()

                alert.mainloop()
        else:
            alert = tk.Tk()

            lbl_empty_fields_alert = tk.Label(alert, text = "This username is incorrect",
            fg = "black",
            bg = "thistle",
            width = 50,
            height = 7)

            lbl_empty_fields_alert.pack()

            alert.mainloop()

    def closeLogin(): #closes gui and saves input to restore if necessary
        GUI.lbl_login.pack_forget()
        GUI.username_save = GUI.ent_username.get()
        GUI.ent_username.pack_forget()
        GUI.password_save = GUI.ent_password.get()
        GUI.ent_password.pack_forget()
        GUI.btn_login.pack_forget()
        GUI.btn_signup_navigate.pack_forget()
        GUI.btn_org_navigate.pack_forget()

#signup

    def openSignup():
        GUI.closeLogin()
        GUI.lbl_login.pack(side='top')
        GUI.ent_username.pack()

        GUI.ent_password.pack()

        GUI.ent_email.pack()
        GUI.ent_email.insert(0, "Email")
        GUI.btn_signup.pack(side='bottom')

    def signupAuthentication():
        username = GUI.ent_username.get()
        username_tuple = (username,) #tuples are used for database comparisons bc that's what the fetch returns
        password = GUI.ent_password.get()
        password_hash = md5(password.encode()).hexdigest() #hashes password
        email = GUI.ent_email.get()
        email_tuple = (email,)

        if username == "" or email == "" or password == "": #empty fields check
            alert = tk.Tk()

            lbl_empty_fields_alert = tk.Label(alert, text = "One or more fields are empty",
            fg = "black",
            bg = "thistle",
            width = 50,
            height = 7)

            lbl_empty_fields_alert.pack()

            alert.mainloop()
        else:
            res = cur.execute("SELECT Username FROM Accounts WHERE Username = ?", username_tuple)
            taken_username = res.fetchone()

            if username_tuple == taken_username: #valid username check
                alert = tk.Tk()

                lbl_empty_fields_alert = tk.Label(alert, text = "This username is already taken",
                fg = "black",
                bg = "thistle",
                width = 50,
                height = 7)

                lbl_empty_fields_alert.pack()

                alert.mainloop()

            else:
                res = cur.execute("SELECT Email FROM Accounts WHERE Email = ?", email_tuple)
                taken_email = res.fetchone()

                if email_tuple == taken_email: #valid email check (duplicates only)
                    alert = tk.Tk()

                    lbl_empty_fields_alert = tk.Label(alert, text = "This email is already taken",
                    fg = "black",
                    bg = "thistle",
                    width = 50,
                    height = 7)

                    lbl_empty_fields_alert.pack()

                    alert.mainloop()

                else:
                    GUI.createAccount(username, email, password_hash)
                    GUI.closeSignup()

    def closeSignup(): #closes signup gui
        GUI.lbl_login.pack_forget()
        GUI.username_save = GUI.ent_username.get()
        GUI.ent_username.pack_forget()
        GUI.ent_email.pack_forget()
        GUI.ent_password.pack_forget()
        GUI.btn_signup.pack_forget()
        GUI.openProfileCreate()

#acc creation

    def getFreshHireeID() -> int: #would not work with concurrent users
        cur = con.cursor()
        cur.execute("SELECT MAX(HireeID) FROM Accounts")
        max = cur.fetchone()
        GUI.freshHireeID = max[0] + 1
        return max[0] + 1
    
    def createAccount(username, email, password_hash): #add manager case
        hiree_id_number = GUI.getFreshHireeID()
        account_info = (hiree_id_number, username, email, password_hash)
        account_cur = con.cursor()
        account_cur.execute("INSERT INTO Accounts (HireeID, Username, Email, PasswordHash) VALUES(?, ?, ?, ?)", account_info )
        con.commit()

#profile creation

    def openProfileCreate():
        GUI.lbl_create_profile.pack()
        hiree_id.set("HireeID: {}".format(GUI.freshHireeID))
        lbl_hiree_id.pack()
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
        GUI.ent_are_you_hired.pack()
        GUI.ent_are_you_hired.insert(0, "If hired, put OrgID. (Erase if N/A)")
        GUI.lbl_are_you_hiring_manager.pack()
        GUI.ent_are_you_hiring_manager.pack()
        GUI.btn_create_profile.pack()

    def createProfileAuthentication(): #TODO: send managers to a menu to make sure they have an org
        first_name = GUI.ent_first_name.get()
        last_name = GUI.ent_last_name.get()
        suffix = GUI.ent_suffix.get()
        department = GUI.ent_department.get()
        job_title = GUI.ent_job_title.get()
        years_of_experience = GUI.ent_years_of_experience.get()
        bachelors_from = GUI.ent_bachelors_from.get()
        are_you_hired = GUI.ent_are_you_hired.get()
        are_you_hiring_manager = GUI.ent_are_you_hiring_manager.get()

        try:
            years_of_experience = int(years_of_experience)
        except:
            alert = tk.Tk()

            lbl_empty_fields_alert = tk.Label(alert, text = "Please input an integer",
            fg = "black",
            bg = "thistle",
            width = 50,
            height = 7)

            lbl_empty_fields_alert.pack()

            alert.mainloop()

        if first_name == "" or last_name == "" or department == "" or job_title == "" or "" or years_of_experience == "":
            alert = tk.Tk()

            lbl_empty_fields_alert = tk.Label(alert, text = "One or more fields are empty",
            fg = "black",
            bg = "thistle",
            width = 50,
            height = 7)

            lbl_empty_fields_alert.pack()

            alert.mainloop()
        else: 
            GUI.createProfile(first_name, last_name, suffix, department, job_title, years_of_experience, bachelors_from, are_you_hired, are_you_hiring_manager)

    def createProfile(first_name, last_name, suffix, department, job_title, years_of_experience, bachelors_from, are_you_hired, are_you_hiring_manager):
        hiree_id_number = GUI.freshHireeID #already assigned during acc creation
        info_info = (hiree_id_number, first_name, last_name, suffix)
        data_info = (hiree_id_number, department, job_title, years_of_experience, bachelors_from)
        hired_info = (hiree_id_number, are_you_hired, are_you_hiring_manager)
        profile_cur = con.cursor()
        profile_cur.execute("INSERT INTO Info (HireeID, First_Name, Last_Name, Suffix) VALUES (?, ?, ?, ?)", info_info)
        profile_cur.execute("INSERT INTO Data (HireeID, Department, JobTitle, YearsOfExperience, BachelorsFrom) VALUES (?, ?, ?, ?, ?)", data_info)
        if hired_info[1] != "": #if hired
            profile_cur.execute("INSERT INTO Hired (HireeID, OrgID, HiringManager) VALUES (?, ?, ?)", hired_info)
            GUI.is_hired = True
        con.commit()
        GUI.closeProfileCreate()

    def closeProfileCreate():
        GUI.lbl_create_profile.pack_forget()
        lbl_hiree_id.pack_forget()
        GUI.ent_first_name.pack_forget()
        GUI.ent_last_name.pack_forget()
        GUI.ent_suffix.pack_forget()
        GUI.ent_department.pack_forget()
        GUI.ent_job_title.pack_forget()
        GUI.ent_years_of_experience.pack_forget()
        GUI.ent_bachelors_from.pack_forget()
        GUI.ent_are_you_hired.pack_forget()
        GUI.lbl_are_you_hiring_manager.pack_forget()
        GUI.ent_are_you_hiring_manager.pack_forget()
        GUI.btn_create_profile.pack_forget()
        GUI.openDefaultScreen()

#org creation

    def getFreshOrgID() -> int: #would not work with concurrent users
        cur = con.cursor()
        cur.execute("SELECT MAX(OrgID) FROM Orgs")
        max = cur.fetchone()
        GUI.freshOrgID = max[0] + 1
        return max[0] + 1

    def openOrgCreate():
        GUI.closeLogin()
        GUI.btn_org_navigate.pack_forget() #finish closing prev window
        GUI.lbl_create_org.pack()
        org_id.set("OrgID: {}".format(GUI.getFreshOrgID()))
        lbl_org_id.pack()
        GUI.ent_org_name.pack()
        GUI.ent_org_name.insert(0, "Org Name")
        GUI.ent_industry.pack()
        GUI.ent_industry.insert(0, "Industry")
        GUI.lbl_org_create_looking_for_applicants.pack()
        GUI.ent_looking_for_applicants.pack()
        GUI.ent_looking_for_applicants.insert(0, "Looking for Applicants?")
        GUI.btn_create_org.pack()

    def closeOrgCreate():
        GUI.lbl_create_org.pack_forget()
        lbl_org_id.pack_forget()
        GUI.ent_org_name.pack_forget()
        GUI.ent_industry.pack_forget()
        GUI.lbl_org_create_looking_for_applicants.pack_forget()
        GUI.ent_looking_for_applicants.pack_forget()
        GUI.btn_create_org.pack_forget()

    def createOrgAuthentication():
        org_name = GUI.ent_org_name.get()
        industry = GUI.ent_industry.get()
        looking_for_applicants = GUI.ent_looking_for_applicants.get()

        try:
            looking_for_applicants = int(looking_for_applicants)
        except:
            alert = tk.Tk()

            lbl_empty_fields_alert = tk.Label(alert, text = "Please input an integer",
            fg = "black",
            bg = "thistle",
            width = 50,
            height = 7)

            lbl_empty_fields_alert.pack()

            alert.mainloop()

        if org_name == "" or industry == "" or looking_for_applicants == "":
            alert = tk.Tk()

            lbl_empty_fields_alert = tk.Label(alert, text = "One or more fields are empty",
            fg = "black",
            bg = "thistle",
            width = 50,
            height = 7)

            lbl_empty_fields_alert.pack()

            alert.mainloop()
        else:
            GUI.createOrg(org_name, industry, looking_for_applicants)

    def createOrg(org_name, industry, looking_for_applicants):
        org_info = (GUI.getFreshOrgID(), org_name, industry, looking_for_applicants)
        org_cur = con.cursor()
        org_cur.execute("INSERT INTO Orgs (OrgID, Name, Industry, LookingForApplicants) VALUES(?, ?, ?, ?)", org_info)
        con.commit()
        GUI.closeOrgCreate()
        GUI.ent_username.delete(0, tk.END)
        GUI.ent_password.delete(0, tk.END)
        GUI.openLogin()

#main GUI

    def searchOrgs():
        table_cur = con.cursor()
        table = ttk.Treeview(root, columns = ("Org Name",), show = "headings")
        for row in table_cur.execute("SELECT Name FROM Orgs WHERE LookingForApplicants = 1"):
            table.insert("", tk.END, values = row)
        table.heading("Org Name", text = "Name")
        table.pack(fill = "both", expand = True)

    def findHirees():
        columns = ("First Name", "Last Name", "Email", "Department", "Job Title", "Years of Experience", "Bachelors From")
        table_cur = con.cursor()
        table = ttk.Treeview(root, columns = columns, show = "headings")
        for row in table_cur.execute("SELECT i.First_Name, i.Last_Name, a.email, d.Department, d.JobTitle, d.YearsOfExperience, d.BachelorsFrom FROM Info AS i JOIN Accounts as a ON i.HireeID = a.HireeID JOIN Data as d ON a.HireeID = d.HireeID"):
            table.insert("", tk.END, values = row)
        table.heading("First Name", text = "First Name")
        table.heading("Last Name", text="Last Name")
        table.heading("Email", text="Email")
        table.heading("Department", text = "Department")
        table.heading("Job Title", text = "Job Title")
        table.heading("Years of Experience", text= "Years of Experience")
        table.heading("Bachelors From", text = "Bachelors From")
        table.pack(fill = "both", expand = True)
   
    def openDefaultScreen():
        username_tuple = (GUI.username_save,)
        cur.execute("SELECT HiringManager FROM Hired AS h JOIN Accounts AS a ON h.HireeID = a.HireeID WHERE a.Username = ?", username_tuple)
        res = cur.fetchone()
        if res[0] == 1:
            GUI.is_manager = True
        else:
            GUI.is_manager = False
    
        GUI.btn_open_profile.pack(side = 'bottom')
        if GUI.is_manager == True:
            GUI.btn_find_hirees.pack()
        else:    
            GUI.btn_search.pack(side = 'bottom')

    def openProfile():
        cur = con.cursor()
        hiree_id_number = GUI.getHireeID(GUI.username_save)
        hiree_id_tuple = (hiree_id_number,)
        cur.execute("SELECT a.Email, i.First_Name, i.Last_Name, i.Suffix, d.Department, d.JobTitle, d.YearsOfExperience, d.BachelorsFrom FROM Accounts AS a JOIN Info as i ON a.HireeID = i.HireeID JOIN Data as d ON i.HireeID = d.HireeID WHERE a.HireeID = ?;", hiree_id_tuple)
        giant_tuple = cur.fetchone()
        name.set("Name: {} {} {}".format(giant_tuple[1], giant_tuple[2], giant_tuple[3]))
        hiree_id.set("HireeID: {}".format(hiree_id_number))
        username.set("Username: {}".format(GUI.username_save))
        email.set("Email: {}".format(giant_tuple[0]))
        department.set("Department: {}".format(giant_tuple[4]))
        job_title.set("Job Title: {}".format(giant_tuple[5]))
        years_of_experience.set("Years of Experience: {}".format(giant_tuple[6]))
        bachelors_from.set("Bachelors From: {}".format(giant_tuple[7]))
        
        GUI.lbl_account_info.pack() #categorizes as acc info
        lbl_name.pack()
        lbl_hiree_id.pack()
        lbl_username.pack()
        lbl_email.pack()
        GUI.lbl_info_info.pack()
        lbl_department.pack()
        lbl_job_title.pack()
        if giant_tuple[6] != "": #hides demotivating fields
            lbl_years_of_experience.pack()
        if giant_tuple[7] != "":
            lbl_bachelors_from.pack()
        if GUI.is_hired:
            cur.execute("SELECT h.OrgID, h.HiringManager, o.Name, o.Industry, o.LookingForApplicants FROM Hired AS h JOIN Orgs AS o ON h.OrgID = o.OrgID WHERE h.HireeID = ?", hiree_id_tuple)
            hired_tuple = cur.fetchone()
            if hired_tuple[1] == 1:
                GUI.lbl_is_manager.pack()
            GUI.lbl_org_info.pack()
            org_id.set("Org ID: {}".format(hired_tuple[0]))
            org_name.set("Org Name: {}".format(hired_tuple[2]))
            industry.set("Industry: {}".format(hired_tuple[3]))

            if hired_tuple[4] == 1:
                hiring = True
            else:
                hiring = False
            looking_for_applicants.set("Looking for Applicants: {}".format(hiring))

            lbl_org_id.pack()
            lbl_org_name.pack()
            lbl_industry.pack()
            lbl_looking_for_applicants.pack()
            
        GUI.btn_close_profile.pack()
        GUI.ent_change_username.pack()
        GUI.ent_change_username.insert(0, "Change username: ")
        GUI.btn_change_username.pack()
        GUI.btn_delete_account.pack(side='bottom')
        if GUI.is_manager:
            GUI.btn_find_hirees.pack_forget()
        else:
            GUI.btn_search.pack_forget()
        GUI.btn_open_profile.pack_forget()

    def closeProfile():
        cur = con.cursor()
        hiree_id_number = GUI.getHireeID(GUI.username_save)
        hiree_id_tuple = (hiree_id_number,)
        cur.execute("SELECT a.Email, i.First_Name, i.Last_Name, i.Suffix, d.Department, d.JobTitle, d.YearsOfExperience, d.BachelorsFrom FROM Accounts AS a JOIN Info as i ON a.HireeID = i.HireeID JOIN Data as d ON i.HireeID = d.HireeID WHERE a.HireeID = ?;", hiree_id_tuple)
        giant_tuple = cur.fetchone()

        if giant_tuple[6] != "":
           lbl_years_of_experience.pack_forget()
        if giant_tuple[7] != "":
            lbl_bachelors_from.pack_forget()
        if GUI.is_hired:
            GUI.lbl_org_info.pack_forget()
            lbl_org_id.pack_forget()
            lbl_org_name.pack_forget()
            lbl_industry.pack_forget()
            lbl_looking_for_applicants.pack_forget()
        if GUI.is_manager:
            GUI.lbl_is_manager.pack_forget()

        GUI.lbl_account_info.pack_forget() #categorizes as acc info
        lbl_name.pack_forget()
        lbl_hiree_id.pack_forget()
        lbl_username.pack_forget()
        lbl_email.pack_forget()
        GUI.lbl_info_info.pack_forget()
        lbl_department.pack_forget()
        lbl_job_title.pack_forget()
        GUI.btn_close_profile.pack_forget()
        GUI.ent_change_username.pack_forget()
        GUI.btn_change_username.pack_forget()
        GUI.btn_delete_account.pack_forget()
        GUI.openDefaultScreen()

    def changeUsername():
        cur = con.cursor()
        hiree_id_number = GUI.getHireeID(GUI.username_save)
        new_username = GUI.ent_change_username.get()
        GUI.username_save = new_username #update username var in class
        tuple = (new_username, hiree_id_number,)
        cur.execute("UPDATE Accounts SET Username = ? WHERE Accounts.HireeID = ?;", tuple)
        con.commit()
        GUI.closeProfile() #updates profile to have new username
        GUI.openProfile()

    def deleteAccount():
        cur = con.cursor()
        hiree_id_number = GUI.getHireeID(GUI.username_save)
        hiree_id_tuple = (hiree_id_number,)
        GUI.closeProfile()
        cur.execute("DELETE FROM Accounts WHERE HireeID = ?", hiree_id_tuple)
        cur.execute("DELETE FROM Info WHERE HireeID = ?", hiree_id_tuple)
        cur.execute("DELETE FROM Data WHERE HireeID = ?", hiree_id_tuple)
        if GUI.is_hired: #if hired, delete from Hired
            cur.execute("DELETE FROM Hired WHERE HireeID = ?", hiree_id_tuple)
        con.commit()
        GUI.openLogin()

#login assets

    #creates and populates a "label"
    #a label cannot be changed
    lbl_login = tk.Label(text="Please Log In Below",
        foreground = "black", #shorthand is fg
        background = "thistle", #shorthand is bg
        width = 50, #remember, these are "text units" not pixels
        height = 7 
        )

    lbl_make_manager = tk.Label(text = "You will be making a manager account",
        fg = "black",
        bg = "thistle",
        width = 50,
        height = 7)
    
    btn_login = tk.Button(text = "Log In", #add authentication
        fg = "black",
        bg = "thistle",
        width = 10,
        height = 1,
        command = loginAuthentication)

    btn_signup_navigate = tk.Button(text = "Sign Up", #leads to signup screen
        fg = "black",
        bg = "thistle",
        width = 10,
        height = 1,
        command = openSignup)

#signup assets

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

    btn_signup = tk.Button(text = "Sign Up", #add into db, pack ent_email, forget login
        fg = "black",
        bg = "thistle",
        width = 10,
        height = 1,
        command = signupAuthentication)
    
    #create profile assets

    lbl_create_profile = tk.Label(text="Create Profile by filling out the fields below. If you are a hiring manager, please create an Org first.",
        fg = "black",
        bg = "thistle",
        width = 100,
        height = 3)

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

    ent_are_you_hired = tk.Entry(fg = "black",
        bg = "white",
        width = 30)

    lbl_are_you_hiring_manager = tk.Label(text = "Are you a hiring manager? (0 for No, 1 for Yes, Erase if N/A to last question)",
        fg = "black",
        bg = "thistle",
        width = 100,
        height = 3)

    ent_are_you_hiring_manager = tk.Entry(fg = "black",
        bg = "white",
        width = 30)

    btn_create_profile = tk.Button(text = "Create Profile", #add into db
        fg = "black",
        bg = "thistle",
        width = 20,
        height = 1,
        command = createProfileAuthentication)

#create org

    lbl_create_org = tk.Label(text="Create Org by filling out the fields below. You may create a Hiring Manager profile after",
        fg = "black",
        bg = "thistle",
        width = 100,
        height = 3)

    btn_org_navigate = tk.Button(text = "Make Org",
        fg = "black",
        bg = "thistle",
        width = 10,
        height = 1,
        command = openOrgCreate)

    btn_create_org = tk.Button(text = "Create Org",
        fg = "black",
        bg = "thistle",
        width = 10,
        height = 1,
        command = createOrgAuthentication)
    
    ent_org_name = tk.Entry(fg = "black",
        bg = "white",
        width = 30)

    ent_industry = tk.Entry(fg = "black",
        bg = "white",
        width = 30)

    lbl_org_create_looking_for_applicants = tk.Label(text = "Are you looking for applicants? (0 for No, 1 for Yes)",
        fg = "black",
        bg = "thistle",
        width = 100,
        height = 3)

    ent_looking_for_applicants = tk.Entry(fg = "black",
        bg = "white",
        width = 30)

#see profile

    #main GUI assets

    lbl_account_info = tk.Label(text="Account Information",
        fg = "black",
        bg = "thistle",
        width = 100,
        height = 3)

    lbl_info_info = tk.Label(text="Hiree Information",
        fg = "black",
        bg = "thistle",
        width = 100,
        height = 3)

    lbl_org_info = tk.Label(text="Org Information",
        fg = "black",
        bg = "thistle",
        width = 100,
        height = 3)

    lbl_is_manager = tk.Label(text = "Our records indicate you are a manager",
        fg = "black",
        bg = "thistle",
        width = 100,
        height = 7)

    btn_open_profile = tk.Button(text = "Open Profile",
        fg = "black",
        bg = "thistle",
        width = 10,
        height = 1,
        command = openProfile)

    btn_close_profile = tk.Button(text = "Close Profile",
        fg = "black",
        bg = "thistle",
        width = 10,
        height = 1,
        command = closeProfile)

    btn_search = tk.Button(text = "Search",
        fg = "black",
        bg = "thistle",
        width = 5,
        height = 1,
        command = searchOrgs)

    btn_change_username = tk.Button(text = "Change Username",
        fg = "black",
        bg = "thistle",
        width = 15,
        height = 1,
        command = changeUsername)

    ent_change_username = tk.Entry(fg = "black",
        bg = "white",
        width = 30)

    btn_delete_account = tk.Button(text = "Delete Account",
        fg = "black",
        bg = "thistle",
        width = 15,
        height = 1,
        command = deleteAccount)
    
    btn_find_hirees = tk.Button(text = "Find Hirees",
        fg = "black",
        bg = "thistle",
        width = 15,
        height = 1,
        command = findHirees) 

#creates our initial login (main)

root = tk.Tk() #creates window TODO: fix second window
root.title("CRUD Corp") #titles window
root.minsize(500,500) #sets window min size
con = sqlite3.connect("CRUD_Corp_Copy.db") #connects to db
cur = con.cursor() #creates our cursor

#main GUI assets continued (with StringVar())

name = tk.StringVar()
hiree_id = tk.StringVar()
username = tk.StringVar()
email = tk.StringVar()
department = tk.StringVar()
job_title = tk.StringVar()
years_of_experience = tk.StringVar()
bachelors_from = tk.StringVar()
org_id = tk.StringVar()
hiring_manager = tk.StringVar()
org_name = tk.StringVar()
industry = tk.StringVar()
looking_for_applicants = tk.StringVar()

lbl_name = tk.Label(textvariable = name,
    fg = "black",
    bg = "thistle",
    width = 100,
    height = 3) 

lbl_hiree_id = tk.Label(textvariable = hiree_id,
    fg = "black",
    bg = "thistle",
    width = 100,
    height = 3) 

lbl_username = tk.Label(textvariable = username,
    fg = "black",
    bg = "thistle",
    width = 100,
    height = 3) 

lbl_email = tk.Label(textvariable = email,
    fg = "black",
    bg = "thistle",
    width = 100,
    height = 3) 

lbl_department = tk.Label(textvariable = department,
    fg = "black",
    bg = "thistle",
    width = 100,
    height = 3) 

lbl_job_title = tk.Label(textvariable = job_title,
    fg = "black",
    bg = "thistle",
    width = 100,
    height = 3) 

lbl_years_of_experience = tk.Label(textvariable = years_of_experience,
    fg = "black",
    bg = "thistle",
    width = 100,
    height = 3) 

lbl_bachelors_from = tk.Label(textvariable = bachelors_from,
    fg = "black",
    bg = "thistle",
    width = 100,
    height = 3) 

lbl_org_id = tk.Label(textvariable = org_id,
    fg = "black",
    bg = "thistle",
    width = 100,
    height = 3)

lbl_org_name = tk.Label(textvariable = org_name,
    fg = "black",
    bg = "thistle",
    width = 100,
    height = 3) 

lbl_industry = tk.Label(textvariable = industry,
    fg = "black",
    bg = "thistle",
    width = 100,
    height = 3) 

lbl_looking_for_applicants = tk.Label(textvariable = looking_for_applicants,
    fg = "black",
    bg = "thistle",
    width = 100,
    height = 3) 

GUI.openLogin() #basically is the bootstrap

root.mainloop() #prevents actions until window closed





