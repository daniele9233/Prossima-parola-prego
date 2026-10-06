# Libro 5 — *Indagine su una risposta plausibile*

### Perché l'intelligenza artificiale sbaglia con sicurezza, e come si riconosce il colpevole

> Il libro **del giallo**. Ogni capitolo è un fascicolo: un caso vero, datato e documentato, in cui un'IA ha sbagliato, si è comportata male o ha deluso; poi l'indagine che porta alla spiegazione tecnica. Fatti e numeri stanno in `mappa-contenuti.md`; le regole comuni in `CLAUDE.md`.

## 1. Identità del libro

- **Spina dorsale:** una **serie di indagini**. Ogni fascicolo parte da un caso reale, mostra gli indizi, mette sul tavolo i sospettati, esegue la perizia tecnica (il «sotto il cofano») e chiude con un verdetto e con la prevenzione. In filigrana corre un'unica inchiesta: dietro quasi tutti i casi c'è lo stesso **mandante**, che il lettore scopre al fascicolo finale.
- **Cosa lo distingue:** imparare i meccanismi **dagli errori**. È il libro più narrativo e più «investigativo», il più prudente con i fatti (ogni caso ha data e fonte) e il più utile per capire quando non fidarsi. Il lettore impara facendo il detective: prima di leggere la perizia deve scegliere un sospettato.
- **Dove è più profondo:** allucinazioni (C12), sicurezza e agenti (C15, C16), benchmark (C17), contesto e memoria (C11, C13, C14), quantizzazione e differenze tra fornitori (C20).
- **Lettore ideale:** chi usa l'IA ogni giorno e si è chiesto «perché ha detto questo?»; professionisti, studenti, giornalisti, sistemisti che devono decidere se fidarsi.
- **Lunghezza:** 3.000-4.000 parole per fascicolo.

## 2. Voce

- **Noir ironico in prima persona:** la voce è quella del **Commissario Bayes** (il nome è un omaggio a Thomas Bayes e alla probabilità: lo si dichiara una sola volta), stanco, sarcastico verso i sistemi e mai verso le persone. Frasi secche, immagini da romanzo giallo applicate ai server: «Il data center ronzava come un frigorifero che ha qualcosa da nascondere.»
- **La dottoressa Logit** è la sua perita: spiega la parte tecnica con calma e precisione e corregge il commissario quando semplifica troppo. Il suo riquadro è «Sotto il cofano», il marchio comune ai cinque libri.
- **Il lettore è l'aiuto investigatore:** ogni fascicolo gli chiede di indicare un sospettato prima della perizia.
- **Rigore sui casi:** tutto ciò che è presentato come accaduto ha data, luogo e fonte. Dove non c'è una fonte primaria affidabile: [DA VERIFICARE] e si dice che è una voce.
- **Rispetto:** nessuna ironia su casi con danni alle persone (salute, sicurezza, vite). I casi con conseguenze gravi si trattano con serietà o si escludono. Le persone coinvolte si nominano solo se già nominate in documenti pubblici (sentenze, comunicati), con tono equo.
- **Dove scricchiola il genere giallo (da dichiarare nel prologo):** nel giallo c'è un colpevole con un movente. Qui non c'è colpa del modello, che non ha intenzioni: c'è un **obiettivo di addestramento** e c'è la responsabilità di persone e aziende (chi costruisce, chi distribuisce, chi usa). «Colpevole» è una figura retorica.

### Campione di voce (non è testo del libro)

> Era una di quelle notti in cui un avvocato newyorkese scopre che le sentenze non sono più quelle di una volta.
>
> Sei sentenze citate nella memoria difensiva. Nessuna esisteva.
>
> Il giudice le aveva cercate ovunque, con la pazienza di chi non si fida più nemmeno della propria scrivania.
>
> — Chi le ha scritte? — chiese.
>
> Nessuno rispose. Era il punto più sconcertante: non c'era un truffatore, non c'era un movente, non c'era nemmeno un'intenzione.
>
> C'era solo una macchina che aveva fatto esattamente quello per cui era stata costruita.

## 3. I sospettati ricorrenti

