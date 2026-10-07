# Capitolo 1

## Il gioco di Shannon: costruisci un LLM con un dado

> *Un LLM parla come chi improvvisa un brindisi: una parola alla volta, e senza poter cancellare.*

Facciamo una cosa insolita, per un libro sull’intelligenza artificiale.

Smettiamo di leggere.

E costruiamo.

Non un’app.

Non un sito.

Non un «agente» che ti prenota la cena e poi, per coerenza, la cena la mangia.

Costruiamo un **modello del linguaggio**.

Un LLM in miniatura.

Fatto a mano.

Ti serve:

- una filastrocca;
- una matita;
- una moneta (se sei ambizioso, un dado).

Tempo stimato: dieci minuti.

Il risultato sarà stupido come un cacciavite.

Ma funzionerà.

E in dieci minuti capirai la cosa più importante di tutto il libro.

Nel prologo abbiamo lasciato una macchina che inventa libri mai scritti con l’aplomb di un professore ordinario. Per capire come ci riesce, dobbiamo prima vedere come nasce una parola.

Una sola.

**La prossima.**

---

## La filastrocca

Il materiale è di pubblico dominio e probabilmente lo sai già a memoria:

> *Ambarabà ciccì coccò,*
> *tre civette sul comò,*
> *che facevano l’amore*
> *con la figlia del dottore,*
> *il dottore s’ammalò,*
> *ambarabà ciccì coccò.*

Non è esattamente *Eugenio Onegin*.

Ma ha il pregio di essere breve, di avere una struttura chiara e di non richiedere un dottorato in letteratura russa.

Il compito è semplice.

Prendi la filastrocca, parola per parola.

Per ogni parola, scrivi **quale parola viene subito dopo**.

Tutto qui.

Niente grammatica.

Niente significato.

Non ti serve sapere che cosa sia una civetta, né perché sia sul comò, né che cosa facciano esattamente con la figlia del dottore (la filastrocca, con elegante reticenza, non lo precisa).

Conti solo le coppie.

Alla fine ottieni questa tabella:

| Parola | Cosa viene dopo |
|---|---|
| ambarabà | ciccì (due volte) |
| ciccì | coccò (due volte) |
| coccò | tre |
| tre | civette |
| civette | sul |
| sul | comò |
| comò | che |
| che | facevano |
| facevano | l’amore |
| l’amore | con |
| con | la |
| la | figlia |
| figlia | del |
| del | dottore |
| **dottore** | **il** (una volta), **s’ammalò** (una volta) |
| il | dottore |
| s’ammalò | ambarabà |

Venti coppie in tutto.

Quasi tutte le righe hanno una sola uscita.

Una sola riga ha un bivio: dopo **dottore** si può andare in due direzioni, *il* oppure *s’ammalò*.

Una volta ciascuna.

Cinquanta e cinquanta.

*(Il secondo «coccò», quello che chiude la filastrocca, non ha niente dopo di sé: per questo nella tabella «coccò» ha un solo seguito, «tre».)*

Congratulazioni.

Hai appena **addestrato un modello**.

Costo dell’operazione: una matita.

Consumo energetico: un caffè, a voler essere onesti sul tempo.

---

## Il dado

Adesso si gioca.

Parti da una parola qualsiasi, per esempio **ambarabà**.

Guardi la tabella: dopo *ambarabà* viene sempre *ciccì*.

Scrivi *ciccì*.

Dopo *ciccì*, *coccò*.

Dopo *coccò*, *tre*.

E via così, parola dopo parola, come se qualcuno stesse chiamando i numeri a uno sportello:

*Prossimo, prego.*

*Prossimo, prego.*

*Prossimo, prego.*

Finché arrivi a **dottore**.

Qui la tabella non decide.

Qui decidi tu, o meglio, **decide la moneta**.

Testa: *il*.

Croce: *s’ammalò*.

Se esce testa, scrivi *il*, poi *dottore*, e ti ritrovi di nuovo al bivio.

Lancia ancora.

Testa.

*Il.*

*Dottore.*

Ancora al bivio.

Lancia.

Croce.

*S’ammalò.*

E la tua filastrocca, a questo punto, suona così:

> *…con la figlia del dottore*
> *il dottore il dottore s’ammalò*
> *ambarabà ciccì coccò…*

Una variante che nessun bambino ha mai recitato.

E che, per fortuna, nessuno ci ha chiesto di approvare.

Quanto era probabile, quella variante?

