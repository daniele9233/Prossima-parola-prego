- **Voce:** il narratore. Parte dalla lite tra Markov e Nekrasov e la racconta a capoversi brevi, con chiusure che spostano la scena e understatement; il lettore entra con due «Immagina» dichiarati.
- **Densità di battute:** 7 in circa 1.645 parole (una ogni 235 circa), almeno una per pagina: aggancio 1, analogia madre 3, «cosa succede davvero» 2, box tecnico 1; asciutte, a fine capoverso.
- **Analogie usate:** la scimmia dattilografa di Borel in tre livelli (madre), la bilancia con otto miliardi di pesi, l'ufficio intorno alla scimmia, la macchinetta del caffè che «ha deciso», la tabella di Markov a due righe.

---

# Capitolo 1 — Il completamento automatico più costoso della storia

> *Una tabella con tutti i contesti possibili non entrerebbe in nessun magazzino. Così, a un certo punto, invece di compilarla qualcuno ha cominciato a calcolarla.*

<!-- parte: aggancio -->
## Ventimila lettere

Ventimila lettere. Sono l'inizio dell'*Eugenio Onegin* di Puškin, il primo capitolo e sedici strofe del secondo, spogliati di spazi e punteggiatura: di un romanzo in versi resta una fila di vocali e consonanti. A contarle, a mano, è Andrej Markov. Lo scopo non è letterario.

Per capirlo, secondo gli storici, bisogna tornare indietro di undici anni, al 1902. Pavel Nekrasov, matematico di Mosca formatosi in seminario, sostiene che la regolarità delle statistiche sociali provi il libero arbitrio. Le cifre tornano di anno in anno, quindi gli atti umani sono indipendenti, quindi liberi. Per lui, stando agli storici, la legge dei grandi numeri varrebbe solo tra eventi indipendenti.

A San Pietroburgo c'è chi non ci sta. Markov è un accademico dal carattere battagliero: a quanto si racconta lo chiamavano «Andrej il Furioso», e scriveva molte lettere ai giornali. Nel 1906 dimostra che la legge dei grandi numeri vale anche per grandezze legate in catena: l'indipendenza non serve. Nel febbraio 1912 scrive al Santo Sinodo e chiede di essere scomunicato, per protesta contro la scomunica di Tolstoj (1901). All'inizio del 1913 porta all'Accademia delle Scienze un esempio di prove collegate in catena: quelle ventimila lettere.

Che cosa trova, secondo i suoi conti? Che la lettera ha memoria. Dopo una vocale ne segue un'altra circa 13 volte su 100; dopo una consonante, una vocale circa 66 volte su 100. Se le lettere fossero indipendenti, in entrambi i casi sarebbero circa 43. [DA VERIFICARE: date, titoli, conteggi e metodo in Hayes, «First Links in the Markov Chain», American Scientist, marzo-aprile 2013; formazione di Nekrasov e scomunica del 1912 in Seneta, Encyclopedia of Mathematics; soprannome e lettere in Vulpiani, Lettera Matematica Pristem n. 94]

Ci sono molti modi di occuparsi di una questione di teologia. Contare le vocali è il meno frequente.

<!-- parte: analogia madre -->
## Una scimmia, tre memorie

Nello stesso 1913 Émile Borel mette al lavoro un milione di scimmie. Ognuna ha una macchina da scrivere e batte i tasti a caso, dieci ore al giorno, per un anno. A sorvegliarle sono capireparto analfabeti, il che toglie ogni speranza di correzione di bozze; raccolgono i fogli e li rilegano in volumi. È la più antica forma dell'immagine che conosciamo, e serve a misurare quanto sia improbabile un evento. [DA VERIFICARE: Borel, «Mécanique statistique et irréversibilité», Journal de Physique, 1913, su Gallica]

Facciamola salire di tre gradini.

**Livello uno: tasti a caso.** Ogni tasto ha la stessa probabilità e la scimmia non ricorda nulla: ogni lettera è indipendente dalle precedenti. Immagina di sfogliare uno dei volumi rilegati: pagine e pagine, quasi nessuna parola che si lasci leggere. Per il caso un romanzo vale come qualunque altra sequenza: possibile, ma mai successo.

