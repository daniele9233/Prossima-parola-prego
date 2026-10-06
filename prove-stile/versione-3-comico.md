- **Voce:** il comico: ritmo da stand-up (setup, punchline, callback), ma ogni battuta serve il meccanismo; si ride delle idee, delle macchine e di noi.
- **Densità di battute:** 16 tra battute e aforismi (epigrafe compresa; 9 aforismi), almeno una per pagina, due nel box tecnico.
- **Analogie usate:** madre, l'orecchio della nonna; parametri, il telecomando con otto miliardi di tasti senza etichetta; secondarie, la nonna distratta dei trigrammi, le parole per aria di famiglia (classi di Pereira), il dado truccato (distribuzione e perplexity).

---

# Capitolo 1 — Il completamento automatico più costoso della storia

> Un LLM parla come chi improvvisa un brindisi: una parola alla volta, e senza poter cancellare.

<!-- parte: aggancio -->
## Cinque parole che non vogliono dire niente

Immagina di dover mettere in crisi un'idea di linguistica con cinque parole. Nel 1957 il linguista Noam Chomsky ci prova: *Colorless green ideas sleep furiously*, cioè «idee verdi incolori dormono furiosamente».

Grammaticalmente è perfetta: soggetto, verbo, avverbio, tutto al suo posto. Per il senso è un modulo compilato senza errori da chi non ha niente da dichiarare.

Poi Chomsky la rovescia: *Furiously sleep ideas green colorless*. La prima è una frase che non vuol dire niente; la seconda è un mucchio di parole. Eppure, scrive lui, è lecito assumere che nessuna delle due, e nemmeno una loro parte, sia mai comparsa in un discorso inglese. Ne conclude, per lui, che un modello statistico di grammaticalità le boccerebbe alla pari.

Dodici anni dopo, nel 1969, definisce la «probabilità di una frase» una nozione «del tutto inutile», sotto ogni interpretazione nota. [DA VERIFICARE: anni e parole di Chomsky (*Syntactic Structures*, 1957; saggio su Quine, 1969)]

Una frase che non dice niente, e ha dato da dire a un'intera disciplina per più di quarant'anni.

Dall'altra parte della barricata, in un laboratorio di IBM (International Business Machines, il gigante americano dei computer), un gruppo di ingegneri faceva proprio la cosa «inutile»: calcolare probabilità di frasi, per insegnare a una macchina a riconoscere il parlato. In ogni grande disputa teorica c'è un ingegnere che, nel frattempo, prova a farla funzionare.

Questo capitolo racconta perché la «probabilità di una frase» lavora oggi dentro ogni chat con un LLM (*Large Language Model*, «modello linguistico di grandi dimensioni»).

Per capirlo serve una nonna.

<!-- parte: analogia madre -->
## L'orecchio della nonna

Tua nonna non ha mai studiato il congiuntivo, ma se dici «che io va» ti corregge a metà frase. Non conosce la regola: conosce il suono. Ha ascoltato per decenni, e se cominci «Chi dorme non piglia...» chiude lei, senza esitare: «pesci».

Un LLM è questa nonna dopo aver ascoltato mezza biblioteca.

Nessuno gli ha dettato le regole: ha un orecchio.

Gli ingegneri di IBM, dai primi anni Settanta, ne costruirono una di cartone: una nonna distratta che ricorda solo le ultime due parole che le hai detto (un LLM, invece, rilegge tutto il testo). Tre parole in fila si chiamano *trigramma*, e il suo sapere era un registro di conteggi: dopo «dorme non», quante volte è venuto «piglia»? [DA VERIFICARE: date IBM: trigrammi dal 1972, perplexity 1977]

Si racconta che Fred Jelinek, il capo del gruppo, dicesse che a ogni linguista che se ne va il riconoscitore migliora. Circolano più versioni e più date, 1985 o 1988, e una registrazione non è nota, quindi la metto tra le leggende, nel cassetto delle storie di pesca: più sono belle, meno si lasciano misurare, e una battuta così perfetta non lascia ricevute. [DA VERIFICARE: discorso di Jelinek, LREC 2004 e Language Resources and Evaluation 39, 2005; Jurafsky e Martin]