Facciamo il conto, perché in questo libro i conti si fanno:

- dopo *dottore*: *il* → **1/2**
- dopo *dottore* di nuovo: *il* → **1/2**
- dopo *dottore* ancora: *s’ammalò* → **1/2**

1/2 × 1/2 × 1/2 = **1/8**.

Una volta su otto.

Non è un miracolo.

È una moneta lanciata tre volte.

Ma guarda che cosa è appena successo.

Il tuo modello ha **generato testo nuovo**.

Testo che non era nella filastrocca.

Usando solo una tabella di coppie e una moneta.

> *Se oggi qualcuno ti dice che un modello linguistico «inventa», puoi rispondere con serenità: il tuo l’ha fatto con una moneta.*

---

## Chiamiamolo col suo nome

Quello che hai costruito si chiama **modello del linguaggio a bigrammi**.

*Bi-grammi* perché guarda coppie: la parola corrente e quella dopo.

Il suo mestiere è uno solo:

**data la parola che c’è, assegnare una probabilità a ciascuna parola che può venire dopo.**

Per quasi tutte le parole della filastrocca la probabilità è 1 (cento per cento).

Per *dottore* è 1/2 e 1/2.

Ecco.

Un LLM, nel suo nucleo, fa **esattamente questo**.

Solo che, al posto della parola corrente, guarda migliaia di parole di testo.

E per «parole che possono venire dopo» ha un elenco di circa **128.000** candidati (nel caso di Llama 3: 128.256 pezzi di testo, che nel capitolo 3 chiameremo *token*).

E la tabella non è una tabella.

È una funzione enorme, calcolata da miliardi di numeri.

Ma il compito non è cambiato di una virgola:

> *Dato ciò che è stato scritto finora, qual è la probabilità di ciascun pezzo che può venire dopo?*

Tre differenze, se vuoi tenere il conto di ciò che separa la tua filastrocca da ChatGPT:

1. **La memoria.** Il tuo modello ricorda *una* parola. Gli LLM ne ricordano migliaia. (Ci arriveremo: capitolo 13.)
2. **La tabella.** La tua sta su un foglio. Quella di un modello vero non starebbe in nessun luogo fisico esistente, e infatti non esiste: al suo posto c’è una *funzione*. (Capitolo 2.)
3. **Il testo.** Tu hai usato sei righe di filastrocca. Loro, qualche migliaio di miliardi di parole. (Capitolo 8.)

Per diventare *Large*, in sostanza, al tuo modello manca una cosa sola:

**tutto il resto.**

---

## Più memoria, meno fantasia

Proviamo a rendere il modello più intelligente.

Anzi: più *informato*.

Invece di guardare una parola, guardiamo **le ultime due**.

Si chiama modello a **trigrammi**, e la tabella cambia così:

| Le ultime due parole | Cosa viene dopo |
|---|---|
| la figlia | del |
| figlia del | dottore |
| **del dottore** | **il** |
| **dottore il** | **dottore** |
| **il dottore** | **s’ammalò** |
| dottore s’ammalò | ambarabà |

Guarda che cosa è successo al bivio.

Non c’è più.

Dopo «del dottore» viene sempre *il*.

Dopo «il dottore» viene sempre *s’ammalò*.

Il modello non ha più nessuna esitazione: **ha memorizzato la filastrocca.**

Genera *esattamente* quella.

Sempre.

Niente varianti.

Niente moneta.

Niente «il dottore il dottore».

Per misurare quanto è sicuro, serve un numero.

Si chiama **perplessità** e lo inventarono, in un contesto molto lontano dalle filastrocche, gli ingegneri che volevano far trascrivere il parlato a una macchina (ci arriviamo tra poco).

L’idea è meravigliosamente semplice:

> *La perplessità dice tra quante parole, in media, il modello sta esitando.*

Se per ogni parola il modello è indeciso tra due scelte ugualmente probabili, la sua perplessità è **2**: esita come davanti a una moneta.

Se è indeciso tra sei scelte ugualmente probabili, è **6**: esita come davanti a un dado.

E se non esita mai, è **1**: non ha dubbi.

Calcoliamo la perplessità del nostro modello a bigrammi **sulla sua stessa filastrocca**.

Venti parole da prevedere.

In diciotto casi la probabilità della parola giusta è 1: nessun dubbio.

In due casi (i due passaggi che partono da «dottore») è 1/2: dubbio da moneta.

