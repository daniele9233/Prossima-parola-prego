# Libro 3 — *Ritmo gara*

### Come si allena, si specializza e si fa correre un'intelligenza artificiale

> Il libro **della corsa**. L'IA resta il tema; l'allenamento è lo strumento per capirla: volume e intensità, specificità, taper, ritmo gara, efficienza. Fatti e numeri stanno in `mappa-contenuti.md`; le regole comuni in `CLAUDE.md`.

## 1. Identità del libro

- **Spina dorsale:** una **tabella di allenamento** verso una gara. Cinque blocchi (base, volume, specificità, giorno gara, affinare) per una «maratona» che è la capacità di usare, far girare e valutare un LLM. Ogni capitolo è un allenamento, con il suo tipo di seduta: lungo, ripetute, fartlek, test, scarico.
- **Cosa lo distingue:** il tema è l'**efficienza** e la **specializzazione**: cosa significa allenare un modello, come si specializza, quanto costa farlo correre. Spiega il «sotto il cofano» dell'inferenza come nessun altro dei cinque: token al secondo, quantizzazione, banda di memoria, hardware, modelli locali.
- **Dove è più profondo:** addestramento e specializzazione (C07-C09), inferenza e velocità (C19), quantizzazione (C20), modelli locali e scelta della macchina (C18, C22), MoE e decodifica speculativa (C23, C24), il «muro» della memoria (C25).
- **Regola del vincolo:** l'IA resta il tema principale. Niente consigli di allenamento che prendano il posto della spiegazione: la corsa serve a capire l'IA, non l'IA a correre meglio. Ogni analogia dichiara dove scricchiola.
- **Lettore ideale:** chi corre (o ha un amico che non smette di parlarne) e si sente escluso dall'IA; il tecnico che vuole numeri e trade-off.

## 2. Voce

- **Il compagno di corsa.** Parla al «tu» a ritmo conversazionale (quello a cui riesci a chiacchierare senza fiatone). Pratico, ironico, un po' sfottente verso la cultura del runner (l'orologio che ti dice che hai bisogno di 72 ore di recupero, le scarpe col carbonio, il «solo 10 chilometri» alle sei di domenica) e verso l'hype dell'IA nello stesso modo.
- **Frasi di media lunghezza, ritmate come un passo:** brevi, brevi, una più lunga, poi di nuovo brevi.
- **Numeri di corsa come lessico:** passo a chilometro, battiti, zone, chilometri per settimana. Ogni numero ha un omologo del mondo IA e viceversa.
- **Motivazione ironica:** mai predicozzi. «Il lungo della domenica non ti rende migliore. Ti rende stanco, con un racconto.»
- **Non attribuire all'autore** tempi, gare o allenamenti reali senza conferma; il runner di esempio è un personaggio inventato (dichiaralo), a meno che l'autore non fornisca i propri dati.

### Campione di voce (non è testo del libro)

> Un modello linguistico non ha mai corso un chilometro, ma funziona come un maratoneta in un punto: fa un passo alla volta, e non può tornare indietro.
>
> Ogni passo è una parola. E come sul percorso vero, il passo successivo dipende da quelli che hai già fatto: se parti troppo forte, la frase te la ricordi solo con il fiatone.
>
> Il modello non pianifica la gara. Prevede il metro dopo.
>
> È un tipo di sportivo molto strano, ma a ben guardare ne conosciamo parecchi.

## 3. Analogie madri e dove scricchiolano

