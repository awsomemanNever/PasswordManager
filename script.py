import json
import time
import hashlib
import caeser_cypher_encrypt.py as encrypt
import caeser_cypher_decrypt.py as decrypt
import password-generation.py as generate

with open('.passwords.json') as f:
    passwords = json.load(f)

print("Password file detecting... \n")
time.sleep(2.0)
print("File detected. You may now use the password manager. \n\n")

print("Enter your master password so that I know you are authorized. ")
test_for_master = input(">")

if hashlib.sha256(test_for_master.encode()) == passwords["master"]:
    pass
else:
    print("Unsuccesful. Terminating attempt. Try again. ")
    exit(0)
    
    
def help():
    print("Commands: ")
    print("show - use this to see one of your passwords. ")
    print("add - use this to add another password to the list. ")
    print("exit - exit the password manager. ")
    print("help - will print out this text containing info on all commands. \n")
    
help()

while True:
    choice_of_command = input("Enter a command. \n>")

    if choice_of_command == "show":
        site_to_see = input("Which site's password would you like to see? \n>")
        if site_to_see in passwords:
            print(f"{site_to_see.decrypt.CaeserDecrypt(site_to_see)}'s password: ")
            print(f"{passwords[site_to_see].decrypt.CaeserDecrypt(passwords[site_to_see])}")
        else: 
            print("You don't have any site with that name. ")
            pass

    elif choice_of_command == "add":
        choice = input("Would you like to supplly your own password. If not you will be guided on making a strong password on your specifications (y/n): ")

        if choice == "n":
            new_website_name = input("What is the name of the website you would like to add? \n(Recommendation: don't put the entire website name, just the main part. Ex: \"discord\" instead of \"discord.com\") \n>")
            new_website_password = input("Enter the password for the new website: ")
            new_website_name = new_website_name.encrypt.CaeserEncrypt(new_website_name)
            new_website_password = new_website_password.encrypt.CaeserEncrypt(new_website_password)
            new_website = {f"{new_website_name}": f"{new_website_password}"}
            passwords.update(new_website)

        else: 
            new_website_name = input("What is the name of the website you would like to add? \n(Recommendation: don't put the entire website name, just the main part. Ex: \"discord\" instead of \"discord.com\") \n>")
            length_check = input("Do you want to specify the length? (y/n): ")
            if length_check == "y":
                length = int(input("Enter the length of the password to be generated: "))
            else:
                length = int(random.randrange(4, 16))

            caps_check = input("Do you want capital letters in the password? (y/n): ")
            if caps_check == "y":
                caps = True
            else:
                caps = False
                                                                                    
            number_check = input("do you want numbers in the password? (y/n): ")
            if number_check == "y":
                numbers = True
            else:
                numbers = False
            symbol_check = input("do you want symbols in the password? (y/n): ")
            if number_check == "y":
                symbols = True
            else:
                symbols = False
            new_website_pasword = generate.Password(length, caps, numbers, symbols)
            print("Your password is: " + new_website_password)
            new_website_name = new_website_name.encrypt.CaeserEncrypt(new_website_name)
            new_website_password = new_website_password.encrypt.CaeserEncrypt(new_website_password)
            new_website = {f"{new_website_name}": f"{new_website_password}"}
            passwords.update(new_website)

        with open(".passwords.json", "w") as outfile:
            json.dump(passwords, outfile)

    elif choice_of_command == "exit":
        break

    elif choice_of_command == "help":
        help()

    else:
        print("Couldn't recognize command. Please try again")
