# Prossima parola, prego

### Viaggio tra le allucinazioni d’autore di un’IA ignorante ma straordinariamente eloquente

Prima ancora che esistessero le macchine che scrivono, esisteva una litigata.

Lunga settant’anni.

Con due fazioni, una domanda e nessuna intenzione di fare pace.

La domanda:

> *Per far parlare una macchina, bisogna insegnarle le regole o farle leggere tanto?*

Detta così sembra una questione da convegno.

In realtà è **tutta** la storia dei modelli linguistici.

E se ti dico chi ha vinto, ti rovino la sorpresa.

Quindi vediamola come un processo.

---

## L’accusa: «le regole»

Nel **1957** un giovane linguista, **Noam Chomsky**, pubblica un libro e un esempio che resterà nei manuali:

> *Colorless green ideas sleep furiously.*

Idee verdi incolori dormono furiosamente.

Grammaticalissima.

Senza senso.

Poi la stessa frase con le parole in ordine inverso:

> *Furiously sleep ideas green colorless.*

Non è nemmeno una frase.

L’argomento è questo: nessuna delle due l’hai mai sentita.

Un modello che impara contando ciò che ha già sentito le tratterebbe allo stesso modo.

Eppure tu vedi la differenza.

Quindi, dice Chomsky, **la grammatica non si ricava dalle statistiche**.

Nel 1969 va oltre: la «probabilità di una frase» sarebbe una nozione del tutto inutile. [DA VERIFICARE: parole esatte e sede, saggio del 1969]

L’accusa è chiara.

Cerchiamo i testimoni della difesa.

---

## La difesa: «i conteggi»

**Primo testimone: Markov, 1913.**

Un matematico russo prende le prime ventimila lettere dell’*Evgenij Onegin* e dimostra, contando, che in un testo ogni lettera dipende da quella che precede.

Dopo una vocale ne segue un’altra circa 13 volte su 100.

Dopo una consonante circa 66. [DA VERIFICARE: i numeri, da riconfrontare con il saggio originale]

Non prevede niente.

Ma ha aperto la porta.

**Secondo testimone: Shannon, 1948 e 1951.**

Un ingegnere dei Bell Labs apre un libro a caso, segue le parole e si costruisce a mano un inglese finto.

Che comincia con *THE HEAD AND IN FRONTAL ATTACK ON AN ENGLISH WRITER…*

Nel 1951 fa indovinare la lettera successiva a delle persone.

Con molto contesto, stima circa un bit per lettera: i tre quarti dell’inglese, più o meno, sono prevedibili. [cifra dell’abstract, una stima]

**Terzo testimone: Jelinek e IBM, anni Settanta.**

**Fred Jelinek** e il suo gruppo vogliono che una macchina trascriva il parlato.

Non gli interessa chi ha ragione.

Gli interessa che funzioni.

Usano tabelle di quante volte tre parole sono comparse in fila: i **trigrammi**.

Nel 1977 propongono la **perplexity**, che misura quanto il modello esita.

E da quel momento, per la prima volta, **si può misurare chi sta migliorando**.

Si racconta che Jelinek dicesse: «ogni volta che licenzio un linguista, il riconoscitore migliora».

Con ogni probabilità è una leggenda, in versioni diverse. [DA VERIFICARE: forma e data originali]

Ma dà bene il tono del dibattimento.

---

## L’obiezione

La difesa ha un problema serio.

Se una sequenza non è mai comparsa, il modello a conteggi dà probabilità **zero**.

E poiché la probabilità di una frase si ottiene **moltiplicando** quelle dei suoi pezzi, bastava un pezzo mai visto per azzerare tutto.

Chomsky, su questo punto, aveva ragione.

Ma aveva ragione solo contro quel tipo di modello.

Nel 2000 **Fernando Pereira** ripete l’esperimento con un modello più furbo, che raggruppa le parole per somiglianza.

La frase di Chomsky esce **circa 200.000 volte più probabile** di quella rovesciata. [DA VERIFICARE: il rapporto, nel paper del 2000]

Le idee verdi continuano a dormire furiosamente.

Ma ora hanno un punteggio.

---

## Il colpo di scena: i dati

Nel **2007** cinque ricercatori — **Brants, Popat, Xu, Och e Dean** — pubblicano *Large Language Models in Machine Translation*.

Tabelle di conteggi su **fino a 2 mila miliardi di parole**, 1.500 macchine, un giorno di calcolo per il corpus più grande.

Il loro trucco per le sequenze mai viste si chiama **Stupid Backoff**.

Il nome, scrivono, risale a quando pensavano che uno schema così semplice non potesse essere buono.

Poi hanno cambiato idea.

Il nome è rimasto.

È la risposta più brutale alla domanda del processo:

**non serviva essere più furbi.**

Serviva avere molto più testo.

---

## Il giudice cambia aula

Nel frattempo, in un’altra stanza, succede una cosa che non rientra né nelle regole né nei conteggi.

Nel **2003** **Yoshua Bengio** e colleghi propongono un modello neurale: ogni parola diventa una fila di numeri, e la probabilità della successiva è **calcolata**, non cercata in una tabella.

È la fine del problema dello zero.

Nel 2010 **Mikolov** applica le reti ricorrenti.

Nel **2014** arriva l’**attenzione** (Bahdanau, Cho, Bengio, 1 settembre).

Nel **giugno 2017** il **Transformer**, otto autori, ordine dei nomi casuale.

Nel **2018** GPT.

Nel **2020** **Kaplan** e colleghi scoprono che l’errore scende in modo prevedibile al crescere di dimensione, dati e calcolo.

E nel **2022**, a coronare tutto, **ChatGPT**.

Nessuno, nel frattempo, ha insegnato a questi modelli la grammatica.

Eppure scrivono in modo grammaticale.

Questo, per la difesa, è l’argomento finale.

---

## La sentenza

Chi ha vinto?

Dipende da cosa si chiede.

Se si chiede: *si può ottenere la grammatica senza scriverla a mano?*

**Sì.**

Il modello non ha una regola per «gli aggettivi vanno prima del nome».

Ha miliardi di numeri che, messi insieme, si comportano come se l’avesse.

Se invece si chiede: *il modello sa che cosa è vero?*

Qui l’accusa può rialzare la testa.

Perché una macchina addestrata a indovinare la parola successiva impara il **suono** della lingua.

Non necessariamente il **mondo**.

La frase di Chomsky del 1957 era perfetta e vuota.

Una risposta di un modello può esserlo altrettanto.

Grammaticale.

Elegante.

Completamente inventata.

> *Settant’anni dopo, la domanda del processo ha cambiato bersaglio: non più «sa la grammatica?», ma «sa di che cosa sta parlando?».*

Prossima parola, prego.

Ed è da qui che comincia questo libro.
