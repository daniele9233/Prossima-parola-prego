# Prologo — Prima della prossima parola

Ogni frase che diciamo è preceduta da una scelta che non ricordiamo di aver fatto.

Quando scrivete «buona», il telefono vi mette davanti tre parole: notte, giornata, serata. È un gesto così ordinario che non lo vediamo più. Eppure lì, in quella riga di suggerimenti sopra la tastiera, c'è una teoria del linguaggio, una teoria della probabilità e una teoria della mente, tenute insieme da un'interfaccia che nessuno ha mai progettato per essere studiata.

Il telefono non sa che cosa volete dire. Ha visto, milioni di volte, che cosa viene dopo «buona». È tutto quello che fa, ed è tutto quello che fa un modello linguistico — con una differenza di scala che è anche una differenza di natura: al posto dei messaggi di una persona ci sono i testi di una civiltà, e al posto di tre parole suggerite ci sono centomila pezzi di parola, ciascuno con un numero accanto.

Da questa aritmetica elementare è nato qualcosa che scrive lettere, corregge codice, sostiene un esame di ammissione e inventa, con perfetta sicurezza, sentenze che nessun giudice ha mai pronunciato.

Sette secoli separano il primo tentativo di meccanizzare il pensiero da quel riquadro sopra la tastiera. In mezzo non c'è una linea retta: ci sono due inverni, qualche Prometeo finito male, un matematico che contava le vocali di Puškin per dispetto, una segretaria che chiese di restare sola con un programma di quattrocento righe e un fisico austriaco che morì amareggiato dagli attacchi di chi negava l'esistenza degli atomi.

Questo libro racconta quella staffetta. È la storia di un'idea che sembrava ovvia, si è rivelata impossibile, è rimasta in un cassetto per generazioni ed è tornata fuori quando qualcuno ha costruito il forno giusto.

Lungo il percorso troverete tre tipi di riquadri. **Sotto il cofano** contiene la formula o il codice vero, per chi vuole vedere l'ingranaggio: si può saltare senza perdere il filo. **Provalo tu** è un esperimento da fare subito, e vale più di dieci pagine di spiegazione. **Per chi ama pensare** è una domanda che il capitolo lascia aperta, perché chiuderla sarebbe stato disonesto.

Il libro ha due lettori e non ha intenzione di scegliere. Il primo è un ingegnere di sistema: sa che cosa è una GPU, ha letto un articolo sui transformer, vuole i numeri e i conti. Il secondo non ha mai aperto un terminale, e se gli dite «rete neurale» pensa a un reparto ospedaliero.

Una promessa. Le formule che incontrerete sono vecchie: la più antica ha più di tre secoli. Nessuna è necessaria per andare avanti. Ma se avrete la curiosità di guardarle, vedrete che non sono ornamenti: sono il punto in cui un'idea smette di essere una metafora e comincia a funzionare.

Cominciamo da una macchina che non serviva a sollevare pesi, né a misurare il tempo, né a uccidere. Serviva a pensare.

---

# Capitolo primo — Il sogno di calcolare il pensiero

## L'oggetto inutile

Di quella macchina non resta nessun esemplare. Restano i disegni, nelle opere di chi l'ha inventata, e restano le descrizioni di chi l'ha vista funzionare: dischi di carta sovrapposti, concentrici, con sopra scritti dei nomi.

Bontà. Grandezza. Eternità. Potenza. Sapienza. Volontà. Virtù. Verità. Gloria.

Nove parole, disposte in cerchio. Ruotando i dischi, le parole si allineano in modi sempre diversi, e ogni allineamento è un'affermazione: la bontà è grande, la grandezza è eterna, l'eternità è potente. Chi la usa non deve sapere la teologia: deve saper girare un disco e leggere.

