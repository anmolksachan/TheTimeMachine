from termcolor import colored
import re

def launch_interactive_menu(urls, target):
    print(colored("\n---- [Select from below options] ----", 'white', 'on_green'))
    print("1: Find /api/ endpoints")
    print("2: Find URLs containing JSON")
    print("3: Find URLs with possible config references")
    print("4: Attack Mode (XSS, LFI, SQLi...)")
    print("5: Show all Wayback URLs")
    print("6: Show subdomains")
    print("7: Custom keyword search")
    print("8: Extract Parameters")
    print("9: Exit")

    while True:
        try:
            choice = int(input("\nEnter a number: "))
        except ValueError:
            print(colored("Enter a valid number!", "red"))
            continue

        if choice == 1:
            find_keyword(urls, "/api/")
        elif choice == 2:
            find_keyword(urls, "json")
        elif choice == 3:
            find_keyword(urls, "conf")
        elif choice == 4:
            mode = input("Enter attack type (xss, sqli, lfi, redirect, jira, wp): ").strip()
            db_path = f"db/{mode}.txt"
            from core.attackmode import run_attack_mode
            run_attack_mode(urls, mode, db_path)
        elif choice == 5:
            for u in urls:
                print(u)
        elif choice == 6:
            from core.subdomains import extract_subdomains_from_urls
            subdomains = extract_subdomains_from_urls(urls)
            for s in subdomains:
                print(s)
        elif choice == 7:
            kw = input("Enter keyword: ").strip()
            find_keyword(urls, kw)
        elif choice == 8:
            from core.parameters import extract_parameters
            extract_parameters(urls)
        elif choice == 9:
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

def find_keyword(urls, keyword):
    print(colored(f"\n[+] Searching for '{keyword}' in URLs...\n", "cyan"))
    matches = [u for u in urls if keyword.lower() in u.lower()]
    for u in matches:
        print(u)
    print(colored(f"\n[+] Found {len(matches)} matches.\n", "green"))
