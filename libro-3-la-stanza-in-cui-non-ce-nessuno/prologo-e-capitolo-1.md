# Prologo — La stanza

L'aria, dentro, è calda.

Non calda come una giornata d'estate: calda come un phon lasciato acceso in una stanza chiusa, per ore, da qualcuno che si è dimenticato di spegnerlo.

La stanza non ha finestre, come tutte quelle di questo tipo. È lunga abbastanza da perdercisi, e larga quanto basta per far passare due file di armadi. Gli armadi sono alti due metri, neri, allineati come libri in una biblioteca che ha rinunciato alle copertine. Dentro ognuno ci sono decine di schede, e ogni scheda produce calore, e il calore va portato via.

Il rumore è la prima cosa che si nota. Non è il ronzio dei computer da ufficio: è un frastuono basso e continuo, come una cascata chiusa in una scatola. Viene dalle ventole e dai circuiti dell'acqua.

I cavi sono turchesi. Non per estetica: è il colore con cui in questi edifici si segnano le fibre ottiche multimodali di ultima generazione, quelle dei collegamenti corti e veloci da una scheda all'altra. Migliaia di fili che salgono dagli armadi e si perdono in un controsoffitto buio, come radici rovesciate.

Fuori c'è l'Iowa. Campi di mais, strade dritte, il cielo più grande del mondo. Dentro, in questa stanza senza finestre, ci sono macchine che hanno imparato a scrivere.

Secondo i dati dell'acquedotto di West Des Moines, riportati dall'Associated Press, nel luglio del 2022 — il mese prima che OpenAI dichiarasse concluso l'addestramento di GPT-4 — i centri di calcolo Microsoft della zona prelevarono circa quarantatré milioni e mezzo di litri d'acqua. Sono diciassette piscine olimpiche, o sedici litri al secondo, giorno e notte, per un mese intero (conti miei). Il sei per cento di tutta l'acqua distribuita dall'acquedotto locale in quel mese. Quanta di quell'acqua sia servita proprio a quel modello, i dati non lo dicono.

Nei sistemi di raffreddamento una parte di quell'acqua evapora, e quella che evapora se ne va nell'atmosfera: non torna all'acquedotto. Non è inquinata. È andata altrove.

E non è solo acqua. Un grande centro di calcolo dedicato all'AI può richiedere più di cento megawatt, l'ordine di grandezza di decine di migliaia di abitazioni. L'Agenzia internazionale dell'energia calcola che nel 2024 i data center abbiano usato circa 415 terawattora, l'1,5 per cento dell'elettricità mondiale, e che nel 2030 arriveranno a circa 945: poco più di quanto consuma oggi il Giappone.

Tutto questo per fare una cosa che, detta così, sembra quasi ridicola.

Indovinare che cosa viene dopo.

Dato un pezzo di testo, calcolare quali elementi potrebbero seguirlo, assegnare a ciascuno una probabilità, sceglierne uno, aggiungerlo, ricominciare. Miliardi di volte al giorno, per ogni persona che ha una connessione, in ogni lingua.

Questo libro racconta come ci siamo arrivati. Non comincia in Silicon Valley e non comincia nel 2022: comincia in una stanza che non è mai esistita, descritta in un libro del 1726, e su un'isola del Mediterraneo, dove un laico maiorchino girava dischi di carta.

Sette secoli, per imparare a indovinare la parola successiva.

Lungo il percorso troverete tre tipi di riquadri. **Sotto il cofano** contiene la formula o il codice vero: si salta senza perdere il filo. **Provalo tu** è un esperimento da fare subito. **Per chi ama pensare** è una domanda che resta aperta.

Il libro ha due lettori e non sceglie. Il primo è un ingegnere di sistema: sa che cosa è una GPU, vuole i numeri, i conti, il punto in cui la macchina si rompe. Il secondo non ha mai aperto un terminale, e se gli dite «rete neurale» pensa a un reparto ospedaliero.

Le formule che incontrerete sono vecchie: la più antica ha più di tre secoli. Nessuna è obbligatoria. Ma se le guardate, vedrete che non sono ornamenti: sono il punto in cui un'idea smette di essere una metafora e comincia a funzionare.

Cominciamo da una stanza che non è mai esistita.


---

# Capitolo primo — La macchina di Lagado

## Quaranta manovelle

La stanza ha il soffitto alto e le pareti di legno. Al centro c'è un telaio quadrato, venti piedi per lato, coperto di tessere. Su ogni tessera è incisa una parola: tutte le parole della lingua, in tutti i modi, i tempi e le declinazioni.