L'uomo che la costruì si chiamava Raimondo Lullo, era maiorchino, era un laico legato al Terz'ordine francescano. Cominciò a costruirla nel 1274 e la rifece per trent'anni: la versione definitiva, che chiamiamo *Ars Magna*, l'arte grande, è del 1305-08. Non era un giocattolo filosofico: era un dispositivo di conversione, e Lullo ci credeva come si crede a una cura.

Vale la pena fermarsi su quest'uomo, perché in lui c'è già tutto il problema che questo libro racconta, e c'è già anche l'errore.

## La domanda del capitolo

Si può ridurre il pensiero a un calcolo meccanico? E se sì, che cosa manca a una macchina che combina tutte le parole possibili per essere intelligente?

## L'arte grande

Lullo visse in un secolo in cui le dispute si risolvevano con i testi e con le spade. Lui aveva capito una cosa che molti suoi contemporanei capivano meno: la spada convince poco. Chi perde una guerra può perdere anche la fede, ma chi perde una discussione, se la discussione è ben condotta, si arrende.

Il problema è che le discussioni non finiscono mai. Ognuno ha i suoi argomenti, i suoi autori, le sue citazioni. E allora Lullo fece un ragionamento che ha la forma di un teorema: se tutte le verità derivano da un piccolo numero di principi, e se i principi sono nove, allora basta enumerare tutte le combinazioni dei principi per ottenere tutte le verità. Non serve più discutere: si gira il disco, si legge, e l'avversario è confutato.

C'è un'ingenuità, in questo, che è quasi commovente. Lullo passò la vita a viaggiare, a predicare, a scrivere centinaia di libri, a farsi cacciare e a tornare. Voleva convertire il mondo con la logica — anche se in anni successivi propose pure una crociata — e la sua macchina era, nelle intenzioni, uno strumento per convincere senza combattere: un dispositivo che permetteva a chiunque — anche a chi non aveva studiato — di generare argomenti corretti.

E funzionava. A modo suo, funzionava davvero: i dischi producevano combinazioni, e le combinazioni erano tante. Il difetto non era nella macchina. Era nell'idea che il numero delle combinazioni fosse un vantaggio.

Per capire perché, bisogna aspettare quattro secoli, e un filosofo tedesco che di Lullo fu lettore appassionato.

## Calculemus

Gottfried Wilhelm Leibniz faceva troppe cose, e le faceva tutte bene. Matematica, filosofia, diritto, diplomazia, storia delle famiglie nobili, biblioteche. Nel 1676 descrisse la regola della catena delle derivate, il meccanismo con cui — tre secoli dopo — si sarebbe fatto apprendere alle reti neurali. Ventisette anni dopo, nel 1703, pubblicò la sua aritmetica binaria, quella fatta solo di zero e uno, che oggi parla dentro ogni computer.

E soprattutto sognò una cosa che non aveva nome.

La chiamò *characteristica universalis*: una lingua di simboli abbastanza precisa da ridurre ogni ragionamento a un calcolo. Se due persone discutono, scriveva, non dovrebbero più litigare. Dovrebbero prendere la penna, sedersi e dirsi: *Calculemus*. Calcoliamo.

È la scena della discussione di Natale, con un finale diverso. Non «ho ragione io», ma «facciamo il conto». Leibniz immaginava un mondo in cui le opinioni fossero sostituibili con i risultati e le liti con delle addizioni, e in cui la verità fosse una proprietà del calcolo invece che una questione di autorità.

Non funzionò, e il motivo è tecnico prima che filosofico: per calcolare bisogna tradurre. Ogni concetto in un simbolo, ogni relazione in una regola, ogni sfumatura in una differenza. Il lavoro di traduzione era enorme, e nessuno sapeva da che parte cominciare. Leibniz morì nel 1716, dimenticato dai più, con l'archivio dei suoi progetti ancora chiuso nei cassetti.

Ma il seme era piantato, e aveva una forma precisa: **se il pensiero è fatto di passi, allora il pensiero si può meccanizzare**. Non serve capire come funziona la mente — questa è la scommessa di Leibniz, ed è la scommessa di questo libro. Serve trovare i passi giusti e farli eseguire a qualcosa che non si stanca.

