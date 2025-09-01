import re
from pathlib import Path
import sys
import urllib.request
import shutil


# Création d'une map pour les callouts (exemple : todo -> activite)
hint_map = {
    "todo": "Manipulation",
    "tip": "infor",
    "info": "infor",
    "warning": "warning",
    "danger": "danger",
    "hint": "infor",
    "question": "idee",
    "attention": "cahierDesCharges"
}

# Regex pour détecter les callouts (hints)
hint_re = re.compile(
    r'^>\s*\[!(\w+)\][-+]?\s?(.*)((?:\n>\s?.*)*)',
    re.MULTILINE | re.IGNORECASE
)

# Regex pour détecter les embeds asciinema
asciinema_re = re.compile(
    r'\[!\[asciicast\]\([^)]+\)\]\(https://asciinema\.org/a/([A-Za-z0-9]+)\)'
)

def process_horizontal_rules(md_text):
    # Détecte --- ou *** seuls sur une ligne (Markdown)
    return re.sub(r'^\s*([-*_]){3,}\s*$', r'\\hrule', md_text, flags=re.MULTILINE)

def remove_header_footer(md_text):
    lines = md_text.splitlines()
    if lines and lines[0].startswith("---"):
        try:
            header_end = lines.index("---", 1)
            lines = lines[header_end + 1:]
        except ValueError:
            pass
    if lines and lines[-1].startswith("---"):
        lines = lines[:-1]
    return "\n".join(lines)

def process_links(md_text):
    return re.sub(
        r'\[([^\]]+)\]\(([^)]+)\)',
        r'\\href{\2}{\1}',
        md_text
    )

def replace_hints(match):
    hint_type = match.group(1).lower()
    title = match.group(2).strip()
    content = match.group(3).strip()
    content = re.sub(r'^>\s?', '', content, flags=re.MULTILINE)
    return f"\\begin{{UPSTI{hint_map.get(hint_type, 'infor')}}}{{{title}}}\n{content}\n\\end{{UPSTI{hint_map.get(hint_type, 'infor')}}}"  

def escape_underscores(md_text):
    parts = re.split(r'(\\begin{lstlisting}.*?\\end{lstlisting})', md_text, flags=re.DOTALL)
    escaped_parts = []
    for part in parts:
        if part.startswith(r'\begin{lstlisting}'):
            escaped_parts.append(part)  # on garde intact
        else:
            #escaped = part.replace('\n', r'\\n')   # d'abord les backslashes
            escaped = part.replace('_', r'\_')
            escaped = escaped.replace('#', r'\#')
            escaped = escaped.replace('\<',r'<')
            escaped = escaped.replace('\>',r'>')
            escaped_parts.append(escaped)
    return ''.join(escaped_parts)


import re

def process_titles(md_text):
    # Séparer code/verbatim du reste
    parts = re.split(r'(```.*?```|\\begin{lstlisting}.*?\\end{lstlisting})', 
                     md_text, flags=re.DOTALL)

    def repl(m):
        level = len(m.group(1))
        text = m.group(2).strip()
        mapping = {
            1: "section",
            2: "subsection",
            3: "subsubsection",
            4: "paragraph",
            5: "subparagraph",
            6: "textbf"
        }
        cmd = mapping.get(level, "section")
        return f"\\{cmd}{{{text}}}"

    processed = []
    for part in parts:
        if part.startswith("```") or part.startswith(r"\begin{lstlisting}"):
            processed.append(part)  # on garde tel quel
        else:
            processed.append(re.sub(r'^(#{1,6})\s*(?:\d\.\s?)?(.*)', repl, part, flags=re.MULTILINE))
    return ''.join(processed)


def process_inline(md_text):
    md_text = re.sub(r'(\*\*|__)(.+?)\1', r'\\textbf{\2}', md_text)
    md_text = re.sub(r'\s(\*|_)(.+?)\1\s', r'\\textit{\2}', md_text)
    md_text = re.sub(r'`([^`]+)`', r'\\texttt{\1}', md_text)
    return md_text

def process_code_blocks(md_text):
    def repl(m):
        lang = m.group(1) if m.group(1) else "bash"
        code = m.group(2)

        # Normaliser les sauts de ligne
        lines = code.splitlines()

        # Supprimer les lignes vides au début/fin
        while lines and lines[0].strip() == "":
            lines.pop(0)
        while lines and lines[-1].strip() == "":
            lines.pop()

        if not lines:
            return f"\\begin{{lstlisting}}[language={lang}]\n\\end{{lstlisting}}"

        # Trouver l'indentation minimale
        indents = [
            len(line) - len(line.lstrip(" "))
            for line in lines if line.strip()
        ]
        min_indent = min(indents) if indents else 0

        # Supprimer cette indentation de toutes les lignes
        dedented = "\n".join(line[min_indent:] for line in lines)

        return (
            f"\\begin{{lstlisting}}[language={lang}"
            f"{',style=console' if lang == 'bash' else ''}]\n"
            f"{dedented}\n"
            "\\end{lstlisting}"
        )

    return re.sub(r'```(\w+)?\n([\s\S]*?)```', repl, md_text)



