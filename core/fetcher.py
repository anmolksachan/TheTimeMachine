# core/fetcher.py

import requests
import os
import time
from rich.console import Console
from rich.progress import track
from rich import box
from rich.table import Table

console = Console()

HEADERS = {
    "User-Agent": "WaybackFetcher/1.0 (https://github.com/Fr13ND0x7f/TheTimeMachine)"
}

WAYBACK_URL = (
    "https://web.archive.org/cdx/search/cdx?url=*.{target}/*&output=txt&fl=original&collapse=urlkey&page=/"
)

def fetch_wayback_urls(target, retries=3, delay=5):
    """
    Fetch archived URLs from the Wayback Machine for a target domain.
    """
    url = WAYBACK_URL.format(target=target)
    attempt = 0

    console.print(f"\n[bold cyan]Fetching Wayback URLs for [green]{target}[/green][/bold cyan]")

    while attempt < retries:
        try:
            with requests.get(url, headers=HEADERS, timeout=60, stream=True) as response:
                if response.status_code == 200:
                    output_path = f"content/{target}/{target}_URLs.txt"
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)

                    total = 0
                    with open(output_path, "w", encoding="utf-8") as f:
                        for line in response.iter_lines(decode_unicode=True):
                            if line:
                                f.write(line + "\n")
                                total += 1
                                if total % 5000 == 0:
                                    console.print(f"[yellow]{total} URLs fetched...[/yellow]")

                    console.print(f"[bold green]Retrieved {total} URLs and saved to {output_path}[/bold green]")
                    return output_path
                else:
                    console.print(f"[red]Received status code {response.status_code} from Wayback[/red]")

        except requests.RequestException as e:
            console.print(f"[red]Request Error:[/red] {e}")

        attempt += 1
        console.print(f"[yellow]Retrying in {delay} seconds... (Attempt {attempt}/{retries})[/yellow]")
        time.sleep(delay)

    console.print("[bold red]Failed to fetch Wayback URLs after multiple attempts.[/bold red]")
    return None


def save_to_file(filename, url_list):
    """
    Save a list of URLs to a file.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(url_list))

    console.print(f"[cyan] Saved {len(url_list)} URLs to [bold]{filename}[/bold][/cyan]")

