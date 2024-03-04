# main_menu.py

import os

def get_user_input():
    url = input("Enter the URL: ")
    return url.strip()

def xss_attack(url):
    os.system(f"python xss.py {url}")

def sql_injection(url):
    os.system(f"python sqli.py {url}")

def pfsense_attack(url):
    os.system(f"python pfSense.py {url}")

def main():
    while True:
        print("\nMenu:")
        print("1. XSS")
        print("2. SQL")
        print("3. pfSense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            url = get_user_input()
            xss_attack(url)
        elif choice == '2':
            url = get_user_input()
            sql_injection(url)
        elif choice == '3':
            url = get_user_input()
            pfsense_attack(url)
        elif choice == '4':
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
