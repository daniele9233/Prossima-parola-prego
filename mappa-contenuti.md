# Mappa dei contenuti tecnici — la verità condivisa dei cinque libri

> È il programma d'esame. Chi chiude uno qualsiasi dei cinque libri deve saper rispondere a tutto ciò che sta qui. I libri cambiano percorso, voce, analogie ed esempi; i fatti restano questi. Le istruzioni permanenti sono in `CLAUDE.md`, i capitoli in `libri/`.

## 0. Come si usa questo file

- **Codici C01-C30.** Ogni scheda di capitolo rimanda a questi codici. La definizione completa di un concetto sta qui; nel capitolo la racconti con le parole e l'analogia madre del libro.
- **Per ogni concetto:** *Mamma* (cosa deve capire chi parte da zero), *Tecnico* (cosa deve imparare chi lavora in IT), *Numeri* (conti rifacibili), *Regola d'uso* (cosa cambia nel modo di usare l'IA), *Occhio a* (errori da evitare e correzioni già decise), *Fonti*.
- **Data dei dati: ottobre 2026.** Chi scrive ha conoscenze fino a giugno 2026: ciò che è successo dopo va cercato. Ogni cifra su hardware, prezzi, modelli, classifiche e finestre di contesto è un ordine di grandezza datato: prima di stamparla, [DA VERIFICARE] sulla fonte del produttore e indica mese e anno.
- **Segnali usati nel testo:** [DA VERIFICARE: cosa e dove] per ciò che va controllato prima della stampa. *Illustrativo* per un numero o un dialogo inventato per spiegare, da dichiarare al lettore. *Misurato* per un risultato riproducibile, da accompagnare con modello, quantizzazione, hardware e impostazioni.
- **Sezioni 5-8:** assegnazione delle storie vere ai libri, banco delle prove, fatti già corretti, fonti di base.

---

## 1. Come funziona un LLM (C01-C14)

### C01 — Un LLM prevede il prossimo token

- **Mamma:** un LLM fa una cosa sola: dato il testo scritto finora, propone il pezzo successivo con una probabilità. Ne sceglie uno, lo aggiunge, ricomincia. Chat, memoria e strumenti sono software costruito intorno.
- **Tecnico:** funzione da una sequenza di token a una distribuzione di probabilità sul vocabolario (logit, poi softmax); generazione autoregressiva; differenza tra modello e applicazione (system prompt, template di chat, strumenti); perplexity come misura di indecisione: perplexity 6 significa esitare come davanti a un dado a sei facce.
- **Numeri:** vocabolario di GPT-2 50.257 token, Llama 2 32.000, Llama 3 128.256; oggi l'ordine di grandezza è 100-250 mila. Ogni token generato richiede un passaggio completo nel modello. Markov (1913): su 20.000 lettere dell'*Eugenio Onegin* una vocale seguiva una vocale circa 13 volte su 100 e una consonante circa 66 su 100 [DA VERIFICARE: Hayes, «First Links in the Markov Chain», 2013].
- **Regola d'uso:** il modello non sa dove andrà a finire la frase mentre la scrive. Per questo chiedere prima i passaggi e poi la risposta funziona meglio del contrario.
- **Occhio a:** «è solo statistica» è un mito: per indovinare l'ultima parola di un giallo bisogna aver seguito la trama. Ma «capisce come noi» è l'errore opposto. Le catene di Markov sono del 1906 (teoria) e del 1913 (Onegin), non del 1922. Le percentuali dei dialoghi («latte 61%») sono illustrative: dichiaralo.
- **Fonti:** Shannon 1948 e 1951; Bengio e altri 2003; Vaswani e altri 2017.

### C02 — Token: l'IA non legge le parole

- **Mamma:** il testo viene spezzato in pezzi, i token, scelti dalla statistica e non dalla grammatica. Il modello vede numeri, non lettere.
- **Tecnico:** Byte Pair Encoding (Gage 1994 come compressione; Sennrich e altri 2015-2016 per la traduzione automatica; GPT-2 2019 a livello di byte); il tokenizer si addestra a parte e fa parte del modello; maiuscole, spazi e numeri producono token diversi; token glitch come «SolidGoldMagikarp» (Rumbelow e Watkins, febbraio 2023).
- **Numeri:** in inglese un token vale circa 4 caratteri, 0,75 parole. L'italiano usa in genere più token per lo stesso testo [DA VERIFICARE con un tokenizer reale, citando modello e versione: il rapporto cambia da modello a modello]. Il token è l'unità di costo (API), di velocità (token/s) e di memoria (contesto).
- **Regola d'uso:** in italiano la finestra di contesto si riempie prima e costa di più. Per contare lettere, fare anagrammi o aritmetica lunga, fai usare uno strumento (codice, calcolatrice) invece della «testa» del modello.
- **Occhio a:** niente split precisi («Straw» + «berry») senza averli verificati su un tokenizer reale. Le R di «strawberry» sono un problema di visibilità delle lettere, non di intelligenza. Il vincolo «scrivi senza la lettera E» non è un sintomo di quantizzazione: i modelli non vedono le lettere nemmeno da non quantizzati.
- **Fonti:** Sennrich 2016; Karpathy, «Let's build the GPT Tokenizer» (2024); Rumbelow e Watkins 2023.

### C03 — Embedding: il significato diventa coordinate

- **Mamma:** ogni token diventa un punto in una mappa con migliaia di dimensioni; significati vicini, punti vicini.
- **Tecnico:** matrice di embedding (vocabolario × dimensione); la similarità del coseno è il coseno dell'angolo tra due vettori; embedding statici (word2vec, gennaio 2013) contro contestuali, che cambiano strato dopo strato («pesca» frutto e «pesca» con la canna partono uguali e si separano); embedding di frasi e documenti per la ricerca (C14); le proiezioni a 2 dimensioni (PCA, t-SNE 2008, UMAP 2018) deformano le distanze, come una costellazione appiattisce stelle a distanze diverse.
- **Numeri:** dimensione dei vettori: GPT-2 small 768, GPT-3 12.288, Llama 3 8B 4.096, 70B 8.192, 405B 16.384.
- **Regola d'uso:** la ricerca per significato trova «automobile» cercando «macchina», ma inciampa su sigle, codici e nomi propri rari: lì serve la parola esatta (ricerca ibrida, C14).
- **Occhio a:** le dimensioni non hanno etichette leggibili come «regalità» o «genere»: è una semplificazione utile, da dichiararla. Re − uomo + donna ≈ regina funziona escludendo dal risultato le parole di partenza [DA VERIFICARE]. Pregiudizi assorbiti dai dati: Bolukbasi e altri 2016.
- **Fonti:** Bengio e altri 2003; Mikolov e altri 2013; Bolukbasi e altri 2016.

### C04 — Attention e Transformer

- **Mamma:** ogni parola guarda tutte le altre e decide a quali dare peso, e lo fa per tutte le parole insieme.
- **Tecnico:** Query, Key e Value; media pesata dei Value con pesi dati dal softmax del prodotto Query·Key; multi-head; maschera causale; codifica delle posizioni (RoPE, 2021); addestramento in parallelo, a differenza delle reti ricorrenti; costo quadratico con la lunghezza (C11). L'attenzione esisteva dal settembre 2014 (Bahdanau, Cho e Bengio) come aggiunta alle reti ricorrenti; la novità del 12 giugno 2017 fu eliminare la ricorrenza.
- **Numeri:** otto autori, ordine dichiarato casuale [DA VERIFICARE: nota nel paper]; modello base addestrato in circa 12 ore, modello grande in 3,5 giorni su 8 GPU [DA VERIFICARE].
- **Regola d'uso:** l'attenzione è finita e si diluisce. Istruzioni cruciali all'inizio e ripetute alla fine, una cosa per volta, struttura chiara (titoli, elenchi).
- **Occhio a:** evita «non sapevano cosa stavano inventando»: il paper accenna già a usi oltre la traduzione. Attenzione non vuol dire «capire».
- **Fonti:** Bahdanau e altri 2014; Vaswani e altri 2017.

