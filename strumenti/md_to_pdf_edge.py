"""Stampa i PDF dei tre libri con Edge/Chrome headless, dagli stessi .md del DOCX.

Uso:  python strumenti/md_to_pdf_edge.py                  # tutti i libri
      python strumenti/md_to_pdf_edge.py libro-2-luomo-che-faceva-indovinare-le-lettere

Geometria come il DOCX (15,24 x 22,86 cm, Palatino 10,5 pt, giustificato, numero di pagina nel footer,
niente numero in prima pagina). Serve Microsoft Edge o Chrome; si può indicarlo con la variabile
d'ambiente BROWSER. Serve anche python-docx, perché il parser dei .md è quello di build_capitoli.py.
Il font «Palatino Linotype» c'è su Windows; altrove il browser ripiega su un serif simile.
"""
import html
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from build_capitoli import BOXES, TOKEN, parse, typographic  # noqa: E402
from make_all import BOOKS, ROOT, STEM  # noqa: E402

CSS = """
@page { size: 15.24cm 22.86cm; margin: 2cm 1.8cm 2cm 2cm;
  @bottom-center { content: counter(page); font-family: 'Palatino Linotype'; font-size: 9pt; color: #6B6B6B; } }
@page :first { @bottom-center { content: none; } }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font-family: 'Palatino Linotype', Palatino, serif; font-size: 10.5pt; color: #1A1A1A;
  line-height: 1.7; text-align: justify; hyphens: manual; orphans: 2; widows: 2; }
p { margin: 0; text-indent: 0.5cm; }
p.first { text-indent: 0; }
.sec { break-before: page; }
.sec.s0 { break-before: auto; }
.stamp { text-align: center; font-size: 9pt; color: #6B6B6B; letter-spacing: 3pt; text-transform: uppercase;
  margin: 0 0 16pt; padding-top: 46pt; text-indent: 0; }
.s0 .stamp { padding-top: 0; }
.title { text-align: center; font-size: 19pt; line-height: 1.3; margin: 0 0 10pt; text-indent: 0; break-after: avoid; }
.orn { text-align: center; font-size: 10pt; color: #6B6B6B; margin: 0 0 24pt; text-indent: 0; }
h2 { font-size: 11.5pt; font-weight: bold; text-align: left; margin: 17pt 0 7pt; break-after: avoid; }
p.quote { text-indent: 0; margin: 15pt 0.7cm; text-align: center; font-style: italic; font-size: 11.5pt;
  color: #2E2E2E; line-height: 1.55; }
.box { break-inside: avoid; margin: 8pt 0 12pt; padding: 0 0.25cm 0 0.45cm; text-align: left; line-height: 1.5; }
.box .lab { font-weight: bold; font-size: 8pt; color: #5A5A5A; letter-spacing: 1.5pt; text-transform: uppercase; }
.box .bt { font-weight: bold; font-size: 10pt; margin: 3pt 0 4pt; }
.box p { font-size: 9.5pt; text-indent: 0; margin: 0; }
.box pre { font-family: Consolas, monospace; font-size: 8pt; color: #222; line-height: 1.2; margin: 6pt 0 0 0.3cm;
  white-space: pre-wrap; overflow-wrap: anywhere; }
.box .end { height: 4pt; }
.pensa { break-inside: avoid; text-align: center; margin: 16pt 0 18pt; }
.pensa .ph { font-weight: bold; font-size: 8pt; color: #6B6B6B; letter-spacing: 2pt; border-top: 0.75pt solid #8A8A8A;
  padding-top: 10pt; margin-bottom: 2pt; }
.pensa .ps { font-style: italic; font-size: 9.5pt; color: #6B6B6B; margin-bottom: 8pt; }
.pensa p { text-indent: 0; text-align: center; font-style: italic; font-size: 10pt; color: #2E2E2E; line-height: 1.55;
  margin: 0 0.6cm 7pt; }
.pensa p.last { margin-bottom: 0; padding-bottom: 10pt; border-bottom: 0.75pt solid #8A8A8A; }
"""


def inline(text: str) -> str:
    out = []
    for part in TOKEN.split(typographic(text)):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            out.append(f"<b>{html.escape(part[2:-2])}</b>")
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            out.append(f"<i>{html.escape(part[1:-1])}</i>")
        else:
            out.append(html.escape(part))
    return "".join(out)


