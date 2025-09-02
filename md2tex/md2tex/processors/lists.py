from __future__ import annotations
import re

def detect_list_type(line: str):
    # Case à cocher non cochée
    m = re.match(r'^\s*-\s\[ \]\s+', line)
    if m:
        indent = len(m.group(0)) - len(m.group(0).lstrip())
        content = re.sub(r'^\s*-\s\[ \]\s+', '', line)
        return ("ul", r"\item[$\Box$]", indent, content)

    # Case cochée
    m = re.match(r'^\s*-\s\[x\]\s+', line, flags=re.IGNORECASE)
    if m:
        indent = len(m.group(0)) - len(m.group(0).lstrip())
        content = re.sub(r'^\s*-\s\[x\]\s+', '', line, flags=re.IGNORECASE)
        return ("ul", r"\item[$\CheckedBox$]", indent, content)

    # Puces simples
    m = re.match(r'^\s*-\s+', line)
    if m:
        indent = len(m.group(0)) - len(m.group(0).lstrip())
        content = re.sub(r'^\s*-\s+', '', line)
        return ("ul", r"\item", indent, content)

    # Listes numérotées
    m = re.match(r'^\s*\d+\.\s+', line)
    if m:
        indent = len(m.group(0)) - len(m.group(0).lstrip())
        content = re.sub(r'^\s*\d+\.\s+', '', line)
        return ("ol", r"\item", indent, content)

    return (None, None, None, line)


def process_lists(md_text: str) -> str:
    lines = md_text.splitlines()
    output = []
    stack: list[tuple[str, int]] = []  # (type, indent)
    in_codeblock = False

    for line in lines:
        # Détection des délimiteurs de bloc de code
        if line.strip().startswith("```"):
            in_codeblock = not in_codeblock
            output.append(line)
            continue

        ltype, marker, indent, content = detect_list_type(line)

        if ltype:
            # Fermer les listes trop profondes
            while stack and indent < stack[-1][1]:
                t, _ = stack.pop()
                output.append("\\end{itemize}" if t == "ul" else "\\end{enumerate}")

            # Ouvrir une nouvelle liste si nécessaire
            if not stack or indent > stack[-1][1] or ltype != stack[-1][0]:
                output.append("\\begin{itemize}" if ltype == "ul" else "\\begin{enumerate}")
                stack.append((ltype, indent))

            # Ajouter l’item
            output.append(f"{marker} {content}")

        else:
            if stack and not in_codeblock:
                # Ligne normale hors code → on ferme les listes
                while stack:
                    t, _ = stack.pop()
                    output.append("\\end{itemize}" if t == "ul" else "\\end{enumerate}")
            output.append(line)

    # Fermer ce qui reste ouvert
    while stack:
        t, _ = stack.pop()
        output.append("\\end{itemize}" if t == "ul" else "\\end{enumerate}")

    return "\n".join(output)