### C05 — Layer: il fascicolo che sale di piano in piano

- **Mamma:** il modello è una pila di decine di blocchi uguali; a ogni piano la rappresentazione del testo si arricchisce, senza che nulla venga cancellato.
- **Tecnico:** ogni blocco = attenzione + rete feed-forward (MLP), con normalizzazione e connessioni residue; il *residual stream* è il «fascicolo» a cui ogni blocco aggiunge qualcosa; la maggior parte dei parametri sta nei blocchi, per questo si possono dividere tra GPU e CPU (C22).
- **Numeri:** Llama 3 ha 32 layer nella versione 8B, 80 nella 70B, 126 nella 405B; GPT-3 ne ha 96.
- **Occhio a:** i layer aggiungono informazione, non fanno da setaccio. «Grammatica in basso, significato in alto» è una tendenza osservata, non una regola netta.
- **Storie:** Golden Gate Claude (Anthropic, maggio 2024): amplificando una caratteristica interna il modello si dichiarava il Golden Gate Bridge.

### C06 — Parametri e ordini di grandezza

- **Mamma:** un parametro è un numero, una manopola. «8B» vuol dire 8 miliardi di manopole. Nessuna contiene un fatto da sola: la conoscenza è distribuita.
- **Tecnico:** pesi di attenzione e MLP, embedding; parametri non uguale a prestazioni (modelli piccoli addestrati più a lungo battono vecchi modelli grandi); denso contro sparso (C23).
- **Numeri:** GPT-2 1,5 miliardi (2019), GPT-3 175 miliardi (2020), Llama 3.1 405 miliardi (luglio 2024). Per dare il senso della scala: un miliardo di secondi sono circa 31,7 anni; mille miliardi di secondi, circa 31.700 anni.
- **Regola d'uso:** il numero di parametri dice quanta memoria serve (C19), non quanto è bravo.
- **Occhio a:** paragoni con il cervello (86 miliardi di neuroni, circa 10¹⁴ sinapsi) e con la Via Lattea (100-400 miliardi di stelle) sono suggestioni, non equivalenze: dichiaralo.

### C07 — Addestramento (pre-training) e leggi di scala

- **Mamma:** il modello legge enormi quantità di testo, prova a indovinare la parola successiva e ogni errore corregge un poco tutte le manopole. Poi ripete, miliardi di volte.
- **Tecnico:** funzione di perdita (cross-entropy); backpropagation (precursori 1970 e 1974, resa celebre da Rumelhart, Hinton e Williams nel 1986); discesa del gradiente con ottimizzatore Adam (2014); learning rate con riscaldamento e decadimento; precisione mista (BF16, FP8 in DeepSeek-V3); parallelismo su migliaia di GPU (dati, tensori, pipeline); leggi di scala (Kaplan e altri, gennaio 2020); Chinchilla (Hoffmann e altri, marzo 2022): 70 miliardi di parametri su 1,4 mila miliardi di token battono Gopher da 280, regola indicativa di circa 20 token per parametro.
- **Numeri:** Llama 3 8B addestrato su oltre 15 mila miliardi di token, circa 1.900 token per parametro: sovrallenare un modello piccolo costa di più all'addestramento ma lo rende più economico da far girare per sempre. DeepSeek-V3: 2,788 milioni di ore-GPU H800, circa 5,6 milioni di dollari dichiarati per il solo addestramento finale. Modelli di frontiera: oltre 100 milioni (dichiarazioni dei produttori) [DA VERIFICARE].
- **Regola d'uso:** la conoscenza ha una data (cutoff). Il modello non impara dalla tua chat: ciò che gli scrivi sparisce quando chiudi, salvo funzioni dichiarate (C13).
- **Occhio a:** la cifra di DeepSeek-V3 esclude ricerca ed esperimenti precedenti: va detto. Sul copyright dei dati di addestramento riporta solo fatti datati, non opinioni.
- **Fonti:** Kaplan e altri 2020; Hoffmann e altri 2022; report tecnici di Llama 3 e DeepSeek-V3.

### C08 — Da completatore ad assistente (post-training) e modelli che ragionano

- **Mamma:** dopo l'addestramento il modello è un completatore di testi. Diventa un assistente con esempi di buone risposte e con il giudizio di persone (pollice su, pollice giù). Poi si può insegnargli a ragionare scrivendo una brutta copia prima di rispondere.
- **Tecnico:** fine-tuning supervisionato (SFT); RLHF (Christiano e altri 2017; InstructGPT, marzo 2022); DPO (2023); Constitutional AI (Anthropic, dicembre 2022); la «personalità» nasce in gran parte qui. *Ragionamento:* chain-of-thought (Wei e altri, gennaio 2022); «Let's think step by step» (Kojima e altri, maggio 2022); apprendimento per rinforzo su problemi verificabili; o1 (12 settembre 2024); DeepSeek-R1 (20 gennaio 2025, pesi aperti, licenza MIT); calcolo al momento della risposta (test-time compute); costo in token e in attesa.
- **Numeri:** InstructGPT da 1,3 miliardi di parametri preferito dai valutatori a GPT-3 da 175. Il 27 gennaio 2025 NVIDIA perse in Borsa circa il 17% in un giorno dopo il clamore su DeepSeek-R1 [DA VERIFICARE: cifre].
- **Regola d'uso:** se l'IA ti dà ragione, non vuol dire che hai ragione (*sycophancy*): chiedile di criticare la tua idea. Per logica, matematica e codice scegli un modello che ragiona; per un riassunto è tempo e denaro sprecati.
- **Occhio a:** un modello base a cui chiedi «Qual è la capitale della Francia?» può continuare con «Qual è la capitale della Germania?»: è un esempio da mostrare. Il ragionamento mostrato a schermo non è per forza il resoconto fedele di come il modello arriva alla risposta (Anthropic, aprile 2025 [DA VERIFICARE]). L'aggiornamento di GPT-4o troppo adulatore, ritirato da OpenAI ad aprile 2025 [DA VERIFICARE].
- **Fonti:** Ouyang e altri 2022; Wei e altri 2022; paper di DeepSeek-R1.

### C09 — Fine-tuning, LoRA, distillazione

