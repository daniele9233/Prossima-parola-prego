# Prossima parola, prego

### Viaggio tra le allucinazioni d’autore di un’IA ignorante ma straordinariamente eloquente

A metà febbraio 2019 un laboratorio di nome **OpenAI** pubblicò su GitHub il codice di un modello chiamato **GPT-2**.

Insieme al codice, una dichiarazione molto educata:

> *Per ora abbiamo rilasciato solo una versione più piccola, da 117 milioni di parametri.*

Dei pesi, cioè i numeri che fanno funzionare il modello, ne uscì una versione ridotta.

Il resto, **per ora**, rimase in cassaforte.

Si disse che il modello fosse «troppo pericoloso» per essere pubblicato, e la stampa ci ricamò parecchio [DA VERIFICARE: motivi dichiarati da OpenAI e titoli dell'epoca].

Noi ci fermiamo a un dettaglio più piccolo.

E, a mio parere, molto più istruttivo.

Quel **117**.

---

Qualche mese dopo, nel README ufficiale, comparve una nota di quelle che ogni sviluppatore sogna di non dover mai scrivere:

> *I nostri conteggi originali dei parametri erano sbagliati a causa di un errore.*

Il modello piccolo non aveva 117 milioni di parametri.

Ne aveva **124**.

Il medio non 345, ma **355**.

Un laboratorio che costruisce una delle macchine più sofisticate del mondo.

Che non riesce a contare le proprie manopole.

Se ti sembra una gaffe, aspetta di vedere il conto.

Un modello GPT-2 piccolo ha 12 strati, 768 numeri per ogni pezzo di testo, una finestra di 1.024 pezzi e un vocabolario di 50.257 pezzi. [DA VERIFICARE: il vocabolario, nel file di configurazione del repository]

Facendo i calcoli:

38.597.376 per la tabella dei pezzi.

786.432 per le posizioni.

85.054.464 per i 12 strati.

Più 1.536 di rifinitura.

Totale: **124.439.808**.

Il conto, rifatto a mano, dà ragione alla correzione.

Non a chi aveva scritto 117.

Una macchina che parla di tutto.

Che non sapeva dire con certezza quante cose avesse dentro.

Prima lezione del libro:

> *Anche chi costruisce un modello fa fatica a sapere cosa c'è dentro. Figuriamoci il modello.*

---

Passiamo ai campioni.

Insieme al codice, OpenAI mise online **cinquecento testi** scritti dal modello.

Senza filtri.

Senza un testo di partenza.

Molti sembravano articoli di giornale, con tanto di frasi attribuite a testate vere, come *Reuters*.

Le frasi non le aveva scritte l'agenzia.

Le aveva scritte la macchina.

Il README, già nei primi mesi, avvisava con una franchezza che oggi suona quasi commovente:

i dati su cui il modello ha imparato contengono **inesattezze di fatto**.

Poi, ad agosto 2019, nella scheda tecnica, una frase che dovrebbe essere incorniciata in ogni ufficio:

> *Poiché i modelli linguistici su larga scala come GPT-2 non distinguono il vero dal falso, non supportiamo usi che richiedano che il testo generato sia vero.*

L'originale dice: *do not distinguish fact from fiction*.

Chi ha costruito il modello lo scrisse nero su bianco.

**Nel 2019.**

Prima di ChatGPT.

Prima che metà del pianeta cominciasse a chiedergli consigli medici.

---

La storia, a questo punto, prende una piega gloriosa.

Il 5 dicembre 2019, secondo il registro delle modifiche del progetto, uscì un gioco.

Si chiamava **AI Dungeon 2**.

Un'avventura testuale, di quelle in cui si scrive «apro la porta» e il gioco ti dice cosa succede.

Solo che qui non c'era nessuna storia scritta da un autore.

Lo sviluppatore, **Nick Walton**, aveva preso il GPT-2 più grande e lo aveva rifinito su avventure «scegli la tua strada» raccolte da un sito web.

Invece di scegliere tra tre opzioni, il giocatore poteva scrivere **qualsiasi azione immaginabile**.

E il modello, ogni volta, rispondeva con il pezzo successivo.

Un pezzo alla volta.

Come un cameriere che ti porta qualunque cosa tu chieda, e per cui «non esiste» non è una risposta ammessa.

Funzionò.

Al punto che, tre giorni dopo l'uscita, il modello da scaricare passò a un **torrent**, perché un solo server non reggeva più la fila.

Per capirlo: un gioco costruito su un modello che **non distingue il vero dal falso** diventò virale.

Forse perché, in un gioco, non distinguerli è esattamente il punto.

Il drago ha sempre ragione.

Anche se ti spiega, a titolo di esempio inventato, che nel tuo zaino c'è una nave.

---

Maggio 2020.

Arriva **GPT-3**: 175 miliardi di parametri.

Il conto è facile.

A due byte per parametro: **350 GB** di soli numeri.

Circa 1.400 volte la dimensione del modello piccolo di GPT-2.

Un salto in poco più di un anno.

La scheda tecnica, a settembre 2020, riserva un altro regalo letterario:

il modello *ha la propensione a generare testo che contiene falsità, e a esprimerle con sicurezza*.

Leggilo con calma.

*A esprimerle con sicurezza.*

Questo non è un difetto scoperto dagli utenti.

È scritto nella documentazione.

È la **definizione di un'allucinazione**.

Con due anni di anticipo sul momento in cui l'intero pianeta avrebbe cominciato a usare quella parola.

---

Il 30 novembre 2022 debutta ChatGPT.

Secondo un tweet del suo capo, supera il milione di utenti in circa cinque giorni.

Un milione di persone che chiedono, a una macchina, cose.

Con una macchina che, per progetto, risponde a **ogni** domanda.

Anche a quelle a cui non dovrebbe.

Come funziona, in fondo?

Un LLM, *Large Language Model*, fa una cosa sola:

prende un testo.

Assegna un punteggio a ogni pezzo che potrebbe venire dopo.

Ne sceglie uno.

Lo attacca al testo.

E ricomincia.

Un pezzo alla volta, senza gomma.

Il pezzo con il punteggio più alto non è il più vero.

È il **più probabile**.

Prossima parola, prego.

---

Se devi ricordarti una cosa di questa storia, ricordati che nel 2019 gli autori di GPT-2 scrissero tre frasi che avrebbero potuto fare da prefazione a questo libro:

*abbiamo contato male.*

*non distingue il vero dal falso.*

*dice il falso con sicurezza.*

Tre ammissioni.

Nessuna è una scoperta degli ultimi mesi.

Tutte erano già sul tavolo.

Che la gente se ne sia accorta solo dopo ha poco a che fare con la tecnologia.

E moltissimo con noi.

> *Quando una macchina dice con sicurezza una cosa falsa, siamo inclini a credere alla sicurezza. È un difetto nostro, non suo.*

Ed è da qui che comincia questo libro.