La media «geometrica» (non preoccuparti dell’aggettivo) è 2 elevato a 2/20, cioè 2 alla 0,1.

Risultato: circa **1,07**.

Il tuo modello, sulla filastrocca che ha studiato, è praticamente un registratore.

Esita una volta ogni dieci parole, e di pochissimo.

Quello a trigrammi: **1,00**.

Zero dubbi.

Zero fantasia.

> *Un modello che non sbaglia mai sul testo che ha studiato non ha imparato la lingua. Ha imparato il testo.*

Tienilo a mente.

Tornerà in questo libro con vari nomi e in diverse circostanze, tutte imbarazzanti.

---

## Il problema delle tabelle

Ti stai chiedendo perché non usare tabelle sempre più grandi.

Quattro parole di contesto.

Dieci.

Cinquanta.

Facciamo due conti.

Prendiamo cinquantamila parole (un vocabolario modesto, per l’italiano).

- Tabella a **bigrammi** (una parola di contesto, una da prevedere): 50.000 × 50.000 = **2,5 miliardi di caselle**.
- Tabella a **trigrammi**: 50.000 × 50.000 × 50.000 = **125.000 miliardi di caselle**.

Centoventicinquemila miliardi.

E sono solo due parole di contesto.

Per tre, quattro, cinque…

Rinuncia.

Quasi tutte quelle caselle resterebbero vuote, per una ragione semplicissima: gli esseri umani non scrivono tutte le combinazioni possibili.

Ne scrivono una piccola frazione.

Ma una frazione che non possiamo prevedere in anticipo, perché **continuiamo a inventare frasi che nessuno aveva mai pronunciato prima**.

Un comportamento francamente poco collaborativo.

---

## Shannon e il libro aperto

Qui entra in scena, di nuovo, l’uomo del monociclo.

Nel prologo l’abbiamo lasciato in corridoio, in equilibrio su una ruota, a lanciare palline.

Adesso lo troviamo al lavoro.

Nel **1948**, nel celebre articolo *A Mathematical Theory of Communication*, **Claude Shannon** mostra come *costruire un testo* usando le statistiche di una lingua.

Il suo modello a tabelle, però, non stava su un computer.

Stava **in una biblioteca**.

Il metodo è questo.

Prendi un libro.

Lo apri a caso.

Scegli, a caso, una parola.

La scrivi.

Poi apri il libro a un’altra pagina e leggi fino a quando incontri quella stessa parola.

Scrivi **la parola che la segue**.

Poi apri il libro a un’altra pagina, cerchi *quella*, e scrivi quella che viene dopo.

Ancora.

Ancora.

Ancora.

La tabella era il libro.

Il lancio del dado era aprire una pagina a caso.

Usando coppie di parole, il risultato fu questo:

> *THE HEAD AND IN FRONTAL ATTACK ON AN ENGLISH WRITER THAT THE CHARACTER OF THIS POINT IS THEREFORE ANOTHER METHOD FOR THE LETTERS THAT THE TIME OF WHO EVER TOLD THE PROBLEM FOR AN UNEXPECTED*

Tradotto liberamente: *La testa e nel frontale attacco a uno scrittore inglese che il carattere di questo punto è dunque un altro metodo per le lettere che il tempo di chiunque raccontò il problema per un inatteso.*

Non è Shakespeare.

Ma leggi bene i pezzetti.

*«Attack on an English writer that the character of this»* sembra una frase vera.

Lo notò anche Shannon: nel testo generato, sequenze di quattro o più parole si lasciano infilare in frasi sensate senza troppa fatica [DA VERIFICARE: commento al campione, stesso paragrafo del paper].

Il resto, invece, è nebbia.

Il motivo è lo stesso che hai visto con la filastrocca: il modello vede **una parola alla volta**.

Ogni coppia è sensata.

Il tutto no.

Un testo costruito così assomiglia al linguaggio **in piccolo**, esattamente fin dove arriva la memoria del modello.

E se pensi che sia un gioco da salotto, ricorda che Shannon lo stava usando per rispondere a una domanda seria:

**quanto è prevedibile una lingua?**

Una delle sue stime: se consideriamo la struttura statistica fino a circa otto lettere, **circa metà** di ciò che scriviamo in inglese è dettata dalle regole della lingua [DA VERIFICARE: Shannon 1948, «roughly 50%»].

E solo l’altra metà la scegliamo noi.

Metà del tuo testo, insomma, **è già scritto**.

