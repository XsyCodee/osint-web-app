import os
import subprocess
from prettytable import PrettyTable

def run_sherlock(username):
    print(f"\nSearching Username '{username}' on social media ...\n")
    try:
        result = subprocess.run(
            ["sherlock", username, "--print-found"],
            capture_output=True,
            text=True
        )
        return result.stdout if result.stdout else "Tidak ditemukan."
    except Exception as e:
        return f"Error: {str(e)}"

def run_holehe(email):
    print(f"\nSearching Email '{email}' on website ...\n")
    try:
        result = subprocess.run(
            ["holehe", email],
            capture_output=True,
            text=True
        )
        return result.stdout if result.stdout else "Tidak ditemukan."
    except Exception as e:
        return f"Error: {str(e)}"

def run_theharvester(domain):
    print(f"\nSearching information for domain '{domain}' ...\n")
    try:
        result = subprocess.run(
            ["python", "theHarvester.py", "-d", domain, "-b", "all"],
            capture_output=True,
            text=True,
            cwd="theHarvester"
        )
        return result.stdout if result.stdout else "Tidak ditemukan."
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("""
    =====================================================================================
                              OSINT All-In-One Tool
                              created by Im-xsyyy
                              ig/telegram: @sephvieraaaaaa

                              donation: 
                              usdt/bnb : 0xc260b410f8296c81ee39c143e559444a183e3d3c
     ======================================================================================
          """)
    print("\nChoose Tools:")
    print("1. Username")
    print("2. Email")
    print("3. Domain")

    choice = input("\nPilihan (1/2/3): ").strip()
    
    if choice == "1":
        username = input("\nFill Username: ").strip()
        result = run_sherlock(username)
    elif choice == "2":
        email = input("\nFill Email: ").strip()
        result = run_holehe(email)
    elif choice == "3":
        domain = input("\nFill Domain: ").strip()
        result = run_theharvester(domain)
    else:
        print("\nPilihan tidak valid.")
        return

    table = PrettyTable()
    table.field_names = ["Query", "Result"]
    table.add_row(["Hasil", result])  # Menampilkan maksimal 500 karakter
    print(table)

if __name__ == "__main__":
    main()