Ai lati del telaio, quaranta studenti tengono le manovelle di ferro.

Il professore dà il segnale. Le manovelle girano, le tessere si rimescolano, le parole cambiano posto. Dopo qualche minuto il telaio si ferma, e il professore ordina agli studenti di leggere ad alta voce le righe che si sono formate.

Ogni tanto, per caso, tre o quattro parole di fila hanno senso. Il professore le fa trascrivere su un foglio. Con questo sistema, spiega, chiunque può scrivere libri di filosofia e di poesia senza alcun talento, e il sapere non è più privilegio di nessuno.

Questa scena non è mai avvenuta. È in un capitolo dei *Viaggi di Gulliver*, pubblicato a Londra nel 1726, e Jonathan Swift la inventò per prendere in giro i filosofi che volevano meccanizzare il pensiero.

Ma la cosa notevole è un'altra. Quattro secoli prima di Swift, in un'isola del Mediterraneo, qualcuno aveva costruito davvero una macchina del genere. Non con le manovelle e non con le tessere di legno: con dischi di carta.

E non ci aveva scherzato sopra. Ci aveva creduto.

## La domanda del capitolo

Si può ridurre il pensiero a un calcolo meccanico? E se sì, che cosa manca a una macchina che combina tutte le parole possibili per essere intelligente?

## Nove parole in cerchio

Raimondo Lullo era maiorchino, laico legato al Terz'ordine francescano, e viveva in un secolo in cui le dispute si risolvevano con i testi e con le spade.

Aveva capito una cosa che molti suoi contemporanei capivano meno: la spada convince poco. Chi perde una guerra può perdere anche la fede, ma chi perde una discussione, se la discussione è ben condotta, si arrende. Il problema è che le discussioni non finiscono mai, perché ognuno ha i suoi argomenti e i suoi testi.

Dal 1274 Lullo costruì e rifece la sua risposta, fino alla forma definitiva del 1305-08: l'*Ars Magna*, l'arte grande. Dischi di carta sovrapposti e concentrici, con sopra scritti nove concetti — bontà, grandezza, eternità, potenza, sapienza, volontà, virtù, verità, gloria. Ruotando i dischi, i concetti si allineavano in combinazioni sempre nuove, e ogni allineamento era un'affermazione sul mondo.

Il ragionamento dietro la macchina ha la forma di un teorema. Se tutte le verità derivano da un piccolo numero di principi, e se i principi sono nove, allora basta enumerare tutte le combinazioni dei principi per ottenere tutte le verità. Non serve più discutere: si gira il disco, si legge la combinazione, e l'avversario è confutato.

Lullo passò la vita a viaggiare, a predicare, a scrivere centinaia di libri, a farsi cacciare e a tornare. Voleva convertire il mondo con la logica, anche se in anni successivi propose pure una crociata. La sua macchina era, nelle intenzioni, uno strumento per convincere senza combattere: un dispositivo che permetteva a chiunque — anche a chi non aveva studiato — di generare argomenti corretti.

Funzionava. A modo suo, funzionava davvero. I dischi producevano combinazioni, e le combinazioni erano tante.

Il difetto non era nella macchina. Era nell'idea che il numero delle combinazioni fosse un vantaggio.

## Calcoliamo

Quattro secoli dopo, un filosofo tedesco che di Lullo era lettore appassionato riprese l'idea e la portò al limite.

Gottfried Wilhelm Leibniz faceva troppe cose e le faceva tutte bene: matematica, filosofia, diritto, diplomazia, storia, biblioteche. Nel 1676 descrisse la regola della catena delle derivate, il meccanismo con cui — tre secoli dopo — si sarebbe fatto apprendere alle reti neurali. Ventisette anni dopo, nel 1703, pubblicò la sua aritmetica binaria, quella fatta solo di zero e uno, che oggi parla dentro ogni computer.

E sognò una cosa che non aveva nome. La chiamò *characteristica universalis*: una lingua di simboli abbastanza precisa da ridurre ogni ragionamento a un calcolo.

Se due persone discutono, scriveva, non dovrebbero più litigare. Dovrebbero prendere la penna, sedersi e dirsi: *Calculemus*. Calcoliamo.

È la scena della discussione di Natale, con un finale diverso. Non «ho ragione io», ma «facciamo il conto». Leibniz immaginava un mondo in cui le opinioni fossero sostituibili con i risultati e le liti con delle addizioni.

