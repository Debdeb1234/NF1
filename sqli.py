# sql.py

import subprocess
import sys
import os

def run_sqlmap(sqlmap_path, url):
    sqlmap_script = os.path.join(sqlmap-master, "sqlmap.py")
    command = f"python {sqlmap_script} -u {url}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sql.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    sqlmap_path = r"C:\NF\sqlmap-master"

    run_sqlmap(sqlmap_path, url)
