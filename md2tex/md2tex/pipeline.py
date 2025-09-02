from __future__ import annotations
from pathlib import Path
from .processors import (
    hint_re,
    replace_hints,
    process_asciinema,
    process_tables,
    process_images,
    process_code_blocks,
    process_lists,
    process_links,
    process_inline,
    process_titles,
    process_horizontal_rules,
    escape_underscores,
    remove_header_footer,
)
from .io_utils import write_text




def process_file_content(md_text: str, output_dir: Path) -> str:
    md_text = remove_header_footer(md_text)
    md_text = hint_re.sub(replace_hints, md_text)
    md_text = process_asciinema(md_text, output_dir)
    # md_text = process_tables(md_text)
    # md_text = process_images(md_text)
    # md_text = process_lists(md_text)
    # md_text = process_code_blocks(md_text)
    # md_text = process_links(md_text)
    # md_text = process_inline(md_text)
    # md_text = process_titles(md_text)
    # md_text = process_horizontal_rules(md_text)
    # md_text = escape_underscores(md_text)
    return md_text




def generate_master_file(output_dir: Path, master_file: str = "main.tex") -> Path:
    tex_files = sorted([p for p in output_dir.rglob("*.tex")])
    master_path = output_dir / master_file
    with master_path.open("w", encoding="utf-8") as f:
        for file in tex_files:
            rel_path = file.relative_to(output_dir)
            f.write(f"\\input{{{rel_path.as_posix()}}}\n")
    print(f"Fichier maître généré : {master_path}")
    return master_path

