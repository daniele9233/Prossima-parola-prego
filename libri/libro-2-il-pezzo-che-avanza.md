# Libro 2 — *Il pezzo che avanza*

### Istruzioni di montaggio, con note a margine, per costruire (e capire) un'intelligenza artificiale

> Il libro **da montare con le mani**: un foglio istruzioni per una libreria a 30 scomparti, uno per concetto. Fatti e numeri in `mappa-contenuti.md`; regole comuni in `CLAUDE.md`. Scheda nuova, da approvare.

## 1. Identità

- **Spina dorsale:** il libro è il foglio istruzioni di un mobile, la libreria PAROLA. Ogni capitolo è un **Foglio** con *Cosa serve*, i *Passi* numerati, le *Note a margine* di chi monta e *Il pezzo che avanza*: l'unica cosa che il foglio non ha risolto, detta con onestà.
- **Ordine hardware-first:** si parte dal pacco da 16 GB che non passa dalla porta (memoria, quantizzazione, velocità, locale), poi si apre la scatola e si arriva ai meccanismi (token, embedding, attenzione, layer, addestramento), poi al comportamento (ragionamento, campionamento, contesto, allucinazioni, memorie), all'uso (agenti, sicurezza, benchmark) e infine al panorama (hardware nuovo, costi, storia). È l'ordine in cui si incontra davvero un'IA in casa.
- **Cosa lo distingue:** unico libro con due voci in conflitto; unico che parte dal «sotto il cofano»; l'oggetto è fisico e si misura. Nessuna cronologia, nessuna famiglia, nessuna cucina.
- **Dove è più profondo:** C06, C18-C26 (locale, memoria e velocità, quantizzazione, GPU, offload, MoE, hardware, costi), C11.
- **Lettore ideale:** chi ha montato un mobile e ha imprecato; il tecnico che vuole il conto.

## 2. Voce

- **Il Manuale:** imperativo, impassibile, numerato, con AVVERTENZE maiuscole («NON FORZARE», «SERVONO DUE PERSONE»), figure descritte a parole («Figura: persona soddisfatta»), tempo stimato sempre ottimistico.
- **Il Montatore:** l'io narrante (inventato, dichiarato, genere non marcato) che scrive le note a margine sudando: onesto, autoironico, cita i numeri veri contro le promesse del Manuale. La comicità sta nella distanza: il Manuale dice «90 minuti», la nota fa il conto e dice 253 anni.
- Mai sarcasmo verso chi legge; mai marchi reali di mobili; lunghi tratti di prosa normale tra le parodie, per non tediare.

**Campione di voce (non è testo del libro)**

> PASSO 7. Avvitare le viti (B) nei fori dei ripiani (C). Servono: 8.000.000.000 di viti (B). Tempo stimato: 90 minuti.
>
> *Nota a margine.* Ho fatto il conto. Una vite al secondo sono 253 anni. Il Manuale ha un rapporto creativo con i numeri.
>
> ATTENZIONE. Non serrare a fondo. Ogni vite va girata di pochissimo, poi si guarda se la libreria sta in piedi meglio o peggio di prima.

## 3. Analogie madri e dove scricchiolano

