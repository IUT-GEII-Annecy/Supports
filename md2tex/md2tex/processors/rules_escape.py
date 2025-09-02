from __future__ import annotations
import re


def process_horizontal_rules(md_text: str) -> str:
    return re.sub(r'^\s*([-*_]){3,}\s*$', r'\\hrule', md_text, flags=re.MULTILINE)


def remove_header_footer(md_text: str) -> str:
    lines = md_text.splitlines()
    if lines and lines[0].startswith("---"):
        try:
            header_end = lines.index("---", 1)
            lines = lines[header_end + 1 :]
        except ValueError:
            pass
    if lines and lines[-1].startswith("---"):
        lines = lines[:-1]
    return "\n".join(lines)


def escape_underscores(md_text: str) -> str:
# Ne pas échapper à l'intérieur des blocs lstlisting
    parts = re.split(r'(\\begin{lstlisting}.*?\\end{lstlisting})', md_text, flags=re.DOTALL)
    escaped_parts = []
    for part in parts:
        if part.startswith(r'\begin{lstlisting}'):
            escaped_parts.append(part)
        else:
            escaped = part.replace('_', r'\_')
            escaped = escaped.replace('%', r'\%')
            escaped = escaped.replace('#', r'\#')
            # On ne modifie pas < >, ils sont valides en LaTeX hors mode math
            escaped_parts.append(escaped)
    return ''.join(escaped_parts)