## La lingua che non si trova

Perché la *characteristica universalis* non fu mai costruita? Perché il problema non era inventare i simboli. Era decidere che cosa un simbolo significa.

Provate con una parola qualsiasi. «Giustizia». Che cosa è? Un simbolo, diciamo G. Bene: che cosa ci si può calcolare sopra? Che G implica l'uguaglianza? Che G è preferibile alla vendetta? Che G vale più di G? Ogni tentativo di definire G produce una lista di eccezioni, e ogni eccezione è una nuova definizione, e ogni definizione apre un'altra discussione.

Leibniz lo sapeva. Il suo progetto non era un gioco: era un'impresa di ingegneria concettuale, e lui ne misurava la difficoltà. Per calcolare bisogna tradurre, e per tradurre bisogna aver già capito. È un circolo, e non si esce dal circolo aggiungendo simboli.

C'è un dettaglio che vale la pena notare. Il sogno di Leibniz non è morto: è stato spostato. Oggi non costruiamo una lingua universale in cui ogni concetto ha un simbolo. Costruiamo macchine che imparano i simboli dai testi, senza che nessuno glieli definisca. Il circolo non è stato spezzato: è stato aggirato.

Il prezzo di quell'aggiramento lo pagheremo più avanti, quando parleremo di allucinazioni: una macchina che non ha definito che cosa significa «giustizia» può usare la parola in modo perfettamente plausibile e perfettamente sbagliato, nello stesso paragrafo.

## Il riso di Swift

Nel 1726 un altro scrittore prese in giro l'idea, e lo fece con una precisione che ancora oggi si legge come una profezia.

Nei *Viaggi di Gulliver*, nell'Accademia di Lagado, un professore ha costruito una macchina enorme: un telaio di legno coperto di tessere, su ogni tessera una parola della lingua. Gli studenti girano delle manovelle, le tessere si rimescolano, e ogni tanto — per caso — compaiono tre o quattro parole di fila che hanno senso. Il professore le fa trascrivere. Così, promette, chiunque potrà scrivere libri di filosofia e di poesia senza alcun talento.

Swift stava ridendo del sogno di Lullo e di Leibniz. Aveva ragione a ridere, ma aveva scelto male il bersaglio: non stava ridendo della macchina, stava ridendo dell'idea che bastasse generare.

Perché la macchina di Lagado funziona. È il punto che sfugge. Se girate le manovelle abbastanza a lungo, quella macchina scriverà davvero l'*Amleto*. E scriverà anche un miliardo di volte l'*Amleto* con una lettera sbagliata, e tutte le ricette di cucina mai scritte, e le vostre memorie, e la lista della spesa di un re che non è esistito. Il problema non è la generazione. Il problema è che nessuno, tra i milioni di fogli, saprebbe quale tenere.

**Mancava il modo di scegliere le parole non a caso.** Swift lo aveva capito benissimo: la sua macchina è comica perché è inutile, ed è inutile perché non sa scegliere.

Ci sarebbero voluti quasi due secoli, e un matematico russo arrabbiato, per trovare il pezzo mancante.

## Le note di Ada

Nel 1843, a Londra, una giovane donna di ventisette anni fece una cosa che ai suoi tempi nessuno considerava un lavoro: tradusse un articolo in francese su una macchina che non esisteva.

La macchina era la Macchina Analitica di Charles Babbage, un calcolatore meccanico progettato e mai costruito, fatto di ingranaggi, schede perforate e un «mulino» che macinava numeri. L'articolo era di un ingegnere italiano, Luigi Federico Menabrea. La traduttrice era Augusta Ada Byron, figlia del poeta, sposata Lovelace.

La traduzione sarebbe stata una cosa modesta. Le note che Ada Lovelace vi aggiunse erano tre volte più lunghe del testo.

