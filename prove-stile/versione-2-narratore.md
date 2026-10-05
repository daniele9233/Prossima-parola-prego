- **Voce:** Il narratore: parte da una storia vera (Markov, 1913) e la porta, per montaggio e non per dettagli inventati, fino al mistero della mail; periodi che respirano e poi si spezzano, ironia per sottrazione.
- **Densità di battute:** media: 6 battute, circa una ogni 240 parole.
- **Analogie usate:** la tastiera dei suggerimenti del telefono (madre); le manopole di un mixer (i parametri); l'eliminacode degli sportelli («prossimo, prego»); in epigrafe, il brindisi.

---

# Capitolo 1 — Il completamento automatico più costoso della storia

> Un LLM parla come chi improvvisa un brindisi: una parola alla volta, e senza poter cancellare.

<!-- parte: aggancio -->
## Ventimila lettere

Nel 1913, a San Pietroburgo, un matematico russo si mette a contare lettere.

Si chiama Markov. Il testo è l'*Eugenio Onegin* di Puškin, che di solito si legge per altri motivi. Ne prende le prime ventimila lettere e le divide in due gruppi: vocali da una parte, consonanti dall'altra. Tutto a mano. Ventimila lettere sono tante, quando si contano una per una.

Il risultato sembra minuscolo e minuscolo non è. La probabilità di trovare una vocale dipende dalla lettera che la precede. Le lettere non arrivano a caso, una indifferente all'altra: quella che viene dopo si lascia condizionare da quella che c'era prima.

È un antenato dei modelli del linguaggio: prevedere il pezzo successivo da ciò che viene prima, con carta e matita.

Più di un secolo dopo, la stessa mossa ci sta in tasca. Mentre scrivi un messaggio, il telefono ti propone la parola seguente, e tu il più delle volte la accetti. Poi apri un'intelligenza artificiale (IA) e le chiedi quello del Prologo: una mail formale all'amministratore di condominio, per rinviare l'assemblea.

Arriva una mail intera. Saluto, motivazione, congedo, il tono giusto dalla prima all'ultima riga.

Un software che completa le frasi. Un altro che scrive la lettera. Possibile che siano la stessa cosa?

La risposta breve è sì. Quella lunga occupa il resto del capitolo, e comincia da una tastiera.

<!-- parte: analogia madre -->
## La tastiera che ha letto troppo

Immagina di scrivere un messaggio sul telefono. Hai appena digitato «Gentile» e sopra le lettere compaiono tre parole suggerite. Tocchi la prima e il messaggio prosegue.

Questa tastiera è l'analogia che ci accompagnerà per tutto il libro, e non è scelta a caso. Le tastiere degli smartphone prevedono la parola successiva da anni, con piccole *reti neurali* (strutture di calcolo fatte di numeri). Il caso documentato è Gboard, la tastiera di Google: un modello di linguaggio per predire la parola successiva (Hard e altri, 2018).

Ora fai crescere quella tastiera, finché non ha letto mezza biblioteca. E poi smetti di scegliere tu: le parole non te le propone più, le sceglie lei, le scrive e riparte da dove è arrivata.

Questa tastiera cresciuta si chiama *Large Language Model*, «modello linguistico di grandi dimensioni», in sigla LLM. Fa una cosa sola: prevede il prossimo pezzo di testo. Può sembrare poco. Ripetuta di fila e senza fiatare, produce mail, riassunti, poesie.

Dove sta il sapere, in tutto questo? Nei parametri: numeri, detti anche pesi, che puoi immaginare come le manopole di un *mixer*. Ognuna è regolata di pochissimo, e tutte insieme decidono quale parola suona bene dopo quale. Il suono non sta in una manopola sola: sta nell'insieme. Un modello «8B» ne ha circa 8 miliardi (la B è per *billion*, che in inglese vuol dire miliardo). A differenza di un fonico, nessuno le gira a mano: con otto miliardi di manopole la prova microfoni durerebbe un pochino. Le regola l'addestramento (cap. 6), e durante la tua conversazione restano ferme.

Le manopole restano ferme. Il testo, invece, si muove.

<!-- parte: cosa succede davvero -->
## Cinque istantanee di una mail

Torniamo all'amministratore. Il tuo *prompt*, cioè la richiesta che scrivi («Scrivi una mail formale all'amministratore di condominio per rinviare l'assemblea.»), entra nel modello. Quello che esce non è la mail. È un pezzo. Uno solo, poi basta: il resto toccherà al giro dopo.

Un pezzo, in gergo *token*: un frammento di testo, che può essere una parola, mezza parola, un segno di punteggiatura. Il modello non legge lettere e non legge parole intere, legge token. Come si spezzano lo scopriremo al capitolo 2.

Quella che segue è una ricostruzione illustrativa, non l'output registrato di un modello reale. E per semplicità qui un pezzo coincide con una parola, o poco più, mentre i veri pezzi no.

Primo giro. Il modello mette in classifica i candidati per l'attacco: «Gentile» in testa, e più indietro «Egregio», «Spettabile», «Buongiorno». Se ne sceglie uno: «Gentile».

