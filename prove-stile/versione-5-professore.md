- **Voce:** il professore simpatico: chiarissimo, procede per passi numerati, anticipa le domande del lettore e risponde subito, sorride insieme a chi legge e mai di lui; il professore che al bar spiega con pazienza, non quello che interroga.
- **Densità di battute:** media: 6 battute, circa una ogni 250 parole
- **Analogie usate:** la tastiera del telefono che suggerisce la parola successiva (madre); la tastiera che si è letta «mezza biblioteca»; i parametri come manopole di un mixer; l'eliminacode degli sportelli («prossimo, prego»).

---

# Capitolo 1 — Il completamento automatico più costoso della storia

> Un LLM parla come chi improvvisa un brindisi: una parola alla volta, e senza poter cancellare.

<!-- parte: aggancio -->
## Due cose che non possono essere la stessa cosa

Prova questo esperimento dal divano. Apri i messaggi sul telefono, scrivi «Ciao» e poi tocca sempre il suggerimento al centro, senza pensare, una dozzina di volte. Ne esce una frase che fila, più o meno, e che sembra scritta da te dopo una notte insonne. Non ha il minimo scopo.

Ora cambia scena. Apri un assistente di intelligenza artificiale e scrivi: «Scrivi una mail formale all'amministratore di condominio per rinviare l'assemblea.» È la richiesta del Prologo, e ci accompagnerà per tutto il libro. Dopo pochi secondi arriva una mail intera: saluto, motivazione, proposta di una nuova data, cordiali saluti. Registro giusto, nemmeno un refuso.

Da una parte un aggeggio che completa le frasi, dall'altra qualcosa che scrive lettere. Ti starai chiedendo: possibile che siano la stessa cosa?

Sì. E la spiegazione sta in una frase sola, che ti chiedo di tenere a mente. Un *Large Language Model* (LLM, in italiano «modello linguistico di grandi dimensioni») fa una cosa soltanto: prevede il prossimo pezzo di testo. Il resto è questa stessa mossa, ripetuta.

Il piano è semplice. Prima vediamo cosa c'è di vero nella tastiera, poi come da lì si arriva alla mail, e infine, per chi ama i conti, i numeri nel riquadro «Sotto il cofano». Quello puoi anche saltarlo: il filo non si spezza.

<!-- parte: analogia madre -->
## La tastiera che si è letta mezza biblioteca

Partiamo dalla tastiera, che sarà la nostra analogia per tutto il capitolo. Guarda ciò che hai scritto e ti offre le parole più probabili: per esempio dopo «Buon» può proporre «compleanno», dopo «Ci vediamo» «domani». Sembra poco, ma è un mestiere serio. Le tastiere degli smartphone usano da anni piccole reti neurali (programmi fatti di numeri che si moltiplicano tra loro). Un caso documentato è Gboard, la tastiera di Google, con un modello di linguaggio per predire la parola successiva (Hard e altri, 2018).

Obiezione legittima: se il mestiere è già questo, perché la tastiera non mi scrive le mail? Perché cambia la scala, e cambia il disegno interno. Tre cose da tenere a mente:

1. **I dati.** Immagina una tastiera che, invece dei tuoi messaggi, si è letta mezza biblioteca: lettere, romanzi, ricette, verbali. Non propone più «domani», ha visto come si scrive una lettera.
2. **I parametri.** Sono numeri, detti anche pesi, e funzionano come le manopole di un mixer: ognuna pesa un po' sul suono finale. Un modello «8B» ne ha circa 8 miliardi (la B sta per *billion*, che in inglese è il miliardo). Nessun fonico ha mai avuto tante manopole, né tanta pazienza: infatti le regola un procedimento automatico, durante l'addestramento (cap. 6). Mentre chiacchieri con il modello, restano ferme. Il mixer regge fino a un certo punto: su un mixer ogni manopola ha un compito comprensibile, qui nessuna lo ha da sola.
3. **Il contesto.** È il testo che il modello ha davanti quando prevede. La tastiera ti aiuta sulla frase che stai scrivendo; un LLM tiene sotto gli occhi un testo lungo, per esempio tutta la tua richiesta.

A questi tre si aggiunge il disegno interno della rete, il *Transformer*, di cui parliamo nel capitolo 4. Scala e architettura, dunque: non un altro mestiere, lo stesso mestiere fatto in grande.

<!-- parte: cosa succede davvero -->
## Un pezzo alla volta, in quattro passi

Prima una parola da definire, perché la userò spesso: *token*. Il modello non legge lettere né parole intere, ma frammenti di testo: una parola, mezza parola, un segno di punteggiatura (come si spezzano, lo vediamo nel capitolo 2). La richiesta che scrivi si chiama *prompt*. Ed ecco il ciclo, in quattro passi:

1. **Previsione.** Il modello legge il testo che ha davanti e dà un punteggio a ogni pezzo possibile. I punteggi si leggono come probabilità: sommano 1, cioè 100%.
2. **Scelta.** Se ne sceglie uno. Come si decide, lo spiega il capitolo 10.
3. **Rientro.** Il pezzo scelto si aggiunge al testo, e il testo allungato rientra come nuovo input.
4. **Si ricomincia**, fino alla fine.

Un pezzo già scritto non si cancella, e condiziona tutto il seguito: come nel brindisi, non si torna indietro.

