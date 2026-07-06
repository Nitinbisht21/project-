import random
import string

passwords ={}

try:
    with open("password.txt","r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd

except:
    pass

def generate_password():
    char = string.ascii_letters + string.digits + "@#$%&"
    password = "".join(random.choice(char) for _ in range(8))
    return password

while True:
    print("1. Generate Password")
    print("2. View Passwords")
    print("3. Save Password")
    print("4. Edit Password")
    print("5. Delete Password")
    print("6. Exit")        

    choice = input("Enter your choice: ")

    if choice == "1":
        pwd = generate_password()
        print("Generated password : ",pwd)
        val = input("Enter Y/y to save the password: ")
        if val == "Y" or val == "y":
            site = input("Enter the site name: ")

            passwords[site] = pwd

            with open("password.txt","w") as file:
                file.write(f"{site}:{pwd}\n")

                print("Saved")  
        else :
            exit
            
    
    elif choice == "2":
        if not passwords:
            print("NO Data is available")
        else:
            for site, pwd in passwords.items():
                print(site ,":",pwd)

    elif choice =="3":
        site = input("Enter the site name: ")
        pwd = input("Enter the password: ")

        passwords[site] = pwd

        with open("password.txt","w") as file:
            file.write(f"{site}:{pwd}\n")

            print("Saved")
        

    elif choice == "4":
        site = input("Enter the website name: ")

        if site in passwords:
            pwd = input("Enter the new password: ")
            passwords[site] = pwd

            with open("password.txt", "w") as file:
                for s, p in passwords.items():
                    file.write(f"{s}:{p}\n")

        else:
            print("No data is found")

    elif choice == "5":
        site = input("Enter site name: ")

        if site in passwords:
            del passwords[site]

            with open("password.txt","w") as file:
                for s,p in passwords.items():
                    file.write(f"{s}:{p}\n")
            print("password deleted")

        else:
            print("Website is not found")
 
    elif choice =="6":
        print("OK bye")
        break
