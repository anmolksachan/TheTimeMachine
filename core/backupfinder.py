# core/backupfinder.py

import os
import requests
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def fetch_backup_urls(target, extensions):
    console.print(f"\n[bold cyan] Finding backup files for [green]{target}[/green]...[/bold cyan]")

    archive_url = f'https://web.archive.org/cdx/search/cdx?url=*.{target}/*&output=txt&fl=original&collapse=urlkey&page=/'

    urls = []
    filtered = {ext: [] for ext in extensions}

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("[yellow]Fetching Wayback URLs...", start=False)
        try:
            progress.start_task(task)
            response = requests.get(archive_url, timeout=60)
            response.raise_for_status()
            urls = response.text.splitlines()
            for url in urls:
                for ext in extensions:
                    if url.lower().endswith(ext.lower()):
                        filtered[ext].append(url)
        except Exception as e:
            console.print(f"[red] Failed to fetch archive data:[/red] {e}")
            return []
    
    output_dir = f"content/{target}"
    os.makedirs(output_dir, exist_ok=True)

    all_urls = []
    for ext, ext_urls in filtered.items():
        if ext_urls:
            path = os.path.join(output_dir, f"{target}_{ext.strip('.')}_backups.txt")
            with open(path, 'w') as f:
                f.write("\n".join(ext_urls))
            console.print(f"[green] {len(ext_urls)} backup URLs found with extension .{ext.strip('.')} →[/green] [cyan]{path}[/cyan]")
            all_urls.extend(ext_urls)

    if not all_urls:
        console.print(f"[bold yellow] No backup files found for {target}[/bold yellow]")

    return all_urls

