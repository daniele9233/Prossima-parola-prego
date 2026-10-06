- **Voce:** professore simpatico: caldo, col «tu»; procede per passi annunciati e risponde a quattro dubbi del lettore.
- **Densità di battute:** 8 battute in circa 1.580 parole, una ogni 200 circa; almeno una per quarto di testo.
- **Analogie usate:** lavagna dell'allibratore (madre); retta della scuola (parametri); osservazione immaginaria (regola di Laplace).

---

# Capitolo 1 — Il completamento automatico più costoso della storia

> Una quota dice quanto ci credi, non quanto hai ragione.

<!-- parte: aggancio -->
## Cinquemila anni di albe

Quanto scommetteresti che domani sorga il sole?

Siamo al bar, è tardi, e io te lo chiedo con la faccia di chi ha un asso nella manica. Tu mi guardi con sospetto, poi per educazione rispondi: «Tutto quello che ho». Bene: hai appena fatto una stima. Il conto, quello vero, lo fa nel 1814 il matematico Laplace nell'*Essai philosophique sur les probabilités* («Saggio filosofico sulle probabilità»). Parte da circa cinquemila anni di albe, cioè 1.826.213 giorni di fila senza un'eccezione, applica la sua regola e dà il verdetto in forma di scommessa: quote di circa 1.826.214 a 1 a favore dell'alba di domani [DA VERIFICARE: cifre e passo sul sole nell'*Essai*, 1814].

Fermati sulle parole «a 1». Vogliono dire una mancata alba ogni 1.826.215, circa: un rischio minuscolo, ricavato da una sola informazione, quanti giorni sono passati. Niente astronomia, niente fisica: solo il calendario.

Il bello viene dopo. Laplace avverte che il suo conto vale per chi non sa niente; per chi conosce il principio che regola i giorni e le stagioni, la probabilità è incomparabilmente più grande. Un previsore che dichiara da solo i limiti del proprio conto: una finezza che a certi *chatbot* (i programmi con cui si chiacchiera) a volte manca.

E che c'entra, ti starai chiedendo, il sole con un'intelligenza artificiale (IA)? Moltissimo. Ogni volta che un'IA scrive una parola fa il mestiere di Laplace: guarda ciò che è già successo, mette le quote su ciò che viene dopo e gioca. Lo scoprirai a piccoli passi.

<!-- parte: analogia madre -->
## La lavagna dell'allibratore

Un'agenzia di scommesse un po' speciale: qui non si punta sui cavalli ma sul prossimo pezzo di testo. Alla parete c'è una lavagna e, per ogni pezzo possibile, una quota. Quota bassa, ci credono tutti; quota alta, è un *outsider* (chi parte sfavorito). Come all'ippodromo, solo che i cavalli sono parole e, a puntare male, non perdi la camicia: perdi il filo.

Chi tiene la lavagna si chiama LLM, *Large Language Model* («modello linguistico di grandi dimensioni»). Gli dai un testo e lui scrive una quota per ogni pezzo che potrebbe seguire: una riga per ogni elemento del suo vocabolario, decine di migliaia, a volte più di centomila. Il pezzo si chiama *token*, frammento di testo: una parola, mezza parola, un segno di punteggiatura (come si spezza un testo, nel capitolo 2). Tradotte in probabilità, le righe coprono insieme tutto il 100%: un pezzo successivo da qualche parte c'è, e nessuno resta fuori dalla lavagna.

La lavagna di Laplace aveva due righe, «il sole sorge» e «il sole non sorge», e ragionava in quote a favore: 1.826.214 a 1 che sorga. L'agenzia ragiona in vincite, e sul sole si incassa quasi niente. Il gioco, però, è lo stesso: le quote dicono quanto ci si crede, e se ne gioca una sola.

Una sola, e non sempre il favorito? Domanda giusta: se vincesse sempre il favorito, due risposte alla stessa domanda sarebbero sempre uguali. Invece il pezzo si estrae a sorte, con più chance per le quote basse; come si regola la sorte, nel capitolo 10.

Le quote hanno anche un albero genealogico. Thomas Bayes scrive un saggio sul problema delle probabilità inverse: partire da ciò che hai visto per dire quanto credere a una probabilità che non conosci. Il saggio esce dopo la sua morte, per cura dell'amico Richard Price; Laplace, con una memoria del 1774, riprende e generalizza il problema [DA VERIFICARE: date e sedi di Bayes, Price e Laplace; Stigler 1986 e testi originali].

<!-- parte: cosa succede davvero -->
## Tre passi e una lavagna

Tre passi, uno alla volta.

Primo passo: il giro. Un esempio costruito (illustrativo, non l'uscita di un modello vero; i pezzi sono parole intere). Scrivi «Il sole sorge a»: sulla lavagna compaiono le quote. «Est» è il favorito, «ovest» un outsider, «mezzanotte» sta in fondo, con la quota di un miracolo. Il modello ne estrae una, di solito il favorito: poniamo «est». Il pezzo si accoda, il testo «Il sole sorge a est» rientra intero: lavagna nuova. Una risposta di cento pezzi sono cento giri, cento attraversamenti completi del modello (in gergo *forward pass*, «passaggio in avanti»); chi lavora così, rimettendo in ingresso le proprie uscite, si dice *autoregressivo*. Se fosse uscito «ovest», le lavagne seguenti sarebbero partite da lì: il già estratto, per i giri dopo, è un fatto.

Secondo passo: i parametri. Le quote le calcola il modello con i suoi parametri, detti anche pesi: numeri regolati durante l'addestramento (capitolo 6). Ricordi la retta della scuola? Due numeri, pendenza (quanto sale) e intercetta (l'altezza da cui parte), scelti perché la retta passi il più vicino possibile a una nuvola di punti. Un LLM di taglia «8B» è la stessa idea con circa 8 miliardi di coefficienti (la B sta per *billion*, miliardo), impilati in decine di strati (capitolo 5) che piegano la linea: ne escono curve complicate, e anche qualche scorciatoia sbagliata. Il limite: la retta ha la forma fissata in partenza, un LLM la impara insieme ai coefficienti. I pesi, poi, si possono anche pesare: a due byte l'uno (il byte, l'unità di misura della memoria), otto miliardi fanno sedici miliardi di byte, cioè 16 GB (gigabyte). Il modello è quel file: pesante, ma pur sempre un file di numeri.

