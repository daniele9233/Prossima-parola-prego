# Prossima parola, prego

### Viaggio tra le allucinazioni d’autore di un’IA ignorante ma straordinariamente eloquente

Nel 1957 un linguista scrisse una frase perfetta.

Perfetta nella grammatica.

Inutile nel significato.

Eccola:

> *Colorless green ideas sleep furiously.*

«Idee verdi incolori dormono furiosamente.»

Soggetto, verbo, avverbio, tutto al posto giusto.

Se la leggi in fretta sembra una frase.

Se la leggi con calma sembra l’oroscopo di un segno zodiacale che non esiste.

Il linguista si chiamava **Noam Chomsky**, e la frase era un'esca.

Subito dopo ne scrisse un'altra, la stessa con le parole in ordine inverso:

> *Furiously sleep ideas green colorless.*

Questa non è nemmeno una frase.

È un mucchio di parole che aspetta l'autobus.

Il ragionamento, in sostanza, era questo: nessuna delle due è mai comparsa in un discorso inglese.

Quindi un modello che impara dalle frasi già sentite le tratterebbe allo stesso modo.

Per lui sarebbero la stessa cosa: **zero**.

Ma noi sappiamo benissimo che la prima è grammaticale e la seconda no.

Quindi, concludeva Chomsky, contare ciò che si è già sentito non può bastare.

Dodici anni dopo, nel 1969, arrivò a definire la «probabilità di una frase» una nozione **del tutto inutile**. [DA VERIFICARE: le parole esatte e la sede, saggio su Quine, 1969]

Tieni a mente questa frase.

Tra qualche pagina scoprirai che è esattamente il mestiere di un LLM.

Ma non anticipiamo.

---

Intanto, in un laboratorio dall'altra parte dell'America, succedeva una cosa molto poco filosofica.

A IBM un gruppo di ingegneri guidato da **Fred Jelinek** voleva che una macchina trascrivesse il parlato.

Non gli interessava sapere se il linguaggio fosse «davvero» statistico.

Gli interessava che funzionasse entro giovedì.

Usavano tabelle di conteggi: dopo queste due parole, quante volte è venuta quest'altra?

Si chiamavano **trigrammi**: tre parole in fila.

Una specie di nonna, ma con la memoria di un pesce rosso.

Ricordava soltanto le ultime due cose che le avevi detto.

E funzionava.

Più o meno.

Nel 1977 il gruppo presentò anche una misura per dire quanto un modello è indeciso: la **perplexity**.

Il nome è l'unico caso in cui un termine tecnico dice la verità sul proprio stato d'animo.

Se la perplexity è 6, il modello sta esitando come davanti a un dado a sei facce.

Se è 100 mila, davanti a un dado che non entra in nessun bicchiere.

---

Di Jelinek circola una frase irresistibile:

> *Ogni volta che licenzio un linguista, il riconoscitore migliora.*

Bellissima.

Si racconta che l'abbia detta lui.

Si racconta in versioni diverse, con date diverse, in posti diversi.

È quasi certamente una **leggenda**: troppo perfetta per non essere stata ritoccata da chi l'ha raccontata. [DA VERIFICARE: forma e data originali]

Come tutte le leggende, viaggia più in fretta dei fatti.

Ha una battuta.

I fatti hanno le note a piè di pagina.

---

Veniamo al punto, che arriva nel 2000.

Un ricercatore, **Fernando Pereira**, prese le due frasi di Chomsky e le diede in pasto a un modello statistico addestrato su testi di giornale.

Non un modello che conta frasi intere.

Uno più furbo, che raggruppa le parole per «aria di famiglia»: *verde* e *rosso* compaiono negli stessi posti, *dormire* e *camminare* pure.

Risultato: la frase grammaticale veniva fuori **circa 200.000 volte più probabile** di quella rovesciata. [DA VERIFICARE: il rapporto e i dettagli del modello nel paper di Pereira, 2000]

Le idee verdi continuavano a dormire furiosamente.

Ma adesso avevano un punteggio.

Attenzione: il colpo del 1957 restava geniale.

Colpiva i modelli che si limitano a contare ciò che hanno già visto.

Non ogni modello statistico.

Sembra un dettaglio.

È tutta la storia.

---

Nel frattempo i conteggi diventavano giganteschi.

Nel 2007 un gruppo di ricercatori pubblicò un articolo con un titolo che oggi suona quasi profetico: *Large Language Models in Machine Translation*.

«Grandi modelli linguistici.»

Nel 2007.

Erano tabelle di conteggi su **fino a 2 mila miliardi di parole**, non reti neurali, ma il nome c'era già.

Lo schema per gestire le sequenze mai viste si chiamava **Stupid Backoff**, «ripiego stupido».

Gli autori lo spiegano con una sincerità rara:

il nome nacque quando pensavano che uno schema così semplice **non potesse essere buono**.

Poi cambiarono idea.

Il nome rimase.

> *In informatica niente è definitivo come un nome provvisorio.*

---

Adesso vediamo cosa c'entra tutto questo con il chatbot che ti sta aspettando sul telefono.

Un modello linguistico, oggi, fa una cosa sola.

Prende un testo.

E assegna un punteggio a **ogni pezzo che potrebbe venire dopo**.

Poi ne sceglie uno.

Lo attacca al testo.

E ricomincia.

Se moltiplichi tra loro le probabilità di tutti i pezzi scelti, ognuna calcolata sapendo quelli che la precedono, ottieni la probabilità dell'**intera frase**.

Cioè proprio quella nozione «del tutto inutile».

Per sessant'anni l'abbiamo chiamata «statistica».

Oggi la chiamiamo ChatGPT.

Cosa è cambiato?

Non la domanda.

La domanda è sempre la stessa: *che cosa viene dopo?*

È cambiato chi risponde.

Prima un registro di conteggi da sfogliare.

Adesso una funzione, con miliardi di numeri regolati su una quantità di testo che nessuna nonna potrebbe ascoltare in mille vite.

Per questo può scrivere poesie, spiegare le tasse e litigare con te sull'uso del congiuntivo.

Ma attenzione.

Una funzione addestrata a indovinare quale parola suona giusta ha una proprietà inquietante.

Non è addestrata a distinguere ciò che è vero.

È addestrata a **suonare giusta**.

E «suonare giusta» è proprio il talento della prima frase di Chomsky.

Perfetta.

Elegante.

Impeccabilmente grammaticale.

E senza il minimo problema a dormire furiosamente.

Prossima parola, prego.

> *Un modello linguistico non sa di non sapere. Ma ne parla con straordinaria eloquenza.*

Ed è da qui che comincia questo libro.