| Concetto | Analogia madre | Dove scricchiola |
|---|---|---|
| Previsione (C01) | Il foglio che si scrive da solo un passo alla volta guardando il mobile montato finora | Nel Manuale il passo dopo è scritto; nel modello è una probabilità e non c'è un disegno finale |
| Token (C02) | Piastrelle intere e tagli ai bordi, con il prezzo a metro quadro | Il piastrellista sceglie la misura; il tokenizer la ricava da quanto spesso compaiono i pezzi |
| Embedding (C03) | Il tintometro: ogni colore è una ricetta di dosi, il bianco panna è vicino al bianco latte | I coloranti hanno un nome; le dimensioni dell'embedding no |
| Attention (C04) | Le frecce tratteggiate: più spesse verso i pezzi con cui un pezzo va davvero | Le frecce le disegna una volta un umano; il modello le ricalcola per ogni parola e per ogni testa |
| Layer (C05) | Ripiani che si aggiungono senza togliere nulla: 32, 80, 126 | I ripiani sono fisici; i layer sono calcoli sullo stesso fascicolo di numeri |
| Parametri (C06) | 8 miliardi di viti da girare di pochissimo: una al secondo sono 253 anni | Nessuna vite regge un ripiano da sola, e girarne una sposta tutto |
| Training (C07) | Girare tutte le viti un po', nella direzione che fa sbagliare meno, e ricominciare | In un mobile si vede l'errore; il modello ha solo un numero di errore |
| RLHF (C08) | Lo showroom: due versioni esposte, i clienti votano | I clienti votano ciò che piace, non ciò che regge |
| Fine-tuning e LoRA (C09) | Il restyling: si cambiano le ante senza rifare il mobile | Cambiare le ante può storcere le cerniere (dimenticanza catastrofica) |
| Campionamento (C10) | Pescare a occhi chiusi dalla cassetta delle viti: più si allarga la mano, più pezzi strani | Le viti nella cassetta sono vere; le probabilità sono apprese |
| Contesto (C11) | I metri quadri della stanza: ciò che non c'è dentro non entra; l'inquilino che ogni mattina rifà l'inventario | Una stanza si può allargare; la finestra è fissa. L'inventario si rifà in parallelo (prefill) |
| Allucinazione (C12) | Il Pezzo Z che il passo 14 cita e che nella busta non c'è | Chi monta se ne accorge; il modello inventa il pezzo e lo avvita |
| Memorie (C13-C14) | Cinque ripostigli (pesi, stanza, inventario, taccuino di casa, biblioteca dei manuali) | Un ripostiglio contiene oggetti; i pesi non contengono fatti separati |
| Velocità (C19) | Cento operai e un solo montacarichi: conta la portata, non gli operai | Lo scatolone consegnato resta al piano; i pesi vanno riletti a ogni token |
| Quantizzazione (C20) | Pannelli del negozio in sole misure standard: la tua misura è arrotondata | A 3 ripiani non si nota; a 80 gli errori si sommano. E le scale per blocco la rendono più furba di un arrotondamento |
| GPU (C21) | La foratrice multi-mandrino: cento fori uguali insieme | Brava a forare, pessima a decidere dove |
| Offload (C22) | Il montacarichi che porta solo il 60% dei colli: il resto va a piedi per le scale | Il tempo si somma: il risultato è molto più vicino alle scale che al montacarichi |
| MoE (C23) | Il magazzino da 256 corsie: affitto per tutte, giro in poche | Le corsie non sono per reparto: il router sceglie per ogni token e per ogni layer |
| Agenti (C15) | Il workflow è il foglio istruzioni; l'agente è montare a occhio. SERVONO DUE PERSONE | L'agente decide, il foglio no |
| Sicurezza (C16) | Il volantino infilato nel pacco che dice «buttate le istruzioni» | Un volantino si distingue dal foglio; per il modello è tutto testo |
| Benchmark (C17) | Il bollino di qualità e i collaudi del produttore | Il produttore collauda i pezzi che già sa reggere |
| Hardware e costi (C25-C26) | La fabbrica di mobili con il contatore della luce | Il contatore misura la corrente, non la qualità |

## 4. Fili conduttori e box

- **La libreria PAROLA** avanza foglio dopo foglio e alla fine sta in piedi, pende un po' a sinistra («come ogni LLM: funziona, e conviene controllarla con una livella»).
- **Tempo stimato contro tempo reale:** gag fissa.
- **SERVONO DUE PERSONE:** icona della verifica umana; la seconda persona è chi controlla.
- **L'Inventario:** scheda di casa con RAM, VRAM e banda del proprio computer, aggiornata a ogni foglio.

