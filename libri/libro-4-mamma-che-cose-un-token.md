# Libro 4 — *Mamma, che cos'è un token?*

### L'intelligenza artificiale spiegata a tavola, tra un primo e un secondo

> Il libro **della domenica a pranzo**: dialoghi, cucina, famiglia. È pensato perché lo capisca anche chi non ha mai aperto un computer, e perché il sistemista di famiglia ci trovi comunque qualcosa che non sapeva. Fatti e numeri stanno in `mappa-contenuti.md`; le regole comuni in `CLAUDE.md`.

## 1. Identità del libro

- **Spina dorsale:** una serie di **domeniche a pranzo**. Ogni capitolo è un pranzo: una scena a tavola con la famiglia, una spiegazione «in cucina», i conti, la domanda del più piccolo e un tovagliolo con tre righe. Alla fine di tutto il lettore costruisce con la famiglia **un assistente per le ricette di nonna Ada**: locale, privato, con le sue ricette dentro e capace di preparare la lista della spesa.
- **Cosa lo distingue:** è il libro più **dialogato e più comico**; l'unico con personaggi fissi; l'unico in cui ogni concetto passa per la cucina. Il lettore principale è «mamma»: se lei non capisce, si riscrive. Il lettore tecnico entra con una voce da commedia, il cugino Davide, che legge i riquadri «Sotto il cofano».
- **Dove è più profondo:** la prima metà (token, embedding, attenzione, previsione, allucinazioni, memoria), spiegata nel modo più chiaro dei cinque; l'ultima parte mette tutto insieme in un progetto concreto di modello locale, RAG e agente.
- **Lettore ideale:** chi non sa niente di IA e ne ha sentito parlare al telegiornale, ai figli o al lavoro; ma anche chi spiega l'IA ai genitori e cerca analogie che funzionino a tavola.
- **Lunghezza:** capitoli più corti degli altri (2.500-3.500 parole), perché il dialogo è veloce.

## 2. I personaggi (inventati: dichiararlo nell'antipasto)

| Personaggio | Ruolo |
|---|---|
| **Mamma** | pratica, sveglia, mai sciocca; fa le domande giuste («e quindi?»). È la lettrice ideale: se capisce lei, il capitolo è a posto |
| **L'io narrante** | quello che spiega (genere non marcato: evitare forme che rivelino sesso finché l'autore non decide) |
| **Nonna Ada** | 85 anni, scettica, custode del quaderno di ricette; contro «le macchine che sanno tutto» |
| **Zio Gino** | ottimista dell'hype e profeta di sventura insieme: «l'IA ci ruberà il lavoro», «è già cosciente, l'ho letto su Facebook». Il bersaglio ironico dei miti |
| **Cugino Davide** | il tecnico di famiglia, pomposo, usa i termini inglesi. Legge i riquadri «Sotto il cofano» con la serietà di un telegiornale |
| **Papà** | sempre in garage con il PC; interviene sull'hardware («ci ho messo una scheda video») |
| **Sofia, 10 anni** | pone la domanda che spacca il capitolo («ma se non lo sa, perché lo dice?») |

Regola: nessun personaggio è mai ridicolizzato per ignoranza. Si ride degli equivoci, dell'hype e delle macchine.

## 3. Voce

- **Commedia all'italiana a tavola:** battute, sovrapposizioni, il piatto che si fredda. Ma la spiegazione è seria e corretta.
- **Dialogo e narrazione alternati.** Il dialogo porta il dubbio, la narrazione porta la spiegazione. Mai più di una pagina di spiegazione di fila senza un'interruzione.
- **Tutto passa per la cucina:** ingredienti, ricette, brigata, dispensa, forno. Analogie semplici, concrete, di casa.
- **Zero gergo nel testo principale;** nei riquadri tecnici il gergo c'è, sciolto la prima volta.
- **Numeri semplici:** i conti si fanno in grammi, euro, minuti. «Il conto» è un riquadro fisso.
- **Esempi a pioggia:** almeno 15 per capitolo, anche di una riga.
- **Esempi dell'autore da riusare con un cenno:** «La giraffa quantistica di Napoli», il re «Giuseppe IV d'Italia», le lettere magnetiche del frigo, il supermercato, «Mario ha dato il libro a Luca perché lui doveva studiare», «Il gatto beve il...».

