# Confronto delle 6 voci — inizio del Capitolo 1

Le sei versioni raccontano le stesse cose: stessa scaletta (`scaletta-comune.md`), stessi fatti, stessa epigrafe, stessa mail all'amministratore, stessi due box. Cambia solo la voce. Una sola eccezione dichiarata: la versione 2 apre con Markov (1913), perché il narratore deve partire da una storia vera; le altre cinque raccontano Markov a metà capitolo.

## Tabella: punti forti e punti deboli

| # | Voce | Punti forti | Punti deboli |
|---|---|---|---|
| 1 | **Bar** (`versione-1-bar.md`) | È il registro che `CLAUDE.md` chiede alla lettera: l'amico competente davanti a un caffè. Scorre, il «tu» è naturale, le battute (8) sono distribuite e quasi tutte nascono dall'osservazione quotidiana. Il rigore resta intatto: immagini secondarie solo tre, ciascuna con il suo limite. È la più sicura da sostenere per 20 capitoli. | È la meno riconoscibile: è la voce «giusta» più che la voce «sua». Interiezioni come «Guarda», «Eh, no», «Ti è mai capitato…?» sono utili in 1.500 parole e rischiano di diventare tic in 80.000. La frase sull'eliminacode («il numero dopo il tuo l'ha già stampato…») è contorta. |
| 2 | **Narratore** (`versione-2-narratore.md`) | L'aggancio più forte: Markov è una storia vera, raccontata senza un solo dettaglio inventato, e la chiusa «molta meno matita» riporta alla storia iniziale. Capoversi brevi e chiusure che spostano la scena. Ha la spiegazione tecnica più nitida del lotto: «che l'ultimo pezzo l'abbia scelto lui non fa nessuna differenza». Ironia sottile, in linea con «ironia sì, sarcasmo no». | Ha bisogno di un aneddoto forte a ogni apertura. Regge nei capitoli con storie (1, 6, 12, 20), molto meno in quelli pratici: le schede dei capitoli 15 e 16 non hanno storie vere. Fa ridere meno (6 battute, sottili). Markov occupa circa metà dell'aggancio e il mistero della mail arriva tardi. |
| 3 | **Comico** (`versione-3-comico.md`) | La più memorabile e citabile: «Costosissimo, ma sempre completamento». Callback e regola del tre ben usati. Nonostante la densità, non perde un fatto e il box tecnico resta preciso, con solo 2 battute. Ottima per i capitoli aperti e leggeri. | La densità dichiarata (21, una ogni 70 parole) è generosa: alcune sono spiegazioni travestite («Non è niente di personale», «È metodico»). Su capitoli da 3.000-4.500 parole significherebbe qualche centinaio di battute per libro: rischio di stanchezza e di battuta forzata, e più difficile far rispettare la regola «la battuta regge solo se il concetto è giusto». |
| 4 | **Sistemista** (`versione-4-sistemista.md`) | La più credibile per il lettore tecnico. Tre immagini da sala server, ognuna con il suo limite dichiarato: il tasto Tab (cerca in un elenco, non prevede), il log (è inerte), la postmortem. Il box «Sotto il cofano» è il più ricco: aggiunge che i 16 GB sono solo i parametri e che la memoria di lavoro si somma. Ironia secca ben dosata: «contenuto in manutenzione», «funzionava fino alla terza». | Rischia di escludere il lettore curioso. Ogni immagine (shell, log, postmortem) va spiegata al volo e appesantisce il testo principale, che per `CLAUDE.md` è scritto per il curioso. Su un libro intero il turno di notte può diventare un tic. È la voce più fredda. |
| 5 | **Professore** (`versione-5-professore.md`) | La più chiara: passi numerati, definizioni prima dell'uso, 4 domande del lettore con risposta subito dopo. Una è un dubbio vero («se prevede solo la parola dopo, come rispetta "formale"?») e la risposta è un contenuto in più rispetto alle altre versioni. Ottima come testo di consultazione. | È la più «cattedra» nonostante le cautele: «Tre cose da tenere a mente», «Obiezione legittima» (due volte, già una formula), elenchi numerati. Va contro «un amico al bar, non un professore dalla cattedra». Fa sorridere meno delle altre (6 battute leggere). |
| 6 | **Dialogo** (`versione-6-dialogo.md`) | La più originale e la più legata al sottotitolo: un'IA ignorante ma eloquente che interrompe, si scusa e sbaglia con sicurezza. Le tre allucinazioni inscenate (8B = otto byte, Markov nel 1922, 16 megabyte) sono smentite subito, e la battuta «Dalla voce non si capisce chi ha ragione» è la lezione del libro. Il lettore curioso segue benissimo. | È la più rischiosa sull'accuratezza: ogni errore inscenato è un falso scritto, corretto subito ma citabile fuori contesto, e va controllato a ogni capitolo. Non sostiene da sola un libro intero: capitoli con tabelle e conti (13-16) non si dialogano. Il dialogo e i box tecnici sono due registri che convivono a fatica. |

