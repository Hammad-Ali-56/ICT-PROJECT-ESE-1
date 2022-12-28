from tkinter import *
import pickle
from tkinter.messagebox import askokcancel, showinfo, WARNING
from tkinter import ttk
from time import sleep
from random import randint
import pandas as pd
import numpy
import csv


# IMPORTING FILES
try:
    files = "info.pkl"
    filesobj = open(files, 'rb')  # reading the file
    info = pickle.load(filesobj)  # storing content of file in
    print(info)
except:
    usernames = {}
    amounts = {}
    credit = {}

    info = [usernames, amounts, credit]

    file = "info.pkl"
    fileobj = open(file, 'wb')  # creating a file
    pickle.dump(info, fileobj)  # dumping the info to the file
    fileobj.close()


user_passes = info[0]
amounts = info[1]
creditCards = info[2]
usernames = user_passes.keys()
password = user_passes.values()

admin_password = "1111"

# Styling_variables
bg = '#008080'
fg = '#1C2833'
font1 = 'calibri 16'

# name_variable
user = ""


# UPDATING
def update_file(info):
    files = "info.pkl"
    filesobj = open(files, 'wb')  # overwriting a file
    pickle.dump(info, filesobj)  # dumping info into the file
    filesobj.close()

def on_enter(e):
    e.widget['foreground'] = fg


def on_leave(e):
    e.widget['foreground'] = '#808B96'


# Front_end
def sign_up_page(root):
    for widget in root.winfo_children():
        widget.destroy()
    global img2
    page = Frame(root)

    Label(root, image=img2).place(x=600, y=0)
    Label(root, text="WELCOME TO BANKING\nMANAGEMENT SYSTEM", justify=CENTER, font='Century 30 bold', bg=bg, fg='#17202A').place(
        x=25, y=80)
    Label(root, text="USERNAME", font=font1, bg=bg, fg=fg).place(x=22, y=226)
    Label(root, text="MASTER CARD NUMBER", font=font1, bg=bg, fg=fg).place(x=22, y=320)
    Label(root, text="PASSWORD", font=font1, bg=bg, fg=fg).place(x=22, y=410)
    Label(root, text="CONFIRM PASSWORD", font=font1, bg=bg, fg=fg).place(x=22, y=500)
    Label(root, text="Already have an account?", font='calibri 12', fg='#808B96', bg=bg).place(x=310, y=603)
    Label(root, text="Sign in as admin", font='calibri 12', fg='#808B96', bg=bg).place(x=310, y=628)
    Button(root, text="SIGN-UP", font='rockwell 19', borderwidth=0, width="15", bg='#1F1A24', fg=bg, cursor='hand2',
           command=lambda: sign_up(en_username.get(), password.get(), pass_confirm.get(),
                                   credit_card_number.get())).place(x=30, y=600)
    Button(root, text="LOG-IN", font='calibri 13 underline', borderwidth=0, width="6", pady=0, padx=0, fg='#17202A',
           bg=bg, cursor='hand2', command=lambda: log_in_page(root)).place(x=483, y=600)
    Button(root, text="ADMIN", font='calibri 13 underline', borderwidth=0, width="6", pady=0, padx=0, fg='#17202A',
           bg=bg, cursor='hand2', command=lambda: admin_log_in_page(root)).place(x=483, y=625)

    en_username = StringVar()
    Label(root, text="___________________________________", font='arial 20', bg=bg, fg=fg).place(x=32, y=265)
    username = Entry(root, textvariable=en_username, font='arial 20', width=35, borderwidth=0, bg=bg, fg='#DAF7A6')
    username.place(x=35, y=260)
    credit_card_number = StringVar()
    Label(root, text="___________________________________", font='arial 20', bg=bg, fg=fg).place(x=32, y=355)
    credit_card = Entry(root, textvariable=credit_card_number, font='arial 20', width=35, borderwidth=0, bg=bg,
                        fg='#DAF7A6')
    credit_card.place(x=35, y=350)
    password = StringVar()
    Label(root, text="___________________________________", font='arial 20', bg=bg, fg=fg).place(x=32, y=445)
    username = Entry(root, textvariable=password, show="●", font='arial 20', width=35, borderwidth=0, bg=bg,
                     fg='#DAF7A6')
    username.place(x=35, y=440)
    pass_confirm = StringVar()
    Label(root, text="___________________________________", font='arial 20', bg=bg, fg=fg).place(x=32, y=535)
    passwordd = Entry(root, textvariable=pass_confirm, show="●", font='arial 20', width=35, borderwidth=0, bg=bg,
                      fg='#DAF7A6')
    passwordd.place(x=35, y=530)