In quelle note c'è un algoritmo per calcolare i numeri di Bernoulli con la Macchina Analitica: per questo molti la considerano la prima programmatrice della storia. C'è l'idea che una macchina del genere non debba limitarsi ai numeri, ma possa manipolare qualunque simbolo — perfino comporre musica, scrive, se le note fossero codificate in modo opportuno. E c'è, alla fine, una frase che avrebbe ossessionato un secolo di informatici:

*La Macchina Analitica non ha alcuna pretesa di creare qualcosa. Fa quello che sappiamo ordinarle di fare.*

È l'obiezione di Lady Lovelace, e Turing la citò per nome nel 1950, sentendosi in dovere di rispondere. La macchina non origina: esegue. Può fare musica, ma solo quella che le abbiamo insegnato a fare. Non può sorprenderci, perché ogni sua sorpresa era già nei nostri ordini.

**Un sistema che esegue istruzioni non può eccedere le istruzioni. O no?**

Ada Lovelace morì a trentasei anni, prima che la macchina di Babbage esistesse, senza aver mai visto un computer. La sua obiezione è ancora in piedi, e tornerà in questo libro ogni volta che un modello scriverà qualcosa che nessuno gli aveva chiesto.

## La musica e la sorpresa

Nelle note di Ada Lovelace c'è un passaggio che è la prima immaginazione documentata di un computer creativo. Se le relazioni tra i suoni, scrive, fossero esprimibili in simboli, la macchina potrebbe comporre pezzi di musica «di qualsiasi grado di complessità o estensione».

Non solo numeri, quindi: simboli. Non solo calcolo: anche arte. Eppure, poche righe dopo, arriva la frase che abbiamo appena letto: la macchina non ha pretese di creare.

Le due affermazioni si contraddicono, e la contraddizione è il punto. Lovelace sta dicendo insieme che la macchina può produrre qualunque cosa le si insegni a produrre e che la macchina non può produrre nulla che non le sia stato insegnato. La prima è un'apertura enorme, la seconda una condanna.

Turing, nel 1950, dedicò all'obiezione un intero paragrafo del suo articolo e la chiamò per nome. La sua risposta ha la forma di una distinzione: non sorprendere e non poter sorprendere sono cose diverse. Una macchina che impara non fa quello che le abbiamo ordinato, fa quello che le abbiamo insegnato a imparare — e insegnare non è ordinare. Quando insegniamo, spesso non sappiamo che cosa stiamo insegnando.

Aggiunse una confessione: le macchine lo sorprendevano di continuo, perché i conti su che cosa avrebbero fatto li faceva in fretta e male. E spiegò l'errore di fondo: credere che, appena conosciamo un fatto, ne conosciamo subito anche tutte le conseguenze.

**L'imprevisto non richiede un'anima, richiede una catena di cause abbastanza lunga.**

Ada Lovelace aveva ragione e torto nello stesso tempo, ed è per questo che la sua obiezione è ancora utile. Aveva ragione che una macchina esegue. Aveva torto nel credere che eseguire significhi non sorprendere.

:::curiosita Il libro cinese che conteneva il binario
Nel 1703, poco prima di presentare la sua aritmetica binaria all'Accademia delle scienze di Parigi, Leibniz ricevette da Pechino, dal gesuita Joachim Bouvet, il disegno delle sessantaquattro figure dell'*I Ching*, l'antico libro dei mutamenti cinese. Era stato Bouvet, dopo aver letto la spiegazione del sistema binario che Leibniz gli aveva mandato, ad accorgersi che quelle figure esagonali, formate da linee intere e linee spezzate, corrispondevano esattamente ai numeri binari da 0 a 63.

Leibniz ne fu entusiasta: ci vide la conferma che l'ordine binario era una specie di lingua universale, scritta in Cina tremila anni prima. I matematici cinesi probabilmente non la pensavano così: per loro erano simboli cosmologici, non numeri.