Non funzionò, e il motivo è tecnico prima che filosofico: per calcolare bisogna tradurre. Ogni concetto in un simbolo, ogni relazione in una regola, ogni sfumatura in una differenza. Il lavoro era enorme, e nessuno sapeva da dove cominciare. Leibniz morì nel 1716, dimenticato dai più, con l'archivio dei suoi progetti ancora chiuso nei cassetti.

Ma il seme era piantato, e la scommessa era chiara: **se il pensiero è fatto di passi, allora il pensiero si può meccanizzare**. Non serve capire come funziona la mente. Serve trovare i passi giusti e farli eseguire a qualcosa che non si stanca.

## Le manovelle

Swift pubblicò la sua satira dieci anni dopo la morte di Leibniz, e scelse bene il bersaglio ma male l'obiettivo.

La macchina di Lagado non è ridicola perché è impossibile. È ridicola perché è inutile, ed è inutile perché non sa scegliere.

Perché se girate quelle manovelle abbastanza a lungo, la macchina scriverà davvero l'*Amleto*. E scriverà anche un miliardo di volte l'*Amleto* con una lettera sbagliata, e tutte le ricette di cucina mai scritte, e le vostre memorie, e la lista della spesa di un re che non è esistito. Il problema non è la generazione. Il problema è che nessuno, tra i milioni di fogli, saprebbe quale tenere.

**Mancava il modo di scegliere le parole non a caso.**

Swift lo aveva capito benissimo. La sua macchina è comica perché è inutile, ed è inutile perché non sa scegliere. Ci sarebbero voluti quasi due secoli, e un matematico russo arrabbiato, per trovare il pezzo mancante.

## Le note di Ada

Nel 1843, a Londra, una giovane donna di ventisette anni fece una cosa che ai suoi tempi nessuno considerava un lavoro: tradusse un articolo in francese su una macchina che non esisteva.

La macchina era la Macchina Analitica di Charles Babbage, un calcolatore meccanico progettato e mai costruito, fatto di ingranaggi, schede perforate e un «mulino» che macinava numeri. L'articolo era di un ingegnere italiano, Luigi Federico Menabrea. La traduttrice era Augusta Ada Byron, figlia del poeta, sposata Lovelace.

La traduzione sarebbe stata una cosa modesta. Le note che Ada Lovelace vi aggiunse erano tre volte più lunghe del testo.

In quelle note c'è un algoritmo per calcolare i numeri di Bernoulli con la Macchina Analitica: per questo molti la considerano la prima programmatrice della storia. C'è l'idea che una macchina del genere non debba limitarsi ai numeri, ma possa manipolare qualunque simbolo — perfino comporre musica, scrive, se le note fossero codificate in modo opportuno. E c'è, alla fine, una frase che avrebbe ossessionato un secolo di informatici:

*La Macchina Analitica non ha alcuna pretesa di creare qualcosa. Fa quello che sappiamo ordinarle di fare.*

È l'obiezione di Lady Lovelace, e Turing la citò per nome nel 1950, sentendosi in dovere di rispondere. La macchina non origina: esegue. Può fare musica, ma solo quella che le abbiamo insegnato a fare. Non può sorprenderci, perché ogni sua sorpresa era già nei nostri ordini.

Ada Lovelace morì a trentasei anni, prima che la macchina di Babbage esistesse, senza aver mai visto un computer. La sua obiezione è ancora in piedi.

## La musica e la sorpresa

Nelle note c'è anche il primo computer creativo della storia dell'immaginazione. Se le relazioni tra i suoni, scrive Ada Lovelace, fossero esprimibili in simboli, la macchina potrebbe comporre pezzi di musica «di qualsiasi grado di complessità o estensione».

Poche righe dopo arriva la frase che abbiamo appena letto: la macchina non ha pretese di creare.

Le due affermazioni si contraddicono. Ed è proprio la contraddizione che rende quelle note ancora oggi interessanti: Lovelace sta dicendo insieme che la macchina può produrre qualunque cosa le si insegni a produrre e che non può produrre nulla che non le sia stato insegnato. La prima è un'apertura enorme, la seconda una condanna.

Turing, nel 1950, dedicò all'obiezione un paragrafo intero e la chiamò per nome. La sua risposta è una distinzione: non sorprendere e non poter sorprendere sono cose diverse. Una macchina che impara non fa quello che le abbiamo ordinato — fa quello che le abbiamo insegnato a imparare. E insegnare non è ordinare.

Poi fece una confessione: le macchine lo sorprendevano di continuo, perché i conti su che cosa avrebbero fatto li faceva in fretta e male. Il vero errore, disse, è credere che appena conosciamo un fatto ne conosciamo subito tutte le conseguenze.

