from tkinter import *
from tkinter import messagebox
import mysql.connector

screen = Tk()
screen.title("REGISTRATION FORM")
screen.geometry("600x600")
screen.resizable(False, False)

def validate_integer_input(P):
    
    if P.isdigit() or P == "":
        return True
    else:
        return False

def register():
    
    name = name_info.get()  
    age = age_info.get()
    address = address_info.get()
    email = email_info.get()
    password = password_info.get()
    gender = gender_info.get()
    agree = agree_info.get()

    
    if email and not email.endswith("@gmail.com"):
        email += "@gmail.com"
        email_info.set(email)

   
    if name == "":
        messagebox.showerror("ERROR", "Please enter your name")
    elif age == "":
        messagebox.showerror("ERROR", "Please enter your age")
    elif address == "":
        messagebox.showerror("ERROR", "Please enter your address")
    elif email == "":
        messagebox.showerror("ERROR", "Please enter your email")
    elif password == "":
        messagebox.showerror("ERROR", "Please enter your password")
    elif agree == 0:
        messagebox.showerror("ERROR", "Please agree to the Terms and Conditions")
    else:
        try:
           
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="PS05@1121", 
                database="RegistrationDB"
            )
            cursor = connection.cursor()

          
            query = "INSERT INTO users (name, age, address, email, password, gender) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (name, age, address, email, password, gender)
            cursor.execute(query, values)
            connection.commit()

          
            messagebox.showinfo("Success", "Registration Successful! Data Saved to Database.")
            
           
            clear()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def clear():
    
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    address_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)


Label(screen, text="My Registration Form", font="Ariel 20 bold", bg="red", fg="black").pack(fill="both")

Label(screen, text="Name", font="20").place(x=50, y=90)
Label(screen, text="Age", font="20").place(x=50, y=130)
Label(screen, text="Address", font="20").place(x=50, y=170)
Label(screen, text="Email", font="20").place(x=50, y=210)
Label(screen, text="Password", font="20").place(x=50, y=250)
Label(screen, text="Gender", font="20").place(x=50, y=300)


name_info = StringVar()
age_info = StringVar()
address_info = StringVar()
email_info = StringVar()
password_info = StringVar()
gender_info = StringVar()
gender_info.set("Male")  
agree_info = IntVar()


name_entry = Entry(screen, font="40", bd="3", textvariable=name_info)
name_entry.place(x=200, y=90)


validate_command = screen.register(validate_integer_input)
age_entry = Entry(screen, font="40", bd="3", textvariable=age_info, validate="key", validatecommand=(validate_command, '%P'))
age_entry.place(x=200, y=130)

address_entry = Entry(screen, font="40", bd="3", textvariable=address_info)
address_entry.place(x=200, y=170)

email_entry = Entry(screen, font="40", bd="3", textvariable=email_info)
email_entry.place(x=200, y=210)

password_entry = Entry(screen, font="40", bd="3", show="*", textvariable=password_info)
password_entry.place(x=200, y=250)


male_button = Radiobutton(screen, text="Male", value="Male", variable=gender_info, font="15")
male_button.place(x=200, y=300)
female_button = Radiobutton(screen, text="Female", value="Female", variable=gender_info, font="15")
female_button.place(x=280, y=300)


terms_checkbox = Checkbutton(screen, text="I agree to the Terms and Conditions", variable=agree_info, font="12")
terms_checkbox.place(x=50, y=350)


Button(screen, text="Register", font="20", bd="6", bg="white", command=register).place(x=200, y=450)
Button(screen, text="Clear", font="20", bd="6", fg="red", bg="white", command=clear).place(x=500, y=500)

screen.mainloop()