E mentre chiacchieriamo, il modello impara da me? No. Durante la conversazione i coefficienti restano fermi: cambia il testo che entra, non la retta.

Terzo passo: tutto il resto. Il modello non conosce finestre di chat, cronologie o calcolatrici: sono programmi che gli stanno intorno, come il bancone e la cassa stanno intorno alla lavagna. Il programma prende il tuo messaggio, lo gira al modello, ritira le quote e ti porta la risposta. La «memoria» è testo vecchio rimesso sotto gli occhi del modello (capitolo 11); gli strumenti, cercare sul web o fare un calcolo, nel capitolo 18.

I verbi di questo capitolo («ci crede», «gioca», «sa») sono metafore da agenzia: nessuno scommette davvero. A ogni giro una catena di moltiplicazioni sforna una lavagna intera, e basta. Ripeterlo a ogni riga stancherebbe tutti, me per primo: portati dietro le virgolette.

Allora il modello è come il previsore di Laplace, che parte dall'ignoranza? No: la regola di Laplace conta soltanto le albe; le quote di un LLM nascono da miliardi di coefficienti messi a punto su una quantità enorme di testo: più informazione di un conteggio, ma ricavata dai testi, non dal cielo. Più informato, però, non vuol dire infallibile (capitolo 12).

Il filo di Laplace arriva ai modelli che contano le sequenze di parole già viste (gli *n-grammi*, sequenze di n parole): stimando con le sole frequenze, una sequenza mai incontrata vale zero, e basta lei ad azzerare l'intera frase. «Mai visto» non vuol dire «impossibile»: vuol dire che non eri lì. Il rimedio più semplice, un'osservazione immaginaria per ogni parola, si chiama *add-one* («aggiungi uno») e porta il nome di Laplace, ma regala a tutte la stessa mancia, e la pagano le parole già viste. La stessa idea, rifinita, è di Good nel 1953 [DA VERIFICARE: Good 1953, *Biometrika*; nome «di Laplace» sui manuali].

<!-- parte: dove l'analogia scricchiola -->
> **Dove l'analogia scricchiola.** Le quote di un allibratore vero contengono il suo margine: se le trasformi in probabilità e le sommi superi il 100%, perché il banco vende più probabilità di quante ne esistano, mentre quelle di un modello sommano esattamente 1 (il conto è nel box qui sotto). Al banco, poi, non serve capire il cavallo, gli basta che i conti tornino; il modello i testi li ha letti, e le sue quote ne portano il segno. Per questo la lavagna spiega bene che cosa esce e molto meno come: dietro ogni quota non c'è un banco che bilancia le puntate, ma un enorme conto di moltiplicazioni.

<!-- parte: sotto il cofano -->
> **Sotto il cofano.** Parti da un'ignoranza dichiarata: di un evento non sai nulla e lo vedi riuscire n volte di fila, senza un'eccezione. Per Laplace la probabilità che riesca ancora è (n+1)/(n+2). A parole: aggiungi uno alle riuscite e due alle prove, come se avessi già visto un successo e un insuccesso immaginari. Per n = 1, 2, 3, 10, 100 viene 2/3, 3/4, 4/5, 11/12 = 0,917, 101/102 = 0,990. Dove l'immagine scade: quei due esiti non sono dati, sono la tua ignoranza messa a verbale, e per una moneta che sai equa tre teste di fila non spostano il 1/2. Ogni probabilità si porta dietro le sue ipotesi, e smarrirle è il modo più preciso di sbagliare.
>
> Il sole. 5000 × 365,2425 (anno gregoriano medio) = 1.826.212,5, circa 1.826.213 giorni; «circa» perché non so quale anno usasse Laplace. Con n = 1.826.213 la probabilità che sorga ancora è 1.826.214/1.826.215. Le quote a favore sono la probabilità del sì divisa per quella del no: (1.826.214/1.826.215) ÷ (1/1.826.215) = 1.826.214 a 1. Il rischio di una mancata alba è 1 su 1.826.215, circa 5,5 su 10 milioni: con un rischio così, la riunione di domani mattina resta convocata.
>
> Il banco. Esempio costruito, non quote vere: tre esiti con quote decimali (quanto incassi per ogni euro puntato, puntata compresa) di 1,8, 3,5 e 4,5. La probabilità nascosta in una quota è uno diviso per la quota: 1/1,8 = 0,556; 1/3,5 = 0,286; 1/4,5 = 0,222. Somma: 1,063, cioè 106,3% (sui valori esatti: i tre arrotondati darebbero 1,064). Il banco vende il 6,3% di probabilità che non esiste, e di quel 6,3% vive: non di fiuto per i cavalli. Le probabilità di un modello, per costruzione, sommano esattamente 1.

*[Il capitolo prosegue con: Mito da sfatare («è solo statistica»), Nell'uso reale, Prova tu, In tre righe.]*
