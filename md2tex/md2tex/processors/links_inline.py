import re

# protège le code inline avant tout
CODE_SPAN = re.compile(r'`([^`]+)`')

def _protect_code_spans(text: str):
    # remplace les `code` par des sentinelles pour éviter toute mise en forme
    buckets = []
    def hold(m):
        buckets.append(m.group(0))
        return f"\uFFF0{len(buckets)-1}\uFFF1"
    return CODE_SPAN.sub(hold, text), buckets

def _restore_code_spans(text: str, buckets):
    for i, raw in enumerate(buckets):
        text = text.replace(f"\uFFF0{i}\uFFF1", raw)
    return text

def process_links(md_text: str) -> str:
    # [texte](url) → \href{url}{texte}
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\\href{\2}{\1}', md_text)

def process_inline(md_text: str) -> str:
    # 1) protéger les `code`
    md_text, buckets = _protect_code_spans(md_text)

    # 2) gras **bold** ou __bold__
    md_text = re.sub(r'(?<!\\)(\*\*|__)(.+?)\1', r'\\textbf{\2}', md_text)

    # 3) italique *em* ou _em_ :
    #    - pas collé à une lettre/chiffre avant/après
    #    - évite de matcher à l'intérieur d'identifiants (ex: nom_du_fichier)
    italic_re = re.compile(r'(?<!\\)(?<!\w)(\*|_)([^*_].*?)\1(?!\w)', re.DOTALL)
    md_text = italic_re.sub(r'\\textit{\2}', md_text)

    # 4) code inline `...` → \texttt{...} (on convertira après restauration)
    #    (déjà protégé ; on s’occupe juste du cas hors backticks)
    md_text = re.sub(r'`([^`]+)`', r'\\texttt{\1}', md_text)

    # 5) placeholders de type <nom_du_fichier> → \texttt<...>
    #    (à faire APRÈS italique, pour éviter _du_ au milieu)
    md_text = re.sub(r'<([A-Za-z0-9_./\-]+)>', r'\\texttt{<\1>}', md_text)

    # 6) restaurer le code inline protégé, en le convertissant en \texttt{...}
    def convert_tt(m):
        inner = m.group(1)
        return f'\\texttt{{{inner}}}'
    # Remplace les backticks par \texttt lors de la restauration
    restored = []
    for raw in buckets:
        if raw.startswith('`') and raw.endswith('`'):
            content = raw[1:-1]
            restored.append(f'\\texttt{{{content}}}')
        else:
            restored.append(raw)
    md_text = _restore_code_spans(md_text, restored)

    return md_text
