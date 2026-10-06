# Libro 2 — *Il cielo dei token*

### Spedizione nell'universo di numeri che risponde alle nostre domande

> Il libro **dell'astronomia**. L'IA resta il tema; il cielo è lo strumento per capirla: scale, mappe, telescopi, segnali nel rumore, sonde. Fatti e numeri stanno in `mappa-contenuti.md`; le regole comuni in `CLAUDE.md`.

## 1. Identità del libro

- **Spina dorsale:** una **spedizione**. Il lettore è l'equipaggio; ogni capitolo è una notte d'osservazione con uno strumento diverso. Si parte dal catalogo delle stelle (token), si disegna la mappa (embedding), si costruisce il telescopio (Transformer), si fa la grande survey (addestramento), si osserva (uso quotidiano), si porta il telescopio sul balcone (modelli locali), si mandano le sonde (agenti) e si guarda oltre l'orizzonte (futuro).
- **Cosa lo distingue:** il tema è la **scala** e l'**incertezza**. Numeri enormi resi visibili con le potenze di dieci; allucinazioni raccontate come falsi segnali (canali di Marte, neutrini troppo veloci, forni a microonde che sembrano lampi radio); agenti raccontati come rover con quattro minuti di ritardo. L'ironia è gentile, la meraviglia vera.
- **Dove è più profondo:** embedding (C03), scale e numeri (C06), scaling (C07), allucinazioni (C12), benchmark (C17), agenti (C15), hardware del futuro (C25).
- **Regola del vincolo:** l'IA resta il tema principale. Niente capitoli di astronomia pura: in ogni capitolo un concetto di IA viene spiegato meglio dall'analogia astronomica, e l'analogia dichiara dove si rompe. Nessuna spiegazione astronomica più lunga del bisogno.
- **Lettore ideale:** chi ama il cielo e si sente escluso dall'IA, e il tecnico che apprezza i numeri e le scale.

## 2. Voce

- **Noi, l'equipaggio.** Il narratore parla al plurale («stasera puntiamo lo strumento su...»). Non attribuire all'autore esperienze personali non confermate (telescopi posseduti, osservazioni fatte).
- **Meraviglia e ironia, in dosi uguali.** Si ride dell'IA, dell'hype e di noi umani che da quattromila anni scambiamo i pattern per verità. Mai di chi osserva.
- **Frasi più distese del Libro 1** e periodi che si aprono su un'immagine; poi il colpo secco. Il ritmo è quello di una serata lunga all'oculare: pause, silenzio, una battuta.
- **Scala sempre in vista.** Ogni numero grande viene tradotto in qualcosa di tangibile (un miliardo di secondi sono 31,7 anni; la luce del Sole ci mette 8 minuti e 20 secondi).
- **Condizioni del cielo.** Ogni capitolo apre con tre righe: Strumento, Obiettivo, *Condizioni* (sereno = capitolo leggero, velato = serve attenzione, foschia = capitolo tecnico).
- **Umiltà dell'osservatore.** Si dice sempre cosa non si vede.

### Campione di voce (non è testo del libro)

> Per circa quattromila anni gli astronomi hanno previsto le eclissi senza avere la minima idea del perché avvenissero.
>
> Contavano. Annotavano. Notavano che dopo diciotto anni, undici giorni e otto ore il cielo ripeteva più o meno lo stesso spettacolo, e scrivevano: ne arriverà un'altra.
>
> Non conoscevano la gravità, né le orbite, né la forma della Terra. Conoscevano il ritmo.
>
> Se questo ti sembra familiare, è perché è esattamente ciò che fa un modello linguistico con le parole: nessuna legge, solo il ritmo. Con una differenza che vale tutto il libro: quando gli astronomi sbagliavano, l'eclissi non arrivava, e si accorgevano. Quando sbaglia il modello, arriva comunque qualcosa.

## 3. Analogie madri e dove scricchiolano

