# Scaletta comune — Capitolo 1, prove di stile

Questa scaletta è la **stessa per tutte e sei le versioni**. Contenuti, fatti, esempi, numeri e ordine delle parti sono fissi: cambia soltanto la voce. Valgono tutte le regole di `CLAUDE.md` (in particolare accuratezza, [DA VERIFICARE], termini inglesi in corsivo, sigle sciolte, una sola formula).

Capitolo: **Cap. 1 — Il completamento automatico più costoso della storia** (scheda in `schede-capitoli.md`). Si scrive solo l'**inizio** del capitolo, circa 1.500 parole (4 pagine di libro, circa 375 parole a pagina).

## 1. Vincoli formali

- **Lunghezza:** da 1.400 a 1.600 parole, contate con `wc -w` sull'intero file escluse le 3 righe d'intestazione.
- **Intestazione:** le prime 3 righe del file sono tre punti elenco contigui, nell'ordine: `- **Voce:** …`, `- **Densità di battute:** …` (numero reale di battute e ritmo, per esempio «alta: 12 battute, circa una ogni 125 parole»), `- **Analogie usate:** …` (tutte le analogie e immagini del testo, la madre per prima). Poi una riga vuota, `---`, una riga vuota.
- **Titolo:** `# Capitolo 1 — Il completamento automatico più costoso della storia`, poi l'epigrafe fissa (sezione 2) come citazione.
- **Marcatori di parte:** ogni parte inizia con un commento HTML invisibile: `<!-- parte: aggancio -->`, `<!-- parte: analogia madre -->`, `<!-- parte: cosa succede davvero -->`, `<!-- parte: dove l'analogia scricchiola -->`, `<!-- parte: sotto il cofano -->`. Servono a contare le parole di ogni parte.
- **Sottotitoli:** liberi e nella voce del testo, per le parti 1-3. I due box hanno il nome fisso e sono blocchi citati: `> **Dove l'analogia scricchiola.** …` e `> **Sotto il cofano.** …`.
- **Riga finale fissa**, identica in tutte le versioni e non conteggiata: `*[Il capitolo prosegue con: Mito da sfatare («è solo statistica»), Storia vera (Shannon, 1948), Nell'uso reale, Prova tu, In tre righe.]*`
- **Battute:** almeno una per pagina, cioè almeno una in ciascun quarto del testo e almeno 4 in tutto. Una battuta è un momento che fa sorridere di proposito: gag, paradosso, understatement, aforisma. Regole di `CLAUDE.md`: brevi, vere (non devono falsare il concetto), si ride delle macchine, dell'hype e di noi umani, mai del lettore. Ironia sì, sarcasmo no. Non riusare gli aforismi che il libro assegna ad altri capitoli.
- **Dai del tu al lettore** e mettilo dentro almeno una scena.

## 2. Epigrafe fissa (uguale per tutte)

> Un LLM parla come chi improvvisa un brindisi: una parola alla volta, e senza poter cancellare.

## 3. Scaletta e budget di parole

Ordine come in `CLAUDE.md`, sezione 5 (il «dove scricchiola» viene prima di «Sotto il cofano»).

| # | Parte | Parole (target) | Cosa deve fare |
|---|---|---|---|
| 1 | Aggancio | 230 (200-260) | Una scena o un piccolo mistero. Il lettore vede un software che «completa le frasi» e un'IA che scrive una mail formale intera: com'è possibile che sia la stessa cosa? |
| 2 | Analogia madre | 300 (260-340) | I suggerimenti della tastiera del telefono, cresciuti fino a leggere mezza biblioteca. I parametri come manopole di un mixer. |
| 3 | Cosa succede davvero | 520 (460-580) | Il ciclo: previsione, scelta, il pezzo rientra nell'input, si ricomincia. Esempio con la mail. Antropomorfismo spiegato. Chat e memoria sono software intorno. Markov in 2-3 frasi. |
| 4 | Dove l'analogia scricchiola (box) | 130 (90-150) | 2-4 frasi: contesto, scala, il ciclo che non aspetta la tua scelta. |
| 5 | Sotto il cofano (box) | 300 (250-340) | Funzione sui token, vocabolario, formula unica, passaggi, conto dei 16 GB, modello contro applicazione. |

**Eccezione dichiarata (solo versione 2, il narratore):** la voce deve partire da una storia vera, quindi l'aggancio è la storia di Markov (fatto F12) e arriva, nelle ultime righe, allo stesso mistero della mail. Nella parte 3 la versione 2 richiama Markov in una frase sola. Tutte le altre versioni aprono con la scena della tastiera e della mail, e raccontano Markov nella parte 3.

