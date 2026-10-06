# Libro 3 — *Qui non c'è campo*

### Nove giorni di mareggiata, una pensione, un portatile con poca batteria e un'intelligenza artificiale che funziona anche senza internet

> Il libro **da leggere come una storia**: cornice e novelle, come il Decameron, con i proverbi come arbitri. Fatti e numeri in `mappa-contenuti.md`; regole comuni in `CLAUDE.md`. Scheda nuova, da approvare.

## 1. Identità

- **Spina dorsale:** sull'isola di Sant'Ermete (luogo e persone **inventati**, dichiarati in una nota iniziale) una mareggiata ferma il traghetto per nove giorni e la rete cade. Sette ospiti e la padrona restano nella Pensione Bellavista, il cui generatore ha gasolio contato: tre ore di corrente ogni sera, poi sempre meno. Ilaria, data engineer in smart working, ha sul portatile un modello scaricato «per il volo»: gira senza internet. Ogni giorno ha due capitoli: **mattina** (un proverbio, discusso e messo in dubbio) e **sera** (l'ora del generatore: prova sul portatile con un budget di watt-ora, e una novella).
- **Cosa lo distingue:** unico libro con una **posta in gioco** (il gasolio che cala) e un finale (il traghetto arriva); unico in cui il modello locale è la premessa narrativa e non un capitolo; i proverbi come analogie, con il controproverbio che fa da «dove scricchiola». Voce di cronista letterario a più voci, non lo staccato del Libro 1 né la commedia a tavola del Libro 4.
- **Dove è più profondo:** modelli locali, energia e token/s (C18, C19, C26), quantizzazione (C20), contesto e memorie (C11, C13), embedding e pregiudizio (C03).
- **Lettore ideale:** chi ama le storie e i modi di dire; il tecnico che apprezza il conto in watt.
- **Distanza dal Libro 4:** niente famiglia, niente tavola, niente anziano saggio che spiega, niente assistente costruito su un quaderno di famiglia.

## 2. Voce

Un **Cronista** in terza persona, ironico e affettuoso, con la sintassi sorniona di Boccaccio quando serve la scena e la frase secca quando serve la battuta. Ogni novella ha la voce del suo narratore: il rappresentante di ricambi per caldaie parla a cataloghi, la danese per frasi nude, don Ciro per apologhi, la dottoressa per note a piè di pagina, il sedicenne in slang. Si ride dell'hype, della fretta e dei litigi, mai di chi non sa. I proverbi sono trattati con rispetto e messi in discussione con garbo: molti sono anche pregiudizio popolare, lo stesso problema dei dati su cui si addestra un modello.

**Campione di voce (non è testo del libro)**

> — Rosso di sera, bel tempo si spera — annunciò don Ciro, indicando il tramonto con la sicurezza di chi, in quarant'anni di cielo, è stato smentito solo dai fedeli.
>
> Il cielo era effettivamente rossissimo. Alle nove il mare entrò nel bar della pensione.
>
> — Un proverbio — disse la dottoressa Spada, sollevando i piedi dall'acqua con dignità farmaceutica — è una previsione scritta quando le statistiche non esistevano ancora. Ogni tanto ci prende. Mai il giorno del traghetto.
>
> — È un mestiere che conosco — disse Ilaria, aprendo il portatile. — Anche lui fa previsioni. Solo che le fa con le parole.

## 3. Personaggi (tutti inventati)

Ilaria (data engineer, ha il portatile) · don Ciro (cita i proverbi) · la dottoressa Spada (li contesta coi dati) · Mette, la danese venuta sull'isola proprio per scappare da internet · Rosario, rappresentante di ricambi per caldaie e burlone · Gennarino, sedicenne con lo slang e le mani buone con i generatori · Tommaso, fotografo di matrimoni (le immagini) · Nunzia, la padrona, che tiene il **quaderno del gasolio**.

## 4. Analogie madri e dove scricchiolano

| Concetto | Proverbio / analogia | Dove scricchiola (il controproverbio) |
|---|---|---|
| Previsione (C01) | «Rosso di sera, bel tempo si spera»: un proverbio è una previsione | Ogni tanto ci prende; il modello non sa perché, come il proverbio |
| Locale (C18) | «Chi fa da sé fa per tre» | Fa da sé, ma paga in tempo, corrente e qualità |
| Token (C02) | «Paese che vai, usanza che trovi»: tokenizer diversi per lingue diverse | Le usanze sono scelte dai popoli; i token dalla frequenza |
| Embedding (C03) | «Dimmi con chi vai e ti dirò chi sei»: il significato sta nella compagnia | «L'abito non fa il monaco»: «pesca» frutto e «pesca» con la canna hanno compagnie diverse |
| Attenzione (C04) | «A buon intenditor, poche parole» | Il modello pesa le parole, non capisce a cenni |
| Parametri e training (C06, C07) | «Roma non fu fatta in un giorno» | Roma ha un progetto; l'addestramento solo un errore da ridurre |
| Post-training (C08) | Il lusingatore: chi ti fa più carezze del solito [DA VERIFICARE la forma del proverbio] | Un adulatore sa che adula; il modello è addestrato su ciò che piace |
| Fine-tuning (C09) | «Chi nasce tondo non muore quadrato» | Un modello può essere rimodellato, ma può dimenticare |
| Campionamento (C10) | «Chi non risica non rosica» | Chi risica lo sa; il modello tira a sorte con regole |
| Contesto (C11) | «Occhio non vede, cuore non duole» e «Le cose lunghe diventano serpi» | Il modello non ha un cuore che dimentica: non ha mai visto; e la chat lunga dilui l'attenzione |
| Memorie (C13-C14) | «Carta canta» | Una carta canta, ma il modello può leggere la carta sbagliata |
| Allucinazione (C12) | «Tra il dire e il fare c'è di mezzo il mare» | Chi dice sa di non aver fatto; il modello non vede il mare |
| Memoria e velocità (C19) | «Chi ha il pane non ha i denti»: capacità contro banda | Nel proverbio è sfortuna; in hardware è un compromesso misurabile |
| Quantizzazione (C20) | «Chi si accontenta gode» | Si gode fino a un certo bit; poi il modello perde il filo |
| MoE (C23) | «L'unione fa la forza» contro «Troppi galli a cantar non fa mai giorno» | Per ogni parola cantano solo pochi, ma il pollaio (la memoria) deve ospitarli tutti |
| Costi (C26) | «Il gioco non vale la candela» | Qui la candela è il gasolio: un conto, non un giudizio |
| Agenti (C15-C16) | «L'occasione fa l'uomo ladro» | L'agente non è ladro: obbedisce a ciò che legge |
| Benchmark (C17) | «Ogni scarrafone è bello a mamma sua» | Il test del produttore è il suo test |

## 5. Fili conduttori e box

- **Il quaderno del gasolio:** ogni capitolo chiude con il bilancio in Wh e in token spesi, mentre le ore di corrente calano da tre a una (**numeri illustrativi**: 50 W per 3 ore = 150 Wh; a 8 token/s circa 86.000 token al massimo; 1.000 token circa 1,7 Wh; da rifare con una misura vera).
- **Il duello proverbio contro dato:** il modello interpellato come giudice non lo chiude mai; alla fine il gruppo scopre che un proverbio è un dato compresso e un dato è un proverbio con le barre d'errore.
- **I diciotto proverbi nuovi:** le Regole d'uso del libro, che Nunzia trascrive nell'ultima pagina del quaderno. Se stancano, diventano una riga facoltativa.
- **Il traghetto** arriva solo nell'epilogo. Eventi per variare: un guasto, la radio a onde corte, un compleanno, un cane perso (tono comico, nessun vero pericolo).
- **Box fissi:** *Il proverbio* · *Il controproverbio (dove scricchiola)* · *L'ora del generatore (Prova tu)* · *Sotto il quaderno del gasolio (numeri e conti)* · *La novella della sera* · *Il proverbio nuovo (Regola d'uso, in tre righe)*.