## I numeri

Parole contate con lo stesso metodo su tutte (escluse intestazione, marcatori e riga finale). Le battute sono quelle dichiarate da chi ha scritto ciascuna versione, non una misura indipendente.

| # | Parole | Battute dichiarate | Una ogni (circa) | Immagini secondarie oltre a tastiera e mixer |
|---|---|---|---|---|
| 1 | 1.462 | 8 | 180 parole | eliminacode, brindisi |
| 2 | 1.416 | 6 | 235 parole | eliminacode |
| 3 | 1.426 | 21 (generosa) | 70 parole | eliminacode, brindisi |
| 4 | 1.426 | 8 | 180 parole | tasto Tab, log, postmortem, eliminacode |
| 5 | 1.475 | 6 | 245 parole | eliminacode |
| 6 | 1.438 | 9 | 160 parole | eliminacode, paragoni nelle gag (biglietto da visita, chiavetta) |

Mixer ed eliminacode compaiono in tutte perché li prescrivono la scheda del capitolo e il titolo del libro: a distinguere le voci sono le immagini di colore.

## Come hanno retto le regole di CLAUDE.md

- **Accuratezza:** tutte e sei usano solo i fatti della scaletta. Nessuna dice «il primo» per Markov. Tutte marcano 128.256 con [DA VERIFICARE]. Nessun nome, citazione o paper inventato.
- **Ricostruzioni dichiarate:** la mail è sempre presentata come illustrazione, non come output reale.
- **Una formula, un [DA VERIFICARE], una gag del titolo:** una sola volta in ciascuna.
- **Lettore curioso senza i box:** tutte stanno in piedi. La più dipendente dal gergo è la 4.

## Cosa ho corretto dopo la scrittura

Le versioni sono state scritte in isolamento; i controlli e le correzioni minime li ho fatti io dopo, senza cambiare le voci.

1. **Esempio della mail:** nella scaletta avevo scritto che un pezzo coincide con una parola, ma le righe dell'esempio crescono di 2-3 parole. È un mio errore. Nelle versioni 1, 2, 3, 4 e 6 l'elenco ora è presentato come «qualche istantanea», con i giri in mezzo saltati.
2. **Versione 4:** l'aggancio presentava come reale un output inventato della tastiera. Ora dice «qualcosa come».
3. **Versione 6:** la battuta «sedici megabyte bastano per salutare» falsava il concetto, perché esistono modelli molto piccoli che fanno di più. L'ho sostituita con un conto esatto: 16 GB sono mille volte 16 MB. Il box «Sotto il cofano» era un unico blocco di testo e l'ho spezzato in paragrafi.
4. **Box «Dove l'analogia scricchiola»:** nelle versioni 1, 2 e 4 superava le 2-4 frasi previste da `CLAUDE.md`. Ora tutte e sei ne hanno 4.
5. **Conteggio parole:** `wc -w` dà risultati diversi a seconda della locale (per la versione 4, 1.456 contro 1.480), quindi ho usato un unico metodo.

## Limiti di questo confronto

- Il test copre 1.500 parole di spiegazione. Non mostra come reggono le voci nelle parti pratiche (schede con tabelle e conti), nei box «Storia vera», «Mito da sfatare» e «Prova tu», né dopo 4.000 parole.
- Le sei versioni le ha scritte lo stesso modello su istruzioni diverse: la differenza è ciò che le istruzioni di voce riescono a ottenere.
- Verificati in rete: Markov (1913, prime 20.000 lettere dell'*Onegin*, vocali e consonanti), l'articolo su Gboard (Hard e altri, 2018) e il vocabolario di circa 128.000 token di Llama 3. **Non verificato:** il valore esatto 128.256, perché Hugging Face era irraggiungibile dalla rete della sessione.

## Mix possibili

Non è una raccomandazione, solo ciò che le sei versioni suggeriscono:

- **Base 1 (bar) + box nella voce 4:** testo principale al bar, «Sotto il cofano» da sistemista.
- **Base 1 o 5 + intermezzi in dialogo (voce 6):** il dialogo come ospite ricorrente nei capitoli sulle allucinazioni (12) e sugli agenti (18), dove l'errore sicuro fa parte della lezione.
- **Voce 2 per le aperture storiche** (cap. 1, 6, 20) e un'altra voce per il resto.
- **Base 5 con più battute prese dalla 3:** chiarezza del professore, ma meno cattedra.

## Cosa mi serve da te

Dimmi il numero della versione, oppure un mix. Poi aggiungo la voce scelta a `CLAUDE.md` come sezione dedicata, così vale per tutti i capitoli, e ti propongo la scaletta del Capitolo 1 completo.
