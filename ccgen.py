import random 
import os
from string import digits as sdigits
from datetime import datetime
import colorama
colorama.init()
print("""\n\n \033[34m██████╗██╗    ██╗████████╗███████╗██╗    ██╗   ██╗███████╗
██╔════╝██║    ██║╚══██╔══╝██╔════╝██║    ██║   ██║██╔════╝
██║     ██║ █╗ ██║   ██║   █████╗  ██║    ██║   ██║█████╗  
██║     ██║███╗██║   ██║   ██╔══╝  ██║    ╚██╗ ██╔╝██╔══╝  
╚██████╗╚███╔███╔╝   ██║   ███████╗███████╗╚████╔╝ ███████╗
 ╚═════╝ ╚══╝╚══╝    ╚═╝   ╚══════╝╚══════╝ ╚═══╝  ╚══════╝\n\t\t\t\t\033[31m MADE BY : @C12\n \033[0m""")
def checking():
    
    bin_input = input("[+] write the path of the file (txt) \n[+] write the bin ex:456654|xx|xx|xxx , 456654 >> ").strip()
    try :
        
        if os.path.exists(bin_input) and os.path.isfile(bin_input):
            with open(bin_input , "r") as bins:
                bin = bins.readlines()
                cleaned_bins = [line.strip() for line in bin if line.strip()]
                
                return cleaned_bins
        elif bin_input.split("|")[0].isdecimal() :
            first_num = bin_input.split("|")[0]
            if 6 <= len(first_num) <= 12:
                return  bin_input
            else:
                print("\033[31mInvalid bin: must be 6-12 digits and even length")
                return False
        else:
            print("\033[31mInvalid input: must be a file path or a numeric bin")
            return False
            
    except Exception as e:
        print( f"\033[31m  the problem of {e}")
        return False

def shufling():
    num_list = sdigits
    choice = random.choice(num_list)
    return choice
def firts_num(num):
    the_num = num.split("|")
    if 1 <= len(the_num) <= 4 and   int(the_num[0]):
        cnum = the_num[0]
        if 6 <= len(cnum) < 16:
            xlen = 16 - len(cnum)
            for _ in range(xlen):
                cnum += shufling()
                if len(cnum) == 16:
                    return cnum
        elif len(cnum) == 16:
            return cnum
        elif len(cnum) > 16:
            
            return False
    else:
        print("none")
        
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
                    if len(year) == 4:

                        return f"{month}|{year}"
                    else:
                        return f"{month}|20{year}"
                else: 
                    if len(year) == 4:

                        return f"{month}|{year}"
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
    else:
        month = random.randint(1 ,12)
        if 0 < month < 10:
            month = f"0{month}"
        year = random.randint(26 ,33)
        return f"{month}|20{year}"
def cvv(num):
    cvv = num.split("|")
    if len(cvv) == 4:
        if cvv[3].startswith(tuple("0123456789")):
            return cvv[3]
        elif cvv[3] =="xxx":
            cvc = ""
            for _ in range(3):
                cvc += shufling()
            return cvc
        elif cvv[3] =="xxxx":
            cvc = ""
            for _ in range(4):
                cvc += shufling()
            return cvc
    else:
        cvv = ""
        for _ in range(3):
            cvv += shufling()
        return cvv
def generating(number):
    if number:
        amount = input("how many cards default 10 >> ")
        
        def excuting():
            if type(number) == list:
                
                with open(f"{datetime.now().strftime("%Y-%m-%d %H-%M-%S")} CCs.txt" , "w") as file:
                    for card in range(len(number)):
                        for _ in range(int(amount)):
                                format = f"{firts_num(number[card])}|{month_year(number[card])}|{cvv(number[card])}\n"
                                if not firts_num(number[card]):
                                    print(f"\033[31mbin length is out of range(6-16) : {number[card]}")
                                    continue
                                file.write(format)
                                print(f"\033[34m {format.strip()}")
            elif int(amount):
                with open(f"{datetime.now().strftime("%Y-%m-%d %H-%M-%S")} CCs.txt" , "w") as file:
                    for _ in range(int(amount)):
                        format = f"{firts_num(number)}|{month_year(number)}|{cvv(number)}\n"
                        file.write(format)
                        print(f"\033[34m {format.strip()}")
        if amount.startswith(tuple("0123456789")):
            excuting()
        else:
            print("\033[31mwrite a correct number")
    else:
        print("\033[31mwrong input")
    
    
        
   
def keep_going():
    generating(checking())
    while True:
        answer = input("to keep generating 'yes' || to exit 'no' >> ").upper()
        if answer == "YES":
            generating(checking())
        elif answer == "NO":
            print("\033[33mthank you for using our script :)")
            break
        else:
            print("write yes or no")

if __name__ == "__main__":
    keep_going()
