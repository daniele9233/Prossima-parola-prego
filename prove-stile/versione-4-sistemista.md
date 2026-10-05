- **Voce:** il sistemista: ironia secca da turno di notte, understatement da postmortem, frasi corte, numeri davanti alle parole, zero entusiasmo di facciata.
- **Densità di battute:** media: 8 battute, circa una ogni 180 parole, secche e mai urlate.
- **Analogie usate:** la tastiera del telefono (madre); le manopole di un mixer (i parametri); l'eliminacode degli sportelli (gag del titolo); il tasto Tab nella shell (limite: cerca in un elenco, non prevede); il registro di sistema, il log (limite: è inerte); la postmortem (limite: serve a scegliere le parole, non a spiegare il motore); due battute di passaggio (turno di notte, aggiornamento del venerdì sera).

---

# Capitolo 1 — Il completamento automatico più costoso della storia

> Un LLM parla come chi improvvisa un brindisi: una parola alla volta, e senza poter cancellare.

<!-- parte: aggancio -->
## Sei tocchi e un cliente

Scrivi «Gentile» sul telefono. La tastiera propone tre parole, per esempio «amministratore», «cliente», «signora». Per gioco tocchi sempre quella in mezzo. Dopo sei tocchi ottieni qualcosa come: «Gentile cliente, la ringrazio per il suo messaggio e per il mio». Grammatica a posto, contenuto in manutenzione. Il telefono ha fatto il suo lavoro sei volte di fila, e nessuno dei sei suggerimenti era sbagliato, preso da solo. È questo il guaio.

Ora apri un'IA (intelligenza artificiale) e scrivi la richiesta che ti accompagnerà per tutto il libro: «Scrivi una mail formale all'amministratore di condominio per rinviare l'assemblea». Pochi secondi, e arriva una mail intera: saluto, motivo del rinvio, proposta di una nuova data, congedo. Tu hai scritto una riga, il resto l'ha fatto lei.

Due programmi, due risultati. Eppure il mestiere è lo stesso: prevedere cosa viene dopo. Il secondo è un *Large Language Model*, «modello linguistico di grandi dimensioni», in sigla LLM, e fa una cosa sola: prevede il prossimo pezzo di testo. La tastiera, in fondo, anche.

Com'è possibile che lo stesso mestiere produca un nonsenso da una parte e una mail dignitosa dall'altra? Chi lavora con i sistemi conosce il copione: due servizi sembrano uguali e si comportano in modo opposto, e la differenza sta in ciò che c'è sotto. Qui sta soprattutto nella scala. Vediamo quanta.

<!-- parte: analogia madre -->
## La tastiera che ha letto mezza biblioteca

L'analogia di questo capitolo è già nella tua tasca: i suggerimenti della tastiera. Guardano ciò che hai scritto e propongono la parola successiva. Non è una semplificazione per comodità del libro. Gboard, la tastiera di Google, usa un modello di linguaggio per predire la parola successiva, ed è documentato in un articolo del 2018 (Hard e altri). Da anni questi suggerimenti nascono da piccole reti neurali: programmi fatti di tanti calcoli semplici collegati tra loro, che imparano dagli esempi invece di seguire regole scritte a mano.

Chi vive nella *shell*, la finestra nera dove si scrivono i comandi, pensa al tasto Tab: scrivi due lettere, premi, e il nome del file si completa. Somiglia, ma il Tab cerca in un elenco di nomi che esistono già. Non prevede niente. È affidabile esattamente perché non azzarda.

Adesso fai crescere la tastiera. Più testi per addestrarla: non le tue chat, ma l'equivalente di mezza biblioteca. Più testo davanti agli occhi mentre decide: pagine intere, non l'ultima parola. Più parametri. E un motore progettato meglio, il *Transformer* (cap. 4). Il salto è di scala e di architettura, non di mestiere.

I parametri sono numeri, detti anche pesi, e funzionano come le manopole di un mixer: ciascuna alza o abbassa un po' l'influenza di qualcosa. Una manopola da sola non decide niente: la parola proposta esce dalla posizione di tutte insieme. «8B» vuol dire circa 8 miliardi di parametri: la B è *billion*, «miliardo» in inglese. Otto miliardi di manopole: le regola l'addestramento (cap. 6). Girarle a mano sarebbe il turno di notte più lungo della storia. Durante la tua conversazione restano ferme.

<!-- parte: cosa succede davvero -->
## Una parola alla volta, senza tornare indietro

Il ciclo è questo. Il modello riceve il testo: la tua richiesta, il *prompt*, più ciò che ha già scritto. Dà un punteggio a ogni pezzo possibile (alto vuol dire «qui ci sta bene», basso «qui stona») e ne sceglie uno. Il pezzo scelto si aggiunge in coda. Il testo allungato rientra come nuovo input. Si ricomincia, fino alla fine.

Un pezzo scritto non si cancella e condiziona tutto il seguito. Pensa a un registro di sistema, il *log*: si aggiunge in fondo, non si corregge. Se la quarta riga è sbagliata, le successive ci costruiscono sopra, e nella postmortem (la relazione che si scrive dopo un guasto, per ricostruire cosa è successo) leggerai: «funzionava fino alla terza». Il limite: un registro è inerte, mentre qui ogni riga nuova cambia le previsioni di quelle dopo.