def box_html(kind: str, title: str, items) -> str:
    if kind == "pensa":
        label = "Per chi ama pensare"
        if title.lower().startswith(label.lower()):
            title = title[len(label):].lstrip(" —-·:")
        texts = [i[1] for i in items if i[0] == "t"]
        parts = ['<div class="pensa"><div class="ph">PER CHI AMA PENSARE</div>']
        if title and title != label:
            parts.append(f'<div class="ps">{html.escape(typographic(title))}</div>')
        for n, t in enumerate(texts):
            cls = ' class="last"' if n == len(texts) - 1 else ""
            parts.append(f"<p{cls}>{inline(t)}</p>")
        parts.append("</div>")
        return "".join(parts)

    label, fill, edge = BOXES.get(kind, ("", "F4F2EC", "2F2F2F"))
    if title.lower().startswith(label.lower()):
        title = title[len(label):].lstrip(" —-·:")
    parts = [f'<div class="box" style="background:#{fill};border-left:2.25pt solid #{edge};padding-top:8pt;">',
             f'<div class="lab">{html.escape(label)}</div>']
    if title:
        parts.append(f'<div class="bt">{html.escape(typographic(title))}</div>')
    for item in items:
        if item[0] == "t":
            parts.append(f"<p>{inline(item[1])}</p>")
        else:
            parts.append(f"<pre>{html.escape(chr(10).join(item[1]))}</pre>")
    parts.append('<div class="end"></div></div>')
    return "".join(parts)


def build_html(md: Path, out: Path) -> None:
    sections = parse(md)
    body = []
    for idx, sec in enumerate(sections):
        label, _, title = sec["title"].partition(" — ")
        if not title:
            label, title = "", sec["title"]
        body.append(f'<section class="sec s{idx}">')
        body.append(f'<div class="stamp">{html.escape(typographic(label or sec["title"]))}</div>')
        body.append(f'<div class="title">{html.escape(typographic(title or sec["title"]))}</div>')
        body.append('<div class="orn">*  *  *</div>')
        first = True
        for block in sec["blocks"]:
            if block[0] == "h2":
                body.append(f"<h2>{html.escape(typographic(block[1]))}</h2>")
                first = True
            elif block[0] == "box":
                body.append(box_html(block[1], block[2], block[3]))
                first = True
            else:
                text = block[1].strip()
                if text.startswith("**") and text.endswith("**") and text.count("**") == 2:
                    body.append(f'<p class="quote">{html.escape(typographic(text[2:-2]))}</p>')
                    first = True
                else:
                    cls = ' class="first"' if first else ""
                    body.append(f"<p{cls}>{inline(text)}</p>")
                    first = False
        body.append("</section>")
    doc = (f'<!doctype html><html lang="it"><head><meta charset="utf-8">'
           f'<title>{html.escape(sections[0]["title"])}</title><style>{CSS}</style></head>'
           f"<body>{''.join(body)}</body></html>")
    out.write_text(doc, encoding="utf-8")


def find_browser() -> str:
    candidates = [
        os.environ.get("BROWSER", ""),
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        shutil.which("msedge") or "",
        shutil.which("google-chrome") or "",
        shutil.which("chromium") or "",
    ]
    for path in candidates:
        if path and Path(path).exists():
            return path
    sys.exit("Nessun Edge/Chrome trovato: imposta la variabile d'ambiente BROWSER.")


def print_pdf(browser: str, html_path: Path, pdf_path: Path, workdir: Path) -> None:
    if pdf_path.exists():
        pdf_path.unlink()
    cmd = [browser, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
           f"--user-data-dir={workdir / 'profilo'}", f"--print-to-pdf={pdf_path}", html_path.as_uri()]
    subprocess.run(cmd, timeout=180, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    if not pdf_path.exists():
        sys.exit(f"PDF non creato: {pdf_path}")


if __name__ == "__main__":
    wanted = set(sys.argv[1:])
    browser = find_browser()
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        for folder, _stamp in BOOKS:
            if wanted and folder not in wanted:
                continue
            md = ROOT / folder / f"{STEM}.md"
            pdf = ROOT / folder / f"{STEM}.pdf"
            page = work / f"{folder}.html"
            build_html(md, page)
            print_pdf(browser, page, pdf, work)
            print(f"OK {pdf.relative_to(ROOT)}")
