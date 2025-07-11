import os
import time
import random
import requests
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

# Configuration
REQUEST_DELAY = 1.5         # Base delay between requests (seconds)
MAX_RETRIES = 3             # Max retries for failed requests
JITTER_RANGE = (0.2, 0.8)   # Random jitter added to delay
RATE_LIMIT_PAUSE = 300     # 5-minute pause on rate limit (429)

def random_delay():
    """Add randomized delay with jitter"""
    delay = REQUEST_DELAY + random.uniform(*JITTER_RANGE)
    time.sleep(delay)

def retry_request(url, timeout=30, max_retries=MAX_RETRIES):
    """Retry logic with exponential backoff and rate limit detection"""
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 429:
                console.print("[yellow]⚠️ Rate limit hit. Pausing for 5 minutes...[/yellow]")
                time.sleep(RATE_LIMIT_PAUSE)
                continue
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            retries += 1
            if retries < max_retries:
                wait = REQUEST_DELAY * (2 ** retries)  # Exponential backoff
                console.print(f"[yellow]⚠️ Request failed: {e}. Retrying in {wait:.1f}s...[/yellow]")
                time.sleep(wait)
            else:
                console.print(f"[red]❌ Failed after {max_retries} retries: {e}[/red]")
                return None
    return None

def fetch_backup_urls(target, extensions):
    console.print(f"\n[bold cyan]🔍 Finding backup files for [green]{target}[/green]...[/bold cyan]")

    archive_url = f'https://web.archive.org/cdx/search/cdx?url=*.{target}/*&output=txt&fl=original&collapse=urlkey&page=/'

    urls = []
    filtered = {ext: [] for ext in extensions}

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("[yellow]📡 Fetching Wayback URLs...", start=False)
        try:
            progress.start_task(task)
            response = retry_request(archive_url, timeout=60)
            if response:
                urls = response.text.splitlines()
                for url in urls:
                    for ext in extensions:
                        if url.lower().endswith(ext.lower()):
                            filtered[ext].append(url)
                            random_delay()  # Delay after each match
        except Exception as e:
            console.print(f"[red]❌ Failed to fetch archive data: {e}[/red]")
            return []

    output_dir = f"content/{target}"
    os.makedirs(output_dir, exist_ok=True)

    def get_snapshot(url):
        wayback_url = f' https://archive.org/wayback/available?url={url}'
        response = retry_request(wayback_url, timeout=30)
        if response:
            try:
                data = response.json()
                if "archived_snapshots" in data and "closest" in data["archived_snapshots"]:
                    return data["archived_snapshots"]["closest"].get("url")
            except ValueError:
                console.print(f"[red]❌ Failed to parse JSON for {url}[/red]")
        return None

    all_urls = []

    for ext, ext_urls in filtered.items():
        if ext_urls:
            # File paths
            backup_path = os.path.join(output_dir, f"{target}_{ext.strip('.').lower()}_backups.txt")
            archive_path = os.path.join(output_dir, f"{target}_{ext.strip('.').lower()}_archive.txt")

            # Separate lists
            original_urls = []
            archive_urls = []

            console.print(f"[yellow]🔎 Checking snapshots for .{ext.strip('.')} files...[/yellow]")

            for url in ext_urls:
                original_urls.append(url)
                snapshot = get_snapshot(url)
                if snapshot:
                    archive_urls.append(snapshot)
                random_delay()  # Delay between snapshot checks

            # Write original URLs
            with open(backup_path, 'w') as f:
                f.write("\n".join(original_urls))
            console.print(f"[green]📄 {len(original_urls)} backup URLs (.{ext.strip('.').lower()}) →[/green] [cyan]{backup_path}[/cyan]")

            # Write archive URLs (if any)
            if archive_urls:
                with open(archive_path, 'w') as f:
                    f.write("\n".join(archive_urls))
                console.print(f"[blue]📦 {len(archive_urls)} archive URLs (.{ext.strip('.').lower()}) →[/blue] [cyan]{archive_path}[/cyan]")

            all_urls.extend(original_urls)

    if not all_urls:
        console.print(f"[bold yellow]🚫 No backup files found for {target}[/bold yellow]")

    return all_urls