def log_in_page(root):
    for widget in root.winfo_children():
        widget.destroy()
    global username, password, amounts, img2, bg, fg
    page = Frame(root)

    Label(root, image=img2).place(x=600, y=0)
    Label(root, text="LOG-IN", font='Century 30 bold underline', bg=bg, fg='#17202A').place(x=220, y=100)
    Label(root, text="USERNAME", font=font1, bg=bg, fg=fg).place(x=22, y=220)
    Label(root, text="PASSWORD", font=font1, bg=bg, fg=fg).place(x=22, y=425)
    Label(root, text="MASTER CARD NUMBER", font=font1, bg=bg, fg=fg).place(x=22, y=325)
    Button(root, text="LOG-IN", font='rockwell 19', borderwidth=0, width="20", bg='#1F1A24', fg=bg, cursor='hand2',
           command=lambda: log_in(en_username.get(), en_password.get(), en_credit.get())).place(x=175, y=530)
    back = Button(root, text="< Back to SIGN-UP", font='calibri 12', borderwidth=0, fg='#808B96', bg=bg, cursor='hand2',
                  command=lambda: sign_up_page(root))
    back.place(x=30, y=50)
    back.bind("<Enter>", on_enter)
    back.bind("<Leave>", on_leave)

    en_username = StringVar()
    Label(root, text="___________________________________", font='arial 20', bg=bg, fg=fg).place(x=32, y=255)
    username1 = Entry(root, textvariable=en_username, font='arial 20', width=35, borderwidth=0, bg=bg,
                      fg='#DAF7A6').place(x=35, y=250)
    en_password = StringVar()
    Label(root, text="___________________________________", font='arial 20', bg=bg, fg=fg).place(x=32, y=455)
    pass_ = Entry(root, textvariable=en_password, show="●", font='arial 20', width=30, borderwidth=0, bg=bg,
                  fg='#DAF7A6').place(x=35, y=450)
    en_credit = StringVar()
    Label(root, text="___________________________________", font='arial 20', bg=bg, fg=fg).place(x=32, y=355)
    cred = Entry(root, textvariable=en_credit, font='arial 20', width=30, borderwidth=0, bg=bg, fg='#DAF7A6').place(
        x=35, y=350)

def admin_log_in_page(root):
    for widget in root.winfo_children():
        widget.destroy()
    global adminpassword, img2, bg, fg
    page = Frame(root)

    Label(root, image=img2).place(x=600, y=0)
    Label(root, text="ADMIN-LOG-IN", font='Century 30 bold underline', bg=bg, fg='#17202A').place(x=120, y=100)
    Label(root, text="PASSWORD", font=font1, bg=bg, fg=fg).place(x=220, y=275)
    Button(root, text="ADMIN-LOG-IN", font='rockwell 19', borderwidth=0, width="20", bg='#1F1A24', fg=bg, cursor='hand2',
           command=lambda: admin_log_in(en_adminpassword.get())).place(x=125, y=480)
    back = Button(root, text="< Back to SIGN-UP", font='calibri 12', borderwidth=0, fg='#808B96', bg=bg, cursor='hand2',
                  command=lambda: sign_up_page(root))
    back.place(x=30, y=50)
    back.bind("<Enter>", on_enter)
    back.bind("<Leave>", on_leave)

    en_adminpassword = StringVar()
    Label(root, text="___________________________________", font='arial 20', bg=bg, fg=fg).place(x=32, y=355)
    pass_ = Entry(root, textvariable=en_adminpassword, show="●", font='arial 20', width=30, borderwidth=0, bg=bg,
                  fg='#DAF7A6').place(x=35, y=350)