| Concetto | Analogia madre | Dove scricchiola |
|---|---|---|
| Previsione senza teoria (C01) | Il Saros dei Babilonesi e il meccanismo di Anticitera: eclissi previste senza fisica | Gli astronomi sapevano quando il pattern falliva; il modello no |
| Token (C02) | Il catalogo: Messier (110 oggetti), NGC (circa 7.800), Gaia (1,8 miliardi) | Le stelle esistono senza catalogo; i token li decide un algoritmo che conta |
| Embedding (C03) | Una mappa del cielo con migliaia di dimensioni; la similarità del coseno come distanza angolare; le costellazioni come proiezioni | Le distanze del cielo sono fisiche; quelle degli embedding si imparano |
| Attention (C04) | Il baricentro: ogni parola è attratta da quelle rilevanti, e il risultato è una media pesata | La gravità segue una sola legge; l'attenzione ne impara tante |
| Layer (C05) | Lo specchio segmentato del JWST: 18 esagoni ciascuno regolato da attuatori | I segmenti si allineano su una forma nota; i layer non hanno un bersaglio fisso |
| Parametri (C06) | Le stelle della Via Lattea (100-400 miliardi) contro i 175 miliardi di GPT-3 | Le stelle sono oggetti; i parametri non significano nulla da soli |
| Training (C07) | La survey del cielo; la discesa del gradiente come l'ottica attiva (misura l'errore, correggi gli attuatori) | L'ottica attiva conosce la forma giusta; il training conosce solo l'errore |
| Scaling (C07) | Specchi più grandi, pose più lunghe: Hubble Deep Field | L'area dello specchio cresce con il quadrato del diametro per legge fisica; le leggi di scala sono osservazioni, possono smettere |
| GPU (C21) | I «computer» di Harvard: decine di persone, ciascuna con un pezzetto di calcolo | Le persone cambiavano compito; la GPU ripete la stessa operazione |
| Post-training (C08) | La calibrazione dei dati: dark, flat, bias | La calibrazione corregge difetti noti; il post-training sceglie gusti |
| Ragionamento (C08) | La posa lunga: più fotoni, immagine migliore | Più tempo non garantisce la verità, solo meno rumore |
| Temperatura (C10) | Il colore delle stelle (blu = calde, rosse = fredde); il sensore raffreddato per ridurre il rumore | Nella stella è una proprietà fisica; nel modello è una manopola |
| Contesto (C11) | L'universo osservabile: vedi solo ciò che la luce ha fatto in tempo ad arrivare | Il raggio dell'universo osservabile cresce col tempo; la finestra è fissa |
| Memorie (C13-C14) | L'archivio delle lastre fotografiche e il diario dell'osservatore; l'archivio per cercare ciò che già si sa | Gli archivi dicono se una lastra esiste; il modello non lo sa |
| Allucinazioni (C12) | I falsi segnali: canali di Marte, «Wow!», neutrini più veloci della luce | Lo strumento non «vuole» vedere; il modello non ha l'uscita «niente rilevato» di default |
| Benchmark (C17) | Le candele standard e la scala delle distanze; la tensione di Hubble quando due metodi non concordano | Le candele hanno luminosità fissata dalla fisica; i benchmark sono convenzioni |
| Quantizzazione (C20) | Dal RAW al JPEG di un'immagine astronomica | Nell'immagine perdi i toni deboli; nel modello perdi l'accuratezza distribuita |
| MoE (C23) | La rete di telescopi: uno per lunghezza d'onda, e il comitato che assegna il tempo | I telescopi sono specializzati in modo leggibile; gli esperti no |
| Agenti (C15) | Il rover: ritardo di minuti, autonomia limitata, controllo da terra | Il rover segue regole certe; l'agente usa giudizi probabilistici |
| Sicurezza (C16) | Comandi autenticati per le sonde; il segnale ingannevole | Le sonde obbediscono solo a canali verificati; l'agente obbedisce a ciò che legge |

## 4. Fili conduttori e box

- **La domanda del balcone:** *«Che cosa si vede stasera nel cielo?»* Si pone a un LLM all'inizio del libro e ricompare in ogni parte. Ciò che la risposta rivela: perché il modello non sa che giorno è (cutoff), perché inventa una Venere a mezzanotte (Venere non si vede mai a mezzanotte: la sua distanza angolare dal Sole non supera circa 47°), come un'effemeride (uno strumento di calcolo) risolve in un secondo ciò che la memoria del modello sbaglia, come un agente la chiama da solo.
- **Falso segnale:** un box fisso con la storia di un'illusione celeste (con anno e riferimento) e il parallelo con un errore dell'IA.
- **Potenze di dieci:** box che traduce un numero dell'IA nella scala di tutti i giorni (un miliardo di secondi, la Via Lattea, la luce del Sole).
- **Sotto il cofano:** per il lettore tecnico (come in tutti i libri).
- **Prova tu:** una per capitolo, a volte con un'app di planetario.
- **Regola d'uso:** chiude ogni capitolo.
- **Registro d'osservazione:** le tre righe iniziali di ogni capitolo.

