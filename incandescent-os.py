import socket
from datetime import datetime
from datetime import date
import ssl
import smtplib
import os
import time
import keyboard
import ctypes
import random
import string
from email.message import EmailMessage

hostname = socket.gethostname()

now = datetime.now()
current_time = now.strftime("%H.%M")
full_date = date.today()

os_name = "Incandescent"
os_version = "0.1.3"

ctypes.windll.kernel32.SetConsoleTitleW(f"{os_name} - {os_version}")

err1 = "INVALID_INPUT"
err2 = "INVALID_OPTION"
err3 = "INVALID_VALUE_INT"
c_err1 = "C_NOT_INTEGER"
c_err2 = "C_INVALID_OPERATOR"
c_err3 = "C_DIVISION_ZERO"
v_err1 = "V_WRONG_PASSWORD"
to_err1 = "TO_INVALID_TASK_INDEX"

def option_show_errorlist():
    print(f"\n  #{err1} = Invalid value entered.")
    print(f"  #{err2} = Invalid option selected. User can only choose inputs on the list.")
    print(f"  #{err3} = Invalid value entered. Value can only be integer.\n")
    print(f"  #{c_err1} = Calculator specific error. Input for number can only be integer.")
    print(f"  #{c_err2} = Calculator specific error. Input for operator can only be +, -, /, *.")
    print(f"  #{c_err3} = Calculator specific error. Numbers can not be divided by zero.\n")
    print(f"  #{v_err1} = Vault specific error. Vault password is entered wrong.")
    print(f"  #{to_err1} = To Do List specific error. Invalid task number entered..")
    user_input()

def option_vault():
    vault_path = "memory/vault.txt" #DONT FORGET TO CREATE ONE
    def read_vault():
        with open(vault_path, "r") as file:
            content = file.read()
            print("\n", content)
    def write_vault():
        with open(vault_path, "a") as file:
            file.writelines(input("Write : "))
    def read_more_write_vault():
        with open(vault_path, "r") as file:
            updated_content = file.read()
            print("\n", updated_content)
    os.system('cls')
    print("\n   - VAULT MODE -\n")
    print("  #return-back-main\n")
    while True:
        vault_pass = input("Password for vault : ")
        if vault_pass in ["return","back","main"]:
            os.system('cls')
            print_main_menu()
            user_input()
        elif vault_pass == "123": #DESIRED PASSWORD
            os.system('cls')
            print("\n   - VAULT MODE -\n")
            break
        else:
            print(f"{v_err1}\n")

    print("  #write-w\n  #read-show-r\n  #return-back-main\n")
    print("  - This is your personal vault -\n  - You can write anything here -\n;\n")
    read_vault()
    while True:
        vault_command = input(f"{hostname} : ")
        print("") #BLANK LINE AFTER INPUT
        if vault_command in ["write","w"]:
            write_vault()
        elif vault_command in ["read","show","open","r"]:
            read_more_write_vault()
        elif vault_command in ["return","back","main"]:
            os.system('cls')
            print_main_menu()
            user_input()
        else:
            print(f"{err2}\n")

def option_time():
    print(f"\n    {current_time} - {full_date} US-FORMAT\n")

def option_timer():
    print("\n  Hold 's' to stop timer. #BETA")
    def countdown_timer(seconds):
        print(f"  Timer set for {seconds} seconds\n")
        for i in range(seconds, 0, -1):
            print(f"    {i}", end='\r')  # Print without newline to overwrite the previous countdown
            time.sleep(1)
            if keyboard.is_pressed('s'):
                print("\n  Timer stopped by user.\n")
                return
        print("  Time is up.\n")
    try:
        seconds = int(input("\n  Set the timer for (second) : "))
        countdown_timer(seconds)
    except ValueError:
        print(f"{err3}\n")

def option_calculator():
    while True:
        try:
            calc_num1 = int(input("\n  Enter a number : "))
            break
        except ValueError:
            print(f"  {c_err1}")
    calc_operator = input("  Select operator (+, -, /, *) : ")
    if calc_operator not in ["+", "-", "/", "*"]:
        print(f"  {c_err2}\n")
        return
    while True:
        try:
            calc_num2 = int(input("  Enter another number : "))
            if calc_operator == "/" and calc_num2 == 0:
                print(f"  {c_err3}\n")
                return
            break
        except ValueError:
            print(f"  {c_err1}\n")
    if calc_operator == "+":
        calc_result = calc_num1 + calc_num2
    elif calc_operator == "-":
        calc_result = calc_num1 - calc_num2
    elif calc_operator == "/":
        calc_result = calc_num1 / calc_num2
    elif calc_operator == "*":
        calc_result = calc_num1 * calc_num2
    print(f"\n  {calc_num1} {calc_operator} {calc_num2} = {calc_result}\n")
    user_input()

def option_reload():
    os.system('cls')
    exec(open("incandescent.py").read())

def option_clear():
    os.system('cls')
    print_main_menu()
    user_input()

def option_help():
    option_help_menu = [
        "\n  #send mail",
        "  #calculator",
        "  #timer",
        "  #time",
        "  #vault\n"
    ]
    for option_help_menu in option_help_menu:
        print(option_help_menu)
    user_input()

def option_send_mail():

    email_sender = '' #DEFINE WHO IS SENDING EMAILS
    email_password = "" #DEFINE MAIL SENDER PASSWORD
    email_receiver = input("\nWho to send (Type 'a' to send admin) : ")
    if email_receiver == "a":
        email_receiver = "" #DEFINE ADMIN MAIL

    subject = input("Subject : ")
    body = input("Body : ")

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

#def option_passwordmaker(length):
#    pass_characters = string.ascii_letters + string.digits
#    pass_password = ''.join(random.choice(pass_characters) for _ in range(length))
#    return pass_password
#
#    password_length = int(input("Password lenght : "))
#    pass_password = generate_password(password_length)
#    print(f"{pass_password}\n")

def version():
    print(f"\n  {os_name} - {os_version}\n")

def print_main_menu():
    main_menu_options = [
        "  ver = show version info",
        "  help = show various commands",
        "  err = show error explanations",
        "  clear = clear the screen",
        "  reload = reload os",
        "  exit = close os\n",
    ]
    print(f"\n   - {os_name} OS _ {os_version} -\n")
    for main_menu_options in main_menu_options:
        print(main_menu_options)

def user_input():
    while True:
        command = input(f"{hostname} : ")
        if command in ["version","ver"]:
            version()
            user_input()
        elif command == "help":
            option_help()
        elif command in ["clear","cls","c","clean"]:
            option_clear()
        elif command in ["errors","error","err"]:
            option_show_errorlist()
        elif command in ["reload","restart"]:
            option_reload()
        elif command in ["calculator","calc"]:
            option_calculator()
        elif command in ["timer",]:
            option_timer()
        elif command in ["time","clock"]:
            option_time()
        elif command in ["vault","personal"]:
            option_vault()
        elif command in ["exit","close",]:
            exit()
        elif command in ["send mail","sendmail","mail"]:
            option_send_mail()
            os.system('cls')
            user_input()
        else:
            print(f"{err2}\n")

if __name__ == "__main__":
    print_main_menu()
    user_input()
