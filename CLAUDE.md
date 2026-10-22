# Prossima parola, prego — istruzioni per Claude

1. **Leggi per prima `PROGETTO-LIBRO.md`**: stato, regole di voce, protocollo sui numeri (§2), curiosità con ID, punti aperti (§11), valutazione critica (§12).
2. **Modifica solo i sorgenti `.md`** (`libro-N-…/prologo-e-capitolo-1.md`). DOCX e PDF sono derivati: non toccarli a mano.
3. **Rigenera** dopo ogni modifica: `python strumenti/make_all.py`, poi `python strumenti/md_to_pdf_edge.py` (Edge/Chrome da una shell normale; serve `python-docx`).
4. La fonte storica è `fonti/prima-della-prossima-parola.pdf` (testo in `fonti/estratto.txt`).
5. **Onestà prima di tutto**: niente fuffa, non assecondare l'autore, segnala errori e cose inventate.
6. Ogni numero e ogni fatto si verifica su fonte, non a memoria; ogni cifra ha una data e un'attribuzione (§2).
7. Niente scene inventate presentate come viste, niente ricordi personali dell'autore: la nonna del Libro 1 è un'immagine, non un memoir.
8. Dopo ogni sessione aggiorna `PROGETTO-LIBRO.md` (registro d'uso, §11) e committa `.md`, DOCX e PDF insieme.