| Box | Contenuto |
|---|---|
| **Cosa serve** | attrezzi, tempo stimato, persone |
| **Passi** | la voce del Manuale |
| **Nota a margine** | la voce del Montatore |
| **Sotto il cofano** | numeri e conti per il tecnico |
| **Dove l'analogia scricchiola** | i limiti della metafora appena usata |
| **Il pezzo che avanza** | un limite aperto del capitolo, che resta tale (non anticipa il capitolo dopo) |
| **Regola d'uso** | cosa cambia quando usi un'IA |
| **Foglio senza parole / Errata corrige / Garanzia** | formati speciali per variare |

## 5. Capitoli (21 fogli)

Ogni scheda: concetti, idea, esempi da usare (conti dalla mappa), storia vera, prova, occhio a.

### Foglio 1 — Il pacco non passa dalla porta
- **Concetti:** C06, C18, C19. **Idea:** apertura tattile: un modello da 8 miliardi di parametri pesa 16 GB e non passa dalla porta di un computer da 8. Il conto da tovagliolo che decide cosa puoi portare in casa.
- **Esempi:** 8 miliardi × 2 byte = 16 GB; il pacco da 70 miliardi: 140 GB; la porta (la tua memoria) e la tua scheda di casa (Inventario); locale contro cloud (chi consegna a domicilio, chi ti fa montare da solo); pesi aperti contro open source; quante persone servono per portare il pacco; il «tempo stimato 90 minuti» per scaricarlo.
- **Prova:** P08. **Occhio a:** GB e GiB; la memoria che conta è quella veloce.

### Foglio 2 — Misure standard
- **Concetti:** C20. **Idea:** il negozio vende pannelli solo da 60, 80 e 90: la quantizzazione. Più errori a ogni ripiano, ma meno peso.
- **Esempi:** 16 → 4 bit = da 16 GB a circa 5 GB per 8 miliardi (Q4_K_M, 4,8-4,9 bit effettivi); 16 livelli contro 65.536; il pannello su misura per blocco di 32; 8 bit (nessuno se ne accorge), 4 (regge), 3 (si ripete), 2 (inventa); il montatore che ordina 84 cm e ne riceve 80; la tabella dei file.
- **Storia:** la dimostrazione di DeepSeek-V3 su Mac Studio da 512 GB (marzo 2025) [DA VERIFICARE]. **Prova:** P09. **Occhio a:** niente percentuali inventate.

### Foglio 3 — Il montacarichi e la foratrice
- **Concetti:** C19, C21. **Idea:** la velocità è la portata del montacarichi (banda), non il numero di operai (calcolo); la GPU è la foratrice a cento mandrini.
- **Esempi:** 96 ÷ 4,9 ≈ 20 token/s su RAM; 1.008 ÷ 4,9 ≈ 205 su una RTX 4090; lettura umana 5-8 token/s; cento operai e un solo montacarichi; prefill (scarico tutto insieme) e decode (un collo alla volta); perché il cloud serve tanti insieme; la foratrice e CUDA.
- **Prova:** P08, P11. **Occhio a:** teorico contro misurato.

### Foglio 4 — Le scale a piedi
- **Concetti:** C22, C23. **Idea:** se il montacarichi porta solo una parte dei colli, il resto va a piedi: offload; e il magazzino da 256 corsie con pochi giri: MoE.
- **Esempi:** il conto 12 GB su 8 GB: 17,5 ms + 62,5 ms = 80 ms, circa 12 token/s (7 solo CPU, 33 tutto in VRAM); `-ngl`; Apple e mini PC con memoria unificata; gpt-oss-120b: 5,1 miliardi attivi, 2,7 GB letti per token; DeepSeek-V3 671 miliardi totali e 37 attivi; l'affitto di tutte le corsie.
- **Prova:** P10. **Occhio a:** il MoE non riduce la memoria; «offload» ha due sensi.

### Foglio 5 — Cosa deve fare, questo mobile
- **Concetti:** C01. **Idea:** la libreria che si completa da sola, un pezzo alla volta: la previsione del prossimo token.
- **Esempi:** il foglio che prevede il passo dopo; il dado; le quote del dado; «pane e…»; la perplexity come numero di strade; ciclo: ogni pezzo scelto rientra; chat e strumenti sono software intorno.
- **Prova:** P01, P07. **Occhio a:** le probabilità dei dialoghi sono illustrative.