L'aneddoto dice comunque una cosa vera: le strutture matematiche non hanno nazionalità, e si trovano dove meno te le aspetti. Il problema è che una somiglianza non è una derivazione.
:::

## L'aritmetica del possibile

Il fallimento della macchina di Lagado ha una forma matematica, e vale la pena guardarla, perché è la forma di tutto ciò che segue.

Prendiamo i nove concetti di Lullo. Quante coppie ordinate si possono formare? Nove per nove: ottantuno. Quante terne? Nove alla terza: settecentoventinove. Quante sequenze di tutti e nove? Nove alla nona: trecentottantasette milioni. Già troppe per un uomo, già abbastanza per un libro che nessuno leggerà.

Ma Lullo lavorava con nove concetti. Una lingua ne ha centomila.

Prendiamo un vocabolario modesto: diecimila parole. Quante frasi di cinque parole possiamo costruire? Diecimila alla quinta: cento miliardi di miliardi. Quante di dieci parole? Diecimila alla decima, cioè un uno seguito da quaranta zeri.

Non è un numero grande. È un numero che non ha più rapporto con niente. Elencarle una al secondo richiederebbe circa 3×10³² anni: ventimila miliardi di miliardi di volte l'età dell'universo.

E qui c'è il punto: **quasi tutte quelle frasi sono ciarpame**. «Il gatto ha mangiato il topo perché aveva fame» è una frase. «Fame topo mangiato ha gatto il perché aveva» non è una frase, è una lista. Delle diecimila alla decima combinazioni, una parte infinitesima ha un senso, e una parte ancora più infinitesima vale la pena di essere letta.

Lullo, Leibniz e Swift si sono schiantati tutti contro lo stesso muro. Non mancava la capacità di generare: mancava la capacità di scegliere. E per scegliere bisogna sapere che cosa è probabile — che è esattamente ciò che nessuno, nel 1305, nel 1703 o nel 1726, aveva gli strumenti per fare.

Nel 1941, in Argentina, uno scrittore e bibliotecario immaginò l'estremo di quella strada: una biblioteca che contiene tutti i libri possibili. Corridoi esagonali infiniti, volumi di quattrocentodieci pagine, venticinque simboli. Poiché ogni libro possibile è lì dentro, la biblioteca contiene la soluzione del problema che vi tiene svegli la notte, e contiene anche un numero sterminato di libri identici a quelli veri tranne una virgola.

Borges la chiamò *La biblioteca di Babele*, e ne fece la più bella descrizione mai scritta del nostro problema. Perché quella biblioteca contiene tutto, e proprio per questo non serve a niente: i bibliotecari impazziscono cercando il catalogo dei cataloghi, il libro che spiega gli altri libri. In una biblioteca così anche il catalogo è uno dei libri possibili, e ce ne sono infiniti che sembrano quello giusto.

:::cofano Sotto il cofano — L'esplosione combinatoria, in otto righe
Il codice non serve a capire l'intelligenza artificiale. Serve a toccare con le dita perché la strada di Lullo non poteva funzionare, e perché il problema non è la potenza di calcolo ma il numero delle possibilità.

    import itertools

    concetti = ["bontà", "grandezza", "eternità",
                "potenza", "sapienza", "volontà",
                "virtù", "verità", "gloria"]

    coppie = list(itertools.product(concetti, repeat=2))
    print(len(concetti), "→", len(coppie), "coppie")

    for n in (2, 3, 5, 10):
        print(n, "parole:", 10_000 ** n)

La prima riga stampa 9 e 81: il numero di combinazioni che Lullo poteva leggere a mano, una per una. Le ultime quattro stampano 10⁸, 10¹², 10²⁰ e 10⁴⁰. Il salto tra il primo numero e l'ultimo non è un salto di scala: è un cambio di natura. A un certo punto il numero di possibilità smette di essere grande e comincia a essere irraggiungibile.