## 4. Fatti da usare (e solo questi)

Se un fatto non è in questa tabella, non usarlo. Se la voce ha bisogno di un fatto in più e non sei sicuro, scrivi [DA VERIFICARE: cosa e dove controllarlo].

| ID | Fatto | Stato e fonte |
|---|---|---|
| F1 | LLM sta per *Large Language Model*, «modello linguistico di grandi dimensioni». Un LLM fa una cosa sola: prevede il prossimo pezzo di testo. | Solido. |
| F2 | Il ciclo: il pezzo previsto si aggiunge al testo, il testo allungato rientra come nuovo input, si ripete fino alla fine. Un pezzo già scritto non si cancella e condiziona tutto il seguito. | Solido. |
| F3 | Chat, memoria della conversazione e strumenti esterni sono software costruito intorno al modello; il modello in sé prevede testo. Rimandi: memoria al cap. 11, strumenti al cap. 18. | Solido. |
| F4 | Le tastiere degli smartphone suggeriscono la parola successiva e da anni usano piccole reti neurali: caso documentato la tastiera Gboard di Google, con un modello di linguaggio per predire la parola successiva (Hard e altri, 2018). Quindi il salto verso un LLM è di scala (dati, parametri, contesto) e di architettura (il Transformer, cap. 4), non di mestiere. | Solido. Fonte: A. Hard et al., «Federated Learning for Mobile Keyboard Prediction», 2018. |
| F5 | I parametri sono numeri (detti anche pesi), come le manopole di un mixer. «8B» vuol dire circa 8 miliardi (la B è *billion*, miliardo). Si regolano durante l'addestramento (cap. 6); durante la tua conversazione restano fermi. | Solido. |
| F6 | Il conto: 8 miliardi di parametri × 2 byte (16 bit) = 16 GB. GB = gigabyte, miliardi di byte. Si può stringere con la quantizzazione (cap. 14). | Solido (conto di `CLAUDE.md`, sezione 4). |
| F7 | Il modello ha un elenco chiuso di token possibili, il vocabolario, e a ogni passo dà un punteggio a ciascuno. Llama 3 (Meta, aprile 2024): circa 128.000 token. Valore esatto: 128.256 [DA VERIFICARE: campo `vocab_size` nel file `config.json` di Llama 3 8B]. | «Circa 128.000»: Meta, presentazione di Llama 3 (18 aprile 2024). Il valore esatto non è stato verificato: **in ogni versione va scritto 128.256 con il marcatore [DA VERIFICARE]**. |
| F8 | Per generare N token servono N passaggi in avanti (*forward pass*, un attraversamento completo del modello). Ipotesi di lavoro: una mail da 300 token, quindi 300 passaggi. La cifra 300 è un'ipotesi dichiarata, non una misura. Con la KV cache (cap. 11) ogni passaggio rilegge meno, ma resta uno per token. | Solido. |
| F9 | I punteggi dei candidati si leggono come probabilità: sommano 1 (cioè 100%). Poi se ne sceglie uno; come, lo dice il cap. 10. Negli esempi niente percentuali: solo classifiche («in testa», «più indietro»). | Solido. |
| F10 | *Autoregressivo*: ogni passo si basa sui risultati dei passi precedenti. | Solido. |
| F11 | **L'unica formula del capitolo**, solo nel box «Sotto il cofano»: P(token successivo \| tutti i token precedenti), da leggere «la probabilità del prossimo pezzo, sapendo tutto ciò che è già scritto». | Solido. |
| F12 | Markov, 1913: il matematico russo, a San Pietroburgo, conta a mano vocali e consonanti nelle prime 20.000 lettere dell'*Eugenio Onegin* di Puškin e scopre che la probabilità di trovare una vocale dipende dalla lettera che precede. È un antenato dei modelli del linguaggio: prevedere il pezzo successivo da ciò che viene prima, con carta e matita. **Non scrivere «il primo».** La teoria è del 1906, l'Onegin del 1913, mai 1922. **Non inventare dettagli di scena, pensieri, dialoghi o citazioni di Markov.** | Documentato. Fonti: A. A. Markov, saggio del 1913 sull'*Eugenio Onegin*; B. Hayes, «First Links in the Markov Chain», *American Scientist*, 2013. |
| F13 | Gag del titolo: l'eliminacode degli sportelli che chiama «prossimo, prego». Il modello chiama una parola alla volta. **Una volta sola** nel testo, dove la voce preferisce. | Titolo del libro (`CLAUDE.md`, sezione 1). |
| F14 | Filo conduttore: la richiesta della mail formale all'amministratore di condominio per rinviare l'assemblea, già presentata nel Prologo. | `CLAUDE.md`, sezione 7. |
| F15 | Il modello non legge lettere né parole intere ma token, frammenti di testo (una parola, mezza parola, un segno di punteggiatura). Dettagli al cap. 2. | Solido. |

