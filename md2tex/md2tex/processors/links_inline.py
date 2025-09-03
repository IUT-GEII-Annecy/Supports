import re

CODE_SPAN = re.compile(r'`([^`]+)`')

# protège/restaure le code inline `...`
def _protect_code_spans(text: str):
    buckets = []
    def hold(m):
        buckets.append(m.group(0))
        return f"\uFFF0{len(buckets)-1}\uFFF1"
    return CODE_SPAN.sub(hold, text), buckets

def _restore_code_spans(text: str, buckets):
    for i, raw in enumerate(buckets):
        text = text.replace(f"\uFFF0{i}\uFFF1", raw)
    return text

# blocs à ignorer : lstlisting, verbatim, et lstinputlisting (une ligne)
CODE_BLOCK_SPLIT = re.compile(
    r'(\\begin{lstlisting}.*?\\end{lstlisting}'
    r'|\\begin{verbatim}.*?\\end{verbatim}'
    r'|\\lstinputlisting[^\n]*\{[^}]+\}[^\n]*\n?)',
    flags=re.DOTALL
)

def process_links(md_text: str) -> str:
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\\href{\2}{\1}', md_text)

def _process_inline_chunk(chunk: str) -> str:
    # 1) protéger les `code`
    chunk, buckets = _protect_code_spans(chunk)

    # 2) gras
    chunk = re.sub(r'(?<!\\)(\*\*|__)(.+?)\1', r'\\textbf{\2}', chunk)

    # 3) italique (évite _dans_identifiants_)
    italic_re = re.compile(r'(?<!\\)(?<!\w)(\*|_)([^*_].*?)\1(?!\w)', re.DOTALL)
    chunk = italic_re.sub(r'\\textit{\2}', chunk)

    # 4) placeholders <...> → \texttt{<...>} (HORS code seulement)
    chunk = re.sub(r'<([A-Za-z0-9_./\-]+)>', r'\\texttt{<\1>}', chunk)

    # 5) restaurer les codes inline en \texttt{...}
    restored = []
    for raw in buckets:
        if raw.startswith('`') and raw.endswith('`'):
            restored.append(f'\\texttt{{{raw[1:-1]}}}')
        else:
            restored.append(raw)
    chunk = _restore_code_spans(chunk, restored)
    return chunk

def process_inline(md_text: str) -> str:
    parts = CODE_BLOCK_SPLIT.split(md_text)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # C'est un bloc code → on ne touche pas
            out.append(part)
        else:
            out.append(_process_inline_chunk(part))
    return ''.join(out)
