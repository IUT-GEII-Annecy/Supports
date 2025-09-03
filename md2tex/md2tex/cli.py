from __future__ import annotations
import argparse
from pathlib import Path
from typing import Optional
from .io_utils import create_root, read_text, write_text
from .pipeline import process_file_content, generate_master_file

import subprocess
import shutil

def auto_indent_tex(file_path: Path) -> None:
    """Lance latexindent.pl sur le fichier .tex si disponible."""
    exe = shutil.which("latexindent")
    if exe:
        try:
            subprocess.run([exe, "-s", "-w", str(file_path)], check=True)
            backup = file_path.with_suffix(".bak0")
            if (backup.exists()):
                backup.unlink()
            print(f"Auto-indent : {file_path}")
        except subprocess.CalledProcessError as e:
            print(f"⚠️ latexindent a échoué : {e}")
    else:
        print("⚠️ latexindent non trouvé (installe TeX Live ou MikTeX).")



def process_file(file_path: Path, output_dir: Path) -> Path:
    md_text = read_text(file_path)
    latex = process_file_content(md_text, output_dir)
    stem = file_path.stem
    if stem == "_index":
        stem = "00_index"
    out = output_dir / (stem + ".tex")
    assert '\\\\item' not in latex, "Un \\ a été doublé quelque part."
    write_text(out, latex)
    auto_indent_tex(out)
    print(f"Conversion terminée : {out}")
    return out




def process_path(path: str, root: Optional[Path] = None, root_name: str = "LaTeX") -> Path:
    p = Path(path)


    if p.is_file() and p.suffix.lower() == ".md":
        if root is None:
                root = create_root(p.parent, root_name, clear=True)
                source = create_root(root, "sources", clear = False)
                process_path(path, source, root_name)
                return root.absolute()
        process_file(p, root)


    elif p.is_dir() and p.name != root_name:
        if root is None:
            root = create_root(p, root_name, clear=True)
            source = create_root(root, "sources", clear = False)
            process_path(path, source, root_name)
            return root.absolute()
        for child in p.iterdir():
            if child.is_dir() and child.name == root_name:
                continue
            if child.is_file() and child.suffix.lower() == ".md":
                process_file(child, root)
            elif child.is_dir():
                sub_root = create_root(root, child.name, clear=False)
                process_path(str(child), sub_root, root_name)


    else:
        # motif glob
        any_found = False
        for md_file in Path().rglob(path):
            if md_file.suffix.lower() == ".md":
                any_found = True
                if root is None:
                    root = create_root(md_file.parent, root_name, clear=True)
                process_file(md_file, root)
            if not any_found:
                raise FileNotFoundError(f"Aucun fichier correspondant au motif : {path}")


    print("Conversion Terminée - Dossier : " + str(root))
    return root.absolute()




def main() -> None:
    parser = argparse.ArgumentParser(description="Convertisseur Markdown → LaTeX")
    parser.add_argument("paths", nargs="+", help="Fichier, dossier ou motif glob")
    parser.add_argument("--root-name", default="LaTeX", help="Nom du dossier de sortie racine")
    parser.add_argument("--master", default="main.tex", help="Nom du fichier maître généré")
    parser.add_argument("--no-master", action="store_true", help="Ne pas générer le fichier maître")
    parser.add_argument("--clear", action="store_true", help="Vider le dossier de sortie s'il existe")
    args = parser.parse_args()


    final_root: Optional[Path] = None
    for arg in args.paths:
        final_root = process_path(arg, root=None, root_name=args.root_name)


    if final_root and not args.no_master:
        generate_master_file(final_root, args.master)




if __name__ == "__main__":
    main()