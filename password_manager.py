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
    print("\n----------Password Manager -----------")
    print("1 To generate the password")
    print("2 To view the password")
    print("3 To save password")
    print("3 To edit the password")
    print("4 To Delete the password")
    print("5 Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pwd = generate_password()
        print("Generated password : ",pwd)
        val = input("Enter Y/y to save the password: ")
        if val == "Y"or"y":
            site = input("Enter the site name: ")

            passwords[site] = pwd

            with open("password.txt","a") as file:
                file.wite(f"{site}:{pwd}\n")

                print("Saved")  
        else :
            exit
            
    
    elif choice == "2":
        if not passwords:
            print("NO Data is available")
        else:
            for site, pwd in passwords:
                print(site ,":",pwd)

    elif choice =="3":
        site = input("Enter the site name: ")
        pwd = input("Enter the password: ")

        passwords[site] = pwd

        with open("password.txt","a") as file:
            file.wite(f"{site}:{pwd}\n")

            print("Saved")
        

    elif choice == "4":
        site = input("Enter the website name: ")

        if site in passwords:
            pwd = input("Enter the new password: ")
            passwords[site] = pwd
        else:
            print("No data is found")
 
    elif choice =="5":
        print("OK bye")
        break