E le idee verdi? Una nonna che conta solo frasi intere le boccia entrambe. Una nonna che raggruppa le parole per aria di famiglia (quelle che compaiono negli stessi posti: «verde», «rosso», «grande») dà alla prima un punteggio molto più alto che alla seconda, pur senza averla, si presume, mai sentita.

Nel 2000 Fernando Pereira addestra su testi di giornale un modello che si inventa da solo le classi di parole. Niente nonne: lo fa un algoritmo. La frase di Chomsky risulta circa 200.000 volte più probabile della gemella rovesciata. [DA VERIFICARE: Pereira 2000: rapporto, modello, frase assente dal corpus]

Il colpo del 1957 resta geniale: secondo Pereira colpiva i modelli che si limitano a contare ciò che hanno visto, non ogni modello statistico.

Le idee verdi dormivano ancora furiosamente, ma ora avevano un punteggio.

<!-- parte: cosa succede davvero -->
## Un dado truccato e un telecomando senza etichette

Tutto il mestiere di un LLM, il «completamento automatico» del titolo, sta in una domanda ripetuta: qual è il pezzo di testo che viene dopo? Il pezzo si chiama *token* (frammento di testo: una parola, mezza parola, un segno di punteggiatura; come si spezza lo vedremo nel capitolo 2).

Prova con la nonna: qui un pezzo è una parola. Tu dici «Chi...» e lei ha già in testa un campionario di finali: «cerca trova», «tace acconsente», «dorme non piglia pesci». Il modello ne farebbe un dado truccato: una faccia per ogni pezzo che conosce, e il trucco è che certe facce escono più spesso. Il dado ha un solo 100%: se una faccia ne prende di più, le altre ne hanno meno.

Un LLM è una funzione, a ogni ingresso un'uscita: gli dai un testo, ti restituisce il dado.

Aggiungi «dorme», «non», «piglia»: a ogni parola il trucco cambia, e le facce dei finali sbagliati si riducono a puntini. Il pezzo scelto si accoda al testo e il giro ricomincia: cento pezzi di risposta, cento giri (*forward pass*, «passaggio in avanti»), ciascuno nutrito dal risultato dei precedenti, ed è questo che vuol dire *autoregressivo*.

Moltiplica le probabilità dei pezzi incontrati, ognuna calcolata sapendo ciò che viene prima, e ottieni la probabilità dell'intera frase: la nozione che nel 1969 Chomsky chiamava inutile.

Come al brindisi, ciò che è detto è detto: se ti scappa «sonno» invece di «pesci», il discorso continua da lì.

Al modello restano «cioè», «anzi» e «volevo dire».

Dov'è il sapere? Nei parametri, i «pesi»: i numeri che l'addestramento (capitolo 6) mette a punto. Un modello «8B» ne ha circa otto miliardi: la B è *billion*.

Immagina un telecomando con otto miliardi di tasti, nessuno con l'etichetta, ciascuno affondato a una profondità precisa; mentre chatti restano fermi. Il paragone zoppica: di norma a ogni pezzo lavorano tutti i tasti insieme. Il telecomando di casa ha trenta tasti e ne usi quattro; questo ne ha otto miliardi e il manuale non è mai stato scritto.

Ingombro: circa 16 GB (gigabyte, miliardi di byte), meno se quantizzato (capitolo 14).

Il telecomando, cioè il modello, non ha memoria da una richiesta all'altra e non può cercare nulla su internet: a impugnarlo è un'applicazione, con la ricerca sul web (capitolo 18) e la memoria della conversazione (capitolo 11), che è un trucco di consegna: a ogni tuo messaggio ridà al modello tutta la conversazione.

Siamo la specie che ringrazia il bancomat: non stupirti se scrivo che il modello «prevede» o «sa». Sono scorciatoie: sotto ci sono moltiplicazioni a catena, e a ogni giro ne esce un dado truccato, non un'intenzione.