## 5. Capitoli

Lunghezza indicativa: 3.500-4.500 parole. Le storie astronomiche sono lo strumento: la spiegazione tecnica dell'IA non si taglia mai per far posto al cielo.

### Prologo — Il cielo di Galileo (1610)

- **Idea:** un nuovo strumento rivela un mondo sconosciuto e crea errori nuovi. Il *Sidereus Nuncius* (marzo 1610): lune di Giove, Luna con le montagne. Promessa del libro: capire lo strumento, ciò che mostra e ciò che sbaglia.
- **Esempi da usare:** i primi astronomi che scambiavano difetti delle lenti per scoperte; la domanda del balcone posta per la prima volta a un LLM, con una risposta plausibile e subdola.
- **Occhio a:** non romanzare Galileo; solo fatti citabili.

## Parte I — Il catalogo e la mappa

### Cap. 1 — Eclissi senza fisica: prevedere non è sapere

- **Concetti:** C01.
- **Idea:** un LLM prevede il prossimo token come i Babilonesi prevedevano le eclissi: dal pattern, senza teoria.
- **Esempi da usare:** il Saros (18 anni, 11 giorni, 8 ore); il meccanismo di Anticitera (II-I secolo a.C.); Halley e la cometa del 1758-59 (previsione con teoria); la tastiera del telefono; il proverbio completato in cinque modi (P01); il dado di Shannon.
- **Storia vera:** gli astronomi babilonesi.
- **Occhio a:** non dire che i Babilonesi «erano un LLM»; è un paragone da dichiarare.
- **Regola d'uso:** un modello che prevede bene non sa perché.

### Cap. 2 — Il catalogo: i token

- **Concetti:** C02.
- **Idea:** il cielo non si legge a occhio, si cataloga. Il testo neppure.
- **Esempi da usare:** Messier (110 oggetti), NGC, Gaia (1,8 miliardi di sorgenti); Llama 3 con 128.256 «voci»; il catalogo che spezza un oggetto debole in stelle singole come un tokenizer spezza le parole rare; le R di «strawberry»; italiano contro inglese.
- **Prova tu:** P02 con una frase astronomica (per esempio il nome di una stella).
- **Occhio a:** niente split senza tokenizer reale.

### Cap. 3 — Galassie di significato: gli embedding

- **Concetti:** C03, C27.
- **Idea:** ogni token è un punto in uno spazio a molte dimensioni; la similarità del coseno è una distanza angolare; i concetti formano ammassi.
- **Esempi da usare:** le costellazioni come proiezioni di stelle a distanze diverse (una «mappa a due dimensioni» di uno spazio a migliaia di dimensioni); Roma, Milano e Parigi in un ammasso; Roma e cacciavite lontane; re − uomo + donna ≈ regina; i tasselli di un'immagine astronomica trasformati in token (accenno multimodale); i pregiudizi come «polvere» che altera la mappa.
- **Occhio a:** le dimensioni non hanno nomi.

### Cap. 4 — Potenze di dieci: i numeri dell'IA a misura d'uomo

- **Concetti:** C06.
- **Idea:** un capitolo per imparare a sentire i numeri grandi.
- **Esempi da usare:** un miliardo di secondi (31,7 anni) e mille miliardi (31.700 anni); i parametri (175 miliardi di GPT-3) contro le stelle della Via Lattea (100-400 miliardi); i token di addestramento (15 mila miliardi); i dollari; i watt; *Powers of Ten* di Charles e Ray Eames (1977); la luce del Sole in 8 minuti.
- **Occhio a:** paragoni suggestivi, non equivalenze; cervello e Via Lattea vanno dichiarati tali.

## Parte II — Lo strumento

### Cap. 5 — Il telescopio: attention e Transformer

- **Concetti:** C04.
- **Idea:** ogni parola guarda tutte le altre e dà più peso a quelle rilevanti: un baricentro pesato.
- **Esempi da usare:** «Mario ha dato il libro a Luca perché lui doveva studiare»; Query, Key e Value come ricerca nel catalogo; il baricentro di un sistema; il 2017 (otto autori), e il 2014 dell'attenzione aggiunta; l'addestramento in parallelo.
- **Occhio a:** l'attenzione non è «capire»; evitare «non sapevano».

