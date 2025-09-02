from __future__ import annotations
import re




CODE_BLOCK_RE = re.compile(r"```(\w+)?\n([\s\S]*?)```", re.MULTILINE)




def _format_listing(lang: str, code: str) -> str:
    lines = code.splitlines()
    while lines and lines[0].strip() == "":
        lines.pop(0)
    while lines and lines[-1].strip() == "":
        lines.pop()
    if not lines:
        return f"\\begin{{lstlisting}}[language={lang}]\n\\end{{lstlisting}}"


    indents = [len(l) - len(l.lstrip(" ")) for l in lines if l.strip()]
    min_indent = min(indents) if indents else 0
    dedented = "\n".join(l[min_indent:] for l in lines)


    style = ",style=console" if lang.lower() == "bash" else ""
    return f"\\begin{{lstlisting}}[language={lang}{style}]\n{dedented}\n\\end{{lstlisting}}"




def process_code_blocks(md_text: str) -> str:
    def repl(m: re.Match) -> str:
        lang = m.group(1) or "bash"
        code = m.group(2)
        return _format_listing(lang, code)

    return CODE_BLOCK_RE.sub(repl, md_text)