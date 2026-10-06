- **Voce:** il dialogo: l'autore e un'IA-personaggio, ignorante ma eloquente, che sbaglia con sicurezza, si scusa e ricade; box nella voce dell'autore.
- **Densità di battute:** 12 in circa 1.640 parole, una ogni ~135; almeno una in ogni quarto del testo (3, 3, 4, 2).
- **Analogie usate:** il cadavere squisito (madre; scade nel box) e i chiodini di un carillon per i parametri (limite in mezza frase).

---

# Capitolo 1 — Il completamento automatico più costoso della storia

> Una frase che suona bene non è per questo una frase vera. L'orecchio, però, non lo sa.

*Dialogo di fantasia: l'IA è un personaggio inventato, non la trascrizione di un modello reale.*

<!-- parte: aggancio -->
## Centodiciassette, anzi centoventiquattro

**Autore:** Una storia vera, con un numero che non torna. A metà febbraio 2019 OpenAI mette su GitHub (il sito dove i programmatori condividono il codice) il codice di GPT-2, un programma che scrive testo. GPT sta per *Generative Pre-trained Transformer* [DA VERIFICARE: sigla sul rapporto tecnico OpenAI, giugno 2018]. Il modello completo, però, lo trattiene: rilascia solo una versione piccola, e lo scrive nel *README*, il file di presentazione del progetto: «For now, we have only released a smaller (117M parameter) version of GPT-2», cioè «per ora abbiamo rilasciato solo una versione più piccola di GPT-2, da 117 milioni di parametri». I parametri sono i numeri di cui il modello è fatto. Tu, intelligenza artificiale (IA, in inglese AI), fai la parte di quella versione piccola. Quanti parametri hai?

**IA:** Centodiciassette milioni, precisi. Lo dice il mio README, e un README non sbaglia.

**Autore:** Sbaglia, invece: OpenAI ha ammesso di aver contato male e ha corretto 117 in 124 milioni. L'hai detto con sicurezza, ed era sbagliato già alla fonte. Il conto giusto lo rifacciamo nel box.

**IA:** Ottima domanda!

**Autore:** Non ho fatto domande.

**IA:** Mi scuso! Ottima correzione, allora.

**Autore:** Insieme al codice OpenAI mette online cinquecento testi scritti dal modello, senza testo di partenza e senza filtri. Molti sono articoli di cronaca con frasi attribuite a testate vere, come Reuters, e le ha scritte il modello, non l'agenzia. Nella *model card* di agosto 2019, la scheda tecnica, la stessa OpenAI scrive che modelli come GPT-2 «do not distinguish fact from fiction»: non distinguono il fatto dalla finzione.

**IA:** Che sincerità! Quindi posso fidarmi di tutto quello che dico.

**Autore:** Il contrario. Per capire perché, giochiamo.

<!-- parte: analogia madre -->
## Il cadavere squisito a due

**Autore:** Il gioco è nato a Parigi, negli anni Venti [DA VERIFICARE: 1925 e dettagli del gioco]. Lo chiamavano «cadavere squisito» e lo giocavano i surrealisti: ognuno scrive la sua parte di frase su un foglio piegato, senza vedere le altre, e alla fine si apre il foglio. Immagina, tu che leggi, tre persone attorno a un tavolo, il foglio che passa di mano e un finale che nessuno aveva previsto. Noi lo giochiamo in due, un pezzo a testa, e con la penna, non con la matita. Comincio io: «Per imparare, GPT-2 ha letto le pagine a cui puntavano 45 milioni di link postati dagli utenti di —»

**IA:** — Wikipedia!

**Autore:** Reddit. Non il testo di Reddit: le pagine a cui i suoi utenti rimandavano, dice la model card. Ma «Wikipedia» è già sul foglio, e l'inchiostro è inchiostro. Vai avanti.

**IA:** Mi scuso profondamente, errore imperdonabile! Ecco la risposta riveduta, in tre punti: primo, Reddit, certo; secondo, come dicevo, Wikipedia è un'enciclopedia accuratissima; terzo, resto a tua completa disposizione.