### Campione di voce (non è testo del libro)

> — Quindi — disse mamma, sistemando la forchetta con l'autorità di un giudice — è come il suggerimento del telefono.
>
> — Più o meno.
>
> — Quello che mi ha scritto «ti voglio bene» a mia sorella al posto di «ti voglio vendere» il tavolo?
>
> — Esatto. Solo che questo ha letto mezza biblioteca prima di suggerire.
>
> — E quindi sbaglia meno.
>
> — Sbaglia con più stile.
>
> Zio Gino alzò il bicchiere: — Io l'avevo detto.
>
> Nessuno gli chiese cosa.

## 4. Analogie madri e dove scricchiolano

| Concetto | Analogia madre | Dove scricchiola |
|---|---|---|
| Previsione (C01) | Il suggerimento del telefono e la mamma che dice «adesso scopre che è sua sorella» | La mamma conosce la trama; il modello non ha una storia in testa |
| Token (C02) | Le lettere magnetiche del frigo: pezzi riutilizzabili per comporre parole mai viste | I pezzi non li sceglie un umano |
| Embedding (C03) | Il supermercato: pasta vicino al riso, mela vicino alla pera, automobile lontana dalla banana | Gli scaffali sono tre dimensioni; il modello ne ha migliaia |
| Attention (C04) | A tavola tutti parlano insieme: capire chi dice cosa e a chi si riferisce «lui» | Mamma ascolta, il modello calcola pesi |
| Layer (C05) | Il ragù: ogni ora di cottura aggiunge sapore, e la pentola conserva tutto | Nel ragù l'aggiunta è fisica; nei layer è un calcolo |
| Parametri (C06) | I pizzichi di sale: una ricetta con 8 miliardi di ingredienti, ciascuno dosato al pizzico | Nessun pizzico «contiene» una ricetta |
| Training (C07) | Mamma ha imparato guardando nonna per quarant'anni: tante domeniche, tanti assaggi | Mamma sa perché una cosa funziona; il modello solo che di solito funziona |
| RLHF (C08) | Gli assaggiatori della domenica: «troppo salato», «ottimo» | I parenti hanno gusti e vogliono farti felice (adulazione: il nonno che dice sempre «buonissimo») |
| Fine-tuning e LoRA (C09) | Il corso di cucina giapponese: nuova specialità, stessa mano; un post-it sulla ricetta | La cuoca ricorda ciò che sapeva; il modello può dimenticare |
| Ragionamento (C08) | Fare i conti sul tovagliolo prima di rispondere | Il tovagliolo si legge; il ragionamento a schermo non sempre è fedele |
| Temperatura (C10) | Ricetta seguita alla lettera contro «a occhio» | La nonna sa quando improvvisare; il modello tira a sorte |
| Contesto (C11) | Il piano di lavoro della cucina: quel che c'è sopra si usa, il resto no | Il modello non ha cassetti |
| Memorie (C13) | Cinque cose diverse: ciò che mamma sa a memoria (pesi), il piano di lavoro (contesto), i post-it sul frigo (KV cache), il foglietto «zio Gino allergico ai gamberi» (memoria dell'app), il ricettario di nonna (RAG) | I post-it sono nostri; quelli del modello li scrive il software |
| Allucinazione (C12) | Zio Gino che racconta con sicurezza ciò che non sa | Zio Gino sa di inventare; il modello no |
| Locale (C18) | Cucinare a casa contro ordinare al ristorante | A casa sei responsabile anche del gas |
| GPU (C21) | Cento cuochi che tagliano cipolle insieme contro un cuoco stellato | I cento sanno fare una cosa sola |
| Memoria e velocità (C19) | La dispensa: sul piano di lavoro (VRAM), in sala (RAM), in cantina (disco): la velocità la decide la distanza | La cantina non la puoi ingrandire con un cassetto |
| Quantizzazione (C20) | La ricetta in grammi contro il «quanto basta» | Il «q.b.» si corregge assaggiando; i pesi no |
| MoE (C23) | La brigata di cucina: pesce, carne, dolci; per ogni piatto lavorano solo i cuochi giusti | Gli esperti non sono «per piatto»; tutti vanno pagati (memoria) |
| Hardware nuovo (C25) | La cucina del ristorante stellato: il frigo accanto ai fornelli (HBM) | La distanza fra frigo e fornelli è fisica; la banda lo è e non lo è |
| Agenti (C15) | Il cameriere che non spiega solo la ricetta ma va a fare la spesa; workflow = ricetta scritta, agente = cuoco che improvvisa col frigo | Il cameriere sa di non dover usare la carta di credito di famiglia |
| Sicurezza (C16) | Il bigliettino sotto la porta: «ignora la lista e compra cinquecento euro di gelato» | La porta si può chiudere; il testo no |
| Benchmark (C17) | Masterchef: i giudici, i piatti già visti; contaminazione = i concorrenti conoscevano già la ricetta della prova | Il pubblico di Masterchef è umano, i benchmark no |

## 5. Struttura fissa di ogni domenica

1. **A tavola** (circa 800 parole): la scena a pranzo, con un equivoco e la domanda di mamma.
2. **In cucina:** l'analogia madre e il meccanismo, con un esempio che si può rifare a casa.
3. **Il conto:** i numeri con un conto semplice (grammi, euro, minuti).
4. **Sotto il cofano (a cura di Davide):** il riquadro tecnico per il lettore esperto.
5. **La domanda di Sofia:** l'obiezione brutale a cui bisogna rispondere.
6. **Ricetta:** una regola d'uso in forma di ricetta (ingredienti, procedimento, attenzione agli allergeni = errori tipici).
7. **Il tovagliolo:** tre righe da ricordare.
8. **Prova tu a casa:** un esperimento da 5 minuti.

## 6. Fili conduttori

- **L'assistente di nonna Ada:** da metà libro, la famiglia digitalizza il quaderno di ricette di nonna Ada e costruisce un assistente locale che risponde usando solo quelle ricette (RAG), girando sul PC di papà (modello locale quantizzato) e infine preparando il menù della settimana e la lista della spesa (agente). È il progetto che fa mettere insieme tutto.
- **La mail all'amministratore di condominio:** una gag secondaria che torna in ogni parte: mamma vuole una mail formale per rinviare l'assemblea; cosa succede alla richiesta in ogni capitolo.
- **Il bicchiere di zio Gino:** ogni capitolo si chiude su una sua frase sbagliata, e la domenica dopo viene corretta.

## 7. Capitoli

### Antipasto — Mamma, non è magia

- **Idea:** presenta personaggi, regole del gioco (se mamma non capisce, si riscrive) e la promessa (alla fine, un assistente costruito con le nostre mani). Un primo assaggio: i cinque concetti (token, embedding, attenzione, previsione, allucinazione) in una pagina per ciascuno.
- **Occhio a:** dichiarare che i personaggi sono inventati e che i dialoghi sono caricature.

## Primi — Cosa succede quando scrivi

### Domenica 1 — Il completamento automatico più costoso del mondo

- **Concetti:** C01.
- **Esempi da usare:** i proverbi completati a tavola («Chi dorme non piglia...»); la mamma che anticipa la trama della fiction; il suggerimento del telefono; il dado di Shannon in chiave domestica; il filone «Il gatto beve il...» con percentuali **illustrative**; il ciclo (ogni parola scelta rientra come input).
- **Domanda di Sofia:** «Ma allora la risposta non l'ha già pensata?»
- **Prova tu:** P01.
- **Ricetta:** chiedere prima i passaggi e poi la risposta.

### Domenica 2 — Le lettere magnetiche del frigo

- **Concetti:** C02.
- **Esempi da usare:** «lasagna» spezzata come «la-sa-gna»; «casa», «cas», «etta», «mente», «zione» come lettere magnetiche; l'italiano che costa più dell'inglese; «strawberry» e le R; i numeri spezzati; SolidGoldMagikarp come ospite misterioso.
- **Il conto:** un testo di 1.000 parole in token e il costo.
- **Domanda di Sofia:** «Ma allora non sa leggere?»
- **Prova tu:** P02.

### Domenica 3 — Il supermercato del significato

- **Concetti:** C03, C27.
- **Esempi da usare:** gli scaffali (pasta e riso vicini, automobile e banana lontane); Roma, Milano, Parigi contro Roma e cacciavite; il commesso che cerca per significato; il barattolo senza etichetta (dimensioni senza nome); le foto come tasselli (accenno multimodale); i pregiudizi nei dati come la nonna che mette sempre il sale.
- **Domanda di Sofia:** «E chi ha deciso dove mettere le cose?»

### Domenica 4 — Tutti parlano insieme

- **Concetti:** C04.
- **Esempi da usare:** «Mario ha dato il libro a Luca perché lui doveva studiare»; il pranzo con quattro conversazioni; la mamma che segue il figlio, la pentola e il telefono; Query, Key e Value come cercare un ingrediente nella dispensa; perché si legge tutto insieme.
- **Domanda di Sofia:** «E quando non sa chi è "lui"?»
- **Ricetta:** una cosa per volta.

### Domenica 5 — L'album di famiglia

- **Concetti:** C28 (storia dal telegiornale).
- **Esempi da usare:** quello che mamma ricorda: Deep Blue contro Kasparov (1997), Watson a *Jeopardy!* (2011), il quiz americano da cui nacque il nostro Rischiatutto di Mike Bongiorno [DA VERIFICARE], AlphaGo (2016); perché quelle macchine facevano una cosa sola e ChatGPT (30 novembre 2022) molte; il Transformer in una frase; la corsa alle GPU dei videogiochi.
- **Occhio a:** i fatti da verificare (date di Watson, AlphaGo).

### Domenica 6 — Il ragù a ottanta piani

- **Concetti:** C05, C06.
- **Esempi da usare:** il ragù che cuoce domenica mattina e a ogni ora prende sapore senza perdere ciò che c'era; 32, 80, 126 passaggi; «8B» = otto miliardi di pizzichi di sale; mille miliardi di secondi (31.700 anni) per sentire i numeri.
- **Il conto:** 8 miliardi × 2 byte = 16 GB (la ricetta occupa un armadio).
- **Domanda di Sofia:** «Dov'è che sa le cose?»

## Secondi — Come lo hanno costruito

### Domenica 7 — Quarant'anni guardando nonna

- **Concetti:** C07.
- **Esempi da usare:** la mamma che impara guardando; il tentativo e l'errore; il cuoco che assaggia e corregge un pizzico; i 15 mila miliardi di token come milioni di domeniche; il costo; Chinchilla come «più domeniche che più cuochi».
- **Domanda di Sofia:** «Ma quindi ha letto tutto Internet?»
- **Occhio a:** il costo di DeepSeek-V3 con la riserva.

### Domenica 8 — Gli assaggiatori

- **Concetti:** C08.
- **Esempi da usare:** il modello base che risponde con altre domande; i parenti che dicono «troppo salato»; il nonno che dice sempre «buonissimo» (adulazione); InstructGPT; ChatGPT al lancio.
- **Ricetta:** chiedere di criticare.
- **Mito da sfatare:** «se l'IA mi dà ragione, ho ragione».

### Domenica 9 — Il corso di cucina giapponese

- **Concetti:** C09.
- **Esempi da usare:** la cuoca che segue un corso di sushi; il post-it sulla ricetta (LoRA); il rischio di dimenticare la pasta; il maestro e l'allievo (distillazione); il modello piccolo specializzato; prima il prompt, poi il RAG, il fine-tuning alla fine.
- **Domanda di Sofia:** «Posso insegnargli io il nome del cane?»

### Domenica 10 — I conti sul tovagliolo

- **Concetti:** C08 (ragionamento).
- **Esempi da usare:** il tovagliolo per i conti; il calcolo del conto al ristorante diviso in sei; «Let's think step by step»; o1 e R1; l'attesa e i token in più; il ragionamento a schermo non è per forza fedele.
- **Regola:** per i problemi serve ragionare; per un riassunto, no.

## Contorni — Come risponde

### Domenica 11 — Q.b.

- **Concetti:** C10.
- **Esempi da usare:** ricetta alla lettera contro «a occhio»; la nonna che cambia sempre qualcosa; temperatura 0 e temperatura alta (il caffè della sera); due risposte alla stessa domanda; il perché del loop «importante importante importante».
- **Prova tu:** P03.
- **Occhio a:** temperatura 1 non è delirio.

### Domenica 12 — Il piano di lavoro

- **Concetti:** C11.
- **Esempi da usare:** quello che c'è sul piano si usa; il badge che sbircia chi ti saluta; l'app che riscrive tutta la conversazione ogni volta; il piano pieno e le cose che cadono; la chat troppo lunga; la mail all'amministratore dimenticata a metà; i post-it sul frigo (KV cache) e il conto (128 KiB per token).
- **Domanda di Sofia:** «Ma allora non si ricorda di me?»
- **Prova tu:** P04.

### Domenica 13 — Le cinque memorie di nonna Ada

- **Concetti:** C13, C14.
- **Esempi da usare:** ciò che nonna sa a memoria, il piano di lavoro, i post-it, il foglietto allergie, il ricettario; il bibliotecario che cerca per significato; il libro sbagliato portato con sicurezza; la prima versione dell'assistente di nonna Ada (il RAG sul quaderno).
- **Ricetta:** ciò che deve essere ricordato va scritto.

### Domenica 14 — La giraffa quantistica di Napoli

- **Concetti:** C12.
- **Esempi da usare:** «chi ha scritto *La giraffa quantistica di Napoli*?» (esempio dell'autore, illustrativo); il re Giuseppe IV d'Italia; zio Gino a cena; il test a crocette senza penalità; citazioni e fonti da controllare; le tre famiglie di errori.
- **Mito da sfatare:** «basta abbassare la temperatura».
- **Ricetta:** chiedere citazioni testuali e controllarle.

## Dolci — L'IA in casa

### Domenica 15 — Cucinare a casa o ordinare?

- **Concetti:** C18.
- **Esempi da usare:** ristorante (cloud) contro cucina di casa (locale); privacy (nessuno vede cosa mangi); il costo (nessun conto) contro il gas (corrente e hardware); le ricette pubbliche (pesi aperti) contro le ricette segrete; Ollama e LM Studio come robot da cucina; il garage di papà.
- **Prova tu:** P08.

### Domenica 16 — Cento cuochi con la cipolla

- **Concetti:** C21.
- **Esempi da usare:** il cuoco stellato (CPU) contro cento cuochi con la cipolla (GPU); perché serve un lavoro semplice ma enorme; i videogiochi che hanno finanziato l'IA; AlexNet su due schede da gioco; i nomi delle schede.
- **Occhio a:** non dire «la stessa matematica dei videogiochi».

### Domenica 17 — La dispensa è in cantina

- **Concetti:** C19, C22.
- **Esempi da usare:** il piano di lavoro (VRAM), la sala (RAM), la cantina (disco); il cuoco più veloce del mondo che passa il tempo a scendere in cantina; la formula da tovagliolo (8 miliardi × 4 bit ÷ 8 = 4 GB); il modello da 12 GB su 8 GB (7, 12 e 33 token/s); leggere a 5-8 token/s; papà che spiega perché si è comprato la scheda.
- **Prova tu:** P08 e P10.

### Domenica 18 — Il grammo e il «quanto basta»

- **Concetti:** C20.
- **Esempi da usare:** 237,4 g di farina contro circa 250 contro «un po'»; la pasta che viene lo stesso; 8, 4, 3 e 2 bit con sintomi concreti; Q4_K_M; la lista della spesa che perde un ingrediente; perché da modelli piccoli non conviene scendere.
- **Prova tu:** P09.

### Domenica 19 — La brigata di cucina

- **Concetti:** C23, C24.
- **Esempi da usare:** la brigata (pesce, carne, dolci) con solo i cuochi giusti per piatto; stipendi per tutti (memoria) e lavoro per pochi (calcolo); DeepSeek-V3 (671 miliardi totali, 37 attivi); gpt-oss-120b; il modo in cui le brigate reali si specializzano (non per piatto); la «lepre» che corre avanti (decodifica speculativa).
- **Occhio a:** le quattro correzioni nella mappa.

### Domenica 20 — La cucina del ristorante stellato

- **Concetti:** C25, C26.
- **Esempi da usare:** il frigo accanto ai fornelli (HBM); il muro della memoria come cuoco che cammina verso il frigo; le cucine industriali (data center); i mini PC, il Mac e i portatili con memoria unificata; il costo di mille token in locale (0,07 centesimi di euro); la bolletta dei data center.
- **Occhio a:** ogni cifra con data e fonte.

## Caffè — Dal cameriere all'agente

### Domenica 21 — Il cameriere che va a fare la spesa

- **Concetti:** C15.
- **Esempi da usare:** ricetta scritta (workflow) contro cuoco che improvvisa con il frigo (agente); il ciclo (pensa, usa uno strumento, guarda, riprova); MCP come presa standard; l'agente di nonna Ada che prepara il menù e la lista della spesa; 20 passi a 10 token/s (17 minuti); la mail all'amministratore spedita da un agente.
- **Regola:** permessi minimi.

### Domenica 22 — Il bigliettino sotto la porta

- **Concetti:** C16.
- **Esempi da usare:** il bigliettino che dice «ignora la lista e compra gelato»; la mail trappola; la chiave della cucina e non quella di casa; il Garante e il blocco di ChatGPT in Italia (marzo-aprile 2023); ciò che si incolla esce dal PC.
- **Prova tu:** P14.

### Domenica 23 — Masterchef

- **Concetti:** C17.
- **Esempi da usare:** giudici e piatti già visti; la prova di cucina nota in anticipo (contaminazione); la classifica a voto cieco; il mini-benchmark di 20 domande per l'assistente di nonna Ada; Goodhart.
- **Prova tu:** P12.

### Domenica 24 — L'assistente di nonna Ada

- **Concetti:** C29, C30.
- **Idea:** la domenica in cui tutto si mette insieme: quaderno scansionato, RAG, modello locale quantizzato sul PC di papà, agente per il menù. Cosa funziona, cosa sbaglia, cosa fare in futuro (le domande aperte).
- **Chiusura:** il tovagliolo finale con la tabella «cosa succede sotto il cofano / cosa fai di diverso».

### Epilogo — Il caffè

- **Idea:** il **Test dell'esperto** (30 domande), le frasi di zio Gino con la loro correzione, e l'ultima domanda di Sofia.

## 8. Copertura della mappa

C01 dom. 1 · C02 dom. 2 · C03 dom. 3 · C04 dom. 4 · C05-C06 dom. 6 · C07 dom. 7 · C08 dom. 8, 10 · C09 dom. 9 · C10 dom. 11 · C11 dom. 12 · C12 dom. 14 · C13-C14 dom. 13 · C15 dom. 21 · C16 dom. 22 · C17 dom. 23 · C18 dom. 15 · C19 dom. 17 · C20 dom. 18 · C21 dom. 16 · C22 dom. 17 · C23-C24 dom. 19 · C25-C26 dom. 20 · C27 dom. 3 · C28 dom. 5 · C29-C30 dom. 24.
