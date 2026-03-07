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
    global UNWANTED_INPUTS
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
        print(f"{RED}Invalid bin input : must contain only digits or a path")
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
    return bin_parts

# # the function to return random digits
def shufling():
    return random.choice(sdigits)

# function to return the first card number 
def first_num(bin_number : str) -> str :
    global UNWANTED_INPUTS
    if not bin_number:
        return False
    card_number = bin_number.strip().split("|")[0]
        # Check if card_number is valid
    if not card_number.isdigit():
        UNWANTED_INPUTS += bin_number + "\n"
        print(f"{RED}Invalid Bin : must contain only digits")
        return False
    
    if not 6 <= len(card_number) <= 16 or not card_number.startswith(tuple("4563")):
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
    final_number =  card_number + str(checksum)
        # Final length validation
    if card_number.startswith(tuple("456")) and len(final_number) != 16:
        UNWANTED_INPUTS += bin_number + "\n"
        
        return False
    elif card_number.startswith("3") and len(final_number) != 15:
        UNWANTED_INPUTS += bin_number + "\n"
        
        return False
    return final_number

# handling month an year 
def month_year(bin_number):

    #handling with month
    parts = bin_number.split("|")
    bin_month = ""
    bin_year = ""
    if len(parts) < 2 or parts[1] in ["" , "xx"]:

            bin_month = f"{random.randint(1,12):02d}"
    else:
        month = parts[1]
        if month.isdigit() :
            month = int(month)
            if 1 <= month <= 12:
                bin_month = f"{month:02d}"
        else:
            bin_month = f"{random.randint(1,12):02d}"
    
    # handling with year
    if len(parts) >= 3 and parts[2] not in ["" , "xx"]:
        year = parts[2]
        if year.isdigit():
            if len(year) == 2:
                bin_year = f"20{year}"
            elif len(year) == 4:
                bin_year = year
            else:
                bin_year = str(random.randint(CURRENT_YEAR, LEGAL_YEAR))
        else: 
            bin_year = str(random.randint(CURRENT_YEAR, LEGAL_YEAR))
    else:
        bin_year = str(random.randint(CURRENT_YEAR, LEGAL_YEAR))

    return f"{bin_month}|{bin_year}"

# cvv handling 
def cvv(num:str) -> str:
    parts = num.split("|")
    if parts[0].startswith("3"):
        cvv_length = 4
    
    else:       
        cvv_length = 3
    if len(parts) >= 4:
        bin_cvv = ""
        if parts[3] in ["x" , "xx" , "xxx" , "xxxx" ]:
            bin_cvv = "".join(shufling() for _ in range(cvv_length))

        elif parts[3].isdigit():
            bin_cvv = parts[3]
        else:
            bin_cvv = "".join(shufling() for _ in range(cvv_length))
    else:
        bin_cvv = "".join(shufling() for _ in range(cvv_length))
    return bin_cvv
    
# checking the luhn validation
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
def main(number:str): #-path : list or single bin number
    global UNWANTED_INPUTS
    filename = f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')} CCs.txt"
    
    if number :
        amount = input("How many cards default 10 >> ").strip()
        # default amount
        if not amount.isdigit() or amount == "" or int(amount) < 10:
            print(f"{RED}Wrong amount : write correct digit setting default 10")
            amount = 10
 
        amount = int(amount)
        with open(filename , "w") as file:
            # handling with list || file path
            if isinstance(number , list) :
                valid_bins = [] 
                bin_list = number
                for bin in bin_list:
                    card_number = first_num(bin)
                    if card_number and luhn_algo(card_number):
                        valid_bins.append(bin)
                    else:
                        UNWANTED_INPUTS += bin
                if not valid_bins :
                    print(f"{RED}No valid bin found in the file")
                    return 

                for bin_number_parts in valid_bins:
                    generated = 0
                    while generated < amount:
                        first_number = first_num(bin_number_parts)
                        if first_number and luhn_algo(first_number):
                            month_year_bin = month_year(bin_number_parts)
                            cvc = cvv(bin_number_parts)
                            
                            format = f"{first_number}|{month_year_bin}|{cvc}"
                            file.write(format+ "\n")
                            print(f"{RED}{format}")
                            generated  += 1
                    
                if UNWANTED_INPUTS:
                    UNWANTED_INPUTS = list(set(UNWANTED_INPUTS))
                    print(f"{RED}These are wrong inputs \n{UNWANTED_INPUTS}")
                return "done"
            # handling with signle bin
            else:
                generated = 0
                while generated < amount:
                    bin_number_parts = number
                    first_number = first_num(bin_number_parts)
                    if first_number and luhn_algo(first_number):
                        month_year_bin = month_year(bin_number_parts)
                        cvc = cvv(bin_number_parts)
                        
                        format = f"{first_number}|{month_year_bin}|{cvc}"
                        file.write(format+ "\n")
                        print(f"{RED}{format}")
                        generated  += 1
                    else:
                        return False
                return "done"
    else: 
        return False
# this function to ask if keep generating or not 
def keep_going():
    while True:
        func = main(checking())
        if func == "done":

                answer = input("\n\nTo keep generating 'yes' || to exit 'no' >> ").upper()
                if answer == "YES":
                    continue

                elif answer == "NO":
                    print("\033[33m🔻Thank you for using our script :)")

                    break
                else:
                    print("Write yes or no")

        else:   
                    continue


if __name__ == "__main__":
    try : 
        keep_going()
    except KeyboardInterrupt:
        print(f"{RED}\n\n🔴 Exiting...")