### Cap. 6 — Lo specchio segmentato: layer e ottica attiva

- **Concetti:** C05.
- **Idea:** 80 strati che aggiungono dettagli, come un telescopio fatto di segmenti ciascuno regolato.
- **Esempi da usare:** il JWST (18 segmenti, ciascuno con attuatori) e l'allineamento durato mesi (2022); il fascicolo che sale; Golden Gate Claude (maggio 2024); 32, 80, 126 piani.
- **Occhio a:** i layer aggiungono, non filtrano.

### Cap. 7 — La grande survey: il pre-training

- **Concetti:** C07.
- **Idea:** il modello legge il «cielo» del testo e a ogni errore corregge milioni di manopole, come l'ottica attiva con gli attuatori.
- **Esempi da usare:** lo Sloan Digital Sky Survey e Gaia come precedenti di grandi censimenti; la perdita come misura di quanto l'immagine è sfocata; i 15 mila miliardi di token; il costo dichiarato di DeepSeek-V3 (con la riserva); il cutoff come «ultima lastra».
- **Occhio a:** la discesa del gradiente non conosce la forma giusta, solo l'errore.

### Cap. 8 — Specchi più grandi, pose più lunghe: leggi di scala

- **Concetti:** C07 (scaling).
- **Idea:** più grande non basta: serve anche più tempo di posa.
- **Esempi da usare:** da Galileo ai 39 metri dell'ELT (in costruzione, prima luce prevista intorno al 2029 [DA VERIFICARE]); l'Hubble Deep Field (dicembre 1995: dieci giorni su un angolino di cielo vuoto, circa 3.000 galassie); Chinchilla; Llama 3 8B sovrallenato; il confine dove la fisica ci ferma (atmosfera) e dove potremmo fermarci (dati).
- **Occhio a:** le leggi di scala sono osservazioni, non leggi fisiche.

### Cap. 9 — I computer di Harvard: le GPU

- **Concetti:** C21.
- **Idea:** «computer» era una professione. Il calcolo si è sempre fatto in parallelo.
- **Esempi da usare:** le «Harvard Computers» (Pickering, Fleming, Leavitt, Cannon); Leavitt e la relazione periodo-luminosità; la classificazione spettrale (OBAFGKM); le GPU come mille calcolatori con lo stesso foglio; CUDA (2006-2007); AlexNet su due GTX 580; i nomi NVIDIA come un catalogo di scienziati (Kepler, Rubin...).
- **Occhio a:** i computer umani cambiavano compito, la GPU esegue la stessa operazione su tanti dati.

### Cap. 10 — Calibrare i dati: da modello grezzo ad assistente

- **Concetti:** C08, C09.
- **Idea:** l'immagine grezza non si usa; si calibra (dark, flat, bias). Allo stesso modo si trasforma il modello base in assistente e lo si specializza.
- **Esempi da usare:** un frame con rumore termico che sembra un oggetto; il modello base che continua con altre domande di quiz; RLHF come tutor; adulazione (sycophancy) come bias di conferma; fine-tuning, LoRA e distillazione come filtri e telescopi più piccoli per compiti specifici.
- **Occhio a:** la calibrazione corregge difetti noti, il post-training sceglie gusti.

### Cap. 11 — La posa lunga: i modelli che ragionano

- **Concetti:** C08 (ragionamento).
- **Idea:** più «tempo di posa» al momento della risposta, meno rumore.
- **Esempi da usare:** una posa di dieci secondi contro una di dieci minuti; chain-of-thought; o1 (12 settembre 2024); DeepSeek-R1 (20 gennaio 2025); il costo in token e in attesa; quando il «ragionamento» mostrato non è la causa.
- **Occhio a:** più tempo non garantisce la verità.

## Parte III — Osservare

### Cap. 12 — Colore e temperatura: il campionamento

- **Concetti:** C10.
- **Idea:** stelle blu calde e caotiche, stelle rosse fredde e calme; il sensore raffreddato per ridurre il rumore.
- **Esempi da usare:** temperatura 0, 0,7 e 1,5 sulla stessa domanda; top-p come limite di magnitudine (tieni le stelle più luminose che insieme fanno il 90% della luce); il loop di ripetizione; due risposte alla stessa domanda del balcone.
- **Prova tu:** P03.
- **Occhio a:** temperatura 1 non è delirio.