def user_account(root):
    for widget in root.winfo_children():
        widget.destroy()
    global user, bg, fg
    logout_img = PhotoImage(file="logout.png")
    page = Frame(root)

    Label(root, text="WELCOME!  " + user.upper(), wraplength=431, justify=CENTER, font='calibri 36 bold underline',
          bg=bg, fg='#1F1A24').place(x=290, y=100)
    Button(root, text="● Log out", font='calibri 14 bold underline', fg=bg, bg='#1F1A24', borderwidth=0, width="11",
           pady=7, command=logout).place(x=860, y=60)
    Button(root, text="● Log out", font='calibri 14 bold ', bg=bg, fg='#1F1A24', borderwidth=0, width="10",
           command=logout).place(x=865, y=66)
    Button(root, text="Deposit", font='arial 16', borderwidth=0, width="15", pady="15", bg='#1F1A24', fg=bg,
           command=deposit).place(x=500, y=250)
    Button(root, text="Withdraw", font='arial 16', borderwidth=0, width="15", bg='#1F1A24', pady="15", fg=bg,
           command=withdraw).place(x=300, y=250)
    Button(root, text="Current Balance", font='arial 16', borderwidth=0, width="15", bg='#1F1A24', pady="15", fg=bg,
           command=CurrentBal).place(x=100, y=250)
    Button(root, text="Transfer Money", font='arial 16', borderwidth=0, width="15", bg='#1F1A24', pady="15", fg=bg,
           command=transfer).place(x=700, y=250)

def admin_account(root):
    for widget in root.winfo_children():
        widget.destroy()
    global  bg, fg
    logout_img = PhotoImage(file="logout.png")
    page = Frame(root)

    Label(root, text="WELCOME ADMIN! " + user.upper(), wraplength=431, justify=CENTER, font='calibri 36 bold underline',
          bg=bg, fg='#1F1A24').place(x=290, y=80)
    Button(root, text="● Log out", font='calibri 14 bold underline', fg=bg, bg='#1F1A24', borderwidth=0, width="11",
           pady=7, command=logout).place(x=860, y=60)
    Button(root, text="● Log out", font='calibri 14 bold ', bg=bg, fg='#1F1A24', borderwidth=0, width="10",
           command=logout).place(x=865, y=66)
    Button(root, text="Display Information", font='arial 16', borderwidth=0, width="15", pady="15", bg='#1F1A24', fg=bg,
           command=display_information).place(x=400, y=250)