Nel 1957 Chomsky mette in dubbio chi si limita a contare; nel 1977 gli ingegneri di IBM presentano la *perplexity*, che misura quanto un modello è ancora indeciso: raro caso di nome tecnico che dice la verità.

Nel 2007 Brants e colleghi, nell'articolo «Large Language Models in Machine Translation», contano fino a 2 mila miliardi di token e costruiscono tabelle di 5-grammi, sequenze di cinque parole. I «grandi modelli linguistici» c'erano già, ma erano tabelle di conteggi, non reti neurali.

Il loro schema di ripiego si chiama *Stupid Backoff*, «ripiego stupido»: pensavano che uno schema così semplice non potesse in alcun modo essere buono. Cambiarono idea, ma il nome è rimasto: in informatica niente è definitivo come un nome provvisorio.

La domanda è sempre la stessa; è cambiato chi risponde: non più un registro da sfogliare, ma una funzione appresa dai testi.

Il pezzo non lo cerca, lo calcola.

<!-- parte: dove l'analogia scricchiola -->
> **Dove l'analogia scricchiola.** La nonna i pesci li ha visti e mangiati; l'LLM li ha incontrati solo nei testi, e il proverbio te lo spiega benissimo, ma con le parole altrui, senza aver mai avuto una canna in mano. Inoltre la nonna sceglie una parola e la dice, mentre l'LLM consegna il dado truccato per intero, con un punteggio per tutti i pezzi possibili, e solo un passaggio separato (capitolo 10) ne estrae uno. Infine l'orecchio della nonna continua ad allenarsi a ogni pranzo di famiglia, mentre quello dell'LLM resta fermo al giorno in cui l'addestramento è finito.

<!-- parte: sotto il cofano -->
> **Sotto il cofano.** Il conto che regge tutto è la regola del prodotto: P(frase) = P(pezzo 1) × P(pezzo 2 | pezzo 1) × P(pezzo 3 | pezzi 1-2) × … In parole: la probabilità (P) di una frase è il prodotto delle probabilità di ogni pezzo, ciascuna calcolata dando per noti i pezzi che lo precedono (la barra si legge «dato»). Per questo «indovinare il pezzo che segue» e «dare un voto a una frase intera» sono lo stesso lavoro visto da due lati.
>
> Primo conto, costruito apposta (una caricatura). Frase di tre pezzi: il primo ha probabilità 0,5; il secondo, dato il primo, 0,2; il terzo, dati i primi due, 0,1. La frase intera vale 0,5 × 0,2 × 0,1 = 0,01, una su cento: tre pezzi plausibili e il prodotto è già minuscolo. Allunga la frase e anche la più ovvia ha una probabilità da lotteria: ecco perché si confrontano due frasi tra loro, come fa il 200.000 di Pereira.
>
> Secondo conto, la perplexity. Prendi un dado truccato a 10 facce: un esito a probabilità 1/2, nove a 1/18 (9 × 1/18 = 1/2). Ogni esito contribuisce con l'inverso della sua probabilità elevato alla probabilità stessa: l'esito da 1/2 con √2, i nove da 1/18, in blocco, con √18. Si moltiplicano: √2 × √18 = √36 = 6, cioè dieci facce con l'indecisione di un dado a sei. Un modello che non sa niente, con i 128.256 token del vocabolario di Llama 3 tutti ugualmente probabili, ha perplexity 128.256: un dado che non entra in nessun bicchiere.
>
> La perplexity vera si misura su testo reale, e due modelli si confrontano solo se spezzano il testo in token allo stesso modo (capitolo 2).
>
> Un LLM è una funzione dai token a una distribuzione di probabilità sul token successivo (128.256 voci, come sopra). Per N token servono N passaggi in avanti: è l'autoregressivo. Il modello è il file dei pesi: 8 miliardi × 2 byte = 16 GB; l'applicazione lo carica e gli rimanda il testo.

*[Il capitolo prosegue con: Mito da sfatare («è solo statistica»), Nell'uso reale, Prova tu, In tre righe.]*