| Concetto | Analogia madre | Dove scricchiola |
|---|---|---|
| Autoregressione (C01) | Un passo dopo l'altro, senza tornare indietro | Il corridore vede il percorso; il modello solo il passo successivo |
| Token (C02) | I parziali (lap): la gara spezzata in segmenti scelti dal cronometrista | I parziali hanno lunghezza fissa; i token no |
| Embedding (C03) | Allenamenti «parenti»: ripetute vicino a fartlek, lontane dal riposo | Le parentele nascono dai dati, non dalla fisiologia |
| Attention (C04) | La scia (drafting): ogni corridore si copre dietro quelli che contano | Nella scia si risparmia fiato; nell'attenzione si pesa |
| Layer (C05) | Il cronometro: ogni chilometro aggiunge qualche secondo al tempo totale, mai cancellando | Il cronometro cresce in una sola dimensione |
| Parametri (C06) | La taglia dell'atleta (da 5K ad ultra): più parametri, più capacità e più consumi | I parametri non sono muscoli: da soli non dicono niente |
| Pre-training (C07) | Il volume: chilometri nelle gambe, la base aerobica | Il volume del modello sono dati, non fatica |
| Learning rate (C07) | Intensità e recupero; riscaldamento e taper | Il corpo si adatta con il tempo; il gradiente no |
| Scaling (C07) | Più chilometri o più atleti? Il volume giusto per la taglia | Le leggi di scala sono osservazioni, non fisiologia |
| GPU (C21) | Il cuore e il VO₂max: conta quanto ossigeno arriva ai muscoli, non quanto sono forti le gambe | La banda è un flusso, il VO₂max un massimo |
| Fine-tuning (C09) | Dal fondo generico alla preparazione per una 10 km | Un atleta torna in forma, un modello può dimenticare (dimenticanza catastrofica) |
| RLHF (C08) | L'allenatore che dà pollice su e giù | L'allenatore ha preferenze e fretta |
| LoRA (C09) | Il plantare o il piano di richiamo: poche modifiche mirate senza rifare tutta la preparazione | Il plantare non cambia la struttura del piede |
| Distillazione (C09) | Il maestro che passa il «colpo d'occhio» al giovane | Il giovane non ha la stessa storia |
| Overfitting (C17) | Il personal best sul giro di casa e il disastro su un percorso nuovo | Il runner sa di non conoscere il percorso |
| Benchmark (C17) | Le gare e i tempi su percorso certificato; Rosie Ruiz come barare | Una gara si corre una volta; un benchmark si ripete |
| Ragionamento (C08) | Il conto ai rifornimenti: «sono a 4:50? devo rallentare?» | Il runner pensa mentre corre, il modello scrive e poi risponde |
| Inferenza (C19) | Il giorno gara: nessun apprendimento, si corre quel che si ha | Il modello non si stanca, ma si degrada con il contesto |
| Token al secondo (C19) | Il passo, cioè la velocità. Il tempo al primo token è la reazione allo sparo | Il passo si misura in minuti al chilometro, la velocità in token al secondo (sono inversi) |
| Quantizzazione (C20) | Lo zaino da ultratrail: togli il superfluo, non l'attrezzatura obbligatoria | Il peso dello zaino si somma; l'errore nel modello si propaga |
| Contesto (C11) | La memoria dell'orologio GPS: quando è piena, cancella i giri più vecchi | L'orologio può esportare; il contesto no |
| Temperatura (C10) | Metronomo contro fartlek («gioco di velocità») | Nel fartlek sai perché cambi; nel modello no |
| MoE (C23) | L'ekiden: la maratona divisa in tappe, ognuna a uno specialista | I frazionisti sono noti; gli esperti non sono per argomento |
| Decodifica speculativa (C24) | La lepre: va avanti a ritmo e il campione verifica | La lepre non può cambiare il risultato; il modello piccolo neppure |
| Memory wall (C25) | Il muro del 30° chilometro | Il muro è un esaurimento; il memory wall è un limite di flusso |
| Allucinazioni (C12) | Il GPS in galleria: un passo plausibile e sbagliato, mostrato con sicurezza | Il GPS si corregge all'uscita, il modello no |
| Agenti (C15) | Il coach virtuale che legge i tuoi dati, propone un piano, ti guarda correre | Un coach vede il corpo; l'agente vede solo ciò che gli dai |
| Sicurezza (C16) | I nastri del percorso spostati da un burlone | I nastri sono visibili; l'istruzione nascosta no |

## 4. Fili conduttori e box

- **La richiesta:** *«Fammi una tabella per correre un 10 km in meno di 50 minuti.»* Si pone a un LLM all'inizio, e la si ripete lungo il libro con modelli diversi: il primo piano è plausibile e sbagliato (troppo volume subito, chilometri inventati), poi arriva con i dati, poi con un agente. Il runner dell'esempio è inventato (illustrativo).
- **La tabella di marcia:** all'inizio del libro un grafico semplice dei 5 blocchi, ripreso a ogni blocco.
- **Box fissi:**

| Box | Contenuto |
|---|---|
| **La seduta** | in cima: tipo di allenamento, durata, zona e scopo del capitolo |
| **Passo e battito** | i numeri (conti rifacibili) |
| **Dal bordo strada** | un aneddoto vero di corsa o di IA |
| **Sotto il cofano** | per il lettore tecnico |
| **Prova tu** | esperimento da 5 minuti |
| **Regola d'uso** | in chiusura |
| **Scarico** | ogni quarto capitolo: riepilogo in tre righe |