## 5. Esempio illustrativo fisso (la mail)

Va dichiarato come **ricostruzione illustrativa, non l'output registrato di un modello reale**, e con la nota che qui un pezzo coincide con una parola per semplicità mentre i veri pezzi no (cap. 2). Niente percentuali.

- Richiesta: «Scrivi una mail formale all'amministratore di condominio per rinviare l'assemblea.»
- Primo giro, candidati in ordine di plausibilità: «Gentile», «Egregio», «Spettabile», «Buongiorno». Se ne sceglie uno: «Gentile».
- Giri successivi, il testo cresce di un pezzo alla volta: «Gentile» → «Gentile amministratore,» → «Gentile amministratore, le scrivo» → «Gentile amministratore, le scrivo per chiederle di» → «… per chiederle di rinviare l'assemblea».

## 6. Termini inglesi e sigle

- In corsivo alla prima occorrenza, con spiegazione immediata: *Large Language Model*, *token* (frammento di testo), *prompt* (la richiesta che scrivi), *forward pass* (solo nel box). Poi senza corsivo.
- Sigle da sciogliere alla prima occorrenza: LLM, GB, la B di «8B», più ogni altra sigla che la voce introduce (anche i sistemisti: nessuna sigla senza spiegazione).

## 7. Confini: cosa NON va in queste 1.500 parole

- Come si spezza il testo in token, e qualunque split preciso («Straw» + «berry»): cap. 2. Perché si sceglie in un modo o nell'altro, temperatura e top-p: cap. 10. L'attenzione e il Transformer: cap. 4. La KV cache nel dettaglio: cap. 11. Se serve, un rimando («ne parliamo nel cap. 10»).
- Le analogie madri degli altri capitoli (ministero, fascicolo, scrivania, tombola, università, corso serale, tazza e pastelli, clinica, esame a libro aperto, tirocinante con la shell, quiz della patente, swap come analogia centrale): arrivano più avanti, non anticiparle. Le immagini di colore che la voce aggiunge sono ammesse, al massimo 2-3, brevi e sempre **subordinate** alla tastiera: la madre resta una sola. Ogni immagine secondaria dichiara il proprio limite in mezza frase.
- Il Mito «è solo statistica», Shannon, «Nell'uso reale», «Prova tu», «In tre righe»: più avanti nel capitolo.
- Nessuna percentuale, nessuna classifica o «oggi il modello migliore è…», nessuna citazione testuale di persone vere, nessun aneddoto fuori da F12, nessun numero fuori dalla tabella dei fatti.
- Antropomorfismo: «prevede», «sceglie», «sa» vanno bene come metafore, ma nella parte 3 spiega in 1-2 frasi cosa succede davvero (numeri che si moltiplicano e producono punteggi, non intenzioni).

## 8. Cosa può cambiare la voce

Ritmo, lunghezza delle frasi, lessico, tipo di battute, immagini secondarie, sottotitoli, il modo di arrivare ai fatti (purché tutti i fatti arrivino e nessuno sia alterato). Non possono cambiare i fatti, l'esempio della mail, l'ordine delle parti, il budget di parole, la madre.

## 9. Controllo prima di consegnare (da `CLAUDE.md`, sezione 10)

- Un lettore non tecnico capisce tutto saltando i box?
- Un sistemista impara almeno una cosa concreta (qui: i 128.256 token, i 300 passaggi per 300 token, i 16 GB)?
- Il «dove scricchiola» è presente e fa il suo lavoro?
- Ogni data, nome e cifra è nella tabella dei fatti, oppure marcata [DA VERIFICARE]?
- Almeno una battuta per pagina, e nessuna falsa il concetto?
- Conteggio parole e budget delle parti rispettati?

## Fonti suggerite (per l'autore, in vista della stampa)

- Markov: A. A. Markov, saggio sul testo dell'*Eugenio Onegin* (1913); B. Hayes, «First Links in the Markov Chain», *American Scientist*, marzo-aprile 2013.
- Tastiera: A. Hard et al., «Federated Learning for Mobile Keyboard Prediction», 2018 (arXiv:1811.03604).
- Vocabolario di Llama 3: presentazione di Meta del 18 aprile 2024 («vocabolario di 128K token»); valore esatto nel file `config.json` del modello, campo `vocab_size` [DA VERIFICARE].
- Conto dei byte: 16 bit = 2 byte per parametro (aritmetica; vedi cap. 13-14).
