import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image , ImageTk


#region commands

#region command show login page

def show_login_page():
    
    label_page1.grid_forget()
    button_login.grid_forget()
    button_registry.grid_forget()
    label_image.grid_forget()
    label_balance.grid_forget()

    label_login.grid(row=0,column=0, padx=250, pady=10, sticky='w')

    label_username_login_page.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    entry_username_login_page.grid(row=1,padx=100,pady=10)

    label_password_login_page.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    entry_password_login_page.grid(row=2, padx=100, pady= 10)

    button_enter.grid(row=3, column=0, padx=210,pady= 10, sticky='w')
    button_back_page2.grid(row=3, column=0, padx=280, pady=10, sticky='w')
    
#endregion

#region command enter    (not finished)

def enter():

    username = entry_username_login_page.get()
    password = entry_password_login_page.get()
    nationalcode = entry_nationalcode.get()

    with open('datafile.txt','r') as file :
        var = file.read()

        if username == nationalcode :

            if username in var and password in var :

                label_login.grid_forget()
                label_username_login_page.grid_forget()
                entry_username_login_page.grid_forget()
                label_password_login_page.grid_forget()
                entry_password_login_page.grid_forget()
                button_enter.grid_forget()
                button_back_page2.grid_forget()
                
                 

                label_balance.grid(row=0 , column=0 , padx = 250 , pady=30 , sticky='w')
                button_logout.grid(row=1 , column=0 , padx = 250 , pady=10 , sticky='w')
                # edame darad

        else:
            messagebox.showerror('Error:', 'Invalid username or password')

            label_login.grid(row=0, column=0, padx=250, pady=10)
            label_username_login_page.grid(row=1, column=0, padx=10, pady=10, sticky='w')
            entry_username_login_page.grid(row=1,padx=100,pady=10)
                
            label_password_login_page.grid(row=2, column=0, padx=10, pady=10, sticky='w')
            entry_password_login_page.grid(row=2, padx=100, pady= 10)

            button_enter.grid(row=3, column=0, padx=210, pady= 10, sticky='w')
            button_back_page2.grid(row=3, column=0, padx=280, pady=10, sticky='w')

#endregion

#region button back login page

def back():
    
    label_login.grid_forget()

    label_username_login_page.grid_forget()
    entry_username_login_page.grid_forget()

    label_password_login_page.grid_forget()
    entry_password_login_page.grid_forget()

    button_enter.grid_forget()
    button_back_page2.grid_forget()

    label_image.grid(row = 0, column = 0, padx=208, pady=10, sticky='w')
    label_page1.grid(row=1,column=0, padx=220, pady=0, sticky='w')

    button_login.grid(row = 2, column = 0, padx=200,pady=10, sticky='w')
    button_registry.grid(row = 2, column = 0, padx=280, pady=10, sticky='w')
       

#endregion

#region logout button
def logout():
    label_balance.grid_forget()
    button_logout.grid_forget()
    
    label_image.grid(row = 0, column = 0, padx=208, pady=10, sticky='w')
    label_page1.grid(row=1,column=0, padx=220, pady=0, sticky='w')

    button_login.grid(row = 2, column = 0, padx=200,pady=10, sticky='w')
    button_registry.grid(row = 2, column = 0, padx=280, pady=10, sticky='w')
#endregion

#region registry button

def registry():
    label_page1.grid_forget()
    button_login.grid_forget()
    button_registry.grid_forget()
    label_image.grid_forget()

    label_registry_page.grid(row=0, column=0, padx=250, pady= 10, sticky='w')

    label_name.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    entry_name.grid(row=1, padx=100, pady=10)

    label_family.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    entry_family.grid(row=2, padx=100, pady=10)

    label_email.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    entry_email.grid(row=3, padx=100, pady=10)

    label_nationalcode.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    entry_nationalcode.grid(row=4, padx=100, pady=10)

    label_age.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    entry_age.grid(row=5, padx=100, pady=10)

    label_password_registry.grid(row=6, column=0, padx=10, pady=10, sticky='w')
    entry_password_registry.grid(row=6, padx=100, pady=10)

    label_confirm_password.grid(row=7, column=0, padx=10, pady=10, sticky='w')
    entry_confirm_password.grid(row=7, padx=100, pady=10)

    button_submit.grid(row = 8, column = 0, padx=210, pady=10, sticky='w')  
    button_back_registry.grid(row = 8, column = 0, padx=280,pady=10, sticky='w') 

#endregion

#region submit button registry page

