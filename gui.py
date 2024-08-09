import tkinter
from BankAccount import BankAccount

global account

accounts = []
passwords = []


def personal_page():
    page = tkinter.Toplevel()
    page.title("Your Bank Page")
    page.geometry('450x450')
    page.configure(bg="#333333")
    page_frame = tkinter.Frame(page, bg="#333333", bd=3, height=400,
                               highlightcolor="white", highlightthickness=3, highlightbackground='white', width=400)
    page_frame.pack(padx=25, pady=25)

    # Labels:
    page_title = tkinter.Label(page_frame, text="Welcome to your page", bg='#333333', fg="#FF3399", font=("Inter", 20))
    balance_lbl = tkinter.Label(page_frame, text="your account balance is :", bg='#333333', fg="#FF3399",
                                font=("Inter", 16))

    acc_name = tkinter.Label(page_frame, text="your account name is :", bg='#333333', fg="#FF3399", font=("Inter", 16))
    acc_name_value = tkinter.Label(page_frame, text=f"{account.name}", bg='#333333', fg="#FF3399", font=("Inter", 16))
    amount_lbl = tkinter.Label(page_frame, text="Enter the money :", bg='#333333', fg="#FF3399", font=("Inter", 16))

    # Labels:
    page_title.place(x=50, y=30)
    acc_name.place(x=0, y=80)
    acc_name_value.place(x=245, y=80)
    balance_lbl.place(x=0, y=120)
    amount_lbl.place(x=0, y=200)

    # Entries:
    global amount_entry
    amount_entry = tkinter.Entry(page_frame, font=("Inter", 16), width=16, bd=4, fg="black", bg="lightblue")
    amount_entry.place(x=180, y=200)

    balance_string = tkinter.StringVar()
    balance_string.set(f"{account.balance:.3f} $")
    balance_value_lbl = tkinter.Label(page_frame, textvariable=balance_string, bg='#333333', fg="#FF3399",
                                      font=("Inter", 16))
    balance_value_lbl.place(x=245, y=121)

    def apply_deposit(amount):
        account.deposit(float(amount))
        balance_string.set(f"{account.balance:.3f} $")

    def apply_withdraw(amount):
        account.withdraw(float(amount))
        balance_string.set(f"{account.balance:.3f} $")

    # Buttons:
    deposit_btn = tkinter.Button(page_frame, text="Deposit", bg="#FF3399", fg="#FFFFFF", font=("Inter", 16),
                                 command=lambda: apply_deposit(float(amount_entry.get())))

    withdraw_btn = tkinter.Button(page_frame, text="Withdraw", bg="#FF3399", fg="#FFFFFF", font=("Inter", 16),
                                  command=lambda: apply_withdraw(float(amount_entry.get())))

    deposit_btn.place(x=70, y=250)
    withdraw_btn.place(x=200, y=250)


def login():
    username = accounts
    password = passwords
    if name_entry.get() in username and password_entry.get() in password:
        tkinter.messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        personal_page()
    else:
        tkinter.messagebox.showerror(title="Error", message="Invalid login.")


def creat_new_account_command():
    # New_window:
    global new_window
    new_window = tkinter.Toplevel()
    new_window.title("Creating new bank account")
    new_window.geometry('450x450')
    new_window.configure(bg="#333333")
    # New_frame:
    new_frame = tkinter.Frame(new_window, bg="#333333", bd=3, height=400,
                              highlightcolor="white", highlightthickness=3, highlightbackground='white', width=400)
    new_frame.pack(padx=25, pady=25)
    # New_labels:
    new_lbl_name = tkinter.Label(new_frame, text="Account name", bg='#333333', fg="#FF3399", font=("Inter", 16))
    new_lbl_password = tkinter.Label(new_frame, text="Password", bg='#333333', fg="#FF3399", font=("Inter", 16))
    new_lbl_repassword = tkinter.Label(new_frame, text="re-Password", bg='#333333', fg="#FF3399", font=("Inter", 16))
    new_lbl_title = tkinter.Label(new_frame, text="Enter your information", bg='#333333', fg="#FF3399",
                                  font=("Inter", 20))

    new_lbl_title.place(x=65, y=30)
    new_lbl_name.place(x=0, y=120)
    new_lbl_password.place(x=0, y=160)
    new_lbl_repassword.place(x=0, y=200)

    # New_Entries:
    global new_name_entry
    new_name_entry = tkinter.Entry(new_frame, font=("Inter", 16), width=16, bd=4, fg="black", bg="lightblue")
    global new_password_entry
    new_password_entry = tkinter.Entry(new_frame, font=("Inter", 16), width=16, bd=4, fg="black", bg="lightblue",
                                       show="*")
    global new_repassword_entry
    new_repassword_entry = tkinter.Entry(new_frame, font=("Inter", 16), width=16, bd=4, fg="black", bg="lightblue",
                                         show="*")

    new_name_entry.place(x=150, y=124)
    new_password_entry.place(x=150, y=164)
    new_repassword_entry.place(x=150, y=200)

    # New_Button:
    create_new_button = tkinter.Button(new_frame, text="Create new account", bg="#FF3399", fg="#FFFFFF",
                                       font=("Inter", 16),
                                       command=create_new)
    create_new_button.place(x=80, y=250)


def contains(lst, f):
    for x in lst:
        if f(x):
            return True
    return False


def create_new():
    password = new_password_entry.get() if new_password_entry.get() else 0
    name = new_name_entry.get()
    account_exists = False

    if contains(accounts, lambda x: name == new_name_entry.get()):
        account_exists = True
    if account_exists:
        tkinter.messagebox.showerror(title="Creating account", message="You already created an account.")
    else:
        if password == new_repassword_entry.get():
            global account
            account = BankAccount(0, name)
            accounts.append(name)
            passwords.append(password)
            tkinter.messagebox.showinfo(title="Success", message="Account created successfully")
            new_window.withdraw()
        else:
            tkinter.messagebox.showerror(title="Wrong password", message="password doesn't match")


# App_window

window = tkinter.Tk()
window.title("Bank account")
window.geometry('450x450')
window.configure(bg="#333333")
window.resizable(True, True)
window.state('normal')

# labels_frame
frame = tkinter.Frame(window, bg="#333333", bd=3, height=400,
                      highlightcolor="white", highlightthickness=3, highlightbackground='white', width=400)
frame.pack(padx=25, pady=25)

# App_labels

lbl_name = tkinter.Label(frame, text="Account name", bg='#333333', fg="#FF3399", font=("Inter", 16))
lbl_password = tkinter.Label(frame, text="Password", bg='#333333', fg="#FF3399", font=("Inter", 16))
lbl_title = tkinter.Label(frame, text="Welcome", bg='#333333', fg="#FF3399", font=("Inter", 30))

lbl_name.place(x=0, y=120)
lbl_password.place(x=0, y=160)
lbl_title.place(x=110, y=30)

# Entries:
name_entry = tkinter.Entry(frame, font=("Inter", 16), width=16, bd=4, fg="black", bg="lightblue")
password_entry = tkinter.Entry(frame, font=("Inter", 16), width=16, bd=4, fg="black", bg="lightblue", show="*")

name_entry.place(x=150, y=124)
password_entry.place(x=150, y=164)

# Buttons:
login_button = tkinter.Button(frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Inter", 16), command=login)
create_button = tkinter.Button(frame, text="Create new account", bg="#FF3399", fg="#FFFFFF", font=("Inter", 16),
                               command=creat_new_account_command)

login_button.place(x=80, y=220)
create_button.place(x=180, y=220)

window.mainloop()
