import re
from pathlib import Path
import sys
# Création d'une map pour les callouts (exemple : todo -> activite)
hint_map = {
    "todo": "Manipulation",
    "tip": "infor",
    "info": "infor",
    "warning": "warning",
    "danger": "danger",
    "hint": "infor",
    "question": "idee"
}

# Regex pour détecter les callouts (hints)
hint_re = re.compile(
    r'^>\s*\[!(\w+)\][-+]?\s?(.*)((?:\n>\s?.*)*)',
    re.MULTILINE | re.IGNORECASE
)


def remove_header_footer(md_text):
    """Supprime le YAML header (--- ... ---) et footer éventuel."""
    lines = md_text.splitlines()

    # Supprimer header YAML
    if lines and lines[0].startswith("---"):
        try:
            header_end = lines.index("---", 1)
            lines = lines[header_end + 1:]
        except ValueError:
            pass

    # Supprimer footer YAML
    if lines and lines[-1].startswith("---"):
        lines = lines[:-1]

    return "\n".join(lines)

def process_links(md_text):
    """Convertit les liens Markdown en LaTeX."""
    return re.sub(
        r'\[([^\]]+)\]\(([^)]+)\)',
        r'\\href{\2}{\1}',
        md_text
    )

def replace_hints(match):
    """Convertit un bloc callout Obsidian en environnement LaTeX UPSTI."""
    hint_type = match.group(1).lower()
    title = match.group(2).strip()
    content = match.group(3).strip()
    content = re.sub(r'^>\s?', '', content, flags=re.MULTILINE)

    return f"\\begin{{UPSTI{hint_map.get(hint_type, 'hint')}}}{{{title}}}\n{content}\n\\end{{UPSTI{hint_map.get(hint_type, 'infor')}}}"  


def process_titles(md_text):
    """Convertit titres Markdown (#, ##, ###…) en LaTeX section/subsection…"""
    def repl(m):
        level = len(m.group(1))
        text = m.group(2).strip()
        mapping = {
            1: "section",
            2: "subsection",
            3: "subsubsection",
            4: "paragraph",
            5: "subparagraph",
            6: "textbf"  # on force gras si titre trop petit
        }
        cmd = mapping.get(level, "section")
        return f"\\{cmd}{{{text}}}"

    return re.sub(r'^(#{1,6})\s*(?:\d\.\s?)?(.*)', repl, md_text, flags=re.MULTILINE)


def process_inline(md_text):
    """Traite gras/italique + code inline."""
    # Gras : **...** ou __...__
    md_text = re.sub(r'(\*\*|__)(.+?)\1', r'\\textbf{\2}', md_text)
    # Italique : *...* ou _..._
    md_text = re.sub(r'\s(\*|_)(.+?)\1\s', r'\\textit{\2}', md_text)
    # Code inline : `...`
    md_text = re.sub(r'`([^`]+)`', r'\\texttt{\1}', md_text)
    return md_text


def process_code_blocks(md_text):
    """Transforme ``` en environnement verbatim."""
    return re.sub(
        r'```([\s\S]*?)```',
        lambda m: f"\\begin{{verbatim}}\n{m.group(1).strip()}\n\\end{{verbatim}}",
        md_text
    )


def process_lists(md_text):
    """Convertit listes Markdown en itemize/enumerate."""
    lines = md_text.splitlines()
    output = []
    in_ul, in_ol = False, False

    for line in lines:
        if re.match(r'^\s*-\s\[.\]\s+|^\s*-\s+', line):
            if not in_ul:
                output.append("\\begin{itemize}")
                in_ul = True
            output.append(re.sub(r'^\s*-\s\[.\]\s+|^\s*-\s+', r'\\item ', line))
        elif re.match(r'^\s*\d+\.\s+', line):
            if not in_ol:
                output.append("\\begin{enumerate}")
                in_ol = True
            output.append(re.sub(r'^\s*\d+\.\s+', r'\\item ', line))
        else:
            if in_ul:
                output.append("\\end{itemize}")
                in_ul = False
            if in_ol:
                output.append("\\end{enumerate}")
                in_ol = False
            output.append(line)

    if in_ul:
        output.append("\\end{itemize}")
    if in_ol:
        output.append("\\end{enumerate}")

    return "\n".join(output)

def process_images(md_text):
    """Convertit les images Markdown en environnement LaTeX."""
    return re.sub(
        r'!\[([^\]]*)\]\(([^)]+)\)',
        r'\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.8\\textwidth]{\2}\n\\caption{\1}\n\\end{figure}',
        md_text
    )   

def process_file_content(md_text):
    md_text = remove_header_footer(md_text)
    md_text = hint_re.sub(replace_hints, md_text)
    md_text = process_images(md_text)   
    md_text = process_code_blocks(md_text)
    md_text = process_lists(md_text)
    md_text = process_links(md_text)    
    md_text = process_inline(md_text)
    md_text = process_titles(md_text)
    return md_text


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        md_text = file.read()

    latex_content = process_file_content(md_text)

    # Sauvegarde le fichier LaTex dans un dossier LaTeX
    output_dir = Path(file_path).parent / "LaTeX"
    output_dir.mkdir(exist_ok=True)
    output_file_path = output_dir / (Path(file_path).stem + ".tex")
    



    output_file_path
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(latex_content)

    print(f"Conversion terminée : {output_file_path}")


def process_path(path: str):
    p = Path(path)

    if p.is_file() and p.suffix == ".md":
        # Cas 1 : un fichier md spécifique
        process_file(p)

    elif p.is_dir():
        # Cas 2 : un dossier → on parcourt récursivement
        for md_file in p.rglob("*.md"):
            process_file(md_file)

    else:
        # Cas 3 : motif de type "*.md"
        for md_file in Path().rglob(path):
            if md_file.suffix == ".md":
                process_file(md_file)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <file|folder|pattern>")
    else:
        for arg in sys.argv[1:]:
            process_path(arg)