def submit():
        
        data_list = []

        name = entry_name.get()
        family = entry_family.get()
        age = entry_age.get()
        national_code = entry_nationalcode.get()
        email = entry_email.get()
        password = entry_password_registry.get()
        confirm_password = entry_confirm_password.get()

        if password == confirm_password :

            with open('datafile.txt', 'a') as file :
                user_info = {
                    'Name': name,
                    'Family': family,
                    'National code': national_code,
                    'Age': age,
                    'E-mail': email,
                    'Password':password
                 }
                data_list.append(user_info)
            
                file.write(str(data_list))
                file.write('\n')

                messagebox.showinfo('Result:', 'Registration was successfully.\nYour username is your National code')

            label_registry_page.grid_forget()
            label_name.grid_forget()
            entry_name.grid_forget()
            label_family.grid_forget()
            entry_family.grid_forget()
            label_email.grid_forget()
            entry_email.grid_forget()
            label_nationalcode.grid_forget()
            entry_nationalcode.grid_forget()
            label_age.grid_forget()
            entry_age.grid_forget()
            label_password_registry.grid_forget()
            entry_password_registry.grid_forget()
            label_confirm_password.grid_forget()
            entry_confirm_password.grid_forget()
            button_submit.grid_forget()
            button_back_registry.grid_forget()

            label_login.grid(row=0, column=0, padx=250)

            label_username_login_page.grid(row=1, column=0, padx=10, pady=10, sticky='w')
            entry_username_login_page.grid(row=1, padx=100, pady=10)

            label_password_login_page.grid(row=2, column=0, padx=10, pady=10, sticky='w')
            entry_password_login_page.grid(row=2, padx=100, pady= 10)

            button_enter.grid(row=3, column=0, padx=200,pady= 10, sticky='w')
            button_back_page2.grid(row=3, column=0, padx=300, pady=10, sticky='w')
            
        else:
            messagebox.showerror('Error!!', 'Please check your information')


#endregion

#region back button registy page

def back_registry():

    label_registry_page.grid_forget()

    label_name.grid_forget()
    entry_name.grid_forget()
    
    label_family.grid_forget()
    entry_family.grid_forget()
    
    label_email.grid_forget()
    entry_email.grid_forget()
    
    label_nationalcode.grid_forget()
    entry_nationalcode.grid_forget()
    
    label_age.grid_forget()
    entry_age.grid_forget()
    
    label_password_registry.grid_forget()
    entry_password_registry.grid_forget()
    
    label_confirm_password.grid_forget()
    entry_confirm_password.grid_forget()
    
    button_submit.grid_forget()
    button_back_registry.grid_forget()

    label_image.grid(row = 0, column = 0, padx=208, pady=10, sticky='w')
    label_page1.grid(row=1,column=0, padx=220, pady=0, sticky='w')
    button_login.grid(row = 2, column = 0, padx=200,pady=10, sticky='w')
    button_registry.grid(row = 2, column = 0, padx=280, pady=10, sticky='w')   

#endregion




#endregion  








app = ttk.Window(themename='darkly')
app.geometry('600x600')
app.title('Bank Application')

#region first page

label_page1 = ttk.Label(app, text='Blu Bank', font=('calibri', 18, 'bold'))
label_page1.grid(row=1,column=0, padx=220, pady=0, sticky='w')

button_login = ttk.Button(app, text='Login', style=SUCCESS, command= show_login_page)
button_login.grid(row = 2, column = 0, padx=200,pady=10, sticky='w')

button_registry = ttk.Button(app, text = 'Registry', style = SUCCESS, command= registry) 
button_registry.grid(row = 2, column = 0, padx=280, pady=10, sticky='w')


ditrect1 = "Bank_Logo.png"
Image1 = Image.open(ditrect1)
image_resized = Image1.resize((120, 120), Image.Resampling.LANCZOS)
Image2 = ImageTk.PhotoImage(image_resized)
label_image = ttk.Label(app , image=Image2)
label_image.grid(row = 0, column = 0, padx=208, pady=10, sticky='w')
label_image.image = Image2

#endregion

#region login page

label_login = ttk.Label(app, text='Login', font=('calibri', 18, 'bold'))
label_login.grid(row=0,column=0, padx=250, pady=10, sticky='w')
label_login.grid_forget()

label_username_login_page = ttk.Label(app, text= 'Username', font= ('calibri', 15, 'bold'))
label_username_login_page.grid(row=1, column=0, padx=10, pady=10, sticky='w')
label_username_login_page.grid_forget()

entry_username_login_page = ttk.Entry(app, style='info')
entry_username_login_page.grid(row=1,padx=100,pady=10)
entry_username_login_page.grid_forget()
        
