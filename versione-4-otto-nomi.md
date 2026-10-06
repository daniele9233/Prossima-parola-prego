# Prossima parola, prego

### Viaggio tra le allucinazioni d’autore di un’IA ignorante ma straordinariamente eloquente

**12 giugno 2017.**

Un lunedì.

Alle 17:57, ora di Greenwich, qualcuno carica su arXiv un file.

Titolo: *Attention Is All You Need*.

Otto autori.

Nella prima pagina, una nota che sembra uno scherzo e non lo è:

> *Equal contribution. Listing order is random.*

Contributo uguale.

Ordine casuale.

Poi, sotto, la lista di chi ha fatto cosa.

Uno ha proposto di sostituire le reti ricorrenti con l’attenzione.

Due hanno costruito i primi modelli.

Uno ha inventato pezzi del meccanismo che usiamo ancora oggi.

Uno ha scritto il codice.

Altri due hanno passato, cito, «innumerevoli lunghe giornate» a riscrivere tutto per farlo andare meglio.

Il titolo, si racconta, sarebbe un omaggio ai Beatles. [DA VERIFICARE: aneddoto riportato da fonti secondarie]

Questo libro ha un conto in sospeso con quel file.

Perché è lì che la storia dei modelli linguistici fa una curva.

Per capirla, torniamo indietro.

Poi andiamo avanti.

---

## Prima del file

**1913.** Un matematico russo, **Markov**, conta le lettere dell’*Onegin* e scopre che ognuna dipende dalla precedente. [DA VERIFICARE: dettagli del saggio]

**1948.** **Shannon** si costruisce a mano un inglese finto aprendo libri a caso, e comincia con *THE HEAD AND IN FRONTAL ATTACK ON AN ENGLISH WRITER…*

**Anni Settanta.** **Jelinek** e IBM contano triple di parole per trascrivere il parlato.

**2003.** **Bengio**: il primo modello linguistico neurale serio, in cui la parola è una fila di numeri.

**2007.** Brants e colleghi: tabelle su fino a 2 mila miliardi di parole.

**2010.** **Mikolov**: rete ricorrente, che legge un pezzo alla volta e si porta dietro un riassunto.

**2013.** **word2vec**: vettori di parole imparati da 1,6 miliardi di parole in meno di un giorno.

**Settembre 2014.** In nove giorni, due articoli gemelli.

Il primo, il **1 settembre**, di **Bahdanau, Cho e Bengio**: il modello che traduce può **tornare a guardare** le parole rilevanti.

Lo chiameranno attenzione.

Il secondo, il **10 settembre**, di **Sutskever, Vinyals e Le**: due reti ricorrenti, una che legge e una che scrive.

Con un trucco di cui gli autori ammettono di non avere una spiegazione completa: **leggere la frase al contrario**.

La perplexity scende da 5,8 a 4,7.

Il punteggio di traduzione sale da 25,9 a 30,6.

Il problema, allora, è questo:

le reti ricorrenti leggono **una parola alla volta**.

Non si possono allenare in parallelo.

Sono come un fax: fanno tutto bene, ma in fila.

---

## Il file

L’idea degli otto, in una riga:

> *Perché leggere una parola alla volta, se ogni parola può guardare tutte le altre contemporaneamente?*

Si chiama **Transformer**.

Niente più lettura in fila.

Niente più riassunto che passa da una parola all’altra.

Solo attenzione, ripetuta a strati.

E parallelismo.

Su una macchina con **8 schede video P100**, il modello base si allena in **12 ore**.

Quello grande, in **3,5 giorni**.

Ed è qui, a mio parere, che sta il punto che di solito si perde:

l’idea non era soltanto *migliore*.

Era **allenabile in fretta**.

E un modello allenabile in fretta si può allenare su molto più testo.

Una nota a margine, dal paper: **Aidan Gomez** è affiliato a Toronto e firma con la dicitura «Work performed while at Google Brain», **Illia Polosukhin** con «Work performed while at Google Research».

I modelli non nascono solo nelle grandi aziende.

Ma nelle grandi aziende, certe volte, ci passano.

---

## Dopo il file

**Giugno 2018.** **GPT**, di OpenAI: un Transformer allenato prima a prevedere la parola successiva su tanto testo, poi adattato a compiti specifici. [DA VERIFICARE: i dettagli dell’architettura, nel rapporto tecnico originale]

**Ottobre 2018.** **BERT**, di Google.

**Febbraio 2019.** **GPT-2**, rilasciato a tappe fino a novembre.

**Gennaio 2020.** **Kaplan** e colleghi: l’errore dei modelli linguistici neurali segue una **legge di potenza** rispetto a dimensione, dati e calcolo, con andamenti su più di sette ordini di grandezza.

Tradotto: se raddoppi gli ingredienti, ottieni un miglioramento prevedibile.

**Maggio 2020.** **GPT-3**: 175 miliardi di parametri.

**Marzo 2022.** **Chinchilla**, DeepMind: 70 miliardi di parametri, 1,4 mila miliardi di token.

Batte modelli molto più grandi, perché è stato allenato più a lungo.

Fa circa 20 token per parametro: un conto sulla tabella del paper, non una frase del paper.

**30 novembre 2022.** **ChatGPT**.

Secondo Sam Altman, un milione di utenti in circa cinque giorni.

**Aprile 2024.** **Llama 3**, di Meta: allenato su oltre 15 mila miliardi di token.

---

## Quello che non è cambiato

In sette anni, dal file alle chat sul telefono, **la domanda** è rimasta uguale a quella di Markov:

*dato ciò che è venuto prima, che cosa viene dopo?*

È cambiata la quantità di testo.

È cambiato chi risponde.

Non è cambiata la natura del gioco.

Il modello assegna un punteggio a ogni pezzo possibile.

Ne sceglie uno.

Lo attacca.

E ricomincia.

Quello con il punteggio più alto non è il più vero.

È il **più probabile**.

Già nel 2019, nella scheda del modello, gli autori di GPT-2 avvertivano che questi modelli *non distinguono il vero dal falso*.

Nessuno dei grandi passi della storia ha cambiato questo dettaglio.

Hanno solo reso più convincente la voce che lo dice.

> *Otto nomi in ordine casuale hanno scritto la pagina più influente degli ultimi anni. Nessuno dei loro modelli sa dirti, però, se ha ragione.*

Prossima parola, prego.

Ed è da qui che comincia questo libro.
