from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
from concurrent.futures import ThreadPoolExecutor, wait

services_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if not attribute.startswith('__'):
            services_sms.append(attribute)

while 1:
    system("cls||clear")
    print("""{}

 
 ░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░  ░▒▓██████▓▒░ ░▒▓█▓▒░         
 ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░             
 ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░             
 ░▒▓███████▓▒░░░▒▓███████▓▒░░░▒▓████████▓▒░░▒▓█▓▒░            
 ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░                
 ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░                
 ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓████████▓▒░                                                                                          

 ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░
 ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░   ░▒▓█▓▒░
 ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░   ░▒▓█▓▒░
  ░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░   ░▒▓█▓▒░
    ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░   ░▒▓█▓▒░
    ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░   ░▒▓█▓▒░
    ░▒▓█▓▒░    ░▒▓█▓▒░░▒▓█▓▒░   ░▒▓█▓▒░

                        {}by {}yigitgulyurt\n  
    """.format(Fore.RED, Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:

        menu = input(Fore.LIGHTWHITE_EX + " 1- Send SMS " + Fore.LIGHTRED_EX + "\n\n 2- Exit\n\n" + Fore.WHITE + " Selection: ")
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Invalid input, please enter the correct option (1 or 2).")
        sleep(1)
        continue
    if menu == 1:
        system("cls||clear")
        print(Fore.WHITE + "Enter the phone number: " + Fore.LIGHTGREEN_EX, end="")
        phone_number = input()
        phone_list = []
        if phone_number == "":
            system("cls||clear")
            print(Fore.WHITE + "Enter the directory of the file containing the phone numbers: " + Fore.LIGHTGREEN_EX, end="")
            directory = input()
            try:
                with open(directory, "r", encoding="utf-8") as f:
                    for line in f.read().strip().split("\n"):
                        if len(line) == 10:
                            phone_list.append(line)
                infinite = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Invalid file directory. Please try again.")
                sleep(3)
                continue
        else:
            try:
                int(phone_number)
                if len(phone_number) != 10:
                    raise ValueError
                phone_list.append(phone_number)
                infinite = "(Press 'Enter' for unlimited)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Invalid phone number. Please try again.") 
                sleep(0.75)
                continue
        system("cls||clear")
        try:
            email = ""
            if ("@" not in email or ".com" not in email) and email != "":
                raise ValueError
        except:
            system("cls||clear")
            continue
        system("cls||clear")
        try:
            print(Fore.WHITE + "Enter the number of SMS to send: " + Fore.LIGHTGREEN_EX, end="")
            count = input()
            if count:
                count = int(count)
            else:
                count = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Invalid input. Please try again.") 
            sleep(0.75)
            continue
        system("cls||clear")
        try:
            print(Fore.WHITE + "Enter the interval in seconds: " + Fore.LIGHTGREEN_EX, end="")
            interval = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Invalid input. Please try again.") 
            sleep(0.75)
            continue
        system("cls||clear")
        if count is None: 
            sms = SendSms(phone_number, email)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if not attribute.startswith('__'):
                            exec("sms."+attribute+"()")
                            sleep(interval)
        for i in phone_list:
            sms = SendSms(i, email)
            if isinstance(count, int):
                while sms.count < count:
                    for attribute in dir(SendSms):
                        attribute_value = getattr(SendSms, attribute)
                        if callable(attribute_value):
                            if not attribute.startswith('__'):
                                if sms.count == count:
                                    break
                                exec("sms."+attribute+"()")
                                sleep(interval)
        print(Fore.LIGHTRED_EX + "\nPress 'Enter' to return to the menu.")
        input()
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Exiting...")
        sleep(1)
        system("cls||clear")
        break