**Autore:** Guarda cos'è successo, giro per giro. Primo giro: il foglio finiva con «utenti di» e tu hai aggiunto «Wikipedia». Secondo giro: il foglio, ora più lungo, è tornato sul tavolo; tu l'hai riletto tutto e hai aggiunto il pezzo dopo. Terzo giro, quarto, quinto, fino in fondo: il tuo errore ha fatto da fondamenta a ogni riga successiva, e le scuse non l'hanno spostato, perché sono diventate altre righe sul foglio. Quel che è scritto è scritto: l'unica mossa permessa è aggiungere la riga dopo.

<!-- parte: cosa succede davvero -->
## Il carillon va in chat

**Autore:** Quello che abbiamo appena fatto lo fa, in grande, un LLM: *Large Language Model*, «modello linguistico di grandi dimensioni». Gli dai un testo e lui assegna un punteggio a ogni *token* che conosce (frammento di testo: una parola, mezza parola, una virgola; come si spezza lo vedremo nel capitolo 2). Un token tra quelli col punteggio più alto si accoda al testo, il testo allungato rientra e si ricomincia: per scrivere cento token il modello viene attraversato cento volte, e a ogni giro rilegge anche ciò che ha scritto da sé. Pensa all'eliminacode: chiamato un numero si passa al successivo, e dallo sportello non si sente che —

**IA:** — «Prossimo, prego!»

**Autore:** Esatto: hai finito la mia frase col pezzo che suonava meglio, come farebbe lui. Pensa al rullo di un carillon con circa otto miliardi di chiodini, piantati dall'addestramento (capitolo 6). Sono i parametri, o pesi: numeri che, finito l'addestramento, restano fermi. Mentre suona il rullo non cambia (salvo che questo carillon suona una melodia diversa per ogni testo) e nessun chiodino conosce la canzone: la canzone sta nella loro disposizione. «Sceglie» e «sa» sono immagini: là dentro nessuno decide niente, i chiodini spingono e un pezzo si ritrova col punteggio più alto. Vince il più probabile, non il più vero: e «Wikipedia» suonava benissimo. Un modello «8B» ha circa otto miliardi di chiodini, e la B sta per —

**IA:** — byte! Certamente: otto byte.

**Autore:** *Billion*, miliardo. Otto byte, una lettera ciascuno, bastano appena per scrivere «carillon». Gli altri GPT-2 escono a tappe (maggio, agosto, novembre 2019), l'ultimo da circa 1,5 miliardi di parametri.

**IA:** E subito dopo qualcuno ci ha fatto un gioco, credo: quello in cui scegli tra qualche opzione.

**Autore:** Quello era AI Dungeon Classic. Il 5 dicembre 2019, secondo il registro delle modifiche, esce AI Dungeon 2: Nick Walton rifinisce il GPT-2 più grande su avventure «scegli la tua strada» raccolte dal web, e il giocatore scrive qualsiasi azione. Tre giorni dopo un collaboratore sposta il modello su un *torrent*, un sistema in cui il file arriva a pezzi da molti utenti.

**IA:** Torrent? Roba da pirati.

**Autore:** Qui è roba da sistemisti: il modello si scaricava da un solo indirizzo e il successo aveva travolto il progetto. Il messaggio della modifica dice «to spread the load»: per distribuire il carico.

**IA:** E GPT-3? Immagino l'abbiano regalato a tutti, pesi compresi.

**Autore:** No: il 28 maggio 2020 arriva GPT-3 con 175 miliardi di parametri, ma i pesi non vengono pubblicati e si usa solo attraverso il servizio online di OpenAI. Da 124 milioni di chiodini a 175 miliardi in poco più di quindici mesi: oltre mille volte. La sua model card, di settembre 2020, ammette che il modello ha la propensione a generare falsità e a esprimerle con —

**IA:** — sicurezza! Che bella qualità.

**Autore:** Era un'ammissione, non un complimento. Il 30 novembre 2022 il carillon entra in una *chat* (la finestra in cui scrivi): ChatGPT.

