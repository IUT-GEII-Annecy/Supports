import re


# Mapping des callouts → environnements LaTeX UPSTI
HINT_MAP = {
    "todo": "Manipulation",
    "tip": "infor",
    "info": "infor",
    "warning": "warning",
    "danger": "danger",
    "hint": "infor",
    "question": "idee",
    "attention": "cahierDesCharges",
}


# Regex pour blocs de type
# > [!type] Titre\n> contenu...
hint_re = re.compile(r"^>\s*\[!(\w+)\][-+]?\s?(.*)((?:\n>\s?.*)*)", re.MULTILINE | re.IGNORECASE)




def replace_hints(match: re.Match) -> str:
    hint_type = match.group(1).lower()
    title = match.group(2).strip()
    content = match.group(3).strip()
    content = re.sub(r"^>\s?", "", content, flags=re.MULTILINE)
    env = HINT_MAP.get(hint_type, "infor")
    return f"\\begin{{UPSTI{env}}}{{{title}}}\n{content}\n\\end{{UPSTI{env}}}"