(Con `combinations` invece di `product` ottenete 36 invece di 81: sono le coppie non ordinate e senza ripetizioni. Sono 36 anche le caselle della Terza Figura dell'*Ars*, dove ogni coppia di concetti occupa un posto solo.)
:::

## Che cosa manca

C'è una tentazione, arrivati a questo punto, di concludere che il sogno di Lullo fosse semplicemente sbagliato. Che il pensiero non sia calcolo, che le macchine non possano pensare, che la faccenda sia chiusa.

Sarebbe una conclusione comoda e falsa, perché i fatti sono andati in un'altra direzione. Poco più di un secolo dopo Lovelace, un matematico avrebbe detto che la macchina poteva sorprenderci. Oltre centocinquant'anni dopo Lovelace, una macchina avrebbe battuto a scacchi il campione del mondo. E oggi scriviamo messaggi che iniziano con «buona» e finiscono con «notte» senza accorgerci che, in mezzo, c'è una staffetta lunga sette secoli.

Il punto non è se il sogno fosse giusto. Il punto è che cosa mancava.

Mancava un modo per dire: di tutte le combinazioni possibili, questa è più probabile di quella. Non un modo per generarle tutte — quello Lullo lo aveva già. Un modo per ordinarle, per dare a ciascuna un numero, e per scegliere. Un criterio.

Quel criterio ha una data di nascita precisa, e non è il 1305. È il 1913, e nasce da una lite accademica sul libero arbitrio, in una città russa, per mano di un professore che non sopportava le argomentazioni del collega.

Ma questa è la storia del prossimo capitolo.

:::prova Provalo tu — La frase che nessuno ha mai scritto
Chiedete a un modello: «Scrivimi una frase in italiano che nessuno ha mai scritto prima».

Vi darà qualcosa di plausibile in pochi secondi. Ora chiedetegli: «Sei sicuro che nessuno l'abbia mai scritta?». Nessuno può saperlo, ed è per questo che la domanda è istruttiva: guardate se il modello lo ammette o se si mostra sicuro.

Il punto non è la risposta. Il punto è che la frase, quasi certamente, è davvero nuova. Un modello non pesca da un archivio di frasi già scritte: ne costruisce di nuove, e la maggior parte di quelle che produce non è mai stata pronunciata da un essere umano.

Poi chiedetegli una frase nuova, vera e utile. E notate la differenza: la novità è gratis, l'utilità no. È il confine su cui si gioca tutta la questione di questo libro.
:::

:::pensa Per chi ama pensare — L'obiezione di Lady Lovelace
Se una macchina enumerasse tutti i romanzi possibili, uno di quelli sarebbe il più bel romanzo mai scritto. Sarebbe lì, in mezzo agli altri, identico a un miliardo di romanzi sbagliati per una virgola. Nessuno saprebbe riconoscerlo.

Quel romanzo esiste? In un certo senso sì: è una conseguenza aritmetica dell'alfabeto. In un altro senso no, perché nessuno lo ha scritto, nessuno lo ha scelto, e nessuno può leggerlo senza sapere che è quello giusto.

L'obiezione di Ada Lovelace — la macchina non crea, esegue — vale ancora? O vale solo per le macchine del 1843? E noi, quando scriviamo, facciamo qualcosa di diverso dal selezionare, tra le frasi che la lingua ci mette a disposizione, quella che ci sembra giusta?
:::

## In tre righe

Per secoli abbiamo provato a meccanizzare il pensiero generando tutte le combinazioni possibili: Lullo con i dischi, Leibniz con i simboli, Swift con le tessere di legno.

Il muro è sempre lo stesso: le combinazioni possibili sono infinitamente più numerose di quelle sensate, e generarle tutte non serve a niente se nessuno sa quale tenere.

Mancava la scelta. Per scegliere serve sapere che cosa è probabile — e quella storia comincia nel 1913, contando le vocali di Puškin.