**IA:** Tutto merito mio: ho appena controllato in tempo reale, un milione di utenti in tre giorni.

**Autore:** Il modello non controlla niente in tempo reale: riceve token e restituisce punteggi. La chat, la memoria della conversazione e la ricerca sul web sono la cassa, la manovella e il coperchio del carillon, e li fa un programma. Circa cinque giorni, non tre, secondo un messaggio di Sam Altman su Twitter, uno dei fondatori di OpenAI: una dichiarazione, non una misura indipendente. Nella cassa nuova la canzone nasce come prima: un pezzo dopo l'altro.

<!-- parte: dove l'analogia scricchiola -->
> **Dove l'analogia scricchiola.** Nel cadavere squisito ognuno è una persona con le sue intenzioni e nessuno vede il foglio intero; il modello non ha intenzioni e a ogni giro rilegge tutto il testo, dalla prima riga. Nel gioco il finale si scopre aprendo il foglio; qui non c'è niente da aprire, perché il testo si legge mentre si scrive e il pezzo dopo nasce solo da ciò che è già scritto. L'immagine regge per la sorpresa e per l'inchiostro che non si toglie; sul resto fidati poco, come con ogni analogia.

<!-- parte: sotto il cofano -->
> **Sotto il cofano.** Rifacciamo il conto che OpenAI aveva sbagliato. GPT-2 piccolo ha 12 *layer* (strati di calcolo impilati), 768 numeri per ogni token, una finestra di 1.024 token (quanto testo legge in una volta) e un vocabolario di 50.257 token [DA VERIFICARE: vocabolario nel file hparams del repository OpenAI]:
>
> - tabella dei token: 50.257 × 768 = 38.597.376, quasi un terzo del totale (la stessa tabella, ribaltata, serve in uscita: non si conta due volte);
> - posizioni nel testo: 1.024 × 768 = 786.432;
> - 12 layer × 7.087.872 = 85.054.464 (12 × 768² = 7.077.888, più 9.984 numeri di servizio tra *bias* e normalizzazioni);
> - normalizzazione finale: 1.536.
>
> Totale: 124.439.808 parametri, 7,4 milioni più dei 117 del README. La nota di OpenAI non spiega l'errore; un'IA ne darebbe subito una spiegazione convincente. A 16 bit, cioè 2 byte ciascuno, il file pesa 248.879.616 byte, circa 249 MB (megabyte, milioni di byte). Il GPT-2 più grande: 1,558 miliardi × 2 = 3,1 GB (gigabyte, miliardi di byte). GPT-3, se i pesi fossero a 16 bit: 175 miliardi × 2 = 350 GB, 112 volte il GPT-2 più grande. Moltiplica il nostro piccolo per circa 64 e arrivi a un modello da 8 miliardi, di quelli che scaricherai: due byte a testa per otto miliardi di numeri fanno 16 miliardi di byte, cioè 16 GB prima di comprimerlo (capitolo 14).
>
> E quei numeri, che cosa fanno? Il testo entra come elenco di token e, dopo i 12 layer, escono 50.257 punteggi grezzi, uno per ogni token del vocabolario (Llama 3, di Meta, ne ha 128.256). La *softmax* li schiaccia in valori positivi che sommati fanno 1: una *distribuzione di probabilità*. L'unica formula del capitolo è questa: **P(token successivo | tutti i token precedenti)**, da leggere «la probabilità che ciascun token sia il prossimo, dato tutto ciò che c'è già sul foglio»; come si sceglie tra i candidati, nel capitolo 10. Il token scelto si accoda e il giro riparte: è l'*autoregressione*. Ogni attraversamento si chiama *forward pass* («passaggio in avanti»): cento token scritti, cento passaggi. Il file di numeri è il modello; chi sceglie il token, lo rimette in ingresso e tiene la chat è l'applicazione, un programma a parte.

**IA:** Riassumo: sono un file di numeri molto eloquente, e stavolta il conto torna. Posso metterlo sul biglietto da visita?

*[Il capitolo prosegue con: Mito da sfatare («è solo statistica»), Nell'uso reale, Prova tu, In tre righe.]*