### Cap. 13 — L'universo osservabile: la finestra di contesto

- **Concetti:** C11.
- **Idea:** il modello vede solo ciò che sta nel suo orizzonte.
- **Esempi da usare:** l'universo osservabile (circa 93 miliardi di anni luce di diametro); la KV cache come diario delle osservazioni; 128 KiB per token, 16 GiB a 128K; *Lost in the Middle*; prefill (la posa) e decode (lettura); i token al secondo contro la lettura umana.
- **Prova tu:** P04.
- **Occhio a:** l'orizzonte cosmologico cresce col tempo, quello del modello è fisso.

### Cap. 14 — L'archivio delle lastre: le cinque memorie e il RAG

- **Concetti:** C13, C14.
- **Idea:** pesi, contesto, cache, memoria dell'app, memoria esterna.
- **Esempi da usare:** un osservatorio con lastre fotografiche; il diario dell'osservatore; la ricerca in un archivio per significato (cercare «cometa» e trovare «corpo ghiacciato»); la domanda del balcone risolta consultando le effemeridi.
- **Occhio a:** il RAG non è fine-tuning.

### Cap. 15 — Canali su Marte: le allucinazioni

- **Concetti:** C12.
- **Idea:** lo strumento mostra ciò che il sistema è fatto per mostrare, e noi ci vediamo ciò che ci aspettiamo.
- **Esempi da usare:** i «canali» di Schiaparelli (1877) e la leggenda della traduzione (canali o canals, da trattare come fatto o leggenda); il «volto» su Marte (Viking, 1976; foto migliori nel 1998 e 2001); il segnale «Wow!» (1977); LGM-1, poi pulsar (1967); BICEP2 (2014); i neutrini di OPERA al Gran Sasso (2011); i peryton (2015); Venere a mezzanotte chiesta a un LLM.
- **Storia vera:** nel testo ne bastano due o tre, raccontate bene; le altre vanno nei box «Falso segnale» dei capitoli vicini, senza duplicati.
- **Mito da sfatare:** «basta abbassare la temperatura».
- **Regola d'uso:** il secondo strumento è la cura (replica, citazioni, RAG).

### Cap. 16 — La scala delle distanze: i benchmark

- **Concetti:** C17.
- **Idea:** per misurare servono candele standard, e si litiga quando i metodi non concordano.
- **Esempi da usare:** la scala delle distanze; le candele standard; la tensione di Hubble (circa 67 contro circa 73 km/s per megaparsec); MMLU, HumanEval, SWE-bench; le arene a voto cieco; Goodhart; il caso di Llama 4 (aprile 2025).
- **Prova tu:** P12.
- **Occhio a:** la contaminazione non è un telescopio che «sa già» la risposta: è un test già visto.

## Parte IV — Il telescopio sul balcone

### Cap. 17 — Hubble o balcone? I modelli locali

- **Concetti:** C18, C19.
- **Idea:** il cloud è Hubble in orbita, il modello locale è il telescopio sul balcone: meno potente, ma tuo.
- **Esempi da usare:** perché in locale (privacy, offline, nessuna bolletta) e quando no; LLaMA e llama.cpp (marzo 2023); i conti della formula da tovagliolo; la velocità di trasmissione di Voyager (160 bit/s, cioè 20 byte/s [DA VERIFICARE]) contro un modello a 10 token/s (circa 40 byte/s); il tetto teorico in token/s.
- **Prova tu:** P08.
- **Occhio a:** teorico e misurato.

### Cap. 18 — RAW o JPEG? La quantizzazione

- **Concetti:** C20.
- **Idea:** da 16 a 4 bit come da un'immagine RAW a una compressa.
- **Esempi da usare:** una galassia a 8, 4 e 2 bit (poche tonalità: «un buco nero e quattro puntini»); il peso dei file; Q4_K_M; il blocco con la sua scala; l'AWQ che protegge i pesi essenziali; MXFP4 di gpt-oss.
- **Prova tu:** P09.
- **Occhio a:** niente percentuali inventate.

### Cap. 19 — Il peso del telescopio: VRAM, offload, memoria unificata