Proviamo sulla tua mail. È una ricostruzione illustrativa, non l'output registrato di un modello reale. Per semplicità un pezzo coincide con una parola; i veri pezzi, i *token*, sono frammenti di testo (una parola, mezza parola, un segno di punteggiatura): ne parla il cap. 2.

Primo giro. Candidati, in ordine di plausibilità: «Gentile», «Egregio», «Spettabile», «Buongiorno». Se ne sceglie uno: «Gentile». Poi il testo cresce di un pezzo alla volta; ti mostro solo qualche istantanea:

- «Gentile amministratore,»
- «Gentile amministratore, le scrivo»
- «Gentile amministratore, le scrivo per chiederle di»
- «Gentile amministratore, le scrivo per chiederle di rinviare l'assemblea»

Tra una riga e l'altra passano uno o più giri completi: ho saltato quelli in mezzo. Dal secondo giro in poi il modello non riceve più soltanto la tua richiesta: riceve la richiesta più tutto ciò che è già stato scritto, e da lì ricalcola tutta la classifica. Come si sceglie tra i candidati lo dice il cap. 10.

Questo è l'eliminacode degli sportelli: «prossimo, prego», una parola alla volta. Con una differenza: chi è appena stato servito resta allo sportello e decide chi viene dopo.

Dico «sceglie», «sa», «prevede»: metafore comode. In una postmortem non si scrive «il server voleva rallentare»: si scrive quale valore ha superato quale soglia. Qui uguale (il paragone vale per le parole che usiamo, non per il motore). Dietro «prevede» ci sono numeri che si moltiplicano tra loro e producono punteggi. Nessuna intenzione, nessun «voglio rinviare l'assemblea». Il risultato sembra un pensiero perché i numeri sono stati regolati su una quantità enorme di testo scritto da persone che pensavano.

E la chat? Chat, memoria della conversazione e strumenti esterni sono software costruito intorno al modello; il modello in sé prevede testo. La memoria arriva al cap. 11, gli strumenti al cap. 18.

Tutto questo ha un antenato di carta. Nel 1913, a San Pietroburgo, il matematico russo Markov contò a mano vocali e consonanti nelle prime 20.000 lettere dell'*Eugenio Onegin* di Puškin. Scoprì che la probabilità di trovare una vocale dipende dalla lettera che precede. Prevedere il pezzo successivo da ciò che viene prima: è lo stesso mestiere. Infrastruttura: carta e matita. Nessun allarme alle tre di notte.

<!-- parte: dove l'analogia scricchiola -->
> **Dove l'analogia scricchiola.** Tre differenze. Il contesto: la tastiera vede la frase che stai scrivendo, un LLM tiene davanti pagine intere (quante, lo dice il cap. 11); la scala: con miliardi di parametri non hai più la stessa tastiera con un po' più di fiato, hai un'altra macchina con lo stesso mestiere. Il ciclo: sul telefono scegli tu, un dito alla volta, e se la frase prende una piega strana scarti e ritocchi; il modello non ha il tuo dito, sceglie, aggiunge e riparte da solo, senza aspettare approvazione, come un aggiornamento lanciato il venerdì sera. Il modello ha già scritto, e ciò che ha scritto diventa l'input del passo dopo.

<!-- parte: sotto il cofano -->
> **Sotto il cofano.** Il modello lavora su token, non su parole, e ha un elenco chiuso di quelli possibili: il vocabolario. Llama 3, il modello di Meta (aprile 2024), ne ha circa 128.000; il valore esatto è 128.256 [DA VERIFICARE: campo `vocab_size` nel file `config.json` di Llama 3 8B]. A ogni passo dà un punteggio a ciascuna voce del vocabolario. I punteggi si leggono come probabilità: sommano 1, cioè 100%. Poi se ne sceglie una (cap. 10).
>
> Il passo, in una riga: `P(token successivo | tutti i token precedenti)`. A parole: la probabilità del prossimo pezzo, sapendo tutto ciò che è già scritto. Il processo si dice *autoregressivo*: suona come una diagnosi e vuol dire solo che ogni passo si basa sui risultati dei passi precedenti.
>
> Il conto dei passaggi. Per generare N token servono N passaggi in avanti (*forward pass*: un attraversamento completo del modello). Ipotesi di lavoro: una mail da 300 token, quindi 300 passaggi; la cifra è un'ipotesi, non una misura. Con la *KV cache* (da *key-value*, «chiave-valore»: appunti che evitano di rifare conti già fatti; cap. 11) ogni passaggio rilegge meno, ma ne resta uno per token.
>
> Il conto della memoria. 8 miliardi di parametri × 2 byte (16 bit; un byte sono 8 bit) = 16 miliardi di byte = 16 GB, dove GB sta per gigabyte, cioè miliardi di byte: tutta la memoria di una buona scheda video da gaming. Sono i soli parametri: la memoria di lavoro per il testo in corso si somma (cap. 11). Si può stringere con la quantizzazione (cap. 14).
>
> Modello contro applicazione. Il modello è un file di parametri più un programma che lo esegue: riceve token, restituisce punteggi. Cronologia, memoria e strumenti stanno nell'applicazione che gli sta intorno.

*[Il capitolo prosegue con: Mito da sfatare («è solo statistica»), Storia vera (Shannon, 1948), Nell'uso reale, Prova tu, In tre righe.]*