La cosa è confortante per le macchine.

E leggermente umiliante per noi.

---

## Dall’altra parte dell’oceano, con un registratore

Passiamo agli anni Settanta.

**Frederick Jelinek**, ingegnere di origine ceca, lavora all’**IBM** a un problema che nessuno aveva ancora risolto: far trascrivere il parlato a una macchina.

Il suo ragionamento è affascinante.

Un microfono cattura un suono confuso.

Il suono è compatibile con molte frasi.

Come scegliere quella giusta?

Con la probabilità delle sequenze di parole.

«Ho comprato una *casa* in campagna» ha un’ottima probabilità.

«Ho comprato una *cassa* in campagna» non è impossibile, ma è molto meno probabile.

Quindi: **serve un modello del linguaggio**.

E serve un modo per dire *quanto è buono*.

Nasce così la **perplessità**: la misura che hai appena calcolato sulla filastrocca, introdotta dal gruppo di Jelinek alla fine degli anni Settanta (il lavoro è del 1977 [DA VERIFICARE]).

Per la prima volta si può rispondere, con un numero, alla domanda:

*quanto è bravo questo modello?*

E il numero si può far scendere.

Il che, in ingegneria, è la cosa più vicina al paradiso.

Su Jelinek circola anche una frase celebre, quella secondo cui ogni volta che licenziava un linguista il riconoscitore vocale migliorava.

È quasi certamente una leggenda, in molte versioni.

Ma spiega il clima dell’epoca:

> *Quando puoi misurare, smetti di discutere.*

---

## Più dati, meno furbizia

Facciamo un salto di trent’anni.

**2007.** Cinque ricercatori di Google (Brants, Popat, Xu, Och e Dean) pubblicano un articolo che si intitola *Large Language Models in Machine Translation*.

*Large Language Models.*

Grandi modelli linguistici.

Quindici anni prima di ChatGPT.

Non sono reti neurali: sono **tabelle di conteggi**, come la tua.

Solo che la loro tabella viene costruita su **fino a 2 mila miliardi di parole** (è la cifra dichiarata dagli autori), con un modello da **300 miliardi di sequenze**.

Duemila miliardi.

La tua filastrocca ne ha venti.

Il problema, come abbiamo visto, è che con tabelle così grandi **moltissime sequenze non compaiono mai**.

E allora che cosa fai, quando devi stimare una sequenza lunga che non hai mai incontrato?

Il metodo che propongono è di un’onestà quasi commovente.

Lo chiamano **Stupid Backoff**.

*Ripiego stupido.*

L’idea: se la sequenza lunga non c’è, **ripiega su quella più corta**, senza nessuna sofisticazione matematica.

Niente teoremi eleganti.

Niente raffinatezze.

Il risultato, secondo gli stessi autori, è che con abbastanza dati questo metodo sbrigativo **si avvicina alla qualità dei metodi sofisticati** che erano considerati lo stato dell’arte.

Una cosa stupida, con tantissimi dati, vale quasi una cosa furba.

Tienilo a mente, perché tornerà.

Il nome è una dichiarazione di umiltà: *Stupid*.

La lezione che il settore ne trasse, negli anni dopo: non conta solo l’eleganza.

**Conta la scala.**

---

## Dove l’analogia scricchiola

Per tutto il capitolo abbiamo usato lo **sportello con l’eliminacode**: «Prossimo, prego».

Funziona benissimo per l’idea di fondo.

Una parola alla volta.

Ognuna chiamata dalla precedente.

Ma c’è un punto in cui l’analogia crolla.

All’eliminacode, il numero successivo è **già deciso**: c’è una fila, e il prossimo è il prossimo.

Un modello linguistico non ha una fila.

Ha un **elenco di candidati**, ciascuno con la sua probabilità.

*Cane. Gatto. Latte. Elefante. Ministero.*

Il «prossimo» lo si **estrae** da quell’elenco, come si estrae un numero dalla tombola.

Lo sportello, in sostanza, non ha mai il dubbio.

Il modello, ad ogni parola, **ne ha qualche migliaio**.

---

## Sotto il cofano