def detect_list_type(line):
    """Retourne (type, marker, content) ou (None, None, line)"""
    # Case à cocher non cochée
    if re.match(r'^\s*-\s\[ \]\s+', line):
        indent = len(re.match(r'^(\s*)-\s\[ \]\s+', line).group(1))
        content = re.sub(r'^\s*-\s\[ \]\s+', '', line)
        return ("ul", r"\item[$\Box$]", indent, content)

    # Case à cocher cochée
    if re.match(r'^\s*-\s\[x\]\s+', line, flags=re.IGNORECASE):
        indent = len(re.match(r'^(\s*)-\s\[x\]\s+', line, flags=re.IGNORECASE).group(1))
        content = re.sub(r'^\s*-\s\[x\]\s+', '', line, flags=re.IGNORECASE)
        return ("ul", r"\item[$\CheckedBox$]", indent, content)

    # Liste à puce simple
    if re.match(r'^\s*-\s+', line):
        indent = len(re.match(r'^(\s*)-\s+', line).group(1))
        content = re.sub(r'^\s*-\s+', '', line)
        return ("ul", r"\item", indent, content)

    # Liste numérotée
    if re.match(r'^\s*\d+\.\s+', line):
        indent = len(re.match(r'^(\s*)\d+\.\s+', line).group(1))
        content = re.sub(r'^\s*\d+\.\s+', '', line)
        return ("ol", r"\item", indent, content)

    return (None, None, None, line)


def process_lists(md_text):
    lines = md_text.splitlines()
    output = []
    stack = []  # pile de (type, indent)

    for line in lines:
        ltype, marker, indent, content = detect_list_type(line)

        if ltype:  # ligne de liste
            # Fermer les listes trop profondes
            while stack and indent < stack[-1][1]:
                t, _ = stack.pop()
                output.append("\\end{itemize}" if t == "ul" else "\\end{enumerate}")

            # Ouvrir nouvelle liste si nécessaire
            if not stack or indent > stack[-1][1] or ltype != stack[-1][0]:
                output.append("\\begin{itemize}" if ltype == "ul" else "\\begin{enumerate}")
                stack.append((ltype, indent))

            # Ajouter l’item
            output.append(f"{marker} {content}")

        else:  # ligne normale
            # Fermer toutes les listes ouvertes
            while stack:
                t, _ = stack.pop()
                output.append("\\end{itemize}" if t == "ul" else "\\end{enumerate}")
            output.append(line)

    # Fermer à la fin
    while stack:
        t, _ = stack.pop()
        output.append("\\end{itemize}" if t == "ul" else "\\end{enumerate}")

    return "\n".join(output)


def process_images(md_text):
    return re.sub(
        r'!\[([^\]]*)\]\(([^)]+)\)',
        r'\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.8\\textwidth]{\2}\n\\caption{\1}\n\\end{figure}',
        md_text
    )

def process_asciinema(md_text, output_dir):
    def repl(m):
        cast_id = m.group(1)
        console_dir = output_dir / "console"
        console_dir.mkdir(exist_ok=True)
        txt_path = console_dir / f"{cast_id}.txt"
        url = f"https://asciinema.org/a/{cast_id}.txt"
        try:
            urllib.request.urlretrieve(url, txt_path)
            print(f"Téléchargé {url} → {txt_path}")
        except Exception as e:
            print(f"Erreur téléchargement {url}: {e}")
        return f"\\lstinputlisting[language=bash, style=console]{{console/{cast_id}.txt}}"
    return asciinema_re.sub(repl, md_text)


def generate_master_file(output_dir: Path, master_file: str = "main.tex"):
    tex_files = sorted(output_dir.rglob("*.tex"))

    master_path = output_dir / master_file
    with master_path.open("w", encoding="utf-8") as f:
        for file in tex_files:
            rel_path = file.relative_to(output_dir)
            f.write(f"\\input{{{rel_path.as_posix()}}}\n")

    print(f"Fichier maître généré : {master_path}")


def process_file_content(md_text, output_dir):
    md_text = remove_header_footer(md_text)
    md_text = hint_re.sub(replace_hints, md_text)
    md_text = process_asciinema(md_text, output_dir)
    md_text = process_images(md_text)   
    md_text = process_code_blocks(md_text)
    md_text = process_lists(md_text)
    md_text = process_links(md_text)    
    md_text = process_inline(md_text)
    md_text = process_titles(md_text)
    md_text = process_horizontal_rules(md_text)
    md_text = escape_underscores(md_text)
    return md_text

def process_file(file_path, output_dir):
    with open(file_path, 'r', encoding='utf-8') as file:
        md_text = file.read()
    latex_content = process_file_content(md_text, output_dir)
    output_file_path = output_dir / (Path(file_path).stem + ".tex")
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(latex_content)
    print(f"Conversion terminée : {output_file_path}")


def create_root(p : Path, rootName:str, clear = False):
    root = p / rootName
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(exist_ok=True, parents=True)
    return root

def process_path(path: str, root=None, rootName="LaTeX"):
    p = Path(path)

    if p.is_file() and p.suffix == ".md":
        if not root:
            create_root(p.parent, rootName)
        process_file(p, root)
    elif p.is_dir() and p.name != rootName:
        if not root : 
            root = create_root(p, rootName, clear=True)
        else:
            root = create_root(root, p.name, clear=False)
        for child in p.iterdir():
            process_path(child, root, rootName)
    else:
        # motif ou autre
        for md_file in Path().rglob(path):
            if md_file.suffix == ".md":
                process_file(md_file, root)

    print("Conversion Terminée - Dossier : " + str(root))
    return root.absolute()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <file|folder|pattern>")
    else:
        for arg in sys.argv[1:]:
            p = process_path(arg)
            generate_master_file(p)
