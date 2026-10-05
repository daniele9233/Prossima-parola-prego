- **Voce:** Il chiacchierone al bar: un amico competente che spiega davanti a un caffè, tutto al «tu», frasi brevi, domande al lettore, interiezioni misurate, digressioni lampo che tornano subito sul punto.
- **Densità di battute:** medio-alta: 8 battute, circa una ogni 187 parole
- **Analogie usate:** madre: la tastiera del telefono che suggerisce la parola dopo, cresciuta fino a leggere mezza biblioteca. Secondarie: il mixer da studio (parametri come manopole; limite dichiarato: nessuna manopola ha un'etichetta), l'eliminacode degli sportelli (gag del titolo; limite dichiarato: il numero successivo), il brindisi (eco dell'epigrafe; limite dichiarato: nessuno arrossisce).

---

# Capitolo 1 — Il completamento automatico più costoso della storia

> Un LLM parla come chi improvvisa un brindisi: una parola alla volta, e senza poter cancellare.

<!-- parte: aggancio -->
## Il telefono che finisce le tue frasi

Ti è mai capitato di giocare con la tastiera del telefono? Scrivi «Ci vediamo» e sopra i tasti compaiono tre parole: «domani», «alle», «stasera». Tocchi quella in mezzo. Poi ancora quella in mezzo. E ancora.

Dopo una decina di tocchi ottieni qualcosa come «Ci vediamo domani alle stasera domani alle»: una frase che sembra scritta da me alle sei del mattino. Sta in piedi a malapena, e non sa dove sta andando.

Adesso cambia scena. Apri un assistente di intelligenza artificiale (IA) e scrivi: «Scrivi una mail formale all'amministratore di condominio per rinviare l'assemblea.» È la richiesta che ci accompagnerà per tutto il libro, quella che hai già incontrato nel Prologo. Passano pochi secondi e hai tutto: il saluto, la motivazione, il tono giusto, una chiusura piena di cortesia. Roba che a mano ti costava mezz'ora e tre bozze.

Ora fermati. Da una parte un aggeggio che ti propone «domani» e poi si perde. Dall'altra una macchina che scrive come uno studio legale. Possibile che siano la stessa cosa?

Guarda, lo sono. Sembra assurdo, lo so. Ma per capirlo non ti serve la matematica: ti serve la tastiera che hai in tasca, e un po' di pazienza. Ti dico di più: hai già metà della spiegazione.

<!-- parte: analogia madre -->
## La tastiera che ha letto mezza biblioteca

Quei suggerimenti non sono un trucchetto, e se scrivi col telefono ci hai a che fare ogni giorno. Da anni arrivano da piccole reti neurali, programmi che imparano dagli esempi invece di seguire regole scritte a mano. Un caso documentato è Gboard, la tastiera di Google, che usa un modello di linguaggio per prevedere la parola successiva (Hard e altri, 2018).

Ecco l'analogia che ti porti a casa: l'IA della mail è la tua tastiera, cresciuta. Si chiama LLM, sigla di *Large Language Model*, «modello linguistico di grandi dimensioni». E fa una cosa sola: prevede il prossimo pezzo di testo. Una. Sembra poco, vero? Eppure tutto il resto, mail compresa, viene da lì.

Cresciuta quanto? La tastiera ha imparato dai tuoi messaggi; l'LLM ha letto mezza biblioteca. La tastiera guarda le ultime parole; l'LLM tiene d'occhio tutta la richiesta. Il salto è di scala (più dati, più parametri, più contesto) e di architettura, cioè di come sono collegati i pezzi: si chiama *Transformer*, ne parliamo al capitolo 4. Non è un salto di mestiere. Il mestiere è sempre lo stesso.

«Parametri», ho detto. Immagina un mixer da studio: ogni manopola alza un suono e ne abbassa un altro. Un fonico passa la serata a spostarle di un millimetro finché il suono torna. I parametri sono numeri, detti anche pesi, e fanno da manopole: messi nella posizione giusta, fanno uscire testo sensato invece di rumore. «8B» vuol dire circa 8 miliardi di parametri, dove la B sta per *billion*, cioè miliardo. Otto miliardi di manopole! Girarle a mano richiederebbe più vite di quante ne abbiano tutti i gatti del quartiere, e infatti non lo fa nessuno: le regola un procedimento automatico durante l'addestramento (capitolo 6). Poi restano ferme. Mentre chiacchieri con l'IA, nessuno tocca il mixer. (Qui il paragone zoppica: su un mixer l'etichetta dice «bassi», qui nessuno sa dire cosa muova una singola manopola.)

<!-- parte: cosa succede davvero -->
## Un pezzo alla volta, senza tasto indietro

Rifacciamo il giro con la mail, piano. Il testo che scrivi si chiama *prompt*: è la richiesta. Il modello lo legge e dà un punteggio a ogni pezzo di testo che potrebbe venire dopo. Questi pezzi si chiamano *token*, frammenti di testo: una parola, mezza parola, un segno di punteggiatura. Come si spezzano lo vediamo al capitolo 2.

Quello che segue è una ricostruzione illustrativa, non la risposta registrata di un modello vero. Qui un pezzo coincide con una parola per semplicità; nei modelli veri no. E niente percentuali: solo classifiche.

Primo giro. In ordine di plausibilità: «Gentile», «Egregio», «Spettabile», «Buongiorno». Se ne sceglie uno (come, te lo spiego al capitolo 10): vince «Gentile».

Secondo giro, ed è qui il trucco. Il pezzo scelto si aggiunge al testo, e il testo allungato rientra da capo, come se fosse la tua nuova richiesta. Nuova previsione, nuova scelta, e il testo cresce. Ti mostro solo qualche istantanea: tra una riga e l'altra i giri sono più d'uno.

- «Gentile»
- «Gentile amministratore,»
- «Gentile amministratore, le scrivo»
- «Gentile amministratore, le scrivo per chiederle di»
- «Gentile amministratore, le scrivo per chiederle di rinviare l'assemblea»

E così fino alla fine. Si chiama *autoregressivo*, che è un modo elegante per dire che ogni passo si appoggia sui risultati dei passi precedenti.

Scritto è scritto. Un pezzo già uscito non si cancella e condiziona tutto il seguito: dopo «Gentile», «Egregio» non torna più. E se un pezzo prende una piega strana, il seguito si costruisce sopra quella piega. Come al brindisi, dove la frase uscita è uscita (con la differenza che qui nessuno arrossisce).

Il titolo del libro nasce da qui: sei allo sportello, «prossimo, prego!», e il modello chiama un pezzo di testo alla volta. Solo che l'eliminacode il numero dopo il tuo l'ha già stampato; il modello il prossimo lo decide quando ha finito con il tuo.

Intanto ho detto «prevede», «sceglie», «sa». Va bene come modo di dire, ma dentro non c'è un omino che soppesa le parole. Il modello prende il testo, lo trasforma in numeri, li fa passare attraverso miliardi di moltiplicazioni (quelle delle manopole di prima) e in fondo escono i punteggi. Niente intenzioni. Tanta aritmetica, però, a una velocità folle.

E la chat? La finestra dove scrivi, la memoria di quello che vi siete detti, gli strumenti esterni: software costruito intorno al modello. Lui, in sé, prevede testo e basta. Della memoria parliamo al capitolo 11, degli strumenti al 18.

Tutto questo è una novità di ieri? Eh, no. Nel 1913, a San Pietroburgo, il matematico russo Markov conta a mano vocali e consonanti nelle prime 20.000 lettere dell'*Eugenio Onegin* di Puškin. Scopre che la probabilità di trovare una vocale dipende dalla lettera che precede. È un antenato dei modelli del linguaggio: prevedere il pezzo successivo da ciò che viene prima, con carta e matita. Oggi per molto meno chiediamo a un'IA di farlo, e se ci mette un secondo di troppo ci lamentiamo.

<!-- parte: dove l'analogia scricchiola -->
> **Dove l'analogia scricchiola.** La tastiera ti offre tre parole e aspetta che scelga tu; l'LLM no: sceglie da solo, riparte e va avanti fino in fondo senza chiederti niente. Poi c'è la scala: la tastiera ha imparato da molto meno testo e guarda le ultime parole, l'LLM tiene conto di tutta la richiesta e di una mole di testo che nessuna tastiera ha mai visto, e per questo può tenere il filo di una richiesta lunga e il tono formale dall'inizio alla fine, cosa che a una tastiera non chiede nessuno. Così «finire la frase» diventa «scrivere la mail»: il mestiere è lo stesso, ma la distanza si sente. Alla tastiera l'ultima parola la dici tu; qui, di solito, anche la prima e tutte quelle in mezzo.

<!-- parte: sotto il cofano -->
> **Sotto il cofano.** Il modello è una funzione: in ingresso una sequenza di token, in uscita un punteggio per ogni token del suo vocabolario, l'elenco chiuso dei pezzi che conosce. Llama 3 (Meta, aprile 2024) ne ha circa 128.000: il valore esatto è 128.256 [DA VERIFICARE: campo `vocab_size` nel file `config.json` di Llama 3 8B]. I punteggi si leggono come probabilità e sommano 1, cioè il 100%; come se ne sceglie uno, capitolo 10. A ogni passo escono quindi tanti punteggi quanti sono i token del vocabolario: un numero per ogni candidato. L'unica formula del capitolo è questa:
>
> P(token successivo | tutti i token precedenti)
>
> Si legge: la probabilità del prossimo pezzo, sapendo tutto ciò che è già scritto. P sta per probabilità, la barra verticale per «sapendo che».
>
> Ogni token generato costa un passaggio in avanti (*forward pass*: un attraversamento completo del modello, dall'ingresso ai punteggi). Ipotesi di lavoro: una mail da 300 token. Sono 300 passaggi, uno dopo l'altro; il 300 è un'ipotesi, non una misura. La *KV cache* (da *key-value*, «chiave-valore»: i calcoli già fatti sul testo precedente, tenuti da parte) fa rileggere meno a ogni passaggio, ma il passaggio resta uno per token. Ne parliamo al capitolo 11.
>
> Conto della memoria: 8 miliardi di parametri × 2 byte (16 bit ciascuno) = 16 miliardi di byte = 16 GB, dove GB sta per gigabyte, miliardi di byte. Si può stringere con la quantizzazione (capitolo 14).
>
> Infine, modello contro applicazione. Il modello è quel file da 16 GB di numeri fermi (un 8B a 16 bit): molto grosso e molto taciturno, da solo non conversa e non ricorda niente. Chat, memoria e strumenti sono l'applicazione che lo carica.

*[Il capitolo prosegue con: Mito da sfatare («è solo statistica»), Storia vera (Shannon, 1948), Nell'uso reale, Prova tu, In tre righe.]*