> **Sotto il cofano.**
>
> Un **modello del linguaggio** è una funzione: riceve una sequenza di pezzi di testo (parole, o *token*) e restituisce, per ogni pezzo possibile, la probabilità che sia il prossimo. Le probabilità sono numeri tra 0 e 1 e, sommate su tutto il vocabolario, fanno 1.
>
> Nei modelli a **n-grammi** quella probabilità si stima contando. Per i bigrammi:
>
> *probabilità di B dopo A = (quante volte compare la coppia «A B») ÷ (quante volte compare A)*
>
> In parole: se «dottore» compare due volte e «dottore il» una volta, la probabilità di «il» dopo «dottore» è 1 ÷ 2.
>
> La **generazione** è un ciclo: si calcola la distribuzione, si estrae un pezzo, lo si aggiunge al testo e si ricomincia con il testo allungato. Per questo si dice *autoregressiva*: ogni uscita rientra come ingresso.
>
> **Perplessità** = l’inverso della media geometrica delle probabilità assegnate alle parole giuste. Se ogni parola ha probabilità 1/N, la perplessità è N. La tua filastrocca a bigrammi: venti parole, due con probabilità 1/2, diciotto con probabilità 1 → 2^(2/20) = 2^0,1 ≈ **1,07**.
>
> **La crescita delle tabelle:** con un vocabolario di V parole, una tabella a n-grammi (sequenze di n parole) ha circa Vⁿ caselle. Con V = 50.000: bigrammi (V²) 2,5 × 10⁹, trigrammi (V³) 1,25 × 10¹⁴.
>
> **Numeri veri:** Llama 3 ha un vocabolario di 128.256 token (GPT-2: 50.257; Llama 2: 32.000). Il modello di Brants e colleghi (2007) usava fino a 2 mila miliardi di parole e circa 300 miliardi di n-grammi.

---

## Mito da sfatare

> **Mito da sfatare.** *«Quindi un LLM è solo una tabella di probabilità, un pappagallo statistico.»*
>
> Il tuo modello da filastrocca lo è davvero: non può dire nulla che non sia già nelle venti coppie, a parte combinarle.
>
> Un LLM vero, però, non ha nessuna tabella: ha una **funzione appresa**, che **generalizza**. Può dare una probabilità sensata a una frase che non ha mai visto, perché ha imparato a riconoscere strutture, non soltanto sequenze.
>
> Il compito, però, resta quello della tua filastrocca: prevedere il pezzo dopo. E per prevedere bene la parola finale di un giallo («l’assassino è…») bisogna aver seguito la trama. Qui «è solo statistica» smette di essere una risposta e diventa una domanda.
>
> Ci torneremo.

---

## Prova tu

> **Prova tu.** *(Dieci righe di Python, o una moneta e una matita.)*
>
> Se hai un computer, incolla questo programma in un file (per esempio `filastrocca.py`) ed eseguilo con Python 3. Fa quello che hai fatto tu a mano: costruisce la tabella delle coppie e genera un testo nuovo.
>
> ```python
> import random
>
> testo = ("ambarabà ciccì coccò tre civette sul comò che facevano "
>          "l'amore con la figlia del dottore il dottore s'ammalò "
>          "ambarabà ciccì coccò").split()
>
> seguenti = {}
> for a, b in zip(testo, testo[1:]):
>     seguenti.setdefault(a, []).append(b)
>
> parola = "ambarabà"
> frase = [parola]
> for _ in range(25):
>     parola = random.choice(seguenti[parola])
>     frase.append(parola)
> print(" ".join(frase))
> ```
>
> Eseguilo più volte. Ogni tanto uscirà «il dottore il dottore il dottore», perché dopo «dottore» la scelta è 50 e 50.
>
> Poi cambia la filastrocca con un testo tuo (un capitolo di libro, un menù, una mail del condominio) e guarda come la tabella si riempie e come il testo generato, a seconda della lunghezza del brano, passa dal «quasi sensato» al «copia incollato». Se la moneta ti basta, sostituisci `random.choice` con il lancio materiale.
>
> *Banco delle prove: P07.* Il programma funziona senza librerie esterne.
>
> **Versione senza computer (P01).** Chiedi a cinque persone di completare «*Tanto va la gatta al lardo che…*» e conta le risposte. Hai appena fatto una distribuzione di probabilità.

---

## Regola d’uso

> **Regola d’uso.** *Il modello legge le sue stesse parole come se fossero un indizio. Anche quelle sbagliate.*
>
> Ogni parola che un LLM scrive diventa parte del testo da cui prevede la successiva (è il ciclo che abbiamo visto, con la moneta). Se una risposta parte storta, **non correggerla con tre messaggi di fila**: il primo errore è ancora lì, nel testo che il modello rilegge.
>
> Rigenera la risposta, oppure riformula la domanda da capo.
>
> Come con una moneta: a volte conviene rilanciare.