Secondo giro. Il pezzo scelto si aggiunge al testo, il testo allungato rientra come nuovo input, e il modello prevede di nuovo. E così via:

- «Gentile»
- «Gentile amministratore,»
- «Gentile amministratore, le scrivo»
- «Gentile amministratore, le scrivo per chiederle di»
- «Gentile amministratore, le scrivo per chiederle di rinviare l'assemblea»

Cinque istantanee e l'assemblea è rinviata. Tra una e l'altra passano più giri, e la mail vera ne richiede molti di più: quanti, lo conti nel box.

Per il modello, a ogni giro, il testo allungato è un input come un altro: che l'ultimo pezzo l'abbia scelto lui non fa nessuna differenza.

Una cosa va detta subito. Un pezzo scritto è scritto: non esiste il tasto per cancellare, e ogni pezzo condiziona tutto quello che segue. Se al primo giro fosse uscito «Egregio», il resto della mail avrebbe dovuto farci i conti. E se il pezzo è sbagliato, il modello può solo proseguire da lì, con la coerenza di chi non può tornare indietro.

Il titolo di questo libro viene da qui. All'eliminacode degli sportelli si sente «prossimo, prego», e si fa avanti il numero dopo. Il modello fa lo stesso con le parole: chiama il prossimo pezzo, lo fa entrare, e quello di prima non torna indietro a correggere il modulo. Con una differenza: all'anagrafe i numeri sono già stampati, qui il prossimo si decide strada facendo.

Dico «prevede», «sceglie», «sa». Sono scorciatoie comode, e adesso togliamole. Cosa succede davvero: il testo diventa numeri, i numeri attraversano il modello moltiplicandosi per i parametri, e dall'altra parte esce un elenco di punteggi, uno per ogni pezzo possibile. I punteggi si leggono come probabilità: sommano 1, cioè 100%. Poi se ne sceglie uno, e come lo spiega il capitolo 10. Nessuna intenzione. Solo aritmetica.

E la chat? La finestra in cui scrivi, la memoria di ciò che hai detto prima, gli strumenti esterni: tutto software costruito intorno al modello. Il modello in sé non ti saluta, non ti ricorda, non va a cercare nulla: prevede testo. La memoria la vedremo al capitolo 11, gli strumenti al 18.

È la mossa di Markov del 1913, prevedere il pezzo successivo da ciò che viene prima, con qualche miliardo di manopole in più e molta meno matita.

<!-- parte: dove l'analogia scricchiola -->
> **Dove l'analogia scricchiola.** Tre differenze. Il contesto, cioè il testo che si ha davanti per prevedere: nella tastiera è poca cosa, in un LLM molto di più; la scala: più dati, più parametri e un'architettura diversa, il *Transformer* (cap. 4), ma il mestiere resta lo stesso. Infine il ciclo: il telefono propone e aspetta che tocchi a te scegliere la parola, ed è lì che l'analogia smette di reggere. Il modello non aspetta nessuno: sceglie, aggiunge e ricomincia fino alla fine, e tu resti a guardare con tutta la dignità che il caso consente.

<!-- parte: sotto il cofano -->
> **Sotto il cofano.** Un LLM è, a conti fatti, una funzione: prende una sequenza di token e restituisce un punteggio per ciascun token del *vocabolario*, l'elenco chiuso dei pezzi che conosce. I token non sono parole: un pezzo può essere una parola, mezza parola o un segno di punteggiatura (cap. 2). Per Llama 3 (Meta, aprile 2024) sono circa 128.000; il valore esatto è 128.256 [DA VERIFICARE: campo `vocab_size` nel file `config.json` di Llama 3 8B]. Ad ogni passo il modello dà un voto a tutte e 128.256 le voci, comprese quelle che in una mail all'amministratore non entrerebbero mai. Pignolo, ma equo.
>
> I punteggi si leggono come probabilità e sommano 1. L'unica formula del capitolo è `P(token successivo | tutti i token precedenti)`: la probabilità del prossimo pezzo, sapendo tutto ciò che è già scritto. Il termine tecnico è *autoregressivo*: ogni passo si basa sui risultati dei passi precedenti.
>
> I passaggi. Per generare N token servono N passaggi in avanti (*forward pass*: un attraversamento completo del modello, dall'ingresso ai punteggi). Se la tua mail fosse di 300 token (un'ipotesi di lavoro, non una misura), i passaggi sarebbero 300. La *KV cache* (*key-value cache*, una memoria dei calcoli già fatti sul testo precedente, cap. 11) fa rileggere meno a ogni passaggio, ma ne resta uno per token.
>
> Il conto della memoria: 8 miliardi di parametri × 2 byte (16 bit) = 16 GB (gigabyte, miliardi di byte). Si può stringere con la quantizzazione (arrotondare i parametri perché occupino meno, cap. 14).
>
> Quei 16 GB sono il modello: un file di numeri che, dato un testo, restituisce punteggi. Chat, memoria della conversazione e strumenti sono applicazione, software scritto a parte intorno a lui (cap. 11 e 18).

*[Il capitolo prosegue con: Mito da sfatare («è solo statistica»), Storia vera (Shannon, 1948), Nell'uso reale, Prova tu, In tre righe.]*
