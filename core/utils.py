from termcolor import colored

def load_extensions_from_file(file_path='extensions.txt'):
    default_exts = [".zip", ".tar.gz", ".rar", ".sql", ".bak", ".7z", ".gz"]
    try:
        with open(file_path, 'r') as f:
            extensions = [line.strip() for line in f if line.strip()]
        return extensions
    except FileNotFoundError:
        print(colored(f"[!] {file_path} not found. Using default extensions.", "yellow"))
        return default_exts
