import re

def _norm_cell(cell: str) -> str:
    # 1) trim
    cell = cell.strip()
    # 2) <br> → \\ (toutes variantes)
    cell = re.sub(r'<br\s*/?>', r'\\\\', cell, flags=re.IGNORECASE)
    # 3) symbole π → $\pi$ (utile dans les énoncés)
    cell = cell.replace('π', r'$\pi$')
    # 4) si la cellule contient un saut de ligne LaTeX, on utilise \makecell
    if r'\\' in cell:
        return r'\makecell[tl]{' + cell + '}'
    return cell

def parse_table_block(block: str) -> str:
    """Convertit un bloc de tableau Markdown en tableau LaTeX."""
    lines = [l.strip() for l in block.strip().splitlines() if l.strip()]
    if len(lines) < 2:
        return block

    headers = [h.strip() for h in lines[0].strip('|').split('|')]
    ncols = len(headers)

    # lignes de données (on saute la ligne de séparation)
    rows = []
    for row in lines[2:]:
        cells = [ _norm_cell(c) for c in row.strip('|').split('|') ]
        rows.append(" & ".join(cells) + r" \\")

    # en-têtes normalisés (gèrent aussi <br>)
    headers = [ _norm_cell(h) for h in headers ]

    latex = []
    latex.append(r"\begin{center}")
    latex.append(r"\begin{tabular}{|" + "l|"*ncols + "}") # type: ignore
    latex.append(r"\hline")
    latex.append(" & ".join(headers) + r" \\")
    latex.append(r"\hline")
    latex.extend(rows)
    latex.append(r"\hline")
    latex.append(r"\end{tabular}")
    latex.append(r"\end{center}" + "\n")
    return "\n".join(latex)





def process_tables(md_text: str) -> str:
    table_re = re.compile(r'(?:^\|.+\|\s*\n^\|(?:\s*:?-+:?\s*\|)+\s*\n(?:^\|.+\|\s*\n?)+)', re.MULTILINE)
    return table_re.sub(lambda m: parse_table_block(m.group(0)), md_text)