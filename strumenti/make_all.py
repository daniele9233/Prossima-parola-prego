"""Rigenera i DOCX dei tre libri dai rispettivi .md (richiede python-docx).

Uso:  python strumenti/make_all.py
Il sorgente è sempre il .md; DOCX e PDF sono derivati. Per i PDF: strumenti/md_to_pdf_edge.py.
"""
from pathlib import Path

from build_capitoli import build

ROOT = Path(__file__).resolve().parent.parent

# (cartella del libro, etichetta nei metadati)
BOOKS = [
    ("libro-1-la-nonna-e-il-forno", "libro 1 · voce affettiva"),
    ("libro-2-luomo-che-faceva-indovinare-le-lettere", "libro 2 · voce saggistica"),
    ("libro-3-la-stanza-in-cui-non-ce-nessuno", "libro 3 · voce reportage"),
]
STEM = "prologo-e-capitolo-1"

if __name__ == "__main__":
    for folder, stamp in BOOKS:
        md = ROOT / folder / f"{STEM}.md"
        docx = ROOT / folder / f"{STEM}.docx"
        build(md, docx, stamp)
        words = len(md.read_text(encoding="utf-8").split())
        print(f"OK {docx.relative_to(ROOT)} - {words} parole")
