# thetimemachine.py
import os
import sys
import argparse
from urllib.parse import urlparse
from core import (
    fetcher,
    jwtxposer,
    attackmode,
    backupfinder,
    lister,
    subdomains,
    menu,
)
from core.ui import show_loader, print_banner
from core.utils import load_extensions_from_file
from core.parameters import extract_parameters
from core.lister import scan_for_listings
from core.fetcher import console


def main():
    parser = argparse.ArgumentParser(description='⏳ TheTimeMachine - Wayback Recon Suite')
    parser.add_argument("target", help="Target domain")
    parser.add_argument("--fetch", action="store_true", help="Fetch Wayback URLs")
    parser.add_argument("--jwt", action="store_true", help="Analyze JWTs")
    parser.add_argument("--backups", action="store_true", help="Find exposed backup files")
    parser.add_argument("--subdomains", action="store_true", help="Extract subdomains")
    parser.add_argument("--listings", action="store_true", help="Scan for directory listings (WaybackLister)")
    parser.add_argument("--attack", choices=["xss", "sqli", "lfi", "redirect", "jira", "wp", "fuzz"], help="Run specific attack pattern")
    parser.add_argument("--menu", action="store_true", help="Launch interactive menu")
    parser.add_argument("--parameters", action="store_true", help="Extract GET parameters from URLs")

    # Show usage if no `--` options are provided
    if not any(arg.startswith('--') for arg in sys.argv[1:]):
        parser.print_usage()
        return

    args = parser.parse_args()

    # Extract target using urlparse
    if "://" not in args.target:
        args.target = "//" + args.target
    target = urlparse(args.target).hostname.lower()
    content_dir = f"content/{target}"
    os.makedirs(content_dir, exist_ok=True)

    urls_file = f"{content_dir}/{target}_URLs.txt"
    urls = []

    if args.fetch:
        # Use a spinner for animation
        with console.status("[bold cyan]Contacting archive dimension...[/bold cyan]", spinner="dots"):
            urls, output_path = fetcher.fetch_wayback_urls(target)

        if urls:
            console.print(f"[bold green]URLs successfully written to {output_path}[/bold green]")
    else:
        # Load existing URLs from file
        with open(urls_file) as f:
            urls = [line.strip() for line in f]

    if args.subdomains:
        subdomains_list = subdomains.extract_subdomains_from_urls(urls)
        print(f"[+] Found {len(subdomains_list)} subdomains")
        with open(f"{content_dir}/{target}_subdomain.txt", "w") as f:
            f.write("\n".join(subdomains_list))

    if args.jwt:
        jwtxposer.analyze_jwts_from_urls(urls)

    if args.parameters:
        extract_parameters(urls)

    if args.backups:
        backup_exts = load_extensions_from_file("extensions.txt")
        if not backup_exts:
            print("[!] No extensions loaded. Skipping backup finder.")
        else:
            print(f"[+] Using extensions: {', '.join(backup_exts)}")
            backupfinder.fetch_backup_urls(target, backup_exts)

    if args.listings:
        scan_for_listings(target, threads=10) # You can customize the thread count

    if args.attack:
        result = attackmode.pattern_match_mode(urls_file, args.attack, db_folder="db")
        if result:
            output_file = f"{content_dir}/{target}_{args.attack}.txt"
            fetcher.save_to_file(output_file, result)
            print(f"[+] Saved {len(result)} possible {args.attack.upper()} links to {output_file}")
        else:
            print(f"[-] No possible {args.attack.upper()} links found.")

    if args.menu:
        menu.launch_interactive_menu(urls, target)


if __name__ == "__main__":
    print_banner()
    show_loader()
    main()
