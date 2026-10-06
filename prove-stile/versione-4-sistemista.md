- **Voce:** il sistemista di turno: frasi corte, numeri in primo piano, ironia secca da relazione sui guasti.
- **Densità di battute:** 10 battute in 1.647 parole (una ogni 165 circa), distribuite 1-3-4-2 nei quattro quarti.
- **Analogie usate:** madre, il compressore; secondarie, il file di log e il file di configurazione in sola lettura.

---

# Capitolo 1 — Il completamento automatico più costoso della storia

> *Comprimere è prevedere con la ricevuta in mano: ogni sorpresa si paga in bit.*

<!-- parte: aggancio -->
## Natasha, a duemila iterazioni

Il 21 maggio 2015 Andrej Karpathy pubblica un articolo (poi ampliato) intitolato «The Unreasonable Effectiveness of Recurrent Neural Networks», «L'irragionevole efficacia delle reti neurali ricorrenti». Una rete neurale ricorrente (*recurrent neural network*, in sigla RNN) è un programma che legge un testo pezzo per pezzo e si porta dietro una piccola memoria del già letto.

Le dai *Guerra e pace* e le chiedi una cosa sola: qual è il carattere successivo? A intervalli crescenti di iterazioni (giri di addestramento: la rete prova, misura l'errore, si corregge) Karpathy mostra cosa scrive.

Iterazione 100: «random jumbles», grovigli di lettere. Iterazione 300: comincia a capire virgolette e punti. Iterazione 500: le parole più brevi, «we», «He», «His». Verso la 2000: parole scritte bene, citazioni, nomi. Il campione di quel punto: «"Why do what that day," replied Natasha, and wishing to himself the fact the» («"Perché fare ciò che quel giorno", rispose Natasha, e desiderando a sé stesso il fatto il»). [DA VERIFICARE: campione completo nel post]

Il frammento si ferma su un «the» senza sostantivo, come l'ultima riga di un *log* (il registro in cui un programma annota ciò che fa) dopo un riavvio brusco: tagliata a metà, di solito la più interessante.

Nessuno ha dato alla rete un dizionario o una grammatica: per lei esistono solo caratteri. Eppure scrive virgolette e nomi propri, e un'altra rete, addestrata su Wikipedia, inventa nello stesso articolo un indirizzo web che non esiste. Karpathy annota che «the model just hallucinated it», «il modello se l'è semplicemente allucinato». È il maggio 2015: la parola c'è già. Per capire come una rete di soli caratteri arrivi a tanto, serve un programma che hai già usato senza sospettare che c'entrasse: il compressore.

<!-- parte: analogia madre -->
## Il compressore, ovvero l'arte di pagare poco

Un compressore (gzip, per esempio) rimpicciolisce un file senza perderne un carattere. Il suo segreto, letto bene, è scommettere sul carattere successivo.

Immagina di dover far trovare a un amico una lettera tra otto, rispondendo solo sì o no. Dimezzando le possibilità a ogni domanda ne bastano 3: da 8 a 4, a 2, a 1. Ogni risposta è un *bit*, la più piccola unità di informazione. Un byte, il pezzo di memoria che di solito contiene un carattere, ne vale 8: tariffa fissa, che il carattere sia una sorpresa o un'ovvietà. Un compressore applica una tariffa variabile. Più il carattere era prevedibile, meno bit paga: un evento che aveva una probabilità su otto costa 3 bit.

Prendi quattro lettere: A capita una volta su due, B una su quattro, C e D una su otto. Costano 1, 2, 3 e 3 bit: in media 1,75, contro i 2 di una tariffa fissa. Per una volta essere banali conviene.

L'immagine da portare a casa: ogni previsione giusta è un bit risparmiato.

Ogni compressore si può leggere come un predittore: la lunghezza del suo codice è il costo delle sue previsioni (equivalenza nota da tempo, ricordata da Delétang e colleghi nel 2023). Per gzip è una lettura, non l'algoritmo; cmix, un compressore da record, ha dentro una rete ricorrente, parente stretta di quella di Karpathy, e prevede davvero. Per pagare meno conviene scoprire le regole: una virgoletta aperta ne chiama una chiusa, e saperlo è uno sconto.

Per un compressore «prevedibile» è un complimento. Lo è anche per chi di notte deve riparare i server.

<!-- parte: cosa succede davvero -->
## Il log cresce, la configurazione no

Un LLM, *Large Language Model* («modello linguistico di grandi dimensioni»), è lo stesso predittore, in grande. A ogni passo produce una cosa sola: la previsione del prossimo *token*, cioè un frammento di testo (una parola, mezza parola, un segno di punteggiatura; vedi capitolo 2).

Il resto è un ciclo: il modello prevede il pezzo successivo, lo aggiunge al testo, il testo allungato rientra in ingresso, si ricomincia. Guarda la rete che Karpathy addestra sul codice del *kernel* Linux (il nucleo del sistema operativo): circa 10 milioni di parametri, il massimo per la sua scheda video. Il campione comincia con la licenza GNU (sigla ricorsiva: «GNU non è Unix»), il testo legale del software libero, recitata carattere per carattere, scrive Karpathy. Se l'ha memorizzata bene, dopo le prime parole il seguito è quasi obbligato e ogni carattere costerebbe pochissimi bit. Previsione giusta, bit risparmiato.

Poi arrivano i nomi delle variabili e la rete non riesce a tenerne traccia. Impatto, per dirla come nelle relazioni sui guasti: Karpathy stesso non crede che il codice compili, cioè che diventi un programma funzionante. Con il LaTeX (il linguaggio con cui i matematici impaginano formule) va meglio: «quasi compila», con qualche ritocco a mano.

Il testo già emesso è un log: si scrive in fondo, nessuno riapre la riga 40 per correggerla, e ogni riga condiziona le seguenti. Solo che il modello, prima di aggiungerne una, rilegge il registro intero. Se sbaglia, la correzione è una riga di scuse in coda, mai una riga in meno.

La conoscenza sta nei *parametri*, detti anche pesi: numeri regolati durante l'addestramento (capitolo 6). Un modello «da 8B» ne ha circa 8 miliardi; la B è *billion*, miliardo. Immagina un file di configurazione (dove un programma tiene le sue impostazioni) con otto miliardi di righe, che nessuno scrive a mano. Nessun commento a margine: chiunque abbia ereditato un server riconosce il genere. In produzione, cioè mentre ci chatti, il file è in sola lettura (anche se nessuna riga, da sola, si legge).

«Prevede», «sa»: verbi in prestito. Aprendo il cofano troveresti quelle righe, otto miliardi, che si moltiplicano per i numeri del tuo testo: dal prodotto escono dei punteggi, uno per ogni pezzo possibile. Nessun «volere»: aritmetica, in quantità industriale.

Il 6 aprile 2017 Alec Radford, Rafal Jozefowicz e Ilya Sutskever pubblicano su GitHub (dove i programmatori condividono il codice) codice e parametri di una loro rete, addestrata a prevedere il carattere successivo su oltre 82 milioni di recensioni Amazon. Una delle sue 4.096 unità (numeri interni alla rete), la 2388 nella demo, ha valori distribuiti diversamente per le recensioni negative e per le positive. Nessuno le aveva chiesto di imparare cos'è un sentimento; nessuno le aveva chiesto niente, a parte la lettera dopo.

Il 23 gennaio 2020 Kaplan e colleghi mostrano che la perdita, cioè l'errore di previsione, scende secondo una curva regolare (una legge di potenza) al crescere di modello, dati e calcolo; alcuni andamenti coprono più di dieci milioni di volte (sette ordini di grandezza). A settembre 2023 un gruppo di DeepMind, con Marcus Hutter tra gli autori, ricorda che addestrare un modello linguistico significa già minimizzare i bit di compressione, e comprime Wikipedia con Chinchilla, 70 miliardi di parametri. Dai 10 milioni di parametri della rete sul kernel ai 70 miliardi di Chinchilla corre un fattore di circa settemila, e in mezzo il motore è stato sostituito (capitolo 4); il carico di lavoro, no: prevedere il pezzo dopo e pagare ogni sorpresa in bit.

<!-- parte: dove l'analogia scricchiola -->
> **Dove l'analogia scricchiola.** Un compressore ti restituisce il file identico, mentre un LLM in chat genera un seguito plausibile, che può anche coincidere con testo memorizzato, ma nessuno garantisce che sia l'originale. Chinchilla porta un miliardo di byte di Wikipedia a 83 milioni (l'8,3%), però Wikipedia l'aveva già letta in addestramento, e lo studio mette in bilancio anche il magazzino: 70 miliardi di parametri × 2 byte (16 bit ciascuno) = 140 GB (gigabyte, miliardi di byte) viaggiano insieme al file da 1 GB che volevi rimpicciolire. Come ottimizzazione libera 917 milioni di byte e ne occupa 140 miliardi: nessun responsabile della sala server la firmerebbe.

<!-- parte: sotto il cofano -->
> **Sotto il cofano.** Il conto di base: costo in bit = −log₂ p. A parole: quante volte devi dimezzare le possibilità per isolare un evento di probabilità p (il meno compensa il logaritmo, negativo per ogni numero minore di 1). Con p = 1/8, 3 bit; con p = 1/1.024, 10.
>
> Il modello ti serve proprio quei p. Visto da fuori è una chiamata di funzione: gli passi i token scritti finora e ti restituisce una tabella sul token che verrà dopo, una riga per ogni token del vocabolario (l'elenco che conosce: 128.256 in Llama 3), valori che, messi insieme, fanno 1, perché la probabilità da spartire è una sola: una *distribuzione di probabilità*. La codifica aritmetica (*arithmetic coding*, anni Settanta) trasforma queste tabelle in un file lungo quanto la somma dei costi dei token arrivati davvero, più al massimo un paio di bit sull'intero messaggio: ridurre la perdita in addestramento e comprimere meglio sono la stessa operazione.
>
> Per scrivere, invece, il modello fa un giro completo dei suoi strati (*forward pass*, passaggio in avanti) a ogni pezzo emesso, che poi rientra nel giro dopo (generazione *autoregressiva*): cento token, cento giri in fila. Il modello è quel file di configurazione: otto miliardi di righe da due byte (16 bit) fanno sedici miliardi di byte, 16 GB. Chat, memoria e strumenti non stanno lì dentro: li aggiunge il programma che carica il file e lo richiama in ciclo (capitoli 11 e 18).
>
> Misure sul *Large Text Compression Benchmark* (classifica pubblica, al 30 settembre 2026), file enwik9: il primo miliardo di byte di Wikipedia inglese del 2006. Bit per byte, sul solo archivio compresso: gzip -9 (livello massimo), 2,58; xz (altro compressore) regolato per il testo, 1,58; cmix v21, 0,86 [DA VERIFICARE: archivio o totale]; nncp v3.2, 0,85. Con 8 bit per byte, gzip riduce di 8 ÷ 2,58 = 3,1 volte, nncp di 8 ÷ 0,85 = 9,4. Due compressori a rete neurale che litigano sui centesimi di bit.
>
> Il conto di Radford, un mese su quattro schede video: 30 giorni × 24 ore × 3.600 secondi = 2.592.000 secondi; 12.500 caratteri al secondo × 2.592.000 = 32,4 miliardi di caratteri (un byte per carattere); 32,4 ÷ 38 ≈ 0,85: poco meno di una passata sui 38 miliardi (e rotti) di byte.
>
> Cifre valide per questo solo file: con altri testi cambiano.

*[Il capitolo prosegue con: Mito da sfatare («è solo statistica»), Nell'uso reale, Prova tu, In tre righe.]*
