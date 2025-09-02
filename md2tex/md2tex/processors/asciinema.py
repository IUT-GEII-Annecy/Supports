from __future__ import annotations
import re
from pathlib import Path
import urllib.request


asciinema_re = re.compile(r"\[!\[asciicast\]\([^)]+\)\]\(https://asciinema\\.org/a/([A-Za-z0-9_-]+)\)")




def process_asciinema(md_text: str, output_dir: Path) -> str:
    def repl(m: re.Match) -> str:
        cast_id = m.group(1)
        console_dir = output_dir / "console"
        console_dir.mkdir(exist_ok=True)
        txt_path = console_dir / f"{cast_id}.txt"
        url = f"https://asciinema.org/a/{cast_id}.txt"
        try:
            urllib.request.urlretrieve(url, txt_path)
            print(f"Téléchargé {url} → {txt_path}")
        except Exception as e: # pragma: no cover (réseau facultatif)
                print(f"Erreur téléchargement {url}: {e}")
        return f"\\lstinputlisting[language=bash, style=console]{{console/{cast_id}.txt}}"
    
    return asciinema_re.sub(repl, md_text)