**L'imprevisto non richiede un'anima, richiede una catena di cause abbastanza lunga.**

Ada Lovelace aveva ragione che una macchina esegue, e torto nel credere che eseguire significhi non sorprendere.

:::curiosita Il progetto per abolire le parole
Nell'Accademia di Lagado, dove Swift colloca la macchina delle parole, c'è un secondo progetto ancora più radicale: abolire del tutto il linguaggio e sostituirlo con gli oggetti. Si parlerebbe mostrando le cose.

Il vantaggio, spiega il professore, è la brevità e la salute: le parole consumano i polmoni. Lo svantaggio è che per una conversazione lunga bisogna portarsi dietro un sacco di oggetti, e i poveri restano svantaggiati.

Swift stava ridendo della filosofia naturale del suo tempo. Tre secoli dopo, la battuta è diventata una domanda tecnica: che cosa succede quando una macchina parla di cose che non ha mai toccato?
:::

## Il muro

Il fallimento della macchina di Lagado ha una forma matematica, e vale la pena guardarla, perché è la forma di tutto ciò che segue.

Nove concetti di Lullo. Coppie ordinate: ottantuno. Terne: settecentoventinove. Sequenze di tutti e nove: trecentottantasette milioni. Già troppe per un uomo, già abbastanza per un libro che nessuno leggerà.

Ma Lullo lavorava con nove concetti. Una lingua ne ha centomila.

Prendiamo un vocabolario modesto: diecimila parole. Frasi di cinque parole: cento miliardi di miliardi. Frasi di dieci parole: un uno seguito da quaranta zeri.

Non è un numero grande. È un numero che non ha più rapporto con niente. Elencarle una al secondo richiederebbe circa 3×10³² anni: ventimila miliardi di miliardi di volte l'età dell'universo.

E quasi tutte sono ciarpame. «Il gatto ha mangiato il topo perché aveva fame» è una frase. «Fame topo mangiato ha gatto il perché aveva» non è una frase, è una lista.

Lullo, Leibniz e Swift si sono schiantati tutti contro lo stesso muro. Non mancava la capacità di generare: mancava la capacità di scegliere. E per scegliere bisogna sapere che cosa è probabile — che è esattamente ciò che nessuno, nel 1305, nel 1703 o nel 1726, aveva gli strumenti per fare.

Nel 1941, a Buenos Aires, uno scrittore e bibliotecario immaginò l'estremo di quella strada: una biblioteca che contiene tutti i libri possibili. Corridoi esagonali infiniti, volumi di quattrocentodieci pagine, venticinque simboli. Poiché ogni libro possibile è lì dentro, la biblioteca contiene la soluzione del problema che vi tiene svegli la notte, e contiene anche un numero sterminato di libri identici a quelli veri tranne una virgola.

Borges la chiamò *La biblioteca di Babele*. È la più bella descrizione mai scritta del nostro problema: una biblioteca che contiene tutto, e proprio per questo non serve a niente.

:::cofano Sotto il cofano — L'esplosione combinatoria, in otto righe
Il codice non serve a capire l'intelligenza artificiale. Serve a toccare con le dita perché la strada di Lullo non poteva funzionare.

    import itertools

    concetti = ["bontà", "grandezza", "eternità",
                "potenza", "sapienza", "volontà",
                "virtù", "verità", "gloria"]

    coppie = list(itertools.product(concetti, repeat=2))
    print(len(concetti), "→", len(coppie), "coppie")

    for n in (2, 3, 5, 10):
        print(n, "parole:", 10_000 ** n)

La prima riga stampa 9 e 81: il numero di combinazioni che Lullo poteva leggere a mano, una per una. Le ultime quattro stampano 10⁸, 10¹², 10²⁰ e 10⁴⁰. Il salto tra il primo numero e l'ultimo non è un salto di scala: è un cambio di natura. A un certo punto il numero di possibilità smette di essere grande e comincia a essere irraggiungibile.