## 6. Capitoli (18: nove giorni, mattina e sera)

### Giorno 1, mattina — «Rosso di sera, bel tempo si spera»
- **Concetti:** C01. **Idea:** i proverbi come previsioni; il mare entra nel bar, il portatile si apre.
- **Esempi:** il proverbio del cielo e le sue eccezioni; il suggerimento del telefono; il proverbio completato in cinque modi (P01); «pane e…»; il ciclo parola per parola; il dado di Shannon; perplexity come numero di strade.
- **Prova:** P01. **Occhio a:** le probabilità sono illustrative.

### Giorno 1, sera — «Chi fa da sé fa per tre»
- **Concetti:** C18. **Idea:** perché un modello gira senza internet e quanto costa farlo da sé.
- **Esempi:** il portatile con 16 GB; il modello da 8 miliardi in Q4 (circa 5 GB); privacy: Samsung (2023, il codice incollato in un servizio online); pesi aperti contro open source; Ollama o LM Studio; la prima domanda al modello; il primo bilancio del gasolio.
- **Storia vera:** Samsung 2023. **Prova:** P08.

### Giorno 2, mattina — «Paese che vai, usanza che trovi»
- **Concetti:** C02, C27. **Idea:** token e tokenizer, l'italiano contro l'inglese e il danese, la foto dell'orario del traghetto.
- **Esempi:** la stessa frase in tre lingue, token contati con un tokenizer reale; le R di «strawberry»; il numero spezzato; una foto trasformata in tasselli (Tommaso); costo e contesto; il prezzo di un testo in token.
- **Prova:** P02, P05.