def display_information():
    def openfile():
        dfa = [list(user_passes.keys()), list(user_passes.values()), list(amounts.values()), list(creditCards.values())]
        dfa = pd.DataFrame(dfa)
        print(dfa)
        table.delete(*table.get_children())
        table["columns"] = list(dfa.columns) # Changed
        table["show"] = "headings"
        table.delete(*table.get_children())
        for column in table["columns"]:
            table.column(column, width=70)
            table.heading(column, text=column)

        table_rows = dfa.to_numpy().tolist()
        for row in table_rows:
            table.insert("", "end", values=row)
        # return None
    for widget in root.winfo_children():
        widget.destroy()
    logout_img = PhotoImage(file="logout.png")
    page = Frame(root)
    global bg, fg
    frame1=Frame(admin_account(root) )
    frame1.place(x=75,y=200,height= 400,width= 900)
    frame1.place(x=80,y=200,height= 400,width= 900)
    table = ttk.Treeview(frame1)
    table.place(relheight=1, relwidth=1)
    scrolly = ttk.Scrollbar(frame1, orient=VERTICAL, command=table.yview)
    scrollx = ttk.Scrollbar(frame1, orient=HORIZONTAL, command=table.xview)
    table.configure(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
    scrollx.pack(fill=X, side=BOTTOM)
    scrolly.pack(fill=Y, side=RIGHT)
    openfile()




def transfer():
    global bg, fg
    money = StringVar()
    to = StringVar()

    Label(root, text="How much money you want to transfer?" + "\t" * 5, font=font1, bg=bg, fg=fg).place(x=300, y=350)
    Label(root, text="________", font='arial 16', bg=bg, fg=fg).place(x=445, y=395)
    Label(root, text="$", font='arial 20 bold', bg=bg, fg=fg).place(x=420, y=385)
    Label(root, text="TO: ", font='arial 16 bold', bg=bg, fg=fg).place(x=270, y=450)
    Label(root, text="_" * 30, font='arial 16', bg=bg, fg=fg).place(x=340, y=460)
    Entry(root, textvariable=money, justify=CENTER, font='arial 20', width=5, borderwidth=0, bg=bg, fg='#DAF7A6').place(
        x=450, y=380)
    Entry(root, textvariable=to, font='arial 20', width=27, borderwidth=0, bg=bg, fg='#DAF7A6').place(x=340, y=448)
    Button(root, text="Send Money", font='arial 16', borderwidth=0, width="15", bg=fg, pady="3", fg=bg, cursor='hand2',
           command=lambda: transfer_confirm(money.get(), to.get())).place(x=410, y=530)


# Back_end
def sign_up(username, password, con_pass, card_number):
    global usernames, user_passes, amounts, info, creditCards, bg, fg
    flag = True

    if username in usernames:
        Label(root, text="Username already taken" + "\t" * 3, bg=bg, fg='red', font='calibri').place(x=30, y=300)
        flag = False
    elif not (username.isalnum()):
        Label(root, text="Invalid username! Try using alphanumerics only." + "\t" * 3, bg=bg, fg='red',
              font='calibri').place(x=30, y=300)
        flag = False
    elif len(username) > 16:
        Label(root, text="Username too long! Try making it less than 16 characters", bg=bg, fg='red',
              font='calibri').place(x=30, y=300)
        flag = False
    if password != con_pass:
        Label(root, text="Passwords do not match!" + "\t" * 5, bg=bg, fg='red', font='calibri').place(x=30, y=480)
        flag = False
    if len(password) < 8:
        Label(root, text="Weak Password! Must be larger than 8 characters", bg=bg, fg='red', font='calibri').place(x=30,
                                                                                                                   y=480)
        flag = False
    if not (card_number.startswith('551155')) or len(card_number) != 16 or (card_number in list(creditCards.values())):
        Label(root, text="Invalid credit card number!", bg=bg, fg='red', font='calibri').place(x=30, y=390)
        flag = False

    if flag:
        showinfo(
            title="Account Made Successfully",
            message='Your account has been created successfully! Please login to continue'
        )
        creditCards[username] = card_number
        user_passes[username] = password
        amounts[username] = 0
        info[0] = user_passes
        info[1] = amounts
        update_file(info)


def log_in(username, password, card_number):
    global user_passes, usernames, root, user, creditCards, bg, fg
    try:
        credit_card = creditCards[username]

        if not (username in usernames) or (len(username)) == 0:
            Label(root, text="Incorrect username", bg=bg, fg='red', font='calibri').place(x=30, y=295)

        if not (user_passes[username] == password) or (len(password)) == 0:
            Label(root, text="Password Incorrect", bg=bg, fg='red', font='calibri').place(x=30, y=495)
        if not (creditCards[username] == card_number) or not (credit_card.startswith('551155')) or (card_number == 0):
            Label(root, text="Incorrect Master Card Number", bg=bg, fg='red', font='calibri').place(x=30, y=395)
        if (username in usernames) and (user_passes[username] == password) and (creditCards[username] == card_number):
            user += username
            user_account(root)
    except:
        showinfo(
            title='Credentials error',
            message='Make sure creditentials places are not empty!',
            icon=WARNING,
        )

def admin_log_in(adminpassword):
    global admin_password, root, bg, fg
    try:
        if not (adminpassword == admin_password) or (len(password)) == 0:
            Label(root, text="Password Incorrect", bg=bg, fg='red', font='calibri').place(x=30, y=395)
        if (adminpassword == admin_password):
            admin_account(root)
    except:
        showinfo(
            title='Credentials error',
            message='Make sure creditentials places are not empty!',
            icon=WARNING,
        )

def CurrentBal():
    global amounts, user, bg, fg

    msg = "Your current balance is $" + str(amounts[user])
    showinfo(
        title='Current Balance',
        message=msg
    )


def withdrawal_update(event, money):
    global amounts, info, bg, fg

    money = int(money)
    if money > int(amounts[user]):
        showinfo(
            title="Withdrawal of money",
            message="As your balance is insufficient.\n" "$" + str(money) + " are not withdrawed successfully from your account"
        )
    else:
        remaining_m = amounts[user] - money
        amounts[user] = remaining_m
        showinfo(
            title="Withdrawal of money",
            message="$" + str(money) + " are withdrawed successfully from your account\nRemaining Balance: $" + str(
                remaining_m)
        )

    info[1] = amounts

    update_file(info)


def withdraw():
    global amounts, user, root, withdrawed, bg, fg
    wd_money = StringVar()

    Label(root, text="\tHow much money in $ you want to withdraw?" + "\n" * 10, font=font1, bg=bg, fg=fg).place(x=210,
                                                                                                                y=350)
    Label(root, text="________", font='arial 16', bg=bg, fg=fg).place(x=445, y=395)
    Label(root, text="$", font='arial 20 bold', bg=bg, fg=fg).place(x=420, y=385)

    temp_ = Entry(root, textvariable=wd_money, justify=CENTER, font='arial 20', width=5, borderwidth=0, bg=bg,
                  fg='#DAF7A6')
    temp_.place(x=450, y=380)
    temp_.bind('<Return>', lambda event: withdrawal_update('<Return>', wd_money.get()))


def deposit_update(event, money):
    global amounts, info, user_passes, creditCards, bg, fg

    money = int(money)
    money = abs(money)
    new_m = amounts[user] + money
    showinfo(title="Deposit of money",
             message="$" + str(money) + " are deposited into your account successfully\nUpdated Balance: $" + str(
                 new_m))
    amounts[user] = new_m
    info[1] = amounts

    update_file(info)


def deposit():
    global bg, fg
    dep_money = StringVar()

    Label(root, text="\tHow much money in $ you want to deposit?\t" + "\n" * 10, font=font1, bg=bg, fg=fg).place(x=210,
                                                                                                                 y=350)
    Label(root, text="________", font='arial 16', bg=bg, fg=fg).place(x=445, y=395)
    Label(root, text="$", font='arial 20 bold', bg=bg, fg=fg).place(x=420, y=385)
    Label(root, text=" " * 200, font='arial 20 bold', bg=bg, fg=fg).place(x=0, y=600)

    temp_ = Entry(root, textvariable=dep_money, justify=CENTER, font='arial 20', width=5, borderwidth=0, bg=bg,
                  fg='#DAF7A6')
    temp_.place(x=450, y=380)
    temp_.bind('<Return>', lambda event: deposit_update('<Return>', dep_money.get()))


def transfer_confirm(money, card_num):
    global creditCards, user, bg, fg

    users = list(creditCards.keys())
    card_numbers = list(creditCards.values())
    current_bal = amounts[user]
    money = int(money)
    otp = StringVar()

    if not (card_num in card_numbers):
        Label(root, text="No user with this master card number found!" + "\t" * 10, bg=bg, fg='red',
              font='calibri').place(x=340, y=490)
    if not (card_num.startswith('551155')) or len(card_num) != 16:
        Label(root, text="Invalid credit card number!" + "\t" * 10, bg=bg, fg='red', font='calibri').place(x=340, y=490)
    if money <= 50:
        showinfo(
            title="Transfer error!",
            message="Money must be more than $50 to transfer"
        )
    if current_bal < money:
        showinfo(
            title="Transfer error!",
            message="You do not have enough money in your account!"
        )
    else:
        Label(root, text="An OTP Code has been sent on your device. Enter OTP:", font=font1, bg=bg, fg=fg).place(x=130,
                                                                                                                 y=600)
        Label(root, text="_" * 7, font='arial 16', bg=bg, fg=fg).place(x=620, y=610)
        otp_pass = Entry(root, textvariable=otp, justify=CENTER, font='arial 20', width=7, borderwidth=0, bg=bg,
                         fg='#DAF7A6')
        otp_pass.place(x=620, y=595)
        otp_ans = str(randint(1000, 9999))
        try:
            to_user = card_numbers.index(card_num)
            reciever = users[to_user]
            showinfo(
                title='One-time Password',
                message='Your OTP is:' + otp_ans
            )
            otp_pass.bind('<Return>', lambda event: transfer_ok('<Return>', otp.get(), otp_ans, money, reciever))
        except:
            Label(root, text="No user with this master card number found!" + "\t" * 10, bg=bg, fg='red').place(x=340,
                                                                                                               y=490)
        sleep(1)

def transfer_ok(event, en_otp, otp, money, reciever):
    global amounts, user, bg, fg

    if en_otp == otp:
        amounts[reciever] += int(money)
        amounts[user] -= int(money)
        update_file(info)
        showinfo(title='Transfer Completed',
                 message='Money has been transfered successfully!')
    else:
        Label(root, text="Wrong OTP code!", bg=bg, fg='red', font='calibri').place(x=620, y=615)


def logout():
    global user, bg, fg
    answer = askokcancel(
        title='Confirmation',
        message='Are you sure you want to log-out?',
        icon=WARNING)

    if answer:
        showinfo(
            title='Logout status',
            message='Successfully logout')
        user = ""  # username_string_empties_after_one_user_logout
        sign_up_page(root)


#######################################################-MAIN PROGRAM-############################################################################

pagenum = 1  # initializing_page_number,later_used_for_switching_between_different_pages

root = Tk()  # creating_window

# importing images
img = PhotoImage(file="bank.png")
img2 = PhotoImage(file="logo.png")

# editing_window
root.title("Group 3 Banking System")  # title_of_window
root.geometry("1070x700")
root.resizable(0,0)
root.config(bg=bg)
root.iconphoto(False, img)
Label(root, image=img2).place(x=600, y=0)

sign_up_page(root)  # defaultly_signup_page_will_show up

root.mainloop()