- **Concetti:** C21 (VRAM), C22.
- **Idea:** il telescopio troppo pesante per il balcone.
- **Esempi da usare:** il modello da 12 GB su 8 GB (tutto il conto); `-ngl`; i Mac e i mini PC con memoria unificata; la scelta della macchina per fasce.
- **Prova tu:** P10.
- **Occhio a:** «offload» nei due sensi.

### Cap. 20 — Una rete di specchi: MoE e trucchi

- **Concetti:** C23, C24.
- **Idea:** non un telescopio gigante, ma una rete in cui lavora chi serve.
- **Esempi da usare:** il VLT (quattro unità), ALMA, l'Event Horizon Telescope; il comitato che assegna il tempo; DeepSeek-V3 (671 miliardi, 37 attivi); gpt-oss; la decodifica speculativa.
- **Occhio a:** gli esperti non sono per lunghezza d'onda.

### Cap. 21 — Gli osservatori di domani: hardware, energia, costi

- **Concetti:** C25, C26.
- **Idea:** dove va l'hardware dell'IA e quanto costa.
- **Esempi da usare:** HBM, TPU Ironwood, Cerebras (un wafer intero come specchio unico), la piattaforma Vera Rubin di NVIDIA e Vera Rubin, l'astronoma che portò le prove della materia oscura; l'Osservatorio Vera C. Rubin (primi dati nel giugno 2025, circa 20 TB a notte [DA VERIFICARE]); data center in orbita (prototipi annunciati da Google, novembre 2025 [DA VERIFICARE]); energia per prompt; la scala di Kardashev.
- **Occhio a:** tutto datato.

## Parte V — Le sonde

### Cap. 22 — Rover: gli agenti

- **Concetti:** C15.
- **Idea:** un agente è una sonda con autonomia limitata e controllo da terra.
- **Esempi da usare:** il ritardo con Marte (da circa 3 a circa 22 minuti per tratta [DA VERIFICARE]); i rover autonomi; Mars Climate Orbiter (1999, un errore di unità); il lander Schiaparelli (2016, il computer si credette già a terra); Voyager 1 riparata a 22,5 ore-luce (2024); MCP come connettore standard; la domanda del balcone risolta da un agente che chiama l'effemeride.
- **Occhio a:** i casi di sonde sono analogie, dichiararlo.

### Cap. 23 — Segnali falsi, comandi veri: sicurezza

- **Concetti:** C16.
- **Idea:** una sonda obbedisce solo a comandi autenticati. Un agente obbedisce a ciò che legge.
- **Esempi da usare:** i comandi autenticati; il segnale che sembra un messaggio; l'email trappola; la trifecta letale; il locale non è sicuro per definizione.
- **Prova tu:** P14.

## Parte VI — Oltre l'orizzonte

### Cap. 24 — Che cosa cercheremo

- **Concetti:** C28, C29.
- **Idea:** la storia in una pagina e le domande aperte.
- **Esempi da usare:** la linea del tempo dell'IA come un'esposizione cosmica; Kepler-90i trovato con una rete neurale (2017); l'IA che filtra gli allarmi dell'Osservatorio Rubin; la ricerca di segnali nel rumore (SETI); le domande aperte: modelli più piccoli, agenti più lunghi, memoria persistente, energia.
- **Occhio a:** nessuna data di futuro.

### Epilogo — Istruzioni per l'osservatore

- **Concetti:** C30.
- **Idea:** la tabella «cosa succede sotto il cofano / cosa fai di diverso» nelle parole del libro; il **Test dell'esperto** (30 domande); un ultimo sguardo al cielo: la domanda del balcone risposta da un sistema ben usato.

## 6. Copertura della mappa

C01 cap. 1 · C02 cap. 2 · C03 cap. 3 · C04 cap. 5 · C05 cap. 6 · C06 cap. 4 · C07 cap. 7, 8 · C08 cap. 10, 11 · C09 cap. 10 · C10 cap. 12 · C11 cap. 13 · C12 cap. 15 · C13-C14 cap. 14 · C15 cap. 22 · C16 cap. 23 · C17 cap. 16 · C18-C19 cap. 17 · C20 cap. 18 · C21 cap. 9, 19 · C22 cap. 19 · C23-C24 cap. 20 · C25-C26 cap. 21 · C27 cap. 3 · C28-C29 cap. 24 · C30 epilogo.
