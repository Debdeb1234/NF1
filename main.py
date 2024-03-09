import subprocess

def show_menu():
    print("Menu:")
    print("1. Headers")
    print("2. XSS")
    print("3. Check for SQL Injection (Using sqlmap)")
    print("4. Quit")

def execute_headers_script():
    try:
        subprocess.run(["python", "headers.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing headers.py: {e}")
    except FileNotFoundError:
        print("headers.py not found in the same directory.")

def execute_xss_script():
    xss_script = "/Users/danny/Website-Vulnerability-Scanner-main/PwnXSS/pwnxss.py"  # Full path to the pwnxss.py script
    xss_command = ["python3", xss_script]

    try:
        xss_process = subprocess.Popen(xss_command)
        xss_process.wait()  # Wait for the process to terminate
    except FileNotFoundError:
        print("pwnxss.py not found in the specified directory.")
    except KeyboardInterrupt:
        print("Execution interrupted.")





def execute_sqlmap_script(url, sqlmap_command):
    try:
        subprocess.run(sqlmap_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing sqlmap command: {e}")

def check_xss():
    execute_xss_script()

def select_sqlmap_command():
    while True:
        print("SQLMap Command Menu:")
        print("1. Using a proxy")
        print("2. Basic authentication")
        print("3. Default")
        print("4. Go back to the main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            target_url = input("Enter the target server URL: ")
            proxy_address = input("Enter the proxy address (e.g., http://proxy_address:port): ")
            sqlmap_command = [
                "C:/Python311/python.exe", "sqlmap/sqlmap.py", "-u", target_url, "--proxy", proxy_address, "--batch"
            ]
            execute_sqlmap_script(target_url, sqlmap_command)
        elif choice == '2':
            target_url = input("Enter the target server URL: ")
            param1 = input("Enter param1 value: ")
            param2 = input("Enter param2 value: ")
            username = input("Enter the basic auth username: ")
            password = input("Enter the basic auth password: ")
            sqlmap_command = [
                "C:/Python311/python.exe", "sqlmap/sqlmap.py", "-u", target_url, "-data=param1={}&param2={}".format(param1, param2),
                "-p", "param1", "--auth-type", "basic", "--auth-cred", "{}:{}".format(username, password), "--batch"
            ]
            execute_sqlmap_script(target_url, sqlmap_command)
        elif choice == '3':
            target_url = input("Enter the target server URL: ")
            sqlmap_command = [
                "C:/Python311/python.exe", "sqlmap/sqlmap.py", "-u", target_url, "--batch"
            ]
            execute_sqlmap_script(target_url, sqlmap_command)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def check_sql_injection():
    select_sqlmap_command()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        execute_headers_script()
    elif choice == '2':
        check_xss()
    elif choice == '3':
        check_sql_injection()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
