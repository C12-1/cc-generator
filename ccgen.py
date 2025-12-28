import random 
import os
from string import digits as sdigits
from datetime import datetime
import colorama
colorama.init()
def checking():
    print("""\n\n \033[34m██████╗██╗    ██╗████████╗███████╗██╗    ██╗   ██╗███████╗
██╔════╝██║    ██║╚══██╔══╝██╔════╝██║    ██║   ██║██╔════╝
██║     ██║ █╗ ██║   ██║   █████╗  ██║    ██║   ██║█████╗  
██║     ██║███╗██║   ██║   ██╔══╝  ██║    ╚██╗ ██╔╝██╔══╝  
╚██████╗╚███╔███╔╝   ██║   ███████╗███████╗╚████╔╝ ███████╗
 ╚═════╝ ╚══╝╚══╝    ╚═╝   ╚══════╝╚══════╝ ╚═══╝  ╚══════╝\n\t\t\t\t\033[31m MADE BY : @C12\n \033[0m""")
    bin_input = input("[+] write the path of the file (txt) \n[+] write the bin ex:456654|xx|xx|xxx >> ").strip()
    try :
        
        if os.path.exists("cc.txt") and os.path.isfile(bin_input):
            with open(bin_input , "r") as bins:
                bin = bins.readlines()
                cleaned_bins = [line.strip() for line in bin if line.strip()]
                
                return cleaned_bins
        elif bin_input.split("|")[0].isdigit() :
            first_num = bin_input.split("|")[0]
            if 6 <= len(first_num) <= 12:
                return  bin_input
            else:
                return "Invalid bin: must be 6-12 digits and even length"
        else:
            return "Invalid input: must be a file path or a numeric bin"
    except Exception as e:
        return f"the problem of {e}"
def shufling():
    num_list = sdigits
    choice = random.choice(num_list)
    return choice
def firts_num(num):
    the_num = num.split("|")[0]
    
    if 0 < len(the_num) <= 16:
        length = 16 - len(the_num)
        for _ in range(length+1):
            the_num += shufling()
            if len(str(the_num)) == 16 :
                return the_num
    else:
        print(f"[-] the number <<< {num} >>> doesnt much (<0 or >16)")
def month_year(num):
    full = num.split("|")
    if len(full) == 4:
        if full[1].startswith(tuple('0123456789')) and full[2].startswith(tuple('0123456789')):
            month = full[1]
            year = full[2]
            if 0 < int(month) <= 12 :
                return f"{month}|{year}"
        elif full[1] == "xx" and full[2].startswith(tuple('0123456789')):
                month = random.randint(1 ,12)
                year = full[2]
                if 0 < month < 10:
                    month = "0" + str(month)

                    return f"{month}|20{year}"
                else: 
                    return f"{month}|20{year}"
        elif full[2] == "xx" and full[1].startswith(tuple('0123456789')):
            year = random.randint(26 ,33)
            month = full[1]
            return f"{month}|20{year}"
        elif full[1] == "xx" and  full[2] == "xx":
            month = random.randint(1 ,12)
            if 0 < month < 10:
                month = "0" + str(month)

                
            else: 
                month = month
            year = random.randint(26 ,33)
            return f"{month}|20{year}"
def cvv(num):
    cvv = num.split("|")[3]
    if cvv.startswith(tuple("0123456789")):
        return cvv
    elif cvv =="xxx":
        cvc = ""
        for _ in range(3):
            cvc += shufling()
        return cvc
    elif cvv =="xxxx":
        cvc = ""
        for _ in range(4):
            cvc += shufling()
        return cvc
def randomizing(number):
    amount = input("how many cards >> ")
    if type(number) == list:
        
        with open(f"{datetime.now().strftime("%Y-%m-%d %H-%M-%S")} CCs.txt" , "w") as file:
            for card in range(len(number)):
                format = f"{firts_num(number[card])}|{month_year(number[card])}|{cvv(number[card])}\n"
                for _ in range(int(amount)):

                        file.write(format)
                        print(f"\033[34m {format.strip()}")
    else:
        with open(f"{datetime.now().strftime("%Y-%m-%d %H-%M-%S")} CCs.txt" , "w") as file:
            for _ in range(int(amount)):
                format = f"{firts_num(number)}|{month_year(number)}|{cvv(number)}\n"
                file.write(format)
                print(f"\033[34m {format.strip()}")
   



randomizing(checking())
