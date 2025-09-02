from __future__ import annotations
import re




def parse_table_block(block: str) -> str:
    lines = [l.strip() for l in block.strip().splitlines() if l.strip()]
    if len(lines) < 2:
        return block


    headers = [h.strip() for h in lines[0].strip('|').split('|')]
    ncols = len(headers)


    rows = []
    for row in lines[2:]:
        cells = [c.strip() for c in row.strip('|').split('|')]
        rows.append(" & ".join(cells) + r" \\")


    latex = [
        r"\begin{tabular}{|" + "c|" * ncols + "}",
        r"\hline",
        " & ".join(headers) + r" \\",
        r"\hline",
        *rows,
        r"\hline",
        r"\end{tabular}",
    ]
    return "\n".join(latex)




def process_tables(md_text: str) -> str:
    table_re = re.compile(r'(?:^\|.+\|\s*\n^\|(?:\s*:?-+:?\s*\|)+\s*\n(?:^\|.+\|\s*\n?)+)', re.MULTILINE)
    return table_re.sub(lambda m: parse_table_block(m.group(0)), md_text)