Proviamo con la tua mail. Questa è una ricostruzione illustrativa, non l'output registrato di un modello reale, e qui un pezzo coincide con una parola per semplicità, mentre i veri pezzi no (cap. 2). Primo giro: i candidati, in ordine di plausibilità, sono «Gentile», «Egregio», «Spettabile», «Buongiorno». Se ne sceglie uno: «Gentile». Poi il testo cresce, e ti mostro solo qualche istantanea:

«Gentile» → «Gentile amministratore,» → «Gentile amministratore, le scrivo» → «Gentile amministratore, le scrivo per chiederle di» → «… per chiederle di rinviare l'assemblea».

Obiezione legittima: se prevede solo la parola dopo, come fa a rispettare «formale»? Semplice: «formale» sta nel testo. La tua richiesta è l'inizio dell'input, e a ogni giro il modello la rilegge insieme a tutto ciò che ha già scritto. Dopo «mail formale all'amministratore», «Gentile» è una continuazione ottima e «Ehi» no. Non esiste un interruttore «formale»: esiste un testo in cui certe parole diventano più plausibili di altre.

Una precisazione sul linguaggio. Quando dico che il modello «prevede», «sceglie» o «sa», uso metafore comode. Cosa succede davvero: i parametri si moltiplicano con i numeri che rappresentano il testo, e ne escono dei punteggi. Intenzioni, zero.

Se ti serve un'immagine, pensa all'eliminacode degli sportelli: «prossimo, prego», e si chiama un numero alla volta. Il titolo del libro mi dà il permesso, e lo uso una volta sola. Con una differenza: alle poste chi viene dopo lo decide la fila; qui il prossimo dipende da tutto ciò che è già stato chiamato.

E la chat? La memoria della conversazione? Domanda che arriva puntuale. Chat, memoria e strumenti esterni sono software costruito intorno al modello; il modello in sé prevede testo. Della memoria parliamo nel capitolo 11, degli strumenti nel 18.

Che l'idea sia più vecchia dei computer lo mostra Markov. Nel 1913, a San Pietroburgo, il matematico russo conta a mano, con carta e matita, vocali e consonanti nelle prime 20.000 lettere dell'*Eugenio Onegin* di Puškin, e scopre che la probabilità di trovare una vocale dipende dalla lettera che precede. È un antenato dei modelli del linguaggio: prevedere il pezzo successivo da ciò che viene prima. Ventimila lettere a mano, mentre noi ci spazientiamo se una pagina web ci mette due secondi.

Fissiamo l'idea: previsione, scelta, rientro, di nuovo da capo. Una mail intera è questo giro, ripetuto.

<!-- parte: dove l'analogia scricchiola -->
> **Dove l'analogia scricchiola.** Primo, la tastiera ti offre tre parole e aspetta che sia tu a scegliere; il ciclo del modello non aspetta nessuno: sceglie da solo e prosegue, senza fermarsi a chiederti «Gentile o Egregio?». Secondo, il contesto: la tastiera ti assiste sulla frase in corso, mentre il modello, a ogni giro, rilegge l'intero testo che ha davanti, richiesta compresa. Terzo, la scala: «lo stesso mestiere, in grande» vale per il mestiere, non per l'esperienza d'uso. Ripetuta su quella scala, la stessa mossa produce comportamenti che sulla tastiera non si vedono, ed è per questo che ti è sembrato di avere davanti un'altra cosa.

<!-- parte: sotto il cofano -->
> **Sotto il cofano.** Un LLM è una funzione: prende in ingresso una sequenza di token e restituisce un punteggio per ogni token del suo vocabolario, l'elenco chiuso di quelli possibili. Per Llama 3 (Meta, aprile 2024) sono circa 128.000; il valore esatto è 128.256 [DA VERIFICARE: campo `vocab_size` nel file `config.json` di Llama 3 8B]. I punteggi, ricordi, sommano 1. L'unica formula del capitolo è questa:
>
> `P(token successivo | tutti i token precedenti)`
>
> Si legge: «la probabilità del prossimo pezzo, sapendo tutto ciò che è già scritto». Il modello è *autoregressivo*: ogni passo si basa sui risultati dei passi precedenti.
>
> I passaggi, con i numeri:
>
> 1. Un *forward pass* (passaggio in avanti: un attraversamento completo del modello) produce 128.256 punteggi.
> 2. Se ne sceglie uno (capitolo 10).
> 3. Il token scelto si accoda all'input.
> 4. Si ripete.
>
> Per generare N token servono N passaggi. Ipotesi di lavoro, non una misura: una mail da 300 token, quindi 300 passaggi, per un messaggio che in sostanza dice «rimandiamo». Con la *KV cache* (KV sta per *key-value*, chiave-valore; capitolo 11) ogni passaggio rilegge meno, ma resta uno per token. Ecco perché la risposta si forma un pezzo alla volta e non tutta insieme.
>
> Il peso: ogni parametro occupa 16 bit (cifre binarie, 0 o 1), cioè 2 byte, perché un byte sono 8 bit. Quindi 8 miliardi di parametri × 2 byte = 16 GB, cioè gigabyte, miliardi di byte. È il conto che puoi rifare per qualunque modello: miliardi di parametri × byte per parametro = GB. Si può stringere con la quantizzazione (capitolo 14).
>
> Infine, modello contro applicazione: il modello è quel file di parametri e prevede testo; chat, memoria della conversazione e strumenti esterni sono l'applicazione che gli sta intorno.

*[Il capitolo prosegue con: Mito da sfatare («è solo statistica»), Storia vera (Shannon, 1948), Nell'uso reale, Prova tu, In tre righe.]*
