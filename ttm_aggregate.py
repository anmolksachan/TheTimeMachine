
import sys
import re
from pathlib import Path
from collections import defaultdict

CATEGORIES = {
    "fetch": ["_URLs.txt"],
    "subdomains": ["_subdomain.txt"],
    "backups": ["_backups.txt"],
    "archives": ["_archive.txt"],
    "parameters": ["_parameters.txt"],
    "jwt": ["_jwt.txt"],
    "xss": ["_xss.txt"],
    "sqli": ["_sqli.txt"],
    "lfi": ["_lfi.txt"],
    "redirect": ["_redirect.txt"],
    "jira": ["_jira.txt"],
    "wp": ["_wp.txt"],
    "fuzz": ["_fuzz.txt"],
}

DOMAIN_RE = re.compile(r"^(?=.{1,253}$)(?!-)([a-z0-9-]{1,63}\.)+[a-z]{2,63}$")


def is_under_apex(domain: str, apex: str) -> bool:
    return domain == apex or domain.endswith("." + apex)


def main():
    if len(sys.argv) != 2:
        print("Usage: python ttm_aggregate.py <apex-domain>")
        sys.exit(1)

    apex = sys.argv[1].lower().strip()
    content_dir = Path("content")
    output_dir = Path("output") / apex

    if not content_dir.exists():
        print("[!] content/ directory not found")
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    buckets = defaultdict(set)

    for subdir in content_dir.iterdir():
        if not subdir.is_dir():
            continue

        domain = subdir.name.lower()

        if not DOMAIN_RE.match(domain):
            continue

        if not is_under_apex(domain, apex):
            continue

        for file in subdir.glob("*.txt"):
            for category, suffixes in CATEGORIES.items():
                if any(file.name.endswith(sfx) for sfx in suffixes):
                    for line in file.read_text(errors="ignore").splitlines():
                        line = line.strip()
                        if line:
                            buckets[category].add(f"[{domain}] {line}")


    for category, values in buckets.items():
        if not values:
            continue

        out_file = output_dir / f"{category}_all.txt"
        with out_file.open("w", encoding="utf-8") as f:
            for entry in sorted(values):
                f.write(entry + "\n")

        print(f"[+] Written {out_file} ({len(values)} lines)")

    print(f"\n[✓] Aggregation complete → {output_dir}")

if __name__ == "__main__":
    main()