### Foglio 6 — Piastrellare la frase
- **Concetti:** C02, C27. **Idea:** token = piastrelle intere e tagli ai bordi. Foglio senza parole, solo disegni a tasselli (le immagini).
- **Esempi:** «lasagna» in tre pezzi (da verificare con un tokenizer reale); italiano più caro dell'inglese; le R di «strawberry»; un numero spezzato; il prezzo a metro quadro (a token); SolidGoldMagikarp lasciato al Libro 1.
- **Prova:** P02, P05. **Occhio a:** niente split senza tokenizer reale.

### Foglio 7 — Il tintometro
- **Concetti:** C03. **Idea:** ogni colore è una ricetta di dosi; colori simili hanno ricette vicine.
- **Esempi:** bianco panna e bianco latte; rosso mattone lontano dal verde; dimensioni: 4.096 per Llama 3 8B; la ricerca per significato (e il codice che non trova); il pregiudizio come pigmento sbagliato; re − uomo + donna.
- **Occhio a:** le dimensioni non hanno nome.

### Foglio 8 — Le frecce tratteggiate
- **Concetti:** C04. **Idea:** ogni pezzo guarda i pezzi con cui va; il Transformer.
- **Esempi:** «Mario ha dato il libro a Luca perché lui doveva studiare»; Query, Key, Value come cercare un pezzo nella cassetta; più teste, più frecce; il 2017 e il 2014; perché l'ordine conta.
- **Regola d'uso:** istruzioni cruciali all'inizio e alla fine.

### Foglio 9 — Ripiani
- **Concetti:** C05. **Idea:** il mobile cresce di piano senza togliere nulla.
- **Esempi:** 32, 80, 126 ripiani; il fascicolo che sale; ogni ripiano è lo stesso modulo; si dividono tra GPU e CPU; i blocchi (attenzione + rete).
- **Occhio a:** i layer aggiungono, non setacciano.

### Foglio 10 — Girare di pochissimo
- **Concetti:** C07. **Idea:** pre-training: si girano tutte le viti un po'.
- **Esempi:** 8 miliardi di viti, una al secondo = 253 anni; 15 mila miliardi di token; Chinchilla; Llama 3 8B con 1.900 token per parametro; costi (DeepSeek-V3 con la riserva); il cutoff.
- **Storia:** AlexNet su due GTX 580 (cardine). **Occhio a:** il costo esclude le ricerche precedenti.

### Foglio 11 — Lo showroom
- **Concetti:** C08. **Idea:** RLHF e adulazione; lo schizzo prima di forare è il ragionamento.
- **Esempi:** due versioni esposte; il cliente vota il più bello; il modello base che continua con altre domande; InstructGPT 1,3 miliardi contro 175; chiedere di criticare; o1 e R1; il costo dei passi in più.
- **Occhio a:** il ragionamento mostrato non sempre è fedele.

### Foglio 12 — Cambiare le ante
- **Concetti:** C09. **Idea:** fine-tuning, LoRA e distillazione.
- **Esempi:** il restyling; l'adattatore in sola lettura (overlay dei container); QLoRA su una scheda da 48 GB; la dimenticanza catastrofica; il modello piccolo specializzato; prima il prompt, poi il RAG.
- **Occhio a:** non insegna fatti che cambiano.

### Foglio 13 — La cassetta delle viti
- **Concetti:** C10. **Idea:** temperatura e top-p.
- **Esempi:** pescare dalla cassetta; temperatura 0, 1 e sopra 1; top-p; lo stesso foglio non dà la stessa libreria; loop di ripetizione; anche a 0 si può variare.
- **Prova:** P03. **Occhio a:** temperatura 1 non è delirio.