label_password_login_page = ttk.Label(app, text= 'Password', font=('arial', 15, 'bold'))
label_password_login_page.grid(row=2, column=0, padx=10, pady=10, sticky='w')
label_password_login_page.grid_forget()
        
entry_password_login_page = ttk.Entry(app, bootstyle='info')
entry_password_login_page.grid(row=2, padx=100, pady= 10)
entry_password_login_page.grid_forget()
        
button_enter = ttk.Button(app, text = 'Enter', style = SUCCESS, command= enter)    # command not finished
button_enter.grid(row=3, column=0, padx=210,pady= 10, sticky='w')
button_enter.grid_forget()

button_back_page2 = ttk.Button(app, text = 'Back', style = SUCCESS, command= back)
button_back_page2.grid(row=3, column=0, padx=280, pady=10, sticky='w')
button_back_page2.grid_forget()

#endregion

#region registry page

label_registry_page = ttk.Label(app, text= 'Registry', font= ('calibri', 18, 'bold'))
label_registry_page.grid(row=0, column=0, padx=250, pady= 10, sticky='w')
label_registry_page.grid_forget()

label_name = ttk.Label(app, text='Name', font= ('calibri', 15, 'bold'))
label_name.grid(row=1, column=0, padx=10, pady=10, sticky='w')
label_name.grid_forget()

entry_name = ttk.Entry(app, bootstyle='info')
entry_name.grid(row=1, padx=100, pady=10)
entry_name.grid_forget()

label_family = ttk.Label(app, text= 'Family', font=('calibri', 15, 'bold'))
label_family.grid(row=2, column=0, padx=10, pady=10, sticky='w')
label_family.grid_forget()

entry_family = ttk.Entry(app, bootstyle='info')
entry_family.grid(row=2, padx=100, pady=10)
entry_family.grid_forget()

label_email = ttk.Label(app, text='E-mail', font=('calibri', 15, 'bold'))
label_email.grid(row=3, column=0, padx=10, pady=10, sticky='w')
label_email.grid_forget()

entry_email = ttk.Entry(app, bootstyle = 'info')
entry_email.grid(row=3, padx=100, pady=10)
entry_email.grid_forget()

label_nationalcode = ttk.Label(app, text='National code', font= ('calibri', 15, 'bold'))
label_nationalcode.grid(row=4, column=0, padx=10, pady=10, sticky='w')
label_nationalcode.grid_forget()

entry_nationalcode = ttk.Entry(app, bootstyle = 'info')
entry_nationalcode.grid(row=4, padx=100, pady=10)
entry_nationalcode.grid_forget()

label_age = ttk.Label(app, text='Date of birth', font=('calibri', 15, 'bold'))
label_age.grid(row=5, column=0, padx=10, pady=10, sticky='w')
label_age.grid_forget()

entry_age = ttk.Entry(app, bootstyle= 'info')
entry_age.grid(row=5, padx=100, pady=10)
entry_age.grid_forget()

label_password_registry = ttk.Label(app, text= 'Password', font=('calibri', 15, 'bold'))
label_password_registry.grid(row=6, column=0, padx=10, pady=10, sticky='w')
label_password_registry.grid_forget()

entry_password_registry = ttk.Entry(app, bootstyle = 'info')
entry_password_registry.grid(row=6, padx=100, pady=10)
entry_password_registry.grid_forget()

label_confirm_password = ttk.Label(app, text= 'Confirm password', font=('calibri', 15, 'bold'))
label_confirm_password.grid(row=7, column=0, padx=10, pady=10, sticky='w')
label_confirm_password.grid_forget()
        
entry_confirm_password = ttk.Entry(app, bootstyle= 'info')
entry_confirm_password.grid(row=7, padx=100, pady=10)
entry_confirm_password.grid_forget()

button_submit = ttk.Button(app, text='Submit', style=SUCCESS, command= submit) 
button_submit.grid(row = 8, column = 0, padx=210, pady=10, sticky='w')  
button_submit.grid_forget()

button_back_registry = ttk.Button(app, text='Back', style=SUCCESS, command= back_registry)
button_back_registry.grid(row = 8, column = 0, padx=280,pady=10, sticky='w') 
button_back_registry.grid_forget()


#endregion


#Dashboard
label_balance = ttk.Label(app , text="5,000,000$" , style=SUCCESS , font= ('calibri', 15, 'bold'))
label_balance.grid(row=0 , column=0 , padx = 250 , pady=10 , sticky='w')
label_balance.grid_forget()

button_logout = ttk.Button(app, text="Log Out" , style=SUCCESS , command=logout)
button_logout.grid(row=1 , column=0 , padx = 250 , pady=10 , sticky='w')
button_logout.grid_forget()
#endregion




app.mainloop()



