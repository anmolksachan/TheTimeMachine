import requests
import os
import time
from rich.console import Console

console = Console()

HEADERS = {
    "User-Agent": "WaybackFetcher/1.0 (https://github.com/Fr13ND0x7f/TheTimeMachine )"
}

WAYBACK_URL = (
    "https://web.archive.org/cdx/search/cdx?url=*.{target}/*&output=txt&fl=original&collapse=urlkey&page=/"
)

def fetch_wayback_urls(target, retries=3, delay=5):
    """
    Fetch archived URLs from the Wayback Machine for a target domain.
    Returns the list of URLs and the output path.
    """
    url = WAYBACK_URL.format(target=target)
    attempt = 0
    url_list = []  # Collect URLs in memory

    console.print(f"\n[bold cyan]Fetching Wayback URLs for [green]{target}[/green][/bold cyan]")

    while attempt < retries:
        try:
            with requests.get(url, headers=HEADERS, timeout=60, stream=True) as response:
                if response.status_code == 200:
                    output_path = f"content/{target}/{target}_URLs.txt"
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)

                    total = 0
                    with open(output_path, "w", encoding="utf-8") as f:
                        for line in response.iter_lines(decode_unicode=False):
                            try:
                                decoded_line = line.decode("utf-8").strip()
                                if decoded_line:
                                    f.write(decoded_line + "\n")
                                    url_list.append(decoded_line)  # Collect URLs
                                    total += 1
                                    if total % 5000 == 0:
                                        console.print(f"[yellow]{total} URLs fetched...[/yellow]")
                            except UnicodeDecodeError:
                                console.print("[red]Skipping invalid line due to decoding error[/red]")

                    console.print(f"[bold green]Retrieved {total} URLs and saved to {output_path}[/bold green]")
                    return url_list, output_path  # Return both list and path
                else:
                    console.print(f"[red]Received status code {response.status_code} from Wayback[/red]")

        except requests.RequestException as e:
            console.print(f"[red]Request Error:[/red] {e}")

        attempt += 1
        console.print(f"[yellow]Retrying in {delay} seconds... (Attempt {attempt}/{retries})[/yellow]")
        time.sleep(delay)

    console.print("[bold red]Failed to fetch Wayback URLs after multiple attempts.[/bold red]")
    return [], None


def save_to_file(filename, url_list):
    """
    Save a list of URLs to a file. Validates input to prevent string writes.
    """
    if not isinstance(url_list, list):
        raise ValueError("url_list must be a list of URLs, not a single string")

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(url_list))

    console.print(f"[cyan] Saved {len(url_list)} URLs to [bold]{filename}[/bold][/cyan]")
