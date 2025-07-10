import re
from termcolor import colored

def extract_parameters(urls):
    print(colored("[+] Extracting parameters with URL context...", "cyan"))
    param_regex = re.compile(r'\?([^#]+)')  # match everything after "?" and before "#"

    seen = set()

    for url in urls:
        match = param_regex.search(url)
        if match:
            param_segment = match.group(1)
            param_pairs = [p.split('=')[0] for p in param_segment.split('&') if '=' in p]

            if param_pairs:
                key = tuple(sorted(set(param_pairs)))
                if (key, url) not in seen:
                    seen.add((key, url))
                    param_str = ", ".join(param_pairs)
                    print(f"{colored(param_str, 'yellow')} → {url}")