**Livello due: tasti con una memoria.** Concedi alla scimmia un solo ricordo, l'ultima lettera battuta, e una regola: dopo la Q arriva quasi sempre la U. Una scimmia che guarda solo la lettera precedente è una catena di Markov, e basta. Quella di Markov sull'*Onegin* è, per quanto si sa, il primo uso documentato di una catena su un testo. Il testo della scimmia non ha ancora senso, ma ha una grafia che promette: uno di quei capireparto, a questo punto, comincerebbe a crederci.

**Livello tre: la scimmia che ha letto la biblioteca.** Non guarda più l'ultima lettera ma tutto il foglio, e per ogni pezzo che sta per battere ha alle spalle una biblioteca intera. Un LLM, *Large Language Model* («modello linguistico di grandi dimensioni»), è questo. E parla bene di tutto, anche di ciò che nella biblioteca non c'era. Non è un difetto di fabbricazione: è la fabbricazione.

<!-- parte: cosa succede davvero -->
## Il foglio che si allunga

Togli l'immagine e resta una sola mossa. Dato un testo, il modello dice quale pezzo viene dopo: il *token*, un frammento che può essere una parola, mezza parola o un segno di punteggiatura (come si spezza: capitolo 2). Il pezzo va in coda al foglio, il foglio si rilegge da capo e si ricomincia. Il ciclo è tutto qui.

Per vederlo girare basta Markov, ridotto all'osso: la scimmia ricorda solo se l'ultima lettera era vocale o consonante. La sua tabella ha due righe e quattro caselle, e ogni riga fa cento. Dopo una vocale, su 100 lettere 13 sono vocali e 87 consonanti; dopo una consonante, 66 vocali e 34 consonanti. Si guarda l'ultima lettera, si tira un dado da cento facce (quello vero: capitolo 10), si aggiunge, si ripete. Esempio costruito, non un output: da una C, i tiri 41, 72, 90, 12, 55 e 30 danno C V C C V C V. Il livello tre fa lo stesso giro, ma legge tutto il foglio (in Llama 3, aprile 2024, fino a circa 8.000 token) e le scelte a ogni giro sono 128.256, non due.

Il foglio che esce da un giro entra nel successivo: una risposta di 200 token sono 200 giri. Quel che è battuto è battuto, e il resto della frase dovrà farsene una ragione.

Con i token di una lingua, le sole coppie di contesto fanno più di sedici miliardi di righe: conti nel box.

Dal 1913 il filo si perde, poi si ritrova. Nel 2003 Yoshua Bengio e colleghi affrontano la parola successiva con una rete neurale, cioè una funzione fatta di piccoli calcoli collegati. Il 12 giugno 2017 otto autori pubblicano il Transformer, l'architettura dei capitoli 4 e 5. Il 18 aprile 2024 Meta rilascia Llama 3, addestrato su oltre 15 mila miliardi di token. Più dei dati e del calcolo è cambiata l'idea: Markov riempiva la sua riga contando a mano, quella di Llama 3 la calcola una funzione, che riceve il foglio e restituisce 128.256 percentuali, una per token, cento in tutto: la domanda resta quella, che cosa viene dopo.

I parametri di quella funzione, detti anche pesi, sono numeri regolati nell'addestramento (capitolo 6) e conservati in un *file*, dati su disco. Immagina una bilancia con otto miliardi di pesi minuscoli sui piatti (nessun peso, da solo, misura qualcosa di leggibile). L'addestramento li sposta, un granello alla volta, finché le percentuali smettono di sbagliare troppo. Poi la bilancia è tarata e nessuno la tocca: in conversazione i pesi restano fermi, e il modello non impara da te, rilegge. Per un salumiere sarebbe un incubo; per un modello è la taglia piccola.

Un file, però, non conversa. Lo fanno funzionare il programma che lo carica, la *chat* (la finestra dove scrivi), la «memoria» della conversazione (capitolo 11), gli strumenti che cercano in rete o fanno un conto (capitolo 18). La scimmia non esegue niente: batte testo, anche quando chiede uno strumento. Per Borel i capireparto rilegano i fogli e basta; il nostro ufficio a ogni giro rimette il foglio intero sotto il naso del modello. Il modello è la scimmia, il resto è l'ufficio.

