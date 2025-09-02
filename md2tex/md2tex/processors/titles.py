from __future__ import annotations
import re




def process_titles(md_text: str) -> str:
    # protéger les blocs de code/lstlisting
    parts = re.split(r'(```.*?```|\\begin{lstlisting}.*?\\end{lstlisting})', md_text, flags=re.DOTALL)


    def repl(m: re.Match) -> str:
        level = len(m.group(1))
        text = m.group(2).strip()
        mapping = {1: "section", 2: "subsection", 3: "subsubsection", 4: "paragraph", 5: "subparagraph", 6: "textbf"}
        cmd = mapping.get(level, "section")
        return f"\\{cmd}{{{text}}}"


    out = []
    for part in parts:
        if part.startswith("```") or part.startswith(r"\begin{lstlisting}"):
            out.append(part)
        else:
            out.append(re.sub(r'^(#{1,6})\s*(?:\d\.\s?)?(.*)', repl, part, flags=re.MULTILINE))
    return ''.join(out)