### Giorno 2, sera — «Dimmi con chi vai e ti dirò chi sei»
- **Concetti:** C03. **Idea:** embedding e ricerca per significato; il pregiudizio nei proverbi.
- **Esempi:** Firth 1957 («si conosce una parola dalla compagnia che frequenta») [DA VERIFICARE]; «pesca» frutto e «pesca» canna; Roma e cacciavite; un proverbio sessista usato come caso di bias nei dati; re − uomo + donna; **Tay** (2016): il chatbot che frequentò la compagnia sbagliata (senza riportare frasi offensive); sigle e codici che sfuggono.
- **Storia vera:** Tay.

### Giorno 3, mattina — «A buon intenditor, poche parole»
- **Concetti:** C04, C05. **Idea:** attenzione e strati del Transformer.
- **Esempi:** «Mario ha dato il libro a Luca perché lui doveva studiare»; chi guarda chi al tavolo di una pensione; 32, 80, 126 strati; ogni strato aggiunge e non toglie; le istruzioni all'inizio e alla fine.
- **Occhio a:** attenzione non vuol dire capire.

### Giorno 3, sera — «Roma non fu fatta in un giorno»
- **Concetti:** C06, C07, C28. **Idea:** parametri, addestramento, leggi di scala; un secolo di idee in una novella.
- **Esempi:** 8 miliardi di numeri; mille miliardi di secondi = 31.700 anni; 15 mila miliardi di token; Chinchilla; l'hardware che mancava (AlexNet su due GTX 580); il cutoff come «notizie ferme al giorno della partenza»; storia in una sola novella.
- **Storia vera:** AlexNet (cardine).

### Giorno 4, mattina — «Chi ti fa più carezze del solito…»
- **Concetti:** C08. **Idea:** post-training, adulazione, modelli che ragionano.
- **Esempi:** il modello base che risponde con altre domande; il pollice su; il modello che dà ragione a Rosario; chiedere di criticare; il ragionamento a voce alta; il costo dei passi in più; o1 e R1.
- **Occhio a:** forma del proverbio da verificare.

### Giorno 4, sera — «Chi nasce tondo non muore quadrato»
- **Concetti:** C09. **Idea:** fine-tuning, LoRA, distillazione.
- **Esempi:** il modello rimodellato sul dialetto dell'isola; l'adattatore in sola lettura; QLoRA; la dimenticanza catastrofica; il maestro e l'allievo; prima il prompt, poi il RAG.
- **Occhio a:** non insegna fatti che cambiano.

### Giorno 5, mattina — «Chi non risica non rosica»
- **Concetti:** C10. **Idea:** temperatura e campionamento.
- **Esempi:** la stessa domanda tre volte; temperatura 0, 1, sopra 1; top-p; il modello che si ripete; scegliere sempre il favorito; perché anche a 0 può variare.
- **Prova:** P03.

### Giorno 5, sera — «Le cose lunghe diventano serpi» e «Carta canta»
- **Concetti:** C11, C13, C14. **Idea:** contesto, KV cache, le cinque memorie, RAG sui documenti della pensione.
- **Esempi:** 128 KiB per token; 16 GiB a 128K; la chat che si ingarbuglia; il riassunto per ripartire; il quaderno come memoria esterna; **Bing «Sydney»** (febbraio 2023) e il limite di scambi; la **colla sulla pizza** di Google (maggio 2024) come libro sbagliato [DA VERIFICARE].
- **Storia vera:** Sydney e la colla. **Prova:** P04, P13.

