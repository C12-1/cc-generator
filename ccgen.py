# libraries
import random 
import os
from string import digits as sdigits
from datetime import datetime
import colorama
colorama.init()

# constants
DIGITS_TUBLE = tuple('0123456789')
CURRENT_YEAR = datetime.now().year
LEGAL_YEAR = CURRENT_YEAR + 8
RED = "\033[31m"
UNWANTED_INPUTS = ""

# the logo of the author
print(f"""\n\n \033[34m██████╗██╗    ██╗████████╗███████╗██╗    ██╗   ██╗███████╗
██╔════╝██║    ██║╚══██╔══╝██╔════╝██║    ██║   ██║██╔════╝
██║     ██║ █╗ ██║   ██║   █████╗  ██║    ██║   ██║█████╗  
██║     ██║███╗██║   ██║   ██╔══╝  ██║    ╚██╗ ██╔╝██╔══╝  
╚██████╗╚███╔███╔╝   ██║   ███████╗███████╗╚████╔╝ ███████╗
 ╚═════╝ ╚══╝╚══╝    ╚═╝   ╚══════╝╚══════╝ ╚═══╝  ╚══════╝\n\t\t\t\t{RED} MADE BY : @C12\n \033[0m""")

# the function of taking the ipute and check the type of it and return it 
def checking():
    bin_input = input(f"{RED}[+] write the path of the file (txt) \n[+] write the bin ex:456654|xx|xx|xxx , 456654 >> ").strip()

    # check if the bin is empty
    if not bin_input :
        print(f"{RED}🔻 The input is empty")
        return False
    
    # file path handling
    if os.path.exists(bin_input) and os.path.isfile(bin_input):
        with open(bin_input , "r") as bin_file:
            bin_list = bin_file.readlines()
            cleaned_bin_list = []
            for line in bin_list:  #loop to check if the card number is only digits
                bin_part = line.split("|")[0].strip()
                if bin_part.isdigit():
                    cleaned_bin_list.append(line)
                else:
                    UNWANTED_INPUTS += line + "\n"
            if not bin_list:
                print(f"{RED}🔻 No bins were found inside the file")
                return False
            return cleaned_bin_list
    # single bin handling 
    bin_parts = bin_input.split("|")
    first_num = bin_parts[0]

    # first number handling 
    if not first_num or not first_num.isdigit():
        print(f"{RED}Invalid bin input : must contain only digits")
        return False
    
    elif not 6 <= len(first_num) <= 16 :
        print(f"{RED}Invalid bin input : length must be around 6 and 16")
        return False
    
    if len(bin_parts) > 1 : 

        # month handling 
        if len(bin_parts) >= 2 and bin_parts[1] != "" and bin_parts[1] != "xx" :
            if not bin_parts[1].isdigit() or 1 > bin_parts[1] > 12:
                print(f"{RED}Invalid month : must be 1-12 digits or xx")
                return False

        # year handling 
        if len(bin_parts) >= 3 and bin_parts[2] not in ["" , "xx"]:
            if not bin_parts[2].isdigit():
                print(f"{RED}Invalid year : must be digits or xx")
                return False

        # cvv cvc handling 
        if len(bin_parts) == 4 and bin_parts[3] not in ["" , "xx" ,"xxx" , "xxxx"]:
            if not bin_parts[3].isdigit():
                return False

# the function to return random digits
def shufling():
    return random.choice(sdigits)

# function to return the first card number 
def firts_num(bin_number : str) -> str :
    global UNWANTED_INPUTS
    if not bin_number:
        UNWANTED_INPUTS += bin_number + "\n"
        return False
    card_number = bin_number.split("|")[0]
    if not card_number.isdigit() and not 6 <= len(card_number) <= 16 or not card_number.startswith(tuple("4563")):
        UNWANTED_INPUTS += bin_number + "\n"
        print(f"{RED}Invalid Bin : out of range or wrong must start with 5-4-6-3")
        return False
    if card_number.startswith(tuple("456")):
        while len(card_number) < 15:
            card_number += shufling()
    elif card_number.startswith("3") : 
        while len(card_number) < 14:
            card_number += shufling()
    # calculate checksum 
    total = 0

    for i , number in enumerate(card_number[::-1] , 1):
        number = int(number)
        if i % 2 == 1:
            number *= 2
            if number > 9:
                number = (number % 10) + 1
        total += number
    checksum = (10 - (total % 10)) % 10

    print( card_number + str(checksum))
def month_year(num):
    full = num.split("|")
    if len(full) == 4:
        if full[1].startswith(DIGITS_TUBLE) and full[2].startswith(DIGITS_TUBLE):
            month = full[1]
            year = full[2]
            if 0 < int(month) <= 12 :
                return f"{month}|{year}"
        elif full[1] == "xx" and full[2].startswith(DIGITS_TUBLE):
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
                    
        elif full[2] == "xx" and full[1].startswith(DIGITS_TUBLE):
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

def luhn_algo(number: str) -> bool:
    luhn_num = number.split("|")[0][::-1]
    total = 0
    for i, x in enumerate(luhn_num):
        x = ord(x) - 48
        if i % 2 == 1:
            x = x*2
            if x > 9 :
                x = (x % 10) + 1
                
        total += x
    return total % 10 == 0 

# the main function
def main(number):
    filename = f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} CCs.txt"
    generated = 0
    max_attempts = 50  # Prevent infinite loops
    
    if number :
        amount = input("How many cards default 10 >> ").strip()
        # default amount
        if not amount.isdigit() or amount == "" or int(amount) < 10:
            print(f"{RED}Wrong amount : write correct digit setting default 10")
            amount = 10
 
        amount = int(amount)
        # handling with list 
        with open(filename , "w") as file:
            if type(number) == list :
                valid_bins = [] 
                bin_list = number
                for bin in bin_list:
                    card_number = firts_num(bin)
                    if card_number and luhn_algo(card_number):
                        return
                    


                


            
    else: 
        return


    
    
        
   
def keep_going():
    func = main(checking())
    if func == "write a correct number"  or func == "wrong input":
        while True:
            func: None | str = main(checking())
    else:
        while True:
            answer = input("To keep generating 'yes' || to exit 'no' >> ").upper()
            if answer == "YES":
                main(checking())
            elif answer == "NO":
                print("\033[33m🔻Thank you for using our script :)")
                break
            else:
                print("Write yes or no")

if __name__ == "__main__":
    try : 
        main(checking())
    except KeyboardInterrupt:
        print(f"{RED}\n\n🔴 Exiting...")