(Con `combinations` al posto di `product` ottenete 36 invece di 81: sono le coppie non ordinate e senza ripetizioni. Sono 36 anche le caselle della Terza Figura dell'*Ars*, dove ogni coppia di concetti occupa un posto solo.)
:::

## La stanza dei conti

Apro il portatile e chiedo a un modello di scrivere una frase sul gatto. Ci mette meno di un secondo.

Non ha girato manovelle. Non ha enumerato le combinazioni. Ha fatto una cosa che Lullo non poteva fare e che Swift non aveva immaginato: ha scelto. Parola dopo parola, ha assegnato una probabilità a ciascuna delle continuazioni possibili, e ha preso la più alta — o una delle più alte, perché anche la scelta ha le sue regole.

La differenza tra la stanza di Lagado e questo secondo è tutta qui. Non nella velocità: anche una macchina lenta avrebbe potuto vincere. Non nella memoria: anche una macchina con poca memoria avrebbe potuto. Nella presenza di un criterio.

E il criterio, in questo caso, non è stato scritto da nessuno. È emerso. La macchina ha letto tanto testo da poter dire, con buona approssimazione, che dopo «il gatto ha mangiato» è probabile «il topo» e improbabile «la Costituzione». La probabilità non è la verità, ma è un ordine — e l'ordine è esattamente ciò che mancava a Lullo.

C'è un'ironia in questa storia. Lullo voleva una macchina che dicesse la verità. Ne è venuta fuori, sette secoli dopo, una macchina che dice la cosa più probabile, e a volte le due cose coincidono. E l'ordine, a quanto pare, basta a sembrare intelligenza.

:::prova Provalo tu — Quante frasi esistono
Chiedete a un modello: «Quante frasi di dieci parole si possono dire in italiano?».

Guardate che cosa risponde: un numero secco, un intervallo, o l'ammissione che non si può dire? Le sequenze di dieci parole, con diecimila parole a disposizione, sono 10⁴⁰; le frasi sensate sono molte meno e nessuno può contarle, quindi la domanda è ingiusta. Vedete se il modello se ne accorge.

Ora chiedetegli: «Scrivimene cento, una diversa dall'altra». Le scriverà. Non ha enumerato niente: ha scelto cento volte, una parola alla volta.

La differenza tra le due risposte è tutta la differenza tra lo spazio delle possibilità e la capacità di muoversi dentro. Un dizionario non sa quante parole contiene. Un romanziere non sa quante frasi esistono. E nessuno dei due, per scrivere, ha bisogno di saperlo.
:::

## Che cosa manca

C'è una tentazione, arrivati a questo punto, di concludere che il sogno di Lullo fosse semplicemente sbagliato. Che il pensiero non sia calcolo, che le macchine non possano pensare, che la faccenda sia chiusa.

Sarebbe una conclusione comoda e falsa, perché i fatti sono andati in un'altra direzione. Poco più di un secolo dopo Lovelace, un matematico avrebbe detto che la macchina poteva sorprenderci. Oltre centocinquant'anni dopo Lovelace, una macchina avrebbe battuto a scacchi il campione del mondo.

Il punto non è se il sogno fosse giusto. Il punto è che cosa mancava.

Mancava un modo per dire: di tutte le combinazioni possibili, questa è più probabile di quella. Non un modo per generarle tutte — quello Lullo lo aveva già. Un modo per ordinarle, per dare a ciascuna un numero, e per scegliere. Un criterio.

Quel criterio ha una data di nascita precisa, e non è il 1305. È il 1913, e nasce da una lite accademica sul libero arbitrio, in una città russa, per mano di un professore che non sopportava le argomentazioni del collega.

Ma questa è la storia del prossimo capitolo.

:::pensa Per chi ama pensare — L'obiezione di Lady Lovelace
Se una macchina enumerasse tutti i romanzi possibili, uno di quelli sarebbe il più bel romanzo mai scritto. Sarebbe lì, in mezzo agli altri, identico a un miliardo di romanzi sbagliati per una virgola. Nessuno saprebbe riconoscerlo.

Quel romanzo esiste? In un certo senso sì: è una conseguenza aritmetica dell'alfabeto. In un altro senso no, perché nessuno lo ha scritto, nessuno lo ha scelto, e nessuno può leggerlo sapendo che è quello giusto.

L'obiezione di Ada Lovelace — la macchina non crea, esegue — vale ancora? O valeva solo per le macchine del 1843? E noi, quando scriviamo, facciamo qualcosa di diverso dal selezionare, tra le frasi che la lingua ci mette a disposizione, quella che ci sembra giusta?
:::

## In tre righe

Per secoli abbiamo provato a meccanizzare il pensiero generando tutte le combinazioni possibili: Lullo con i dischi, Leibniz con i simboli, Swift con le tessere di legno.

Il muro è sempre lo stesso: le combinazioni possibili sono infinitamente più numerose di quelle sensate, e generarle tutte non serve a niente se nessuno sa quale tenere.

Mancava la scelta. Per scegliere serve sapere che cosa è probabile — e quella storia comincia nel 1913, contando le vocali di Puškin.

