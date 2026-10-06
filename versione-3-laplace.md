# Prossima parola, prego

### Viaggio tra le allucinazioni d’autore di un’IA ignorante ma straordinariamente eloquente

Domanda semplice.

Quanto scommetteresti che domani il sole sorga?

Non è una domanda da astronomi.

È una domanda da bar, di quelle che si fanno dopo il secondo caffè.

Pensaci un secondo.

Il sole è sorto ieri.

E l'altro ieri.

E tutti i giorni di cui hai memoria.

Ma «tutti i giorni di cui hai memoria» è una prova?

Oppure siamo soltanto una specie che, dopo averlo visto sorgere abbastanza volte, ha smesso di preoccuparsi?

Nel **1814** un matematico francese, **Pierre-Simon Laplace**, decise di rispondere con un numero.

Ed è proprio il tipo di numero che ti fa venire voglia di rileggere la frase.

---

Il ragionamento era questo.

Supponi di non sapere assolutamente nulla del Sole.

Non sai che è una stella.

Non sai niente di astronomia.

Sai soltanto che finora è sorto sempre.

Laplace fece i conti con circa **cinquemila anni** di albe, cioè **1.826.213 giorni** di fila senza un'eccezione.

Il verdetto, in forma di scommessa:

**1.826.214 a 1.**

Quote di un milione e ottocentomila a uno a favore dell'alba di domani. [DA VERIFICARE: le cifre e il passo nell'*Essai philosophique sur les probabilités*, 1814]

Attenzione alle parole «a 1».

Significa una probabilità di mancata alba di circa **una su 1.826.215**.

Piccolissima.

Non zero.

Il bello è che Laplace non finì lì.

Aggiunse una cautela che oggi suona deliziosamente moderna:

per chi conosce il principio che regola i giorni e le stagioni, la probabilità è **incomparabilmente più grande**.

Tradotto:

il mio numero vale per chi non sa niente.

Chi conosce l'astronomia può scommettere molto di più.

Un previsore che dichiara fin dove arriva il proprio conto.

Una finezza che a certi chatbot, ogni tanto, manca.

---

La regola che Laplace usò è così semplice da sembrare uno scherzo.

La chiamiamo **regola di successione**.

Se un evento è riuscito *n* volte di fila, e non sai nient'altro, la probabilità che riesca anche la prossima volta è:

> **(n + 1) / (n + 2)**

Una volta: 2/3.

Due volte: 3/4.

Tre volte: 4/5.

Dieci volte: 11/12, cioè circa il 92%.

Cento volte: 101/102, circa il 99%.

È come se ti dicessi:

«Aggiungi un successo immaginario e un insuccesso immaginario, e poi conta.»

Un po' di sano scetticismo preventivo.

Attenzione però, perché qui il lettore tecnico alza la mano.

Se lancio una moneta che so essere equa e viene testa tre volte di fila, la probabilità della quarta **non è 4/5**.

È 1/2.

Perché io qualcosa sulla moneta lo so.

La regola funziona solo quando parti dall'ignoranza totale.

> *Ogni probabilità si porta dietro le sue ipotesi. Dimenticarle è il modo più preciso di sbagliare.*

---

Perché ti sto raccontando questa storia?

Perché dentro quella regola c'è già, in miniatura, tutto ciò che fa un modello linguistico.

**Guarda ciò che è già successo.**

**Assegna delle quote a ciò che viene dopo.**

**Scommetti.**

Se oggi apri una chat con un'intelligenza artificiale e scrivi:

«Il sole sorge a…»

dietro le quinte c'è una specie di **lavagna di un allibratore**.

Per ogni pezzo di testo possibile, una quota.

*est*: favorito, quota bassa, ci credono tutti.

*ovest*: outsider.

*mezzanotte*: quota da miracolo.

La differenza con Laplace è soltanto nelle dimensioni.

La lavagna di Laplace aveva due righe: *il sole sorge*, *il sole non sorge*.

La lavagna di un modello linguistico ne ha una per ogni pezzo del suo vocabolario.

In un modello come Llama 3, quello rilasciato da Meta nell'aprile 2024: **128.256**.

Cioè 128.000 pezzi di base più 256 segnali di servizio.

Un'agenzia di scommesse con più di centoventimila cavalli.

E si punta su uno solo.

---

C'è un dettaglio da allibratori che amo particolarmente.

Le quote vere di un allibratore **non sommano al 100%**.

Facciamo un esempio, costruito apposta.

Tre esiti, con quote decimali 1,8; 3,5; 4,5.

La probabilità implicita è 1 diviso la quota:

1 ÷ 1,8 = 0,556.

1 ÷ 3,5 = 0,286.

1 ÷ 4,5 = 0,222.

Somma: **1,063**.

Cioè il 106,3%.

Il banco vende il 6,3% di probabilità **che non esiste**.

È così che si guadagna.

Le probabilità di un modello linguistico, invece, sommano esattamente a 1.

Non c'è nessun banco da mantenere.

C'è soltanto un conto.

Enorme.

Fatto di moltiplicazioni.

---

E il primo problema serio, in tutta questa storia, è quasi filosofico.

Se un evento non è **mai** successo, quale probabilità gli assegno?

Zero?

È la risposta più ovvia.

Ed è anche la più pericolosa.

Perché i primi modelli di testo funzionavano contando le sequenze di parole già viste.

Se una sequenza non compariva mai nel materiale, la sua probabilità valeva zero.

E poiché la probabilità di una frase si calcola **moltiplicando** quella dei suoi pezzi, bastava un solo pezzo mai visto per azzerare tutta la frase.

Un'intera poesia, cancellata da una parola che il modello non aveva mai incontrato.

Il rimedio più semplice, due secoli dopo, fu proprio quello di Laplace:

**aggiungere a ogni parola un'osservazione immaginaria**.

Una mancia per tutti.

Anche per chi non è mai entrato nel locale.

Il difetto è evidente: la mancia la pagano quelli che c'erano.

Per questo è passato alla storia come un rimedio un po' grossolano, ma efficace, e per anni è rimasto in giro con il nome del suo inventore.

Poi, per fortuna, qualcuno ha cambiato approccio.

(Ci sarà tempo di raccontarlo.)

Oggi i modelli non contano più le sequenze.

Le **calcolano**.

Con una funzione, regolata da miliardi di numeri, che dà a ogni pezzo possibile una probabilità positiva, almeno sulla carta.

Questo è l'altro lato della medaglia.

Un modello non dice mai «impossibile».

Dice sempre «poco probabile».

> *Un modello linguistico non ha il coraggio di dire «non lo so». Ha l'educazione di assegnare una quota a tutto.*

---

E adesso viene la parte che mi interessa davvero.

Laplace aveva avvisato:

il mio numero vale per chi non sa niente.

Un modello linguistico è un previsore che sa **moltissimo** sul linguaggio.

E **niente** sul mondo, nel senso in cui lo sapeva Laplace guardando il cielo.

Ha letto una quantità di testo enorme.

Ha imparato quali pezzi tendono a venire dopo quali altri.

Ma non ha mai alzato gli occhi.

Non sa che il sole è una stella.

Sa soltanto che, dopo «Il sole sorge a», di solito arriva *est*.

E qui sta il problema.

Un previsore che dichiara i limiti del proprio conto è una rarità.

Un previsore che **non li conosce affatto**, ma ha una quota per ogni cosa e una voce impeccabile, è una macchina meravigliosa.

E, a volte, pericolosa.

Prossima parola, prego.

Ed è da qui che comincia questo libro.
