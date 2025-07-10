import os
import re
from termcolor import colored

def load_patterns(file_path):
    try:
        with open(file_path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(colored(f"[!] Pattern file not found: {file_path}", "red"))
        return []

def pattern_match_mode(urls_file, mode, db_folder="db", output_folder="content"):
    db_map = {
        "xss": "xss.txt",
        "sqli": "sqli.txt",
        "lfi": "lfi.txt",
        "redirect": "openredirect.txt",
        "jira": "jira.txt",
        "wp": "wp-fuzz.txt",
        "fuzz": "fuzz.txt"
    }

    if mode not in db_map:
        print(colored(f"[-] Unsupported mode: {mode}", "red"))
        return

    pattern_file = os.path.join(db_folder, db_map[mode])
    patterns = load_patterns(pattern_file)
    if not patterns:
        print(colored(f"[-] No patterns loaded for mode: {mode}", "yellow"))
        return

    print(colored(f"[~] Scanning {urls_file} for {mode.upper()} patterns...\n", "cyan"))
    domain = os.path.basename(urls_file).split("_")[0]
    output_path = os.path.join(output_folder, domain, f"{domain}_{mode}.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    matched = []
    with open(urls_file, "r") as f:
        for line in f:
            url = line.strip()
            for pattern in patterns:
                if pattern in url:
                    print(colored(f"[+] Flagged: {url}", "green"))
                    matched.append(url + "\n")
                    break

    if matched:
        with open(output_path, "w") as out:
            out.writelines(matched)
        print(colored(f"\n[!] {len(matched)} URLs matched for {mode.upper()} — saved to {output_path}", "blue"))
    else:
        print(colored(f"\n[-] No matches found for {mode.upper()}.", "yellow"))

    return matched
