import re

# --- Protège le code inline `...` pour éviter toute mise en forme pendant les remplacements
CODE_SPAN = re.compile(r'`([^`]+)`')

def _protect_code_spans(text: str):
    buckets = []
    def hold(m):
        buckets.append(m.group(0))  # on stocke le backticked tel quel
        return f"\uFFF0{len(buckets)-1}\uFFF1"
    return CODE_SPAN.sub(hold, text), buckets

def _restore_code_spans(text: str, buckets):
    for i, raw in enumerate(buckets):
        text = text.replace(f"\uFFF0{i}\uFFF1", raw)
    return text

# --- Blocs à ignorer pour tout le traitement inline
CODE_BLOCK_SPLIT = re.compile(
    r'(\\begin{lstlisting}.*?\\end{lstlisting}'
    r'|\\begin{verbatim}.*?\\end{verbatim}'
    r'|\\lstinputlisting[^\n]*\{[^}]+\}[^\n]*\n?)',
    flags=re.DOTALL
)

def process_links(md_text: str) -> str:
    # [texte](url) → \href{url}{texte}
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\\href{\2}{\1}', md_text)

def _process_inline_chunk(chunk: str) -> str:
    # 1) protéger le code inline
    chunk, buckets = _protect_code_spans(chunk)

    # 2) gras
    chunk = re.sub(r'(?<!\\)(\*\*|__)(.+?)\1', r'\\textbf{\2}', chunk)

    # 3) italique (évite _dans_identifiants_)
    italic_re = re.compile(r'(?<!\\)(?<!\w)(\*|_)([^*_].*?)\1(?!\w)', re.DOTALL)
    chunk = italic_re.sub(r'\\textit{\2}', chunk)

    # 4) exposants simples a^b → $a^{b}$ (hors code)
    chunk = re.sub(r'(\b[0-9A-Za-z]+)\^([0-9A-Za-z]+)\b', r'$\1^{\2}$', chunk)

    # 5) placeholders <...> → \texttt{<...>}
    chunk = re.sub(r'<([A-Za-z0-9_./\-]+)>', r'\\texttt{<\1>}', chunk)

    # 6) restaurer le code inline protégé (avec échappement \)
    restored = []
    for raw in buckets:
        if raw.startswith('`') and raw.endswith('`'):
            content = raw[1:-1]
            # échappement des caractères LaTeX dangereux dans \texttt
            content = content.replace('\|', r'\textbar ')
            content = content.replace('\\', r'\textbackslash ')
            content = content.replace('{', r'\{').replace('}', r'\}')
            content = content.replace('%', r'\%').replace('&', r'\&')
            content = content.replace('$', r'\$').replace('#', r'\#')
            
            restored.append(r'\texttt{' + content + '}')
        else:
            restored.append(raw)
    chunk = _restore_code_spans(chunk, restored)

    return chunk


def process_inline(md_text: str) -> str:
    parts = CODE_BLOCK_SPLIT.split(md_text)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # bloc code → on ne touche pas
            out.append(part)
        else:
            out.append(_process_inline_chunk(part))
    return ''.join(out)