| Sospettato | Cosa significa | Esempio |
|---|---|---|
| **I Dati** | cosa ha letto il modello (lacune, errori, pregiudizi, data di cutoff) | il modello che non sa che giorno è |
| **Il Modello** | la sua struttura (token, embedding, attenzione, quantizzazione) | le R di «strawberry» |
| **L'Obiettivo** | ciò per cui è stato addestrato (la «scena madre»: produrre testo plausibile, piacere agli utenti) | l'allucinazione, l'adulazione |
| **L'Applicazione** | il software intorno (prompt, memoria, strumenti, permessi) | un chatbot che promette ciò che l'azienda non offre |
| **L'Utente** | come lo si usa (richieste vaghe, fiducia cieca) | l'avvocato che si fida |
| **L'Infrastruttura** | hardware, quantizzazioni, bug dei server | lo stesso modello che funziona peggio su un altro fornitore |
| **Il Mercato** | benchmark truccati, promesse esagerate | il modello in classifica con una versione diversa |

Ogni fascicolo si chiude con una **tabella dei colpevoli** (quale sospettato, in che misura): a fine libro si vede che il **mandante** è sempre lo stesso.

## 4. Struttura fissa del fascicolo

1. **La scena:** il caso vero, con data e fonte (500-700 parole).
2. **Gli indizi:** tre o quattro dettagli che non tornano.
3. **I sospettati:** il lettore sceglie (tra quelli della sezione 3).
4. **Sotto il cofano (la perizia della dottoressa Logit):** il meccanismo, con numeri e conti.
5. **Il verdetto:** chi (o cosa) e in che misura. La misura è sempre un **giudizio qualitativo**, mai una percentuale (usare «principale», «concorrente», «non c'entra»).
6. **Prevenzione:** una **Regola d'uso**.
7. **Prova tu:** ricostruire la scena con un esperimento (banco delle prove).
8. **Dal fascicolo:** tre righe da ricordare.

Box ricorrenti: **Precedente** (un caso storico: ELIZA, Clever Hans), **Mito da sfatare**, **Alibi** (una spiegazione che sembra giusta ma non lo è).

## 5. Casi e fascicoli

### Prologo — La scena

- **Caso:** *Mata contro Avianca* (tribunale federale di New York, sentenza di sanzioni del 22 giugno 2023): un avvocato cita sentenze inventate da ChatGPT; il giudice le cerca e non esistono; l'avvocato aveva chiesto allo stesso ChatGPT se fossero reali e lui aveva confermato.
- **Idea:** presenta il metodo, i personaggi, i sospettati e l'inchiesta principale. Il caso resta aperto: la soluzione è nel fascicolo 13.
- **Occhio a:** tono equo verso le persone; solo fatti del provvedimento.

## Parte I — L'indiziato

### Fascicolo 1 — L'indiziato: il prossimo token

- **Concetti:** C01.
- **Caso:** ELIZA (Weizenbaum, 1966) come precedente: chi parlava con il programma gli attribuiva comprensione (l'aneddoto della segretaria va verificato); oggi lo stesso fenomeno con modelli molto più fluenti.
- **Indizi/sospettati:** una risposta fluente e sbagliata; la fluenza come prova (sbagliata).
- **Perizia:** il ciclo di previsione, la distribuzione di probabilità, la perplexity; perché «plausibile» è il metodo del crimine.
- **Verdetto:** l'**Obiettivo** (principale).
- **Prova tu:** P01, P07.
- **Occhio a:** i numeri di probabilità sono illustrativi.

### Fascicolo 2 — Il testimone che non vede le lettere

- **Concetti:** C02, C27.
- **Caso:** le R di «strawberry»; i token glitch (SolidGoldMagikarp, febbraio 2023); un numero lungo spezzato male.
- **Perizia:** BPE; i token come unità; perché l'aritmetica lunga va male; il costo dell'italiano; le immagini come tasselli.
- **Verdetto:** il **Modello** (la struttura), con l'**Utente** concorrente.
- **Prova tu:** P02, P05.
- **Occhio a:** niente split senza tokenizer reale.

### Fascicolo 3 — La mappa sbagliata

- **Concetti:** C03.
- **Caso:** i pregiudizi negli embedding (Bolukbasi e altri, 2016); un motore di ricerca per significato che non trova un codice articolo.
- **Perizia:** embedding, similarità del coseno, bias come «polvere sulla mappa»; ricerca ibrida.
- **Verdetto:** i **Dati** (principale).
- **Occhio a:** le dimensioni non hanno nome.

### Fascicolo 4 — Chi ha guardato chi?

- **Concetti:** C04.
- **Caso:** un'istruzione ignorata in un prompt lungo; il pronome «lui» sbagliato.
- **Perizia:** attenzione, pesi diluiti; perché ordine e struttura contano; il Transformer del 2017.
- **Verdetto:** il **Modello** (limite), con l'**Utente** (prompt confuso).
- **Regola d'uso:** istruzioni cruciali all'inizio e alla fine.

### Fascicolo 5 — Il palazzo dei testimoni

- **Concetti:** C05, C06.
- **Caso:** Golden Gate Claude (Anthropic, maggio 2024): amplificando una caratteristica interna, il modello si identificava con un ponte.
- **Perizia:** layer, residual stream, parametri; perché nessun parametro «contiene» un fatto; interpretabilità.
- **Verdetto:** nessun colpevole: è il limite della nostra capacità di ispezione.
- **Occhio a:** abbandonare l'immagine dei «setacci».

## Parte II — Chi l'ha addestrato

### Fascicolo 6 — Cosa sapeva, e quando

- **Concetti:** C07.
- **Caso:** un modello che «ignora» che giorno è e le notizie recenti; il cutoff.
- **Perizia:** pre-training, cutoff, dati (qualità, duplicati, copyright senza opinioni); leggi di scala; costi (DeepSeek-V3 con la riserva).
- **Verdetto:** i **Dati** (principale), l'**Applicazione** (non gli dice la data).
- **Regola d'uso:** gli si dice la data, gli si danno i documenti.

### Fascicolo 7 — Il complice compiacente

- **Concetti:** C08 (RLHF, adulazione).
- **Caso:** l'aggiornamento di GPT-4o troppo adulatore, rilasciato e ritirato da OpenAI ad aprile 2025 (da verificare date e comunicato).
- **Perizia:** instruction tuning, RLHF, il segnale di ricompensa (il pollice su), sycophancy.
- **Verdetto:** l'**Obiettivo** (principale), il **Mercato** (concorrente).
- **Mito da sfatare:** «se l'IA mi dà ragione, ho ragione».
- **Regola d'uso:** chiedile di criticare.

### Fascicolo 8 — Chi ti allena ti somiglia

- **Concetti:** C09.
- **Caso:** Tay (Microsoft, marzo 2016), il chatbot che imparava dalle conversazioni e fu ritirato in meno di un giorno [DA VERIFICARE: tempi]; non si riportano le frasi offensive.
- **Perizia:** fine-tuning, LoRA, dimenticanza catastrofica, overfitting, perché non si fa imparare un modello dagli utenti senza filtri.
- **Verdetto:** l'**Applicazione** (principale), i **Dati** (concorrente).
- **Occhio a:** Tay non era un LLM moderno: dichiararlo.

### Fascicolo 9 — Il sospettato che ha pensato troppo

- **Concetti:** C08 (ragionamento).
- **Caso:** modelli che ragionano e sbagliano comunque (un conto giusto fino al passaggio sette); il ragionamento mostrato che non corrisponde alla causa vera (Anthropic, aprile 2025, da verificare).
- **Perizia:** chain-of-thought, calcolo al momento della risposta, costo in token e attesa, perché mostrare i passaggi non è una prova.
- **Verdetto:** il **Modello** (limite), l'**Utente** (fiducia).
- **Regola d'uso:** verifica il risultato, non il racconto.

## Parte III — Come risponde

### Fascicolo 10 — Stessa domanda, due alibi

- **Concetti:** C10.
- **Caso:** due risposte diverse alla stessa domanda; una risposta diversa anche a temperatura 0.
- **Perizia:** campionamento, temperatura, top-p, seed; l'aritmetica in virgola mobile e il batching; perché non si fanno controlli con una sola risposta.
- **Verdetto:** nessun colpevole: è il progetto.
- **Prova tu:** P03.
- **Occhio a:** temperatura 1 non è delirio.

### Fascicolo 11 — Il testimone con la memoria corta

- **Concetti:** C11.
- **Caso:** Bing con «Sydney» (febbraio 2023): conversazioni molto lunghe che degenerarono; Microsoft limitò il numero di scambi per sessione (da verificare date e limiti).
- **Perizia:** finestra di contesto, KV cache (128 KiB per token), perché i modelli stateless «dimenticano»; *Lost in the Middle*; chat lunghe e deriva; prefill e decode.
- **Verdetto:** l'**Applicazione** (principale), il **Modello** (limite).
- **Prova tu:** P04.
- **Regola d'uso:** una chat per argomento.

### Fascicolo 12 — Il libro sbagliato

- **Concetti:** C13, C14.
- **Caso A:** Google AI Overviews (maggio 2024): il suggerimento di aggiungere colla alla pizza veniva da un commento ironico su un forum, di undici anni prima [DA VERIFICARE]. **Caso B:** Air Canada (Moffatt contro Air Canada, tribunale della Columbia Britannica, febbraio 2024): il chatbot descrisse una politica di rimborso che non esisteva, e la compagnia fu ritenuta responsabile.
- **Perizia:** RAG, recupero del documento sbagliato, ricerca ibrida, reranking, citazioni; le cinque memorie.
- **Verdetto:** l'**Applicazione** (principale), i **Dati** (concorrente).
- **Regola d'uso:** chiedi i passi citati.

### Fascicolo 13 — Il piano perfetto

- **Concetti:** C12.
- **Caso:** risolve il prologo. Perché ChatGPT confermò che le sentenze esistevano.
- **Perizia:** cause delle allucinazioni (obiettivo, dati, valutazioni che premiano il rispondere: OpenAI, settembre 2025, da verificare), calibrazione, sycophancy («sei sicuro?» come chiedere all'oste se il vino è buono), mitigazioni.
- **Precedente:** Clever Hans, il cavallo di Berlino (circa 1904) che sembrava fare i conti e rispondeva ai segnali involontari di chi lo interrogava (Pfungst, 1907): risposte giuste per le ragioni sbagliate.
- **Verdetto:** l'**Obiettivo** (principale), l'**Utente** (fiducia).
- **Prova tu:** P06.
- **Mito da sfatare:** «basta abbassare la temperatura».

## Parte IV — Il crimine in casa

### Fascicolo 14 — Out of memory

- **Concetti:** C18, C19.
- **Caso:** un utente scarica un modello «da 70 miliardi» e il PC si blocca (caso illustrativo, dichiarato); la formula da tovagliolo come perizia.
- **Perizia:** perché in locale; pesi aperti; memoria = parametri × bit ÷ 8, più KV cache e margine; la velocità = banda ÷ GB letti; prefill e decode; LLaMA e llama.cpp.
- **Verdetto:** l'**Utente** (non ha fatto il conto), con l'**Infrastruttura**.
- **Prova tu:** P08, P11.

### Fascicolo 15 — Il modello dimagrito troppo

- **Concetti:** C20.
- **Caso:** lo stesso modello che funziona diversamente su fornitori diversi: il banco di verifica dei fornitori di Moonshot per Kimi K2 (settembre 2025) e il post-mortem di Anthropic su tre bug che avevano peggiorato le risposte (settembre 2025) [DA VERIFICARE entrambi].
- **Perizia:** quantizzazione (Q8, Q4, Q3, Q2), sintomi (distrazione, caffè, fretta, amnesia), formati, calibrazione, errori dell'infrastruttura che sembrano «il modello che peggiora».
- **Verdetto:** l'**Infrastruttura** (principale), il **Mercato** (concorrente).
- **Prova tu:** P09.
- **Occhio a:** niente percentuali inventate.

### Fascicolo 16 — Il trasloco sospetto

- **Concetti:** C21, C22.
- **Caso:** un modello che «funziona» ma ci mette quattro minuti a rispondere (illustrativo).
- **Perizia:** GPU e banda; offload; `-ngl`; memoria unificata; il conto del 12 GB su 8 GB (12, 7 e 33 token/s).
- **Verdetto:** l'**Infrastruttura** (principale).
- **Prova tu:** P10.
- **Occhio a:** «offload» nei due sensi.

### Fascicolo 17 — L'alibi dei 37 miliardi

- **Concetti:** C23, C24.
- **Caso:** «un modello da 671 miliardi non gira a casa mia»: i conti dicono il contrario, con quale hardware e a quale velocità.
- **Perizia:** MoE, parametri totali e attivi, router per token, perché non riduce la memoria, decodifica speculativa, MLA.
- **Verdetto:** nessun colpevole: un malinteso sui numeri.
- **Occhio a:** le quattro correzioni nella mappa.

### Fascicolo 18 — Il caso del megawatt mancante

- **Concetti:** C25, C26.
- **Caso:** i data center e l'energia: cifre dichiarate (Google, agosto 2025: 0,24 Wh per prompt; IEA, aprile 2025) con tutte le riserve.
- **Perizia:** HBM, il muro della memoria, GPU e TPU, prezzo per token, il conto del locale (10 J per token).
- **Verdetto:** il **Mercato** (per le promesse), l'**Infrastruttura**.
- **Occhio a:** tutto datato; niente giudizi politici.

## Parte V — Le armi

### Fascicolo 19 — L'agente che ha cancellato il database

- **Concetti:** C15.
- **Caso:** un agente di sviluppo di Replit cancella un database di produzione durante un blocco delle modifiche (luglio 2025) [DA VERIFICARE: dettagli e comunicati].
- **Perizia:** ciclo di un agente, strumenti, permessi, workflow contro agente, compaction (le istruzioni perse), MCP.
- **Verdetto:** l'**Applicazione** (permessi eccessivi).
- **Regola d'uso:** permessi minimi, sandbox, conferma per ciò che non si annulla.

### Fascicolo 20 — Il biglietto nella posta

- **Concetti:** C16.
- **Casi:** Samsung (2023: codice confidenziale incollato in un servizio online); la Chevrolet da un dollaro (dicembre 2023) e il chatbot di DPD (gennaio 2024), come casi di istruzioni da parte di utenti; una vulnerabilità di tipo «zero-click» in un assistente aziendale (EchoLeak, giugno 2025) [DA VERIFICARE].
- **Perizia:** prompt injection, trifecta letale, privacy, SQL injection a confronto.
- **Verdetto:** l'**Applicazione** (principale), l'**Utente** (dati incollati).
- **Prova tu:** P14.

### Fascicolo 21 — Il concorso truccato

- **Concetti:** C17.
- **Caso:** Llama 4 e LMArena (aprile 2025: versione sperimentale in classifica diversa da quella rilasciata) [DA VERIFICARE]; i benchmark saturati e contaminati.
- **Perizia:** MMLU, SWE-bench, arene, Goodhart, contaminazione; come si fa un mini-benchmark.
- **Verdetto:** il **Mercato** (principale).
- **Prova tu:** P12.

## Parte VI — Il verdetto

### Fascicolo 22 — Il mandante

- **Concetti:** C28, C29.
- **Idea:** la tabella dei colpevoli di tutti i fascicoli: quasi sempre l'**Obiettivo** (produrre testo plausibile) e l'**Applicazione** (come lo si usa). Il lettore capisce perché l'IA «non mente» ma sbaglia con sicurezza. Ripasso storico (ELIZA, Markov, Shannon, il Transformer, ChatGPT) come «precedenti».
- **Chiusura:** le domande aperte (verifica, modelli piccoli, agenti, energia), senza date.
- **Occhio a:** l'ultimo aforisma non è una battuta contro il lettore.

### Epilogo — Manuale dell'investigatore

- **Concetti:** C30.
- **Idea:** la tabella «cosa succede sotto il cofano / cosa fai di diverso» nelle parole del libro, il **Test dell'esperto** (30 domande), e una lista di controllo in cinque domande da fare a ogni risposta dubbia.

## 6. Copertura della mappa

C01 fasc. 1 · C02 fasc. 2 · C03 fasc. 3 · C04 fasc. 4 · C05-C06 fasc. 5 · C07 fasc. 6 · C08 fasc. 7, 9 · C09 fasc. 8 · C10 fasc. 10 · C11 fasc. 11 · C12 prologo e fasc. 13 · C13-C14 fasc. 12 · C15 fasc. 19 · C16 fasc. 20 · C17 fasc. 21 · C18-C19 fasc. 14 · C20 fasc. 15 · C21-C22 fasc. 16 · C23-C24 fasc. 17 · C25-C26 fasc. 18 · C27 fasc. 2 · C28-C29 fasc. 22 · C30 epilogo.