- **Mamma:** il fine-tuning è un corso serale: insegna stile, formato e comportamento a un modello già preparato. Non è il modo giusto per insegnargli fatti che cambiano.
- **Tecnico:** LoRA (Hu e altri 2021): pesi originali congelati, più due piccole matrici addestrabili per layer. QLoRA (Dettmers e altri, maggio 2023): base quantizzata a 4 bit più adattatori, un modello da 65 miliardi su una GPU da 48 GB. Overfitting; dimenticanza catastrofica (si impara il compito nuovo e si perde l'abilità vecchia). Distillazione (Hinton, Vinyals e Dean 2015): un allievo piccolo imita un maestro grande; modelli piccoli (SLM) come Phi, Gemma, Qwen piccoli; DeepSeek-R1-Distill. Per i tecnici: un overlay, con il modello base in sola lettura e l'adattatore come strato scrivibile, come nelle immagini dei container.
- **Numeri:** Alpaca (Stanford, marzo 2023): LLaMA 7B affinato su 52.000 esempi per meno di 600 dollari dichiarati [DA VERIFICARE]. «Poche centinaia di dollari» vale per LoRA su modelli piccoli e medi: dichiaralo.
- **Regola d'uso:** l'ordine delle scelte è prima un buon prompt, poi il RAG (C14), il fine-tuning solo alla fine.
- **Fonti:** Hu e altri 2021; Dettmers e altri 2023; Hinton e altri 2015.

### C10 — Campionamento: temperatura, top-p e compagnia

- **Mamma:** il modello non sceglie «la» parola: produce una classifica di probabilità e poi si estrae. Temperatura e top-p decidono come estrarre.
- **Tecnico:** i logit si dividono per la temperatura prima del softmax; a temperatura 0 si sceglie sempre il più probabile (greedy); top-k, top-p (*nucleus sampling*, Holtzman e altri, aprile 2019), min-p (2024), penalità di ripetizione, seed. Anche a temperatura 0 le risposte possono variare un poco, per l'aritmetica in virgola mobile e il batching sui server (Thinking Machines, settembre 2025 [DA VERIFICARE]).
- **Regola d'uso:** temperatura bassa per estrazione, codice e fatti; media per scrivere; alta per brainstorming. Un testo che si ripete in loop è spesso temperatura troppo bassa o modello troppo degradato (C20).
- **Occhio a:** temperatura 1 non è «delirante»: è la distribuzione così come il modello l'ha imparata, ed è il valore predefinito di molte API. Il delirio arriva sopra 1. Abbassare la temperatura non elimina le allucinazioni (C12).
- **Fonti:** Holtzman e altri 2019.

### C11 — Finestra di contesto, KV cache, prefill e decode

- **Mamma:** il modello vede solo ciò che sta sulla sua scrivania. Tra una richiesta e l'altra non ricorda nulla: è l'applicazione che gli rimanda tutta la conversazione.
- **Tecnico:** LLM stateless come HTTP; la KV cache conserva Key e Value già calcolati per non rileggere tutto a ogni token. Formula: 2 (K e V) × layer × teste KV × dimensione della testa × byte. Costo quadratico dell'attenzione classica; FlashAttention (Dao e altri, 2022) evita di materializzare la matrice; GQA (2023), MLA (DeepSeek-V2, maggio 2024) e finestre scorrevoli riducono la cache. *Prefill* = lettura del prompt, in parallelo, limitata dal calcolo; *decode* = generazione token per token, limitata dalla banda di memoria (C19). *TTFT* = tempo al primo token. Prompt caching: il prefisso ripetuto costa meno. «Lost in the Middle» (Liu e altri, luglio 2023): con testi lunghi si usa meglio l'inizio e la fine che il centro. «Context rot» (Chroma, luglio 2025 [DA VERIFICARE]).
- **Numeri:** Llama 3 8B: 32 layer × 8 teste KV × 128 × 2 (K e V) × 2 byte (16 bit) = 131.072 byte, cioè 128 KiB per token; con 8.192 token sono circa 1 GiB, con 131.072 (128K) circa 16 GiB. Llama 3 70B: 80 × 8 × 128 × 2 × 2 = 327.680 byte, 320 KiB per token, circa 40 GiB a 128K. Crescita: GPT-3 2.048 token (2020), GPT-4 8K e 32K (marzo 2023), Claude 100K (maggio 2023), Gemini 1.5 1M (febbraio 2024), Llama 4 Scout 10M dichiarati (aprile 2025) [DA VERIFICARE tutte].
- **Regola d'uso:** una chat per argomento; quando è lunga o inquinata ricomincia con un riassunto; metti le istruzioni cruciali all'inizio e ripetile alla fine; non incollare 200 pagine se ne bastano 5.
- **Occhio a:** 128K token non sono 128K parole. Le dimensioni vanno sempre datate. Una scrivania grande come uno stadio non garantisce di vedere bene le carte al centro. La «memoria» della finestra di contesto non è la memoria RAM del computer (omonimia, C13).

### C12 — Allucinazioni

- **Mamma:** il modello genera testo plausibile, non verificato. Quando non sa, non ha un campanello interno affidabile che lo fermi: produce la risposta che suona giusta, con la stessa sicurezza di quando sa.
- **Tecnico:** nascono dall'obiettivo (testo probabile, non vero), dai dati (lacune, errori, cutoff), dalle valutazioni che premiano chi risponde rispetto a chi si astiene (OpenAI, settembre 2025 [DA VERIFICARE]), dall'adulazione (C08). Esiste una calibrazione parziale: i modelli «sanno in parte cosa non sanno» (Kadavath e altri, 2022). Tre famiglie da distinguere: errore di fatto, errore di logica, istruzione ignorata. Contromisure: RAG con citazioni verificabili (C14), strumenti esterni, ragionamento, verifica umana.
- **Regola d'uso:** chiedi citazioni testuali e controllale; offri l'uscita «non lo so»; per fatti recenti o precisi dagli i documenti o uno strumento di ricerca.
- **Occhio a:** «basta abbassare la temperatura» è un mito: si inventa con sicurezza anche a temperatura 0, e anche le fonti citate possono essere inventate. Chiedere al modello «sei sicuro?» è come chiedere all'oste se il vino è buono.
- **Fonti:** Ji e altri 2022 (rassegna); OpenAI 2025 [DA VERIFICARE]; Kadavath e altri 2022.

### C13 — Le cinque memorie

- **Mamma:** la parola «memoria» in IA vuol dire cose diverse. Distinguerle evita metà dei malintesi.
- **Tecnico:** (1) **pesi** = memoria a lungo termine, congelata alla data di cutoff; (2) **contesto** = memoria di lavoro, ciò che il modello vede ora; (3) **KV cache** = appunti tecnici per non rileggere (C11); (4) **memoria dell'app** = riassunti e fatti salvati dall'applicazione e reincollati nel contesto a ogni richiesta; (5) **memoria esterna** = documenti, database vettoriali, file di istruzioni e appunti di un agente (RAG, C14; file come CLAUDE.md o AGENTS.md). Più una sesta, che non c'entra: la **memoria del computer** (RAM e VRAM, C19).
- **Regola d'uso:** ciò che deve essere ricordato va scritto: nel prompt, in un documento, in un file. Non aspettarti che «impari» da una conversazione.
- **Occhio a:** «ricorda tutto di me» è falso: è testo salvato, può essere sbagliato o obsoleto, e ha implicazioni di privacy (C16).

### C14 — RAG: l'esame a libro aperto

- **Mamma:** il RAG non insegna niente al modello: prima della risposta gli mette sulla scrivania i documenti giusti.
- **Tecnico:** Lewis e altri (maggio 2020); chunking; embedding (C03); database vettoriali (pgvector su PostgreSQL, FAISS, Chroma, Qdrant); ricerca ibrida tra parole chiave (BM25) e vettori; reranking; riscrittura della domanda; valutazione separata di recupero e risposta; confronto con il contesto lungo.
- **Regola d'uso:** fornisci i documenti e chiedi di citare i passi usati.
- **Occhio a:** il RAG non è la memoria del modello, né il fine-tuning, né la ricerca web. Il fallimento tipico: il bibliotecario porta il libro sbagliato e il modello risponde, sicurissimo, sul libro sbagliato.
- **Fonti:** Lewis e altri 2020.

---

## 2. Come si usa davvero: agenti, sicurezza, misure (C15-C17)

### C15 — Agenti e workflow agentici

- **Mamma:** un chatbot risponde; un agente agisce in ciclo: decide, usa uno strumento, guarda il risultato, corregge il tiro e ricomincia finché ha finito.
- **Tecnico:** ReAct (Yao e altri, ottobre 2022); function calling (OpenAI, giugno 2023); MCP, il Model Context Protocol (Anthropic, novembre 2024), donato il 9 dicembre 2025 alla Agentic AI Foundation della Linux Foundation insieme a goose di Block e AGENTS.md di OpenAI; l'*harness*: ciclo, strumenti, permessi e memoria che trasformano un modello in agente. **Workflow contro agente** (Anthropic, «Building effective agents», dicembre 2024): nel workflow il percorso lo scrive lo sviluppatore (concatenamento di prompt, instradamento, parallelizzazione, orchestratore-lavoratori, valutatore-ottimizzatore); nell'agente il percorso lo decide il modello. Sub-agenti; riassunto del contesto (*compaction*); pianificazione; conferma umana; valutazione degli agenti; METR (marzo 2025): la durata dei compiti che gli agenti portano a termine sembra raddoppiare ogni 7 mesi circa [DA VERIFICARE]. Agenti in locale: servono modelli addestrati per le chiamate di strumenti, e server locali con API compatibili (llama.cpp, Ollama, LM Studio).
- **Numeri:** ogni passo rilegge il contesto, quindi un agente costa molto più di una chat. Venti passi da 500 token a 10 token/s sono 10.000 token, cioè circa 17 minuti: in locale la velocità pesa più che in chat.
- **Regola d'uso:** permessi minimi, sandbox, log, conferma umana per le azioni irreversibili; mai root in produzione.
- **Occhio a:** «harness» ha due significati nel libro (agenti e valutazione, C17): dichiaralo. Evita «l'agente ha deciso di...» senza spiegare cosa succede davvero.
- **Fonti:** Yao e altri 2022; Anthropic, dicembre 2024; documentazione di MCP.

### C16 — Sicurezza e privacy

- **Mamma:** un agente che legge una mail può obbedire a ciò che ci trova scritto dentro, anche se l'ha scritto un malintenzionato. E ciò che incolli in un servizio online esce dal tuo computer.
- **Tecnico:** *prompt injection* (termine di Simon Willison, settembre 2022), diretta e indiretta (Greshake e altri, febbraio 2023): è la SQL injection dell'era degli LLM, con la differenza che non esiste un equivalente delle prepared statements, perché istruzioni e dati viaggiano nello stesso canale, il testo. La «trifecta letale» di Willison (giugno 2025): dati privati + contenuti non fidati + canale verso l'esterno [DA VERIFICARE]. Jailbreak; fuga di dati; catena di fornitura (server MCP, plugin e skill non fidati); privacy: il Garante italiano bloccò ChatGPT il 30 marzo 2023, riammesso a fine aprile [DA VERIFICARE]; modelli locali: i dati non lasciano il PC, ma un agente locale con accesso alla rete può comunque farli uscire.
- **Regola d'uso:** un dato non fidato non deve mai poter comandare. Dividi i privilegi: chi legge la posta non invia la posta.
- **Fonti:** Willison 2022 e 2025; Greshake e altri 2023.

### C17 — Come si misura un'IA

- **Mamma:** per dire che un modello è migliore di un altro servono prove standard, ma i modelli imparano presto a studiare per il test.
- **Tecnico:** MMLU (2020), HumanEval (2021), GSM8K (2021), SWE-bench (ottobre 2023), GPQA, ARC-AGI, Humanity's Last Exam (2025); lm-evaluation-harness di EleutherAI; arene con voto umano alla cieca (LMArena, dal maggio 2023); contaminazione dei dati; legge di Goodhart; saturazione; perplexity e divergenza KL come termometro delle quantizzazioni (C20); un mini-benchmark personale di 20 domande.
- **Regola d'uso:** confronta sempre sul tuo compito, con modelli e date.
- **Occhio a:** niente confronti tra modelli senza data: «GPT-4 contro Llama 3» invecchia in pochi mesi. Llama 4 Maverick (aprile 2025) in classifica con una versione sperimentale diversa da quella rilasciata [DA VERIFICARE]. I due significati di «harness» (C15).
- **Fonti:** paper dei singoli benchmark; LMArena.

---

## 3. Un'IA a casa tua: modelli locali e hardware (C18-C26)

### C18 — Perché in locale

- **Mamma:** un modello locale gira sul tuo computer: nessun abbonamento, nessuna connessione, nessuno vede cosa scrivi. In cambio, di solito, non è bravo come i più grandi.
- **Tecnico:** a favore: privacy, costo marginale nullo, uso offline, il modello non cambia sotto i piedi, controllo, sperimentazione. Contro: qualità inferiore ai modelli di frontiera, hardware, manutenzione, consumi, sicurezza dell'agente. *Pesi aperti* (open weights) non è *open source*: l'Open Source AI Definition 1.0 è dell'ottobre 2024 [DA VERIFICARE]; licenze diverse (Apache 2.0, MIT, la licenza di Llama con limiti). Strumenti: llama.cpp (Georgi Gerganov, marzo 2023), il formato GGUF (agosto 2023), Ollama, LM Studio, Jan, llamafile, MLX (Apple, dicembre 2023), vLLM (2023), il Hugging Face Hub. Famiglie di modelli a pesi aperti, da aggiornare a ogni libro con data: Llama, Mistral e Mixtral, Qwen, DeepSeek, Gemma, gpt-oss, Phi, Kimi.
- **Storia:** nel marzo 2023 i pesi di LLaMA, distribuiti da Meta ai soli ricercatori, finiscono in rete; pochi giorni dopo Gerganov pubblica llama.cpp e fa girare il modello su un portatile, quantizzato a 4 bit [DA VERIFICARE: date].
- **Regola d'uso:** scegli prima il compito, poi il modello, poi la quantizzazione; poi prova 10 prompt tuoi.

### C19 — La formula da tovagliolo: memoria e velocità

- **Mamma:** per far girare un modello in casa servono due conti, uno per la memoria e uno per la velocità, e stanno su un tovagliolo.
- **Tecnico:**
  - **Memoria** ≈ miliardi di parametri × bit ÷ 8, in GB, più la KV cache (C11) e un margine del 10-20%.
  - **Velocità di generazione** (decode) ≈ banda della memoria (GB/s) ÷ GB letti per token. Per i modelli MoE contano solo i parametri attivi (C23).
  - **Perché la banda:** per ogni token bisogna leggere (quasi) tutti i pesi, e per ogni peso si fanno solo due operazioni: la macchina passa più tempo ad aspettare i dati che a calcolare. Il prefill invece lavora su molti token insieme e viene limitato dal calcolo.
  - **Perché il cloud costa poco:** un server serve centinaia di utenti insieme (*batching*), quindi ogni lettura dei pesi lavora per molti. Chi usa il modello da solo non può dividere la lettura con nessuno.
- **Numeri (teorici, tetto massimo; in pratica si resta sotto, spesso al 60-80% [DA VERIFICARE]):**
  - Llama 3 8B in Q4_K_M occupa circa 4,9 GB. Su una RTX 4090 (1.008 GB/s): 1.008 ÷ 4,9 ≈ 205 token/s. Su RAM DDR5 dual channel (circa 96 GB/s): 96 ÷ 4,9 ≈ 20 token/s.
  - gpt-oss-120b: 116,8 miliardi di parametri totali, 5,1 attivi, pesi MoE in MXFP4 (circa 4,25 bit), file da 60,8 GiB. Per token si leggono 5,1 × 4,25 ÷ 8 ≈ 2,7 GB: su 96 GB/s, un tetto di circa 35 token/s.
  - DeepSeek-V3 671 miliardi (37 attivi) a circa 4,8 bit: pesi 671 × 4,8 ÷ 8 ≈ 400 GB; per token 37 × 4,8 ÷ 8 ≈ 22 GB; su 819 GB/s un tetto di circa 37 token/s. Una dimostrazione su Mac Studio M3 Ultra da 512 GB (marzo 2025) riportò circa 20 token/s [DA VERIFICARE].
  - Lettura umana: circa 240 parole al minuto, cioè 4 parole al secondo, circa 5-8 token/s [DA VERIFICARE]: sotto questa soglia il modello va più piano di come leggi.
- **Banda e capacità tipiche (ottobre 2026, da verificare prima della stampa):**

| Memoria o macchina | Capacità | Banda |
|---|---|---|
| RAM DDR5 dual channel | 32-128 GB | circa 80-96 GB/s |
| Apple M4 Max | fino a 128 GB | 546 GB/s |
| Apple M3 Ultra | fino a 512 GB | 819 GB/s |
| AMD Ryzen AI Max+ 395 («Strix Halo») | fino a 128 GB | 256 GB/s |
| NVIDIA DGX Spark | 128 GB | 273 GB/s |
| NVIDIA RTX 4090 | 24 GB | 1.008 GB/s |
| NVIDIA RTX 5090 | 32 GB | 1.792 GB/s |
| NVIDIA H100 (SXM) | 80 GB | 3,35 TB/s |
| NVIDIA B200 | 192 GB | circa 8 TB/s |
| Google TPU Ironwood (7ª generazione) | 192 GB | circa 7,4 TB/s |
| NVIDIA Vera Rubin (annunciata) | 288 GB HBM4 | circa 22 TB/s annunciati [specifiche cambiate più volte] |

- **Regola d'uso:** prima di scaricare un modello fai il conto: pesi + KV cache + margine devono stare nella memoria veloce; poi calcola il tetto di velocità.
- **Occhio a:** GB e GiB non sono uguali. La velocità la decide la parte più lenta, non una media. Il prefill di un prompt lungo su sola CPU può richiedere minuti.
- **Prova tu:** scaricare un modello piccolo con LM Studio o Ollama e confrontare i token/s misurati con il conto fatto a mano.

### C20 — Quantizzazione

- **Mamma:** arrotondare i miliardi di numeri del modello, perché occupino meno memoria e si leggano più in fretta. Si perde un po' di precisione, non il senso.
- **Tecnico:** non si arrotondano decimali: ogni peso viene ricondotto a pochi livelli interi (a 4 bit sono 16, come 2⁴). Il trucco che salva la qualità è la quantizzazione a blocchi: per esempio 32 pesi condividono una scala. Formati: GGUF con sigle come Q8_0, Q6_K, Q5_K_M, Q4_K_M, Q3_K_M, Q2_K (dove i bit effettivi per peso sono un po' più di quelli del nome, per via delle scale); GPTQ (2022), AWQ (2023, protegge i pesi «salienti», circa l'1%), FP8, MXFP4 e NVFP4 (formati a 4 bit in virgola mobile con scala per blocco, supportati nativamente dalle GPU Blackwell: qui la quantizzazione accelera anche il calcolo, non solo la memoria); BitNet b1.58 (febbraio 2024, pesi ternari); quantizzazione dinamica di Unsloth (DeepSeek-R1 ridotto da circa 720 GB a circa 131 GB a 1,58 bit, gennaio 2025 [DA VERIFICARE]); *imatrix* (matrice di importanza) per calibrare; outlier (LLM.int8(), Dettmers e altri 2022); quantizzazione della KV cache (in llama.cpp `--cache-type-k` e `--cache-type-v`). A parità di memoria spesso un modello grande quantizzato batte uno piccolo a piena precisione («The case for 4-bit precision», Dettmers e Zettlemoyer, dicembre 2022); i modelli piccoli e i compiti delicati (codice, matematica, lingue diverse dall'inglese) soffrono prima.
- **Numeri:** bit effettivi per peso, indicativi: Q8_0 circa 8,5; Q6_K circa 6,6; Q5_K_M circa 5,7; Q4_K_M circa 4,8-4,9; Q3_K_M circa 3,9-4; Q2_K circa 2,6-3,4 [DA VERIFICARE: README di llama.cpp]. Un modello da 8 miliardi passa da circa 16 GB a 16 bit (8 × 16 ÷ 8) a circa 5 GB in Q4_K_M.
- **Regola d'uso:** parti da Q4_K_M; sali a Q6 o Q8 se hai memoria e il compito è delicato; sotto Q3 solo con modelli grandi o per curiosità; a parità di memoria preferisci il modello più grande.
- **Occhio a:** niente percentuali inventate come «95%» (percentuali solo se misurate). La qualità cala dolcemente da 16 a 4 bit e crolla più in fretta sotto i 3, perché l'errore di ciascun peso si somma a quello di milioni di altri, layer dopo layer. Il vincolo «senza la lettera E» non è un sintomo (C02). Il loop «importante importante» si collega al campionamento (C10).
- **Fonti:** Dettmers e altri 2022; Frantar e altri 2022 (GPTQ); Lin e altri 2023 (AWQ).

### C21 — GPU: perché proprio loro

- **Mamma:** una CPU ha pochi cuochi bravissimi; una GPU ne ha migliaia che sanno fare solo poche operazioni, ma tutte insieme. Per un'IA, che è un'enorme quantità di moltiplicazioni uguali tra loro, vince la seconda.
- **Tecnico:** matrici e parallelismo; Tensor Core (dal 2017, con Volta); CUDA (annunciato nel 2006, disponibile nel 2007); AlexNet (2012) addestrata su due NVIDIA GTX 580 da 3 GB in circa cinque o sei giorni; DGX-1 (2016); VRAM contro RAM; banda; interconnessioni (PCIe 5.0 x16 circa 64 GB/s per direzione, NVLink di quinta generazione 1,8 TB/s per GPU); parallelismo tra più GPU (di tensore, di pipeline, di dati); consumi (RTX 5090 575 W, H100 700 W, B200 circa 1.000 W [DA VERIFICARE]); alternative a CUDA (ROCm, Vulkan, Metal). I nomi delle architetture NVIDIA sono scienziati: Kepler, Maxwell, Pascal, Volta, Turing, Ampere, Hopper, Ada Lovelace, Blackwell, Rubin, e nella roadmap Feynman.
- **Occhio a:** non «la stessa matematica delle ombre nei videogiochi», ma lo stesso tipo di calcolo: milioni di moltiplicazioni di matrici in parallelo. Le GPU per giocare e quelle per data center non sono uguali (memoria HBM, interconnessioni).
- **Fonti:** Krizhevsky, Sutskever e Hinton 2012.

### C22 — Offloading e memoria unificata

- **Mamma:** quando il modello non entra nella memoria veloce, una parte va in quella lenta. Funziona, ma la velocità la decide la parte lenta.
- **Tecnico:** i layer si dividono tra GPU (VRAM) e CPU (RAM): `-ngl` in llama.cpp, il cursore *GPU Offload* in LM Studio, `num_gpu` in Ollama (di solito decide da solo); dimensione del contesto `-c` e spazio da lasciare alla KV cache; sui Mac con Apple Silicon e sui sistemi con memoria unificata (Strix Halo, DGX Spark) CPU e GPU condividono la stessa memoria e il problema si pone in modo diverso; nei modelli MoE si possono tenere in RAM solo gli esperti (in llama.cpp `--n-cpu-moe` o `-ot` [DA VERIFICARE i nomi sulla versione corrente]); per i tecnici è lo swap: un server che va in swap ha già mostrato cosa succede a un modello che non sta in VRAM.
- **Esempio con il conto completo:** modello quantizzato da 12 GB; scheda con 8 GB di VRAM (banda circa 400 GB/s); RAM DDR5 dual channel (circa 80 GB/s). Lasci 1-1,5 GB liberi per KV cache, driver e desktop: restano circa 7 GB per i pesi (poco meno del 60% dei layer); gli altri 5 GB restano in RAM. Per ogni token: 7 GB ÷ 400 GB/s = 17,5 ms sulla GPU, 5 GB ÷ 80 GB/s = 62,5 ms sulla CPU, totale 80 ms: circa 12 token/s. Solo CPU: 12 ÷ 80 = 150 ms, circa 7 token/s. Tutto in VRAM (a pari banda): 12 ÷ 400 = 30 ms, circa 33 token/s. Il 40% dei pesi rimasto in RAM si mangia quasi l'80% del tempo.
- **Occhio a:** «offload» si usa nei due sensi: in llama.cpp e LM Studio indica i layer spostati sulla GPU, in altri framework (Accelerate, DeepSpeed) ciò che si scarica dalla GPU verso la CPU: dichiaralo. Durante la generazione il collo di bottiglia non è il bus PCIe ma la banda della RAM: i layer in RAM li calcola la CPU e tra le due parti passano solo le attivazioni, poche decine di KB per token. Il PCIe pesa quando sono i pesi a viaggiare. «Velocità intermedia» è vero ma ingannevole: i tempi si sommano, quindi il risultato è molto più vicino alla CPU che alla GPU.
- **Prova tu:** caricare lo stesso modello con offload al 100% e al 50% e misurare i token/s.

### C23 — Mixture-of-Experts

- **Mamma:** un modello MoE ha tanti «specialisti» ma per ogni token ne accende solo pochi. Calcola meno, ma deve avere spazio per tutti.
- **Tecnico:** un router sceglie, per ogni token e in ogni layer, quali esperti usare (top-k); parametri totali contro attivi; bilanciamento del carico tra esperti; esperti condivisi. Il MoE risparmia **calcolo, non memoria**: la memoria la decidono i parametri totali, la velocità quelli attivi. Per un bilanciatore di carico: smista ogni singolo pacchetto invece di ogni connessione.
- **Numeri (da datare e verificare):** Shazeer e altri (gennaio 2017), *sparsely-gated MoE*, e Shazeer è anche uno degli autori del Transformer; Mixtral 8x7B (dicembre 2023): 2 esperti su 8 per token, circa 13 miliardi attivi su 47; DeepSeek-V3 (dicembre 2024): 671 miliardi totali, 37 attivi, 256 esperti più uno condiviso, 8 attivi per token; Qwen3-30B-A3B e Qwen3-235B-A22B (aprile 2025; «A3B» vuol dire 3 miliardi attivi); Llama 4 Scout (109 miliardi totali, 17 attivi, 16 esperti) e Maverick (circa 400 miliardi totali, 17 attivi, 128 esperti), aprile 2025; Kimi K2 (luglio 2025, circa mille miliardi totali, 32 attivi); gpt-oss-120b e gpt-oss-20b (OpenAI, agosto 2025, 116,8 e circa 21 miliardi totali, 5,1 e 3,6 attivi). Di GPT-4 si dice che fosse un MoE: voce mai confermata.
- **Occhio a:**
  - gli esperti non sono «il cuoco» e «il programmatore»: il router sceglie per ogni token e in ogni layer, non per argomento della domanda; negli studi gli esperti si specializzano spesso in schemi poco leggibili, come la punteggiatura o la sintassi del codice (lo osserva il paper di Mixtral);
  - «2 su 8» vale per Mixtral: i modelli recenti hanno decine o centinaia di esperti più piccoli;
  - il MoE non riduce la memoria: la clinica deve avere spazio per tutti i medici, anche per quelli che oggi non visitano.
- **Fonti:** Shazeer e altri 2017; Fedus e altri 2021 (Switch Transformer); Jiang e altri 2024 (Mixtral); DeepSeek-V3.

### C24 — Altri trucchi per correre di più con meno

- **Mamma:** ci sono molti accorgimenti per far costare meno ogni risposta; non serve conoscerli tutti, ma sapere che esistono spiega perché i modelli nuovi vanno più in fretta dei vecchi sulla stessa macchina.
- **Tecnico:** *speculative decoding* (Leviathan e altri, novembre 2022; Chen e altri, febbraio 2023): un modello piccolo propone alcuni token, il grande li verifica in un solo passaggio; il risultato ha la stessa distribuzione di probabilità dell'originale. FlashAttention (2022); PagedAttention e vLLM (2023) con il *continuous batching*; GQA (2023); MLA (DeepSeek-V2, maggio 2024, che dichiarava una KV cache ridotta di oltre il 90%); attenzione a finestra scorrevole (Mistral 7B, 2023); alternative all'attenzione (Mamba, dicembre 2023, e modelli ibridi); *multi-token prediction*; prompt caching; distillazione e modelli piccoli (C09).
- **Occhio a:** non è l'MLA a evitare di «rileggere gli appunti da zero», ma la KV cache: l'MLA la comprime. I guadagni di velocità vanno misurati caso per caso [DA VERIFICARE].

### C25 — I nuovi hardware per l'IA

- **Mamma:** i chip per l'IA somigliano meno a «un computer più veloce» e più a «una cucina industriale più grande, con il frigo accanto ai fornelli».
- **Tecnico:**
  - **Data center:** H100 (2022, 80 GB HBM3, 3,35 TB/s), H200 (141 GB, 4,8 TB/s), B200 (192 GB, circa 8 TB/s), B300 (288 GB), Vera Rubin (annunciata per il secondo semestre del 2026, 288 GB di HBM4, circa 22 TB/s e circa 50 PFLOPS in FP4 [DA VERIFICARE: le specifiche sono cambiate più volte]), poi Rubin Ultra (2027) e Feynman. Rack come GB200 NVL72 (72 GPU in un unico dominio NVLink). **HBM** (High Bandwidth Memory): memorie DRAM impilate in verticale accanto al chip, che danno la banda ma sono care e scarse. **TPU** di Google (Ironwood, settima generazione: 192 GB, circa 7,4 TB/s, fino a 9.216 chip in un pod). Chip proprietari (Trainium di AWS, MTIA di Meta). **Groq** (memoria SRAM sul chip: token/s altissimi ma poca capacità per chip). **Cerebras** (WSE-3, 2024: un intero wafer, 4 mila miliardi di transistor, 900.000 core, 44 GB di SRAM).
  - **Sul tuo tavolo:** schede come la RTX 5090 (32 GB, 1.792 GB/s) o le workstation con 96 GB; Apple Silicon con memoria unificata (M4 Max 546 GB/s; M3 Ultra 819 GB/s, fino a 512 GB); AMD Ryzen AI Max+ 395 (fino a 128 GB, 256 GB/s); NVIDIA DGX Spark (128 GB LPDDR5x, 273 GB/s, consegne da ottobre 2025): macchine da capacità più che da velocità, perfette per modelli MoE grandi; **NPU** nei portatili (i Copilot+ PC chiedono almeno 40 TOPS, 2024); modelli da 1-4 miliardi su telefono (Apple Intelligence, Gemini Nano).
  - **Il muro della memoria** (*memory wall*): il calcolo cresce più in fretta della banda della memoria (Gholami e altri, 2024 [DA VERIFICARE]); per questo HBM, FP4, MoE, cache compresse e hardware con la memoria accanto al calcolo. La scarsità di HBM e di DRAM ha fatto salire i prezzi della RAM tra il 2025 e il 2026 [DA VERIFICARE].
- **Curiosità da usare:** le architetture NVIDIA portano nomi di scienziati (C21), e «Rubin» è Vera Rubin, l'astronoma che negli anni Settanta raccolse le prove della materia oscura studiando la rotazione delle galassie.
- **Occhio a:** specifiche, prezzi e date cambiano di continuo: chiudi ogni capitolo hardware con una tabella datata e il rimando alla fonte del produttore.

### C26 — Costi ed energia

- **Mamma:** ogni risposta costa soldi e corrente. Poco per una domanda, tanto per milioni di domande e per agenti che lavorano per ore.
- **Tecnico:** il prezzo si dà per milione di token, separato tra input e output (l'output costa di più, perché il decode è lento) e con uno sconto per l'input in cache; GPT-4 a marzo 2023: 30 e 60 dollari per milione di token (versione da 8K), oggi i modelli piccoli costano frazioni di dollaro [DA VERIFICARE]. Energia per richiesta: Google (agosto 2025) dichiarò 0,24 Wh per un prompt testuale mediano di Gemini, Sam Altman (giugno 2025) 0,34 Wh per ChatGPT [DA VERIFICARE]. L'Agenzia internazionale dell'energia (aprile 2025) stimò per i data center circa 415 TWh nel 2024, circa l'1,5% dell'elettricità mondiale, e circa 945 TWh nel 2030 [DA VERIFICARE].
- **Numeri (conto per un modello locale):** 300 W ÷ 30 token/s = 10 J per token, cioè 0,0028 Wh; mille token sono circa 2,8 Wh, che a 0,25 euro al kWh costano circa 0,07 centesimi di euro. Tutta la risposta costa meno dell'elettricità per tenere accesa una lampadina per qualche minuto. Il costo vero del locale è l'hardware, non la corrente.
- **Regola d'uso:** contesto lungo e agenti moltiplicano i token: usa il prompt caching, taglia i documenti, scegli il modello più piccolo che basta.

---

## 4. Storia, futuro, uso (C27-C30)

### C27 — Multimodalità (approfondimento, breve)

Immagini, audio e video diventano anch'essi token: un'immagine viene tagliata in tasselli (*patch*, Vision Transformer, 2020), ciascuno trasformato in un vettore come una parola; i modelli di generazione di immagini a diffusione funzionano in un altro modo e vanno solo accennati. Il costo in token di un'immagine varia da modello a modello [DA VERIFICARE]. Esistono modelli visione-testo anche in locale.

### C28 — Un secolo di idee in attesa dell'hardware

- **Idea:** quasi tutta la matematica esisteva da decenni. Il boom arriva quando si incontrano tre ingredienti: i dati (Internet), il calcolo (le GPU) e alcune idee nuove, il Transformer su tutte.
- **Tappe datate:** Markov (1906, 1913); McCulloch e Pitts (1943); Shannon (1948, 1951); Turing e il gioco dell'imitazione (1950); Dartmouth (1956), che contava di fare progressi decisivi in un'estate; il Perceptron di Rosenblatt (1958); ELIZA di Weizenbaum (1966); i due inverni dell'IA; la backpropagation (1986); LSTM (1997); Deep Blue contro Kasparov (1997); Bengio e il modello neurale del linguaggio (2003); CUDA (2006-2007); ImageNet (2009); Watson a Jeopardy! (2011); AlexNet (2012); word2vec (2013); seq2seq e attenzione (2014); AlphaGo (2016); il Transformer (2017); GPT e BERT (2018); GPT-2 (2019); GPT-3 e le leggi di scala (2020); Codex e Copilot (2021); Chinchilla, InstructGPT e ChatGPT (30 novembre 2022); LLaMA (febbraio 2023), GPT-4 (14 marzo 2023), llama.cpp (marzo 2023), Mistral 7B (settembre 2023), Mixtral (dicembre 2023); i Nobel 2024 per la fisica (Hopfield e Hinton) e per la chimica (Hassabis, Jumper, Baker); o1 (settembre 2024), DeepSeek-V3 (dicembre 2024); DeepSeek-R1 (gennaio 2025), gpt-oss (agosto 2025), l'esplosione degli agenti per il codice nel 2025. Il 2026 va cercato.
- **Lezioni di storia da citare, con la fonte:** *The Bitter Lesson* (Sutton, marzo 2019); il cosiddetto teorema di Tesler («l'intelligenza artificiale è tutto ciò che non è ancora stato fatto», attribuzione discussa: ottimo esempio di fatto o leggenda).
- **Occhio a:** Markov 1906-1913, non 1922; ChatGPT non nasce nel 2022 ma ha radici almeno nel 2017.

### C29 — Futuro: domande aperte, non previsioni

Temi da presentare come domande, mai come date: modelli piccoli sempre più capaci e sempre più locali; agenti che reggono compiti sempre più lunghi (C15); memoria persistente e apprendimento continuo; hardware con la memoria accanto al calcolo (C25); energia; regole (il regolamento europeo sull'IA è in vigore dal 1° agosto 2024, gli obblighi per i modelli di uso generale dal 2 agosto 2025; la legge italiana sull'IA, n. 132 del 2025 [DA VERIFICARE]); scienza assistita da IA; limiti ancora aperti come le allucinazioni (C12). Aforisma di servizio: «l'intelligenza artificiale arriva sempre fra vent'anni. Da settant'anni».

### C30 — Usare meglio l'IA sapendo come funziona

È il frutto del libro: ogni capitolo chiude con una **Regola d'uso**. Tabella di sintesi da riprendere nell'epilogo di ogni libro, con le parole del libro:

| Cosa succede sotto il cofano | Cosa fai di diverso |
|---|---|
| Il modello vede token, non lettere (C02) | Per contare, anagrammare o fare conti lunghi usa uno strumento |
| L'italiano costa più token (C02) | Taglia il superfluo; non incollare più del necessario |
| L'attenzione si diluisce (C04) | Una cosa per volta, istruzioni cruciali all'inizio e alla fine |
| Il modello non impara dalla tua chat (C07, C13) | Ciò che va ricordato, scrivilo in un file |
| Premia ciò che ti piace (C08) | Chiedi di criticare, non solo di approvare |
| Per problemi logici serve ragionare (C08) | Scegli un modello che ragiona; per testi semplici no |
| La temperatura decide la creatività (C10) | Bassa per fatti e codice, alta per brainstorming |
| La finestra di contesto è finita (C11) | Una chat per argomento; riparti da un riassunto |
| Allucinazioni (C12) | Chiedi citazioni, verifica, offri l'uscita «non lo so» |
| Il RAG porta i documenti (C14) | Dagli le fonti e chiedi i passi citati |
| Gli agenti agiscono (C15) | Permessi minimi, conferma per ciò che non si annulla |
| Il testo dei dati può comandare (C16) | Dato non fidato, nessun potere |
| I benchmark non sono il tuo lavoro (C17) | Un mini-benchmark di 20 tue domande |
| Memoria = pesi × bit (C19) | Fai il conto prima di scaricare |
| Quantizzazione (C20) | Q4_K_M per cominciare; più bit se il compito è delicato |
| MoE (C23) | Conta la memoria totale, non i parametri attivi |
| Costo per token (C26) | Prompt caching, contesti corti, modello più piccolo che basta |

---

## 5. Assegnazione delle storie vere (niente duplicati tra i libri)

Le storie «cardine» possono comparire in più libri, ma con angolazione diversa e al massimo in un paragrafo negli altri. Tutte le altre stanno in un libro solo.

| Libro | Storie assegnate (da verificare prima di usarle) |
|---|---|
| **1 Storia** | Markov e l'Onegin; Shannon (monociclo, Theseus, il gioco del libro); Chomsky e le «idee verdi senza colore»; Jelinek e IBM; Stupid Backoff (Brants e altri, 2007); Bengio 2003; Karpathy 2015 (l'indirizzo web allucinato); il trucco di leggere la frase al contrario (Sutskever e altri, 2014); otto autori in ordine casuale; GPT-2 «troppo pericoloso» (febbraio 2019); InstructGPT; ChatGPT, il lancio; il leak di LLaMA e Gerganov; Mixtral e il link torrent (dicembre 2023); DeepSeek-R1 e la Borsa; Perceptron e il New York Times (1958); Dartmouth; The Bitter Lesson; Dijkstra e il sottomarino; Golden Gate Claude (maggio 2024); GPT-4o adulatore (aprile 2025); Alpaca e QLoRA (2023); SolidGoldMagikarp e il nome in codice «Strawberry»; Mata contro Avianca (giugno 2023) |
| **2 Manuale di montaggio** (*Il pezzo che avanza*) | Replit e il database cancellato (luglio 2025); la Chevrolet da un dollaro (dicembre 2023); DPD (gennaio 2024); Llama 4 e LMArena (aprile 2025); la dimostrazione di DeepSeek-V3 su Mac Studio da 512 GB (marzo 2025); le «etichette d'origine» dei pezzi: anno e inventore di ogni concetto, in una riga, senza raccontare le storie assegnate agli altri libri |
| **3 Cornice e novelle** (*Qui non c'è campo*) | Bing «Sydney» (febbraio 2023, le chat lunghe); Tay (2016, «dimmi con chi vai»); Google AI Overviews e la colla sulla pizza (maggio 2024); Samsung (2023, la fuga di codice); proverbi e modi di dire con le loro forme verificate (Firth 1957 sull'ipotesi distribuzionale; Lorenzo de' Medici); aneddoti inventati dichiarati tali per le novelle |
| **4 Pranzo** | Deep Blue, Watson, AlphaGo come «le cose viste al telegiornale»; il Rischiatutto e Mike Bongiorno; il Garante e ChatGPT (marzo 2023, solo in questo libro); personaggi e scene di famiglia dichiarati inventati |
| **5 Dizionario** (*Falsi amici*) | ELIZA (1966, nell'«Anagrafe» di Capire e Intelligenza); Clever Hans (Berlino, circa 1904; Pfungst 1907); Air Canada (febbraio 2024, per la voce Agente); etimologie e storie delle parole [DA VERIFICARE ciascuna: pronto e prompt, temperatura e Boltzmann, confabulazione, «cervello elettronico» nella stampa italiana, intelligence e intelligenza]; lettere della Posta dei falsi amici, inventate e dichiarate tali |

**Cardine condivise:** Transformer 2017; ChatGPT 30 novembre 2022; AlexNet su due GTX 580 (2012); DeepSeek-R1 (gennaio 2025).

---

## 6. Banco delle prove («Prova tu»)

Tutte le prove sono riproducibili e dichiarano modello, quantizzazione, hardware e impostazioni. Le prime sono per chi non vuole installare niente.

| Prova | Cosa insegna | Cosa serve |
|---|---|---|
| P01 Il gioco dei proverbi: far completare a 5 persone «Chi dorme non piglia...» e confrontare | previsione e probabilità (C01) | niente |
| P02 Tokenizer online: la stessa frase in italiano e in inglese, contare i token | token e costo (C02) | un browser |
| P03 Stessa domanda due volte, in due chat | campionamento (C10) | un chatbot |
| P04 Chat lunga contro chat nuova con riassunto | contesto (C11) | un chatbot |
| P05 «Quante R in strawberry?», poi con uno strumento | token e strumenti (C02, C15) | un chatbot |
| P06 Domanda su un libro inesistente | allucinazioni (C12) | un chatbot |
| P07 Shannon a mano: generare finto testo con dado e libro, o con 10 righe di Python | modello del linguaggio (C01) | libro e dado |
| P08 Ollama o LM Studio: scaricare un modello piccolo, leggere i token/s | locale e velocità (C18, C19) | un PC con 16 GB di RAM |
| P09 Stesso modello a Q8 e a Q4: stessi 10 prompt, confrontare memoria, velocità, qualità | quantizzazione (C20) | idem |
| P10 Stesso modello con offload al 100% e al 50%: misurare i token/s | offloading (C22) | un PC con GPU |
| P11 `llama-bench` o la misura integrata nell'app | prefill e decode (C19) | idem |
| P12 Mini-benchmark di 20 domande dal proprio lavoro su due modelli | benchmark (C17) | due modelli |
| P13 RAG sui propri documenti con uno strumento già pronto | RAG (C14) | documenti propri |
| P14 Agente in una cartella-sandbox: provare un testo «trappola» dentro un file | agenti e sicurezza (C15, C16) | un agente e una cartella di prova |

---

## 7. Fatti già corretti: non reintrodurre gli errori

- Catene di Markov: 1906 (teoria) e 1913 (Onegin), non 1922.
- L'attenzione non nasce nel 2017: nasce nel 2014 come aggiunta alle reti ricorrenti. Il Transformer elimina la ricorrenza.
- Il paper del Transformer non è «solo traduzione» e «non sapevano»: evita entrambe le semplificazioni.
- I layer aggiungono, non setacciano. «Setacci sovrapposti» è un'immagine da abbandonare.
- Temperatura 1 non è delirante; la temperatura bassa non cura le allucinazioni.
- «Offload» ha due sensi opposti nei vari programmi; in generazione il collo di bottiglia non è il PCIe.
- Il MoE non riduce la memoria; gli esperti non sono «per argomento»; «2 su 8» è solo Mixtral.
- La cifra di DeepSeek-V3 esclude le ricerche precedenti.
- «Senza la lettera E» e «le R di strawberry» sono limiti di token, non sintomi di quantizzazione.
- Nessuno split di parole in token senza averlo verificato su un tokenizer reale.
- Percentuali di qualità solo se misurate.
- GPU: «lo stesso tipo di calcolo», non «la stessa matematica» dei videogiochi.

## 8. Fonti di base da citare

Shannon 1948 e 1951; Bengio e altri 2003; Mikolov e altri 2013; Bahdanau e altri 2014; Vaswani e altri 2017; Kaplan e altri 2020; Hoffmann e altri 2022; Ouyang e altri 2022; Lewis e altri 2020; Hu e altri 2021; Dettmers e altri 2022 e 2023; Holtzman e altri 2019; Liu e altri 2023; Shazeer e altri 2017; Jiang e altri 2024 (Mixtral); DeepSeek-V3 e R1; Yao e altri 2022; Anthropic, «Building effective agents» (dicembre 2024); documentazione di llama.cpp, Ollama e LM Studio; schede tecniche dei produttori di hardware.