---

## Il boss del livello dopo

Il tuo modello, adesso, genera.

Ma c’è una domanda che non gli abbiamo ancora fatto.

Che cosa succede se gli chiediamo di valutare una frase **mai vista**?

Prendiamo:

> *Il dottore con la figlia.*

Italiano perfetto.

Sensatissimo.

Ma guarda la tabella.

Dopo *dottore*, nella filastrocca, ci sono solo *il* e *s’ammalò*.

Mai *con*.

La probabilità che il tuo modello assegna a «dottore con» è **zero**.

E siccome la probabilità di una frase si calcola **moltiplicando** quelle dei suoi pezzi, un solo zero basta a cancellare tutto:

1 × 1 × 0 × 1 = **0.**

Per il tuo modello, la frase è **impossibile**.

Non «improbabile».

*Impossibile.*

Una frase perfettamente normale, bocciata perché nessuno l’aveva mai scritta prima.

Un limite piuttosto serio, per qualcosa che vorrebbe parlare.

> **Il boss del livello dopo:** una frase mai vista vale zero.

---

*Fatti da verificare, termini nuovi, rimandi e scelte editoriali*

**1. Fatti da verificare (con la fonte primaria suggerita)**

- I sei campioni di testo e il passo «apri un libro a caso» di Shannon: citati dal paper originale, C. E. Shannon, *A Mathematical Theory of Communication*, Bell System Technical Journal, 1948. **Controllare** la stringa esatta del campione a parole (riportata sopra) e l’affermazione sulla ridondanza (circa il 50% considerando la struttura fino a circa otto lettere) sul testo originale.
- La traduzione «libera» del campione di Shannon è un esercizio di stile del libro, non una traduzione ufficiale.
- La **perplessità** introdotta dal gruppo di Jelinek: Jelinek, Mercer, Bahl, Baker, «Perplexity — a measure of the difficulty of speech recognition tasks», 1977 [DA VERIFICARE: titolo, rivista e anno].
- La frase attribuita a Jelinek sui linguisti: presentata come leggenda; se la si vuole citare, verificare forma e data originali.
- Brants, Popat, Xu, Och, Dean, *Large Language Models in Machine Translation*, EMNLP-CoNLL 2007: «fino a 2 mila miliardi di token» e «fino a 300 miliardi di n-grammi» (dal sommario del paper); il fatto che Stupid Backoff «si avvicini alla qualità del Kneser-Ney al crescere dei dati» (idem). **Non verificato:** il racconto sul perché del nome «Stupid Backoff». Nel testo è volutamente lasciato indeterminato.
- Vocabolari: GPT-2 50.257, Llama 2 32.000, Llama 3 128.256 (mappa C01).
- Filastrocca «Ambarabà ciccì coccò»: tradizionale, di pubblico dominio; le varianti regionali esistono, il testo usato è quello più diffuso.

**2. Termini nuovi per il glossario**

- **modello del linguaggio**: funzione che dà una probabilità a ogni possibile pezzo di testo successivo.
- **bigramma / trigramma / n-gramma**: sequenza di 2 / 3 / n parole consecutive.
- **perplessità**: quante scelte, in media, il modello sta soppesando a ogni parola; 1 = nessun dubbio.
- **autoregressivo**: che rimette la propria uscita in ingresso.
- **Stupid Backoff**: ripiego sulla sequenza più corta quando quella lunga non compare.

**3. Rimandi**

Token → cap. 3; funzione al posto della tabella e problema dello zero → cap. 2; memoria di migliaia di parole → cap. 13; addestramento su miliardi di parole → cap. 8; perché il modello inventa → cap. 15.

**4. Scelte editoriali fatte in autonomia**

- Ho usato una filastrocca e una moneta, invece di un testo letterario, perché l’esercizio si completa in dieci minuti e ha un solo bivio.
- Ho lasciato Markov e Shannon al prologo e qui ho tenuto solo il metodo del libro aperto di Shannon.
- Ho dato la formula dei bigrammi una sola volta, nel box tecnico, con la lettura a parole.
- L’eliminacode compare una volta nel corpo e una volta nel «dove l’analogia scricchiola».
- Ho cambiato il rimando alla perplessità (da «dado a sei facce» a «moneta e dado»), per dare anche un conto fatto a mano.
