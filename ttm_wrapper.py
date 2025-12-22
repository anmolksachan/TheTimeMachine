#!/usr/bin/env python3
import subprocess
import sys
import re
from pathlib import Path

# =========================
# EXACT TTM PIPELINE
# =========================

PIPELINE = [
    ["--fetch"],
    ["--backups"],
    ["--listings"],
    ["--parameters"],
    ["--jwt"],
    ["--attack", "xss"],
    ["--attack", "sqli"],
    ["--attack", "lfi"],
    ["--attack", "redirect"],
    ["--attack", "jira"],
    ["--attack", "wp"],
    ["--attack", "fuzz"],
    ["--subdomains"],
]

DOMAIN_RE = re.compile(r"^(?=.{1,253}$)(?!-)([a-z0-9-]{1,63}\.)+[a-z]{2,63}$")

# =========================
# HELPERS
# =========================

def normalize(domain: str) -> str:
    domain = domain.strip().lower()
    domain = re.sub(r"^https?://", "", domain)
    return domain.split("/", 1)[0].rstrip(".")

def load_subdomains(path: Path, apex: str):
    results = set()
    for line in path.read_text(errors="ignore").splitlines():
        d = normalize(line)
        if DOMAIN_RE.match(d) and (d == apex or d.endswith("." + apex)):
            results.add(d)
    return sorted(results)

# =========================
# MAIN
# =========================

def main():
    if len(sys.argv) != 3:
        print("Usage: python ttm_wrapper.py <apex-domain> <subdomains.txt>")
        sys.exit(1)

    apex = normalize(sys.argv[1])
    sub_file = Path(sys.argv[2])

    base_dir = Path(__file__).resolve().parent
    ttm_script = base_dir / "thetimemachine.py"

    if not ttm_script.exists():
        print("[!] thetimemachine.py not found in this directory")
        sys.exit(1)

    targets = load_subdomains(sub_file, apex)

    print(f"[+] Apex      : {apex}")
    print(f"[+] Targets   : {len(targets)}")
    print(f"[+] TTM Dir   : {base_dir}")

    for i, target in enumerate(targets, 1):
        print(f"\n==============================")
        print(f"[{i}/{len(targets)}] TARGET → {target}")
        print(f"==============================")

        for step in PIPELINE:
            cmd = ["python", "thetimemachine.py", target] + step
            print("\n[CMD]", " ".join(cmd))
            print("-" * 60)

            # 🔥 LIVE OUTPUT — NOTHING HIDDEN
            subprocess.run(
                cmd,
                cwd=base_dir
            )

    print("\n[✓] All scans completed")
    print("[i] Check ./content/ for raw results")

if __name__ == "__main__":
    main()