### Foglio 14 — Inventario della stanza
- **Concetti:** C11, C24. **Idea:** contesto e KV cache; trucchi per correre di più.
- **Esempi:** 128 KiB per token (32 × 8 × 128 × 2 × 2 byte); 1 GiB a 8.192 token e 16 GiB a 131.072; l'inquilino che ogni mattina rifà l'inventario; *Lost in the Middle*; GQA e MLA; decodifica speculativa; prompt caching.
- **Prova:** P04. **Occhio a:** 128K token non sono 128K parole.

### Foglio 15 — Il pezzo Z
- **Concetti:** C12. **Idea:** il passo 14 chiede un pezzo che nella busta non c'è.
- **Esempi:** il modello che inventa il pezzo e lo avvita; il libro che non esiste; test a crocette senza penalità; tre famiglie di errori; chiedere citazioni; l'uscita «non lo so».
- **Prova:** P06. **Occhio a:** non basta abbassare la temperatura.

### Foglio 16 — Cinque ripostigli
- **Concetti:** C13, C14. **Idea:** le cinque memorie e il RAG.
- **Esempi:** pesi, stanza, inventario, taccuino di casa, biblioteca; il RAG come manuale in biblioteca; chunk e vettori; il manuale sbagliato; ricerca ibrida.
- **Prova:** P13.

### Foglio 17 — Servono due persone
- **Concetti:** C15, C16. **Idea:** workflow come foglio istruzioni, agente come montaggio a occhio; il volantino nel pacco.
- **Esempi:** 20 passi × 500 token a 10 token/s ≈ 17 minuti; MCP come presa standard; permessi minimi; la trifecta letale in versione volantino; la seconda persona.
- **Storia:** Replit e il database cancellato (luglio 2025) [DA VERIFICARE]; la Chevrolet da un dollaro (dicembre 2023); DPD (gennaio 2024).
- **Prova:** P14.

### Foglio 18 — Bollino di qualità
- **Concetti:** C17. **Idea:** collaudi, bollini e come si imbroglia.
- **Esempi:** MMLU, HumanEval, SWE-bench; contaminazione; Goodhart; il mini-benchmark di 20 domande; arene a voto cieco; due bollini che non concordano.
- **Storia:** Llama 4 e LMArena (aprile 2025) [DA VERIFICARE]. **Prova:** P12.

### Foglio 19 — La fabbrica di mobili e il contatore
- **Concetti:** C25, C26. **Idea:** HBM, GPU, TPU, NPU, costi ed energia.
- **Esempi:** tabella datata di capacità e banda (mappa); il muro della memoria; 300 W ÷ 30 token/s = 10 J per token; mille token = 2,8 Wh ≈ 0,07 centesimi; prezzi per milione di token; DGX Spark e Strix Halo.
- **Occhio a:** tutto datato e con fonte.

### Foglio 20 — Un secolo di istruzioni
- **Concetti:** C28, C29. **Idea:** le «etichette d'origine» dei pezzi (anno e inventore) e le domande aperte.
- **Esempi:** Markov 1913, Shannon 1948, Bengio 2003, word2vec 2013, il Transformer 2017, GPT-3 2020, ChatGPT 2022; il pezzo che manca ancora; nessuna data di futuro.

### Foglio 21 — Collaudo finale
- **Concetti:** C30. **Idea:** la libreria sta in piedi; livella alla mano. Tabella «cosa succede sotto il cofano / cosa fai di diverso» e **Test dell'esperto** (30 domande).
- **Esempi:** la lista di controllo in cinque domande per ogni risposta dubbia; il tempo stimato contro il tempo reale; quanto pende a sinistra.

## 6. Copertura della mappa

C01 f.5 · C02 f.6 · C03 f.7 · C04 f.8 · C05 f.9 · C06 f.1 · C07 f.10 · C08 f.11 · C09 f.12 · C10 f.13 · C11 f.14 · C12 f.15 · C13-C14 f.16 · C15-C16 f.17 · C17 f.18 · C18 f.1 · C19 f.1, 3 · C20 f.2 · C21 f.3 · C22-C23 f.4 · C24 f.14 · C25-C26 f.19 · C27 f.6 · C28-C29 f.20 · C30 f.21.
