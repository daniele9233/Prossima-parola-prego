# Prossima parola, prego

### Viaggio tra le allucinazioni d’autore di un’IA ignorante ma straordinariamente eloquente

Nessuno ha inventato l’intelligenza artificiale che scrive.

Se la sono passata.

Come in una staffetta, ma con più litigi e meno tute aderenti.

Ogni corridore ha preso il testimone, ha corso la sua frazione, ha detto «io più di così non so fare» e l’ha passato a quello dopo.

Il testimone, per tutta la gara, è stato una domanda sola:

> *Dato ciò che è già stato scritto, che cosa viene dopo?*

Vediamo chi l’ha portata.

---

## Prima frazione: un matematico che conta lettere

Siamo nel **1913**, a San Pietroburgo.

Un matematico russo, **Andrej Markov**, prende le prime **ventimila lettere** dell’*Evgenij Onegin* di Puškin.

Non per gusto letterario.

Per litigare con un collega.

La disputa riguardava l’indipendenza degli eventi, e non era nemmeno l’unica che Markov avesse in corso. [DA VERIFICARE: la polemica con Nekrasov e i dettagli del saggio]

Markov si chiede una cosa banale: la lettera che arriva dipende da quella che c’era prima?

Conta vocali e consonanti.

Risultato, secondo i suoi conti: dopo una vocale ne segue un’altra circa **13 volte su 100**.

Dopo una consonante, circa **66 volte su 100**.

Se le lettere fossero indipendenti, sarebbero circa 43 su 100 in entrambi i casi. [DA VERIFICARE: i numeri, da riconfrontare con il saggio originale]

Dunque il passato conta.

Markov **non** prevede niente.

Conta.

Ma ha messo nel testimone la prima cosa che serviva:

> *In un testo, ogni pezzo dipende da quelli che lo precedono.*

---

## Seconda frazione: un ingegnere con un libro

**1948.** **Claude Shannon**, ai Bell Labs, pubblica la teoria dell’informazione.

Dentro, quasi di passaggio, c’è un gioco.

Come si costruisce un inglese finto?

Si apre un libro a caso, si sceglie una parola, si apre un altro punto e si legge fino a ritrovarla, poi si annota quella che la segue.

E si ripete.

Il risultato comincia così:

> *THE HEAD AND IN FRONTAL ATTACK ON AN ENGLISH WRITER THAT THE CHARACTER OF THIS POINT IS THEREFORE ANOTHER METHOD…*

Shannon stesso commenta che il pezzo «attack on an English writer that the character of this» non è per niente irragionevole.

Il primo generatore di testo della storia funzionava con carta, libri e pazienza.

Nel **1951** fa di meglio: chiede a delle persone di indovinare la lettera successiva di un testo vero.

Dai risultati ricava che l’inglese, con molto contesto, richiede circa **un bit per lettera**, con una ridondanza di circa il **75%**: la cifra è nel suo abstract, ed è una stima, non una misura esatta.

Tradotto: più o meno tre lettere su quattro, in inglese, sono prevedibili.

Il testimone cambia così:

> *Prevedere la lettera successiva non è un trucco da salotto. È misurare quanto una lingua è prevedibile.*

---

## Terza frazione: l’arbitro fischia

**1957.** Un linguista, **Noam Chomsky**, scrive una frase perfetta e senza senso:

> *Colorless green ideas sleep furiously.*

Argomento: nessuno l’ha mai sentita, quindi un modello che conta ciò che ha già sentito la tratta come la sua versione rovesciata.

Eppure noi vediamo la differenza.

Dunque — conclude — **contare non basta**.

È un fischio d’arbitro.

I modelli a conteggi, così com’erano, hanno un problema serio.

Ma nel frattempo, in un laboratorio dall’altra parte dell’America, qualcuno ha deciso che il problema è un problema d’ingegneria.

---

## Quarta frazione: IBM, con le tabelle

Dal **1972** **Fred Jelinek** guida a IBM un gruppo che tratta il parlato come un messaggio che arriva da un canale rumoroso.

Il suo lavoro: indovinare, tra tutte le frasi possibili, quella che la persona ha davvero detto.

Per farlo servono le probabilità delle sequenze di parole.

Quindi: **trigrammi**.

Tre parole in fila, e una tabella enorme di quante volte sono comparse.

Nel **1977** il gruppo propone la **perplexity**, una misura di quanto un modello è indeciso.

Perplexity 6 significa: esita come davanti a un dado a sei facce.

Per la prima volta ci si può chiedere, con un numero: *quanto è bravo questo modello?*

E il numero si può far scendere.

Si racconta che Jelinek dicesse che ogni volta che licenziava un linguista il riconoscitore migliorava.

È quasi certamente una leggenda, in molte versioni. [DA VERIFICARE: forma e data originali]

Ma spiega il clima.

---

## Quinta frazione: più dati, più furbizia

**2007.** Cinque ricercatori — Brants, Popat, Xu, Och e Dean — pubblicano un articolo che si intitola *Large Language Models in Machine Translation*.

Sì: «grandi modelli linguistici», quindici anni prima di ChatGPT.

Ma sono tabelle di conteggi, non reti neurali.

Addestrate su **fino a 2 mila miliardi di parole**, su 1.500 macchine.

Lo schema per le sequenze mai viste si chiama **Stupid Backoff**.

Il nome, spiegano gli autori, è nato quando pensavano che uno schema così semplice non potesse essere buono.

Poi hanno cambiato idea.

Il nome è rimasto.

Lezione di quegli anni, che il testimone si porterà dietro:

> *Una cosa stupida con tantissimi dati batte spesso una cosa furba con pochi.*

---

## Sesta frazione: la corsia accanto

Intanto, in un’altra corsia, un gruppo di ricercatori canadesi aveva fatto una cosa diversa.

Nel **2003**, **Yoshua Bengio** e colleghi pubblicano *A Neural Probabilistic Language Model*.

Invece di contare le sequenze, un modello impara a **calcolare** la probabilità della parola successiva.

Usando una rete neurale, che impara anche una rappresentazione dei numeri delle parole.

Il vantaggio è enorme: una frase mai vista non vale più zero.

Perché le parole simili hanno numeri simili.

A quei tempi, la strada dei conteggi era più veloce e più facile.

Ci sono voluti dieci anni perché le due corsie si ricongiungessero.

Nel 2010 **Tomas Mikolov** e colleghi propongono un modello a rete neurale ricorrente.

Nel gennaio 2013 arriva **word2vec**, che impara i vettori di 1,6 miliardi di parole in meno di un giorno.

---

## Ultima frazione, quella che tutti ricordano

Il resto lo trovi nel prossimo capitolo, ma ti do le tappe.

**Settembre 2014:** un modello impara a «cercare» le parti rilevanti della frase mentre traduce.

**Giugno 2017:** otto persone pubblicano il *Transformer*.

**Giugno 2018:** **GPT**.

**Febbraio 2019:** **GPT-2**.

**Maggio 2020:** **GPT-3**, 175 miliardi di parametri.

**30 novembre 2022:** **ChatGPT**.

Il testimone è sempre lo stesso.

Cambia solo chi risponde.

Da una tabella a una funzione con miliardi di numeri.

E questa è la parte interessante.

Un modello addestrato a dire ciò che viene dopo non è addestrato a dire ciò che è **vero**.

È addestrato a dire ciò che **suona giusto**.

Prossima parola, prego.

> *Ogni corridore ha consegnato al successivo una cosa che sapeva fare e una che non sapeva ancora. L’ultima è la nostra.*

Ed è da qui che comincia questo libro.