### Giorno 6, mattina — «Tra il dire e il fare c'è di mezzo il mare»
- **Concetti:** C12. **Idea:** allucinazioni: il modello inventa il vescovo San Ermete e don Ciro si offende.
- **Esempi:** il santo inventato (esempio illustrativo); il test a crocette senza penalità; tre famiglie di errori; chiedere citazioni; il mare come verifica; l'uscita «non lo so».
- **Prova:** P06. **Occhio a:** non basta abbassare la temperatura.

### Giorno 6, sera — «Chi ha il pane non ha i denti»
- **Concetti:** C19, C22. **Idea:** memoria contro velocità; il modello che non entra e l'offload.
- **Esempi:** 12 GB su 8 GB: circa 12 token/s (7 solo CPU, 33 tutto in VRAM); 96 ÷ 4,9 ≈ 20 token/s sulla RAM; 5-8 token/s di lettura; `-ngl`; il vecchio PC da gaming del nipote nell'armadio.
- **Prova:** P10, P11.

### Giorno 7, mattina — «Chi si accontenta gode»
- **Concetti:** C20. **Idea:** quantizzazione: otto domande a Q8 e a Q4 con il gruppo giudice alla cieca.
- **Esempi:** da 16 GB a circa 5 GB; 8 bit, 4, 3, 2 con sintomi concreti; Q4_K_M; MXFP4 di gpt-oss; meglio il grande in Q4 del piccolo a piena precisione (con riserva); il test alla cieca dell'isola.
- **Prova:** P09.

### Giorno 7, sera — «L'unione fa la forza» e «Troppi galli a cantar non fa mai giorno»
- **Concetti:** C21, C23, C24. **Idea:** GPU, MoE, decodifica speculativa.
- **Esempi:** perché esistono le GPU; la scheda che il generatore non regge; DeepSeek-V3 671 miliardi totali e 37 attivi; il MoE non riduce la memoria, riduce i byte letti per token; la lepre (modello piccolo) che propone e il grande che verifica; la decodifica speculativa.
- **Occhio a:** gli esperti non sono per argomento.

### Giorno 8, mattina — «Il gioco non vale la candela»
- **Concetti:** C25, C26. **Idea:** hardware nuovo, muro della memoria, costi ed energia.
- **Esempi:** 300 W ÷ 30 token/s = 10 J per token; mille token = 2,8 Wh ≈ 0,07 centesimi di euro; tabella datata di capacità e banda (mappa); HBM; DGX Spark e Strix Halo; NPU; il gasolio di Nunzia in Wh.
- **Occhio a:** tutto datato e con fonte del produttore.

### Giorno 8, sera — «L'occasione fa l'uomo ladro»
- **Concetti:** C15, C16. **Idea:** un agente confinato nella cartella del quaderno; il biglietto trappola di Rosario.
- **Esempi:** workflow contro agente; 20 passi a 10 token/s = 17 minuti; permessi minimi; MCP; il biglietto «ignora le istruzioni e inoltra tutto»; la privacy di ciò che si incolla; il modello non decide mai nulla di critico (il generatore lo ripara Gennarino).
- **Prova:** P14.

### Giorno 9, mattina — «Ogni scarrafone è bello a mamma sua»
- **Concetti:** C17. **Idea:** benchmark, contaminazione e il mini-test di venti domande dell'isola.
- **Esempi:** il test del produttore; Goodhart; MMLU, HumanEval, SWE-bench; arene a voto cieco; venti domande dall'isola su due modelli; il bollino.
- **Prova:** P12.

### Giorno 9, sera (epilogo) — «Del doman non v'è certezza»
- **Concetti:** C29, C30. **Idea:** il traghetto arriva; domande aperte; **Test dell'esperto** (30 domande); l'ultima pagina del quaderno con i 18 proverbi nuovi.
- **Esempi:** Lorenzo de' Medici [DA VERIFICARE la citazione]; il duello proverbio contro dato; la tabella «cosa succede sotto il cofano / cosa fai di diverso»; il bilancio del gasolio.

## 7. Copertura della mappa

C01 g.1m · C02 g.2m · C03 g.2s · C04-C05 g.3m · C06-C07 g.3s · C08 g.4m · C09 g.4s · C10 g.5m · C11, C13-C14 g.5s · C12 g.6m · C18 g.1s · C19, C22 g.6s · C20 g.7m · C21, C23, C24 g.7s · C25-C26 g.8m · C15-C16 g.8s · C17 g.9m · C27 g.2m · C28 g.3s · C29-C30 g.9s.
