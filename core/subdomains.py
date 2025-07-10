import re
from termcolor import colored

def extract_subdomains_from_urls(urls, root_domain=None):
    """
    Extract unique subdomains from a list of URLs.

    :param urls: List of URLs
    :param root_domain: If provided, filters only subdomains of this root (e.g., example.com)
    :return: List of unique subdomains
    """
    seen = set()
    subdomains = []

    for url in urls:
        match = re.search(r"https?://([a-zA-Z0-9.-]+)", url)
        if match:
            domain = match.group(1).lower().split(':')[0]  # remove port if present
            if domain not in seen:
                if root_domain and not domain.endswith(root_domain):
                    continue  # skip unrelated domains
                seen.add(domain)
                subdomains.append(domain)
                print(colored(f"[subdomain] {domain}", "cyan"))

    print(colored(f"\n[+] Total Unique Subdomains Found: {len(subdomains)}", "green"))
    return subdomains