Diciamo che il modello «preferisce» una parola o «conosce» un argomento come diciamo che la macchinetta del caffè «ha deciso» di non funzionare: dentro non ha deciso nessuno. Nel modello c'è una fila di moltiplicazioni che finisce in una percentuale per pezzo di testo. Se basti per dire «conosce» è una domanda aperta, ripresa più avanti.

A Markov, nel 1913, bastavano ventimila lettere e quattro caselle.

<!-- parte: dove l'analogia scricchiola -->
> **Dove l'analogia scricchiola.** Una scimmia non impara dai libri e non ha parametri: nel livello tre «aver letto una biblioteca» vuol dire soltanto che miliardi di pesi sono stati spostati finché il modello sbagliava meno a prevedere il testo mostrato. E quella biblioteca non c'è più: mentre scrive, il modello non può aprire nessun libro, ha solo i pesi; per consultare documenti veri c'è il RAG (*retrieval-augmented generation*, capitolo 17). La scimmia di Borel, poi, non è mai stata un modello del linguaggio: è un'ipotesi estrema sul caso. Quanto a Markov, contava e non scriveva: un antenato, non l'inventore del modello del linguaggio.

<!-- parte: sotto il cofano -->
> **Sotto il cofano.** Il muro, in tre mosse. Con i 128.256 token di Llama 3 (aprile 2024: 128.000 di base più 256 speciali), una tabella con un token di contesto ha 128.256² = 16.449.601.536 celle. Con due, 128.256³ ≈ 2,11 × 10¹⁵, circa 140 volte i 15 mila miliardi di token di addestramento: quasi tutte vuote. Con tre, 128.256⁴ ≈ 2,71 × 10²⁰: un faldone che nessun ufficio saprebbe archiviare. I modelli a *n-grammi* (sequenze di n token) aggiravano il muro salvando soltanto le sequenze effettivamente viste. Qui serve una funzione con parametri: miliardi di numeri al posto di 10¹⁵ celle.
>
> Una riga nasce dai conti di Markov su 20.000 lettere: 8.638 vocali e 11.362 consonanti, cioè 8.638 ÷ 20.000 = 0,4319 di vocali. Se le lettere fossero indipendenti, le coppie vocale-vocale sarebbero 20.000 × 0,4319² ≈ 3.731; Markov ne contò 1.104 e 3.827 consonante-consonante. Dopo una vocale ne segue un'altra con probabilità 1.104 ÷ 8.638 = 0,128. Dopo una consonante ne segue un'altra con 3.827 ÷ 11.362 = 0,337, quindi una vocale con 1 − 0,337 = 0,663. Ogni riga (0,128 e 0,872; 0,337 e 0,663) ha voci non negative che fanno 1 in tutto: è una *distribuzione di probabilità*. [DA VERIFICARE: Hayes 2013 o la traduzione di Link e Custance, Science in Context, 2006]
>
> Quanto pesa il file? 8 × 10⁹ pesi × 16 bit = 128 × 10⁹ bit; diviso 8, 16 × 10⁹ byte, cioè 16 GB (gigabyte, miliardi di byte); a 4 bit, circa 4-5 GB (capitolo 14). Ogni giro del ciclo è un *forward pass*, un attraversamento completo del modello, strato dopo strato (i *layer*, capitolo 5); i giri vanno in fila, perché ciascuno parte dal foglio allungato dal precedente: un processo che si nutre delle proprie uscite si dice *autoregressivo*. L'unica formula del capitolo dice cosa calcola ogni giro:
>
> **P(token successivo | tutti i token precedenti)**
>
> Si legge: la probabilità (P) di ciascun token possibile, dato (la barra verticale) tutto ciò che è già stato scritto. È la riga di Markov, allungata a 128.256 voci.

*[Il capitolo prosegue con: Mito da sfatare («è solo statistica»), Nell'uso reale, Prova tu, In tre righe.]*