## 5. Capitoli

Lunghezza indicativa: 3.500-4.500 parole. Il linguaggio sportivo serve a spiegare l'IA: se un paragrafo parla più di corsa che di IA, va tagliato.

### Prologo — Chilometro zero

- **Idea:** presenta la tabella, il runner inventato e la richiesta. «Fidippide» come fatto o leggenda: Erodoto lo fa correre da Atene a Sparta (circa 240 km) prima di Maratona; la corsa da Maratona ad Atene è una tradizione tarda; 42,195 km sono lo standard dal 1921. Un modello linguistico è un maratoneta che fa un passo alla volta.
- **Esempi da usare:** la richiesta della tabella, con una prima risposta plausibile e sbagliata.
- **Occhio a:** non confondere il fatto con la leggenda.

## Blocco 1 — La base: come funziona

### Allenamento 1 — Un passo dopo l'altro

- **Concetti:** C01. **Seduta:** corsa lenta, ritmo da chiacchierata.
- **Idea:** il modello fa un passo (token) alla volta, senza tornare indietro, e ogni passo dipende dai precedenti.
- **Esempi da usare:** l'orologio che suggerisce il prossimo allenamento; il proverbio completato (P01); «Domenica lungo di...» (quanti chilometri? probabilità); la perplexity come numero di strade tra cui indecidere; il dado di Shannon in due righe; l'ordine dei passi nella gara.
- **Prova tu:** P01.
- **Regola d'uso:** chiedi prima il piano, poi la risposta.

### Allenamento 2 — I parziali

- **Concetti:** C02. **Seduta:** ripetute corte.
- **Idea:** il testo si spezza in segmenti scelti dalla statistica, non dalla grammatica.
- **Esempi da usare:** i parziali al chilometro e quelli del cronometrista; le R di «strawberry»; la stessa frase in italiano e in inglese con il costo in token; un numero lungo spezzato; il token come moneta (costa, occupa, rallenta).
- **Prova tu:** P02.
- **Occhio a:** niente split senza tokenizer reale.

### Allenamento 3 — Percorsi parenti

- **Concetti:** C03. **Seduta:** corsa tranquilla con osservazione.
- **Idea:** ogni token è un punto in una mappa; i significati simili stanno vicini.
- **Esempi da usare:** «ripetute», «fartlek» e «variazioni di ritmo» vicini, «riposo» lontano; le mappe di calore delle app dei runner come immagine di «vicino»; Roma e Milano vicine, Roma e cacciavite lontane; la ricerca per significato; il rischio di sigle e codici.
- **Occhio a:** le dimensioni non hanno nomi.

### Allenamento 4 — La scia

- **Concetti:** C04. **Seduta:** corsa di gruppo.
- **Idea:** ogni parola decide chi guardare, come un corridore sceglie dietro chi mettersi in scia.
- **Esempi da usare:** «Mario ha dato il libro a Luca perché lui doveva studiare»; il gruppo di testa; chi ti copre dal vento; Query, Key e Value come «chi sono, cosa offro, cosa porto»; il Transformer del 2017 e l'attenzione del 2014.
- **Occhio a:** attenzione non vuol dire capire.
- **Regola d'uso:** una cosa per volta.

### Allenamento 5 — Quarantadue chilometri di cronometro

- **Concetti:** C05, C06. **Seduta:** lungo, con riepilogo.
- **Idea:** i layer sono tappe: a ogni chilometro il cronometro aggiunge qualcosa, senza cancellare.
- **Esempi da usare:** i passaggi ai 10, 21, 30 e 40 km; i 32 layer di Llama 3 8B come una mezza maratona abbondante, gli 80 della 70B come un ultra corto, i 126 della 405B come un ultra vero; che cos'è «8B»; le taglie come categorie (5K, 10K, mezza, maratona, ultra); Golden Gate Claude.
- **Scarico:** riepilogo del blocco.

## Blocco 2 — Il volume: come si addestra

### Allenamento 6 — Chilometri nelle gambe

- **Concetti:** C07. **Seduta:** lungo progressivo.
- **Idea:** il pre-training è volume: miliardi di passi, ogni errore corregge un po' tutte le manopole.
- **Esempi da usare:** la base aerobica; la regola del 10% (una regola empirica da dichiarare tale) e perché per i modelli non vale; la perdita come tempo al chilometro; learning rate come intensità; riscaldamento (warmup) e **taper** (il learning rate che scende a fine addestramento); infortunio come divergenza dell'addestramento; i 15 mila miliardi di token.
- **Occhio a:** il modello non «si stanca».

