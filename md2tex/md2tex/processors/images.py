import re




def process_images(md_text: str) -> str:
    return re.sub(
        r'!\[([^\]]*)\]\(([^)]+)\)',
        r'\\begin{figure}[h!t]\n\\centering\n\\includegraphics[width=0.8\\textwidth]{\2}\n\\caption{\1}\n\\end{figure}',
        md_text,
)