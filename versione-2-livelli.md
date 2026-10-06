# Prossima parola, prego

### Viaggio tra le allucinazioni d’autore di un’IA ignorante ma straordinariamente eloquente

Ogni grande idea dell’informatica nasce così:

qualcuno trova un problema nella grande idea di prima.

Non è un difetto del progresso.

È il suo motore.

I modelli linguistici sono la storia di **cinque problemi**, e di chi ha avuto la pazienza di risolverli.

Uno alla volta.

Come in un videogioco in cui ogni livello ti regala il boss del livello dopo.

---

## Livello 1. «Chi viene dopo?»

**Il problema.** Un testo non è un mucchio di parole.

Ogni pezzo dipende da quelli che lo precedono.

**Chi l’ha affrontato.** **Andrej Markov**, matematico russo, **1913**: le prime ventimila lettere dell’*Evgenij Onegin*, contate a mano.

Dopo una vocale ne segue un’altra circa 13 volte su 100.

Dopo una consonante circa 66. [DA VERIFICARE: i numeri, da riconfrontare con il saggio originale]

**Claude Shannon**, **1948**, prende il discorso e lo rovescia: se so le probabilità, posso **generare** il testo.

Apre un libro a caso, segue le parole, e ottiene un inglese finto che comincia con *THE HEAD AND IN FRONTAL ATTACK ON AN ENGLISH WRITER…*

Un generatore di testo fatto di carta e pazienza.

**La soluzione.** Contare quanto spesso, dopo certe parole, ne arrivano certe altre.

Si chiamano **n-grammi**: due parole, tre parole, cinque.

Negli anni Settanta **Fred Jelinek**, a IBM, li usa per far trascrivere il parlato a una macchina.

E nel 2007 un gruppo — Brants, Popat, Xu, Och, Dean — li porta a **2 mila miliardi di parole**.

Con un articolo che si intitola, già allora, *Large Language Models in Machine Translation*.

Il livello è superato.

Ma il boss del livello dopo è già sullo schermo.

---

## Livello 2. «Ma questo non l’ho mai visto»

**Il problema.** Con i conteggi, una sequenza mai incontrata vale **zero**.

E poiché la probabilità di una frase si calcola **moltiplicando** quella dei suoi pezzi, uno zero cancella tutto.

Chomsky lo disse con eleganza nel **1957**:

> *Colorless green ideas sleep furiously.*

Una frase che nessuno ha mai sentito, e che un modello a conteggi tratta come spazzatura.

Anche se è grammaticale.

**Rattoppi.** Tantissimi.

Aggiungere un po’ di probabilità a tutto.

Dare un po’ di quella a chi non è mai comparso.

Quando non trovi un trigramma, ripiega su un bigramma, con uno sconto.

Il ripiego del 2007 si chiama **Stupid Backoff**.

Il nome, scrivono gli autori, nacque quando pensavano che fosse una soluzione troppo semplice per essere buona.

**La vera soluzione.** Nel **2003**, **Yoshua Bengio** e colleghi cambiano il modo di pensare.

Invece di una tabella di sequenze, una **funzione**.

Ogni parola diventa una fila di numeri.

Parole simili, numeri simili.

Così, una frase mai vista somiglia a una già vista, e non vale zero.

Il livello è superato.

Ma adesso c’è un altro boss.

---

## Livello 3. «Mi sono dimenticato che cosa stavo dicendo»

**Il problema.** Un trigramma ricorda tre parole.

Una frase lunga, di più.

**Chi l’ha affrontato.** Le **reti ricorrenti**.

Leggono un pezzo alla volta e tengono un riassunto di quello che hanno letto.

Nel **2010** **Tomas Mikolov** e colleghi ne propongono una per il linguaggio.

Nel **2015** **Andrej Karpathy** ne addestra una su *Guerra e pace*, e un’altra su Shakespeare: lettera dopo lettera, scoprono le virgolette, i nomi, i due punti.

Sul codice del kernel di Linux recitano la licenza GNU.

E in un campione da Wikipedia, scrive lui, il modello inventa un indirizzo web.

> *Il modello se l’è semplicemente allucinato.*

(Era il maggio 2015.)

**La novità del 2014.** **Sutskever, Vinyals e Le** traducono con due reti ricorrenti: una legge la frase, l’altra la scrive.

E scoprono un trucco bizzarro: se leggi la frase **al contrario**, il risultato migliora.

Il punteggio di traduzione passa da 25,9 a 30,6.

Loro stessi ammettono di non avere una spiegazione completa.

Una scoperta fatta per tentativi.

Come un meccanico che batte sul motore e funziona.

**Il boss nuovo.** Tutta la frase deve passare per un **collo di bottiglia**.

Una sola fila di numeri, per riassumere venti parole.

---

## Livello 4. «Guarda dove ti serve»

**La soluzione.** Il **1 settembre 2014**, **Bahdanau, Cho e Bengio**.

Il modello, invece di riassumere tutta la frase in un colpo solo, può **tornare a guardare** le parole giuste mentre scrive.

Lo chiameranno **attenzione**.

(Non l’hanno inventata dal nulla: citano un lavoro analogo di Graves sulla scrittura a mano.)

Funziona.

Ma restano due problemi, uno tecnico, uno di tempo.

Leggere una parola alla volta non si può **fare in parallelo**.

E per allenare le reti su cose grandi serve parallelismo.

---

## Livello 5. «Basta con la fila»

**La soluzione.** **12 giugno 2017.** Otto persone caricano su arXiv un articolo dal titolo *Attention Is All You Need*.

**Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin.**

L’ordine dei nomi, dichiarano, è **casuale**.

L’idea: togliere del tutto la lettura parola per parola.

Dare a ogni parola la possibilità di guardare tutte le altre, **insieme**.

Si chiama **Transformer**.

Su una macchina con otto schede video, il modello base si allena in **dodici ore**.

Quello grande in tre giorni e mezzo.

Il testo non è mai stato così facile da allenare.

E questo, a sorpresa, apre un livello senza fine.

---

## Bonus level: più grande

Se un modello si allena in parallelo, puoi darlo in pasto a più testo.

Nel **giugno 2018** **GPT** impara prima a leggere, poi a fare un compito.

Nel **gennaio 2020** **Kaplan** e colleghi mostrano che l’errore del modello scende in modo prevedibile quando crescono dimensione, dati e calcolo.

Nel **maggio 2020** **GPT-3**: 175 miliardi di parametri.

Nel **marzo 2022** **Chinchilla** (DeepMind) scopre che conta anche allenare a lungo: con 70 miliardi di parametri e 1,4 mila miliardi di token, batte modelli molto più grandi.

E il **30 novembre 2022** esce **ChatGPT**.

Cinque problemi.

Cinque soluzioni.

E in cima alla scala, un boss che nessuno aveva previsto.

---

## Il boss finale

Ogni livello ha una cosa in comune.

Ogni soluzione ha migliorato la **previsione**.

Nessuna ha migliorato la **verità**.

Un modello è addestrato a indovinare cosa viene dopo.

Non a controllare se è vero.

Un indirizzo web inventato ha lo stesso aspetto di uno vero.

Perché, per chi indovina, **ha lo stesso aspetto**.

> *Ogni livello risolve il problema del precedente e ne regala uno nuovo. Questo, con tutta probabilità, vale anche per il prossimo.*

Prossima parola, prego.

E da qui, davvero, comincia questo libro.