### Allenamento 7 — Più volume o più atleti? Le leggi di scala

- **Concetti:** C07 (scaling). **Seduta:** progressivo.
- **Idea:** conta la taglia, conta il volume, e il rapporto giusto è stato misurato.
- **Esempi da usare:** Chinchilla (70 miliardi di parametri su 1,4 mila miliardi di token battono 280 miliardi); Llama 3 8B con 1.900 token per parametro come atleta piccolo con volume enorme (costa più nell'addestramento, meno ogni volta che corre); i costi (DeepSeek-V3: 5,6 milioni dichiarati, con la riserva).
- **Dal bordo strada:** Zátopek a Helsinki 1952 (5.000, 10.000 e maratona nei Giochi; la prima maratona della sua vita): un atleta, tanti compiti. Parallelo da dichiarare con cura: un solo modello base, tanti compiti.
- **Occhio a:** le leggi di scala non sono fisiologia.

### Allenamento 8 — Cuore e gambe: perché servono le GPU

- **Concetti:** C21. **Seduta:** ripetute lunghe.
- **Idea:** il motore non sono le gambe (calcolo) ma l'ossigeno che arriva (banda di memoria).
- **Esempi da usare:** VO₂max; la CPU come maratoneta solitario, la GPU come mille velocisti coordinati; gambe da atleta e polmoni da fumatore (TFLOPS alti, banda bassa); CUDA (2006-2007); AlexNet su due GTX 580; le architetture NVIDIA con nomi di scienziati.
- **Occhio a:** le schede da gioco non sono quelle dei data center.

## Blocco 3 — La specificità: come si specializza

### Allenamento 9 — Dal fondo generale alla 10 km

- **Concetti:** C09. **Seduta:** ripetute a ritmo gara.
- **Idea:** fine-tuning = preparazione specifica per una distanza. Funziona, ma si può perdere ciò che si sapeva (dimenticanza catastrofica).
- **Esempi da usare:** 5K, 10K e maratona; «ti alleni solo sui 100 m e dimentichi il fondo»; esempi di fine-tuning (un assistente per un'azienda, uno stile); prima il prompt, poi il RAG, il fine-tuning solo alla fine; costi (da pochi dollari a centinaia per modelli piccoli e medi).
- **Occhio a:** il fine-tuning non insegna fatti che cambiano.

### Allenamento 10 — L'allenatore e il pollice

- **Concetti:** C08. **Seduta:** tecnica.
- **Idea:** instruction tuning e RLHF trasformano un completatore in un assistente.
- **Esempi da usare:** il modello base che continua con altre domande di quiz; il coach che dice solo «bravo» (adulazione); InstructGPT da 1,3 miliardi preferito a GPT-3 da 175; GPT-4o adulatore (aprile 2025).
- **Regola d'uso:** chiedi di criticare.

### Allenamento 11 — Il plantare: LoRA, distillazione, modelli piccoli

- **Concetti:** C09. **Seduta:** corsa con attrezzo.
- **Idea:** LoRA e QLoRA come piccole modifiche mirate; la distillazione come passaggio di mestiere.
- **Esempi da usare:** un plantare costa poco e cambia molto; i post-it sull'enciclopedia; QLoRA e il modello da 65 miliardi su una scheda da 48 GB; Alpaca; il maestro che allena il giovane.
- **Occhio a:** il plantare non cambia il piede.

### Allenamento 12 — Il personal best sul giro di casa

- **Concetti:** C17. **Seduta:** test cronometrato.
- **Idea:** overfitting e benchmark: il tempo migliore su un percorso che conosci a memoria.
- **Esempi da usare:** il giro di casa; percorsi certificati e tempi ufficiali; **Rosie Ruiz** (New York 1979, Boston 1980: percorso non regolare, titolo revocato [DA VERIFICARE: tempi e date]); le scarpe col carbonio e il limite di 40 mm di suola fissato da World Athletics nel 2020 (benchmark e tecnologia) [DA VERIFICARE]; MMLU, HumanEval, SWE-bench; le arene a voto cieco; Goodhart; il mini-benchmark di 20 domande.
- **Prova tu:** P12.
- **Occhio a:** i risultati dei benchmark vanno datati.
- **Scarico:** riepilogo del blocco.

### Allenamento 13 — Il conto ai rifornimenti: i modelli che ragionano

- **Concetti:** C08 (ragionamento). **Seduta:** lungo con soste.
- **Idea:** scrivere i conti prima di rispondere.
- **Esempi da usare:** chain-of-thought; «Let's think step by step»; o1 e R1; il negative split (partire piano, finire forte) come immagine di calcolo speso al momento giusto; il costo in token e in attesa; il ragionamento mostrato non è sempre fedele.
- **Regola d'uso:** per logica e codice un modello che ragiona; per testi semplici no.

## Blocco 4 — Il giorno gara: far correre un modello

### Allenamento 14 — Ritmo gara: i token al secondo

- **Concetti:** C19, C11 (prefill e decode). **Seduta:** il lungo della settimana: ritmo gara.
- **Idea:** la velocità di un modello si capisce con un conto: banda ÷ GB letti per token.
- **Esempi da usare:** il passo come velocità; la reazione allo sparo (TTFT) e il passo (decode); 5 token/s è camminata veloce, 30 un amatore, oltre 100 un élite (scala simbolica); la formula da tovagliolo con conti completi (Llama 3 8B in Q4 su RTX 4090 e su RAM DDR5, gpt-oss-120b, DeepSeek-V3 su Mac Studio); perché il cloud serve tanti utenti insieme (come un grande gruppo che si copre a vicenda).
- **Prova tu:** P08, P11.
- **Occhio a:** teorico e misurato.

### Allenamento 15 — Lo zaino da ultratrail: la quantizzazione

- **Concetti:** C20. **Seduta:** lungo con zaino.
- **Idea:** togliere peso senza togliere l'attrezzatura obbligatoria.
- **Esempi da usare:** 16, 8, 4 e 2 bit come il passo dato al decimo di secondo («4:58,3»), al secondo («4:58»), a spanne («circa cinque minuti») e a gesti («piano o forte»); lo zaino da ultra: giacca antivento e luce frontale sono i pesi essenziali (AWQ protegge circa l'1% dei pesi salienti); Q4_K_M; il peso dei file; MXFP4; quantizzazione della KV cache.
- **Prova tu:** P09.
- **Occhio a:** niente percentuali inventate.
- **Regola d'uso:** Q4_K_M come punto di partenza.

### Allenamento 16 — La memoria dell'orologio: contesto, cache, cinque memorie, RAG

- **Concetti:** C11, C13, C14. **Seduta:** progressivo.
- **Idea:** quando la memoria dell'orologio è piena cancella i giri più vecchi: così il contesto.
- **Esempi da usare:** KV cache (128 KiB per token); *Lost in the Middle*; i diari degli allenamenti come memoria esterna; il RAG come il quaderno da consultare; memoria dell'app come promemoria.
- **Prova tu:** P04.

### Allenamento 17 — Metronomo o fartlek: il campionamento

- **Concetti:** C10. **Seduta:** fartlek.
- **Idea:** temperatura e top-p decidono quanto si improvvisa.
- **Esempi da usare:** ripetute a ritmo fisso e fartlek (gioco di velocità, dallo svedese); due risposte alla stessa domanda; il loop di ripetizione; il motivo per cui anche a temperatura 0 il risultato può variare.
- **Prova tu:** P03.
- **Occhio a:** temperatura 1 non è delirio.

### Allenamento 18 — Il GPS in galleria: le allucinazioni

- **Concetti:** C12. **Seduta:** test in condizioni difficili.
- **Idea:** il GPS in galleria segna un passo plausibile e sbagliato, con sicurezza.
- **Esempi da usare:** l'orologio che dice 6:10 al chilometro mentre vai a 4:30; il piano di allenamento inventato (chilometri impossibili, gare inesistenti); il campanello che manca; il test a crocette senza penalità; citazioni da verificare.
- **Mito da sfatare:** «basta abbassare la temperatura».
- **Regola d'uso:** il secondo strumento (un'altra fonte, un'altra app).

### Allenamento 19 — Scegliere le scarpe: locale, hardware, offload

- **Concetti:** C18, C22. **Seduta:** prova materiali.
- **Idea:** scegliere la macchina secondo la gara.
- **Esempi da usare:** gara a pagamento (cloud) contro uscita libera (locale); il leak di LLaMA e llama.cpp; le fasce (8 GB, 16-24 GB, 32 GB, Mac con memoria unificata, mini PC); il modello da 12 GB su una scheda da 8 GB (con il conto: 12, 7 e 33 token/s); `-ngl`; «offload» nei due sensi.
- **Prova tu:** P10.

### Allenamento 20 — L'ekiden e la lepre: MoE e decodifica speculativa

- **Concetti:** C23, C24. **Seduta:** tappa di squadra.
- **Idea:** pochi specialisti attivi per ogni frazione; la lepre che propone e il campione che controlla.
- **Esempi da usare:** l'ekiden (la maratona in tappe); la società sportiva che paga tutti ma ne schiera due; DeepSeek-V3 (671 miliardi totali, 37 attivi); gpt-oss-120b (5,1 attivi); la decodifica speculativa e Kipchoge a Vienna 2019 (1:59:40, evento non omologato, con lepri a rotazione) [DA VERIFICARE].
- **Occhio a:** gli esperti non sono «per argomento»; il MoE non riduce la memoria.

### Allenamento 21 — Il muro del 30° chilometro: hardware nuovo, energia, costi

- **Concetti:** C25, C26. **Seduta:** lungo con muro.
- **Idea:** il muro della memoria. Il calcolo cresce più in fretta della banda: come il maratoneta che arriva al 30° chilometro senza più scorte.
- **Esempi da usare:** HBM; B200 e Vera Rubin (specifiche annunciate, da datare); TPU, Groq, Cerebras; le scarpe col carbonio come hardware specializzato (ASIC) contro la scarpa da allenamento (CPU) e quella da trail (GPU); l'economia di corsa e i joule per token (300 W ÷ 30 token/s = 10 J); il costo di mille token in locale (circa 0,07 centesimi di euro).
- **Occhio a:** tutto datato.
- **Scarico:** riepilogo del blocco.

## Blocco 5 — Affinare: agenti, sicurezza, futuro

### Allenamento 22 — Il coach nel taschino: gli agenti

- **Concetti:** C15. **Seduta:** test di tecnica.
- **Idea:** un agente legge i tuoi dati, propone, controlla, corregge.
- **Esempi da usare:** un coach virtuale che legge il diario, propone un piano e lo aggiusta; workflow (la tabella scritta) contro agente (il coach che decide); MCP come presa standard (anche per le app di corsa); 20 passi a 10 token/s = 17 minuti; la durata dei compiti degli agenti, dai 5K agli ultra (METR, marzo 2025: raddoppio circa ogni 7 mesi, da verificare).
- **Occhio a:** i dati personali vanno sempre chiesti: l'autore deve dare il consenso per qualsiasi uso di dati reali.

### Allenamento 23 — I nastri spostati: sicurezza e privacy

- **Concetti:** C16. **Seduta:** corsa di orientamento.
- **Idea:** un agente che legge un testo può obbedire a un testo ostile.
- **Esempi da usare:** i nastri del percorso spostati da un burlone (caricatura, dichiararla); la mail trappola; il permesso minimo; privacy: ciò che incolli esce dal tuo computer; il locale non vuol dire sicuro.
- **Prova tu:** P14.

### Allenamento 24 — Il taper: dove stiamo andando

- **Concetti:** C28, C29. **Seduta:** scarico prima della gara.
- **Idea:** il riepilogo della storia (da Markov agli agenti) come una carriera; le domande aperte.
- **Esempi da usare:** Bannister (3:59,4 il 6 maggio 1954) e le barriere che si rompono dopo la prima volta; Kathrine Switzer a Boston (1967, pettorale 261); i record che rallentano (rendimenti decrescenti); modelli piccoli, agenti, memoria persistente, energia.
- **Occhio a:** nessuna data di futuro.

### Epilogo — La tabella da portarti a casa

- **Concetti:** C30.
- **Idea:** la tabella «cosa succede sotto il cofano / cosa fai di diverso» nelle parole del libro; il **Test dell'esperto** (30 domande); la richiesta iniziale ripetuta con un sistema ben usato.

## 6. Copertura della mappa

C01 all. 1 · C02 all. 2 · C03 all. 3 · C04 all. 4 · C05-C06 all. 5 · C07 all. 6, 7 · C08 all. 10, 13 · C09 all. 9, 11 · C10 all. 17 · C11 all. 14, 16 · C12 all. 18 · C13-C14 all. 16 · C15 all. 22 · C16 all. 23 · C17 all. 12 · C18 all. 19 · C19 all. 14 · C20 all. 15 · C21 all. 8 · C22 all. 19 · C23-C24 all. 20 · C25-C26 all. 21 · C27 (accenno in all. 3) · C28-C29 all. 24 · C30 epilogo.
