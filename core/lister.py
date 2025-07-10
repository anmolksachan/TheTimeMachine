# core/lister.py

import requests
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import tempfile
from termcolor import colored


def fetch_wayback_urls(domain):
    url = f"https://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=txt&fl=original&collapse=urlkey"
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        return list(filter(None, r.text.splitlines()))
    except requests.RequestException as e:
        print(colored(f"[!] Failed to fetch from Wayback: {e}", "red"))
        return []


def extract_unique_paths(urls, domain):
    paths = set()
    for url in urls:
        parsed = urlparse(url)
        if parsed.hostname == domain:
            path = parsed.path
            if path and path != "/":
                paths.add(path)
    return sorted(paths)


def check_directory_listing(domain, path):
    patterns = [
        "Index of /", "Parent Directory", "Directory listing", "Last modified", "Name</a>"
    ]
    for scheme in ["http", "https"]:
        full_url = f"{scheme}://{domain}{path}"
        try:
            r = requests.get(full_url, timeout=5)
            if r.status_code == 200:
                if any(p in r.text for p in patterns):
                    return full_url
        except:
            continue
    return None


def scan_for_listings(domain, threads=10):
    print(colored(f"\n[+] Scanning {domain} for open directory listings...", "cyan"))
    urls = fetch_wayback_urls(domain)
    if not urls:
        print(colored("[-] No Wayback URLs found.", "red"))
        return

    paths = extract_unique_paths(urls, domain)
    print(f"[+] Found {len(paths)} unique paths to scan.")

    listings = []
    with ThreadPoolExecutor(max_workers=threads) as exec:
        futures = [exec.submit(check_directory_listing, domain, path) for path in paths]
        for future in as_completed(futures):
            result = future.result()
            if result:
                listings.append(result)
                print(colored(f"[+] Directory Listing Found: {result}", "green"))

    if listings:
        output_dir = f"content/{domain}"
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, f"{domain}_dir_listings.txt")
        with open(path, 'w') as f:
            f.write("\n".join(listings))
        print(colored(f"[+] Listings saved to {path}", "yellow"))
