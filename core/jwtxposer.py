import requests
import re
import jwt
import json
from urllib.parse import urlparse, parse_qs, unquote
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.table import Table

console = Console()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; JWT-Finder/1.0; +https://github.com/yourusername/jwt_finder)"
}
JWT_REGEX = re.compile(r'eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}')
JUICY_FIELDS = ["email", "username", "password", "api_key", "access_token", "session_id", "role", "scope"]


def extract_jwt_from_url(url):
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)

    for key, values in query_params.items():
        for value in values:
            val = unquote(value)
            if re.match(JWT_REGEX, val):
                return val

    # Check raw URL
    decoded_url = unquote(url)
    match = JWT_REGEX.search(decoded_url)
    return match.group(0) if match else None


def check_url_status(url):
    try:
        resp = requests.head(url, headers=HEADERS, allow_redirects=True, timeout=10)
        if resp.status_code in [200, 301, 302]:
            return url
    except requests.exceptions.RequestException:
        return None


def decode_jwt(token):
    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        return decoded
    except jwt.exceptions.DecodeError:
        return None


def analyze_jwt(decoded_data):
    return {k: v for k, v in decoded_data.items() if k in JUICY_FIELDS}


def analyze_jwts_from_urls(urls):
    console.print("[bold cyan][*] Scanning URLs for JWTs...[/bold cyan]")
    jwt_map = {}

    for url in urls:
        token = extract_jwt_from_url(url)
        if token:
            jwt_map[url] = token
            console.print(f"[green][+] JWT Found:[/green] {token}")

    if not jwt_map:
        console.print("[red][-] No JWT tokens found.[/red]")
        return

    console.print(f"[cyan][*] Checking which URLs are live...[/cyan]")
    with ThreadPoolExecutor(max_workers=10) as executor:
        live_urls = list(filter(None, executor.map(check_url_status, jwt_map.keys())))

    if not live_urls:
        console.print("[red][-] No live URLs with JWTs found.[/red]")
        return

    console.print(f"[green][+] {len(live_urls)} live URLs detected.[/green]")

    results = {}
    for url in live_urls:
        token = jwt_map[url]
        decoded = decode_jwt(token)
        if decoded:
            juicy = analyze_jwt(decoded)
            results[url] = {"jwt": token, "decoded": decoded, "juicy": juicy}

    if not results:
        console.print("[yellow][!] No decodable JWTs found.[/yellow]")
        return

    _save_results(results)
    _render_table(results)


def _save_results(results):
    with open("jwt_results.json", "w") as f:
        json.dump(results, f, indent=2)
    console.print("[green][+] Saved results to jwt_results.json[/green]")


def _render_table(results):
    table = Table(title="Extracted JWTs and Juicy Claims")
    table.add_column("URL", style="cyan", no_wrap=True)
    table.add_column("JWT", style="magenta")
    table.add_column("Juicy Fields", style="green")

    for url, data in results.items():
        juicy = json.dumps(data["juicy"], indent=2)
        table.add_row(url, data["jwt"], juicy)

    console.print(table)
