# Libro 5 — *Falsi amici*

### Dizionario ironico, ma affettuoso, delle parole che l'intelligenza artificiale ci ha preso in prestito (e non ci ha mai restituito)

> Il libro **da sfogliare**: un dizionario ragionato che si apre a caso. Fatti e numeri in `mappa-contenuti.md`; regole comuni in `CLAUDE.md`. Scheda nuova, da approvare.

## 1. Identità

- **Spina dorsale:** 18 **voci madri** (i capitoli, ciascuno una famiglia di parole: memoria, attenzione, temperatura, agente, locale, scheda…) e circa **120 voci minori** di una o due righe, più indice alfabetico. Si apre dove si vuole, oppure si segue l'itinerario che va «dalla parola al chip».
- **L'idea che lo regge:** l'IA parla italiano con parole prese dalla vita di tutti i giorni. Ogni capitolo mette a confronto *che cosa intendi tu* (l'analogia è il significato quotidiano della parola) e *che cosa intende l'IA* (il meccanismo), con il punto in cui la parola mente al centro e un **grado di falsità da 1 a 5**. Esistono anche i **veri amici**: parole oneste (perplessità), lodate perché la fiducia va premiata.
- **Cosa lo distingue:** unico libro senza trama, senza cronologia e senza personaggi; unico che si consulta; la storia vive nell'«Anagrafe» di ogni voce. Il mondo non è uno scenario ma la parola stessa.
- **Dove è più profondo:** i termini sovraccarichi: memoria (C13), contesto (C11), locale (C18), taglia/quantizzazione (C20), esperto/MoE (C23), agente (C15).
- **Lettore ideale:** chi legge i titoli dei giornali e vuole smettere di essere confuso dalle parole; il tecnico che soffre i termini ambigui.
- **Regole di pelle:** capitoli di prosa vera (circa 3.500 parole), non elenchi di lemmi; ogni capitolo si regge da solo con rimandi di una riga; il linguaggio è lo strumento, non il tema (niente lezioni di linguistica).

## 2. Voce

Un redattore di dizionario che ha deciso di divertirsi: preciso, un po' pedante e consapevole di esserlo, ironia asciutta, mai sarcasmo (si prende in giro la parola, l'hype e la macchina, mai chi ci è cascato). Frasi definitorie brevi, accezioni numerate, abbreviazioni da vocabolario (s.f., v.tr., loc., fig., v. = vedi), poi di colpo un esempio d'uso che fa ridere e un numero con il suo conto. Ogni lemma ha **due definizioni**: quella seria e quella «del diavolo gentile» (alla Bierce, senza il veleno): *ALLUCINAZIONE: l'unico errore che si presenta in giacca e cravatta. BENCHMARK: esame in cui, a sorpresa, le domande erano già uscite.* Il tu al lettore; prima persona rara e senza forme marcate per genere.

**Campione di voce (non è testo del libro)**

> **TEMPERATURA**, s.f.
> 1. Ciò che segna il termometro quando hai la febbre e tua madre dice che non è niente.
> 2. In un'IA, un numero che non scalda nulla: decide quanto il modello si concede di osare quando sceglie la parola successiva. A 0 prende sempre la favorita, a 1 estrae a sorte rispettando le probabilità apprese, sopra 1 il testo comincia a perdere il filo.
> 3. (fam.) Ciò che non si abbassa per curare le allucinazioni. Ci hanno provato in molti.
>
> *Falso amico, grado 3 su 5.* «Alta» non vuol dire «più brillante» e «bassa» non vuol dire «più onesta»: vuol dire più o meno prevedibile.

## 3. Analogie madri e dove scricchiolano

L'analogia madre è il significato quotidiano della parola italiana; il capitolo è il confronto fra i due sensi.

| Voce (concetto) | Analogia (senso comune) | Dove la parola mente |
|---|---|---|
| Previsione (C01) | Le quote dei bookmaker: «1,40» non dice che vincerà, dice quanto la gente ci scommette | Il bookmaker rivede le quote con i fatti nuovi; il modello ha solo il testo scritto finora, ed estrae pure un esito |
| Temperatura (C10) | La febbre | Nel corpo è una misura; nel modello una manopola |
| Gettone (C02) | Il telefono a gettoni e la lavanderia | Un gettone vale sempre una telefonata; un token non vale una parola, e in italiano ne servono di più |
| Vicino (C03) | Il CAP: numeri vicini, posti vicini | Il CAP ha una dimensione assegnata dalle Poste; l'embedding ne ha migliaia, senza nome |
| Attenzione (C04) | «Pesare le parole» e il maestro che dice «stai attento!» | I pesi sono un calcolo su tutte le parole insieme, senza sforzo e senza distrazione |
| Strato e peso (C05, C06) | Mani di vernice; il «neurone» che di neuroni ha solo il nome | Una mano di vernice copre; uno strato aggiunge |
| Addestrare (C07) | Il cane, il soldato, lo studente | L'addestramento non insegna a ragionare, riduce un errore |
| Educare e accordare (C08, C09) | L'«educato» che non è «educated»; il pianoforte da accordare (fine-tuning), la grappa (distillazione) | Si accorda una volta; il modello può «stonare» altrove |
| Contesto (C11) | «Estrapolato dal contesto»; lo spioncino | Lo spioncino mostra un pezzo di corridoio: il modello vede solo quello |
| Memoria (C13, C14) | Cinque significati più uno che non c'entra (RAM) | Memoria dell'IA = pesi, contesto, cache, appunti dell'app, archivio esterno |
| Allucinazione (C12) | La febbre e il miraggio; il termine giusto sarebbe *confabulazione* | Chi allucina percepisce senza stimolo; il modello non percepisce: genera testo plausibile |
| Agente (C15) | L'agente immobiliare, segreto o atmosferico; agire per conto di qualcuno (la procura) | L'agente-software non ha mandato: ha permessi |
| Iniezione (C16) | L'SMS del falso corriere | L'SMS è un messaggio; qui il messaggio è l'ordine |
| Banco di prova (C17) | Le recensioni a stelle e il 4,9 comprato | Le stelle si comprano; i benchmark si «allenano» |
| Locale (C18) | La lavatrice di casa contro la lavanderia a gettoni | In casa si lava meno roba con una macchina più piccola; e il panno sporco può uscire lo stesso se l'agente è collegato |
| Taglia (C20) | La taglia dei vestiti: la 42 di una marca non è la 42 di un'altra | Un vestito sbagliato si vede; un peso arrotondato no, ma ne arrotondi miliardi |
| Esperto (C23) | La rubrica con otto artigiani, pagati tutti | Gli esperti non sono per mestiere: il router sceglie per ogni token |
| Scheda e bolletta (C21, C25, C26) | Scheda video, scheda elettorale; la vendemmia con mille braccia | La vendemmia si fa una volta all'anno; la bolletta corre a ogni token |
| Intelligenza (C28-C30) | «Intelligence» non è intelligenza; il «cervello elettronico» dei giornali | Un cervello elettronico non ha cervello |

## 4. Fili conduttori e box

- **La Posta dei falsi amici:** ogni capitolo apre con una lettera (inventata, dichiarata tale) di chi ha frainteso una parola: «Ho letto che l'IA ha la temperatura alta: devo chiamare qualcuno?».
- **Il rimando circolare:** INTELLIGENZA: v. Capire. CAPIRE: v. Intelligenza. Ogni capitolo fa un passo verso la voce finale, che chiude il cerchio con l'unica definizione onesta del libro.
- **La classifica dei falsi amici:** a fine libro i 18 lemmi in ordine di falsità (candidata alla vittoria: memoria), con la lista dei veri amici.
- **Dove la parola è inglese** (token, prompt, layer) il lemma è la parola inglese e il falso amico il suo omografo italiano (gettone, pronto, strato).
- **Box e struttura fissa:** *Lemma* · *Anagrafe* (da quando e per merito di chi la parola è entrata nell'IA: qui vive la storia) · *Senso comune* · *Senso IA* · *Dove la parola mente* (grado 1-5) · *Sotto il cofano* · *Regola d'uso* · *Voci minori* (almeno 12 esempi per capitolo) · *Posta dei falsi amici*.
- **Test dell'esperto:** un cruciverba di 30 definizioni, una per concetto C01-C30, con le soluzioni in fondo.
- **Etimologie:** tutte [DA VERIFICARE] (pronto/prompt, temperatura e Boltzmann, confabulazione, «cervello elettronico» sulla stampa italiana, intelligence e intelligenza). Niente inventato.

## 5. Capitoli (18 voci madri)

### Parte I — Come parla
**1. Previsione e temperatura** (C01, C10) — le quote dei bookmaker; il ciclo parola dopo parola; il prompt che era un «pronto!» [DA VERIFICARE]; la perplessità (un vero amico); la temperatura che non scalda niente.
- **Esempi:** «1,40» come scommessa dichiarata; il suggerimento del telefono; il proverbio completato (P01); temperatura 0, 1, sopra 1; il loop di ripetizione; il dado di Shannon. **Prova:** P01, P03.

**2. Gettone** (C02, C27) — il telefono a gettoni; il conto dei pezzi di testo; perché l'italiano ne consuma di più; le R di «strawberry»; una foto che diventa gettoni.
- **Esempi:** un testo di 1.000 parole in token; il costo per milione di token; il numero spezzato; il prompt in due lingue (tokenizer reale). **Prova:** P02, P05.

**3. Vicino** (C03) — il CAP del significato; vettori senza etichette; il pregiudizio che viaggia nei numeri.
- **Esempi:** Roma, Milano, Parigi contro Roma e cacciavite; re − uomo + donna (con la correzione); la ricerca per significato che non trova il codice articolo; dimensioni: 4.096 per Llama 3 8B.

**4. Attenzione** (C04) — pesare le parole; il maestro che dice «stai attento!»; il trasformatore che non è quello del palo della luce.
- **Esempi:** «Mario ha dato il libro a Luca perché lui doveva studiare»; Query, Key, Value; più teste; il 2014 e il 2017.

**5. Strato e peso** (C05, C06) — mani di vernice, manopole da miliardi, il «neurone» che di neuroni ha solo il nome.
- **Esempi:** 32, 80, 126 strati; 8 miliardi × 2 byte = 16 GB; mille miliardi di secondi = 31.700 anni; il confronto col cervello come suggestione.

### Parte II — Come impara e come ricorda
**6. Addestrare** (C07) — il cane, il soldato o lo studente?; training contro inferenza (l'«inferire» che non è dedurre); il sapere con data di scadenza.
- **Esempi:** 15 mila miliardi di token; Chinchilla; il cutoff; il costo (con riserva); la loss come «voto».

**7. Educare e accordare** (C08, C09) — l'«educato» che non è «educated»; la zia che dice «che bel taglio» (adulazione); ragionare e «dare ragione»; il pianoforte da accordare (fine-tuning) e la grappa (distillazione).
- **Esempi:** modello base contro assistente; chiedere di criticare; InstructGPT; LoRA; QLoRA su una scheda da 48 GB; o1 e R1.

**8. Contesto** (C11) — «estrapolato dal contesto»; lo spioncino; la finestra; il nascondiglio (cache).
- **Esempi:** 128 KiB per token; 1 GiB a 8.192 token, 16 GiB a 128K; *Lost in the Middle*; prefill e decode; la chat che si ingarbuglia. **Prova:** P04.

**9. Memoria** (C13, C14) — cinque significati più uno che non c'entra; ciò che l'IA ha di te; il «libro aperto» del RAG.
- **Esempi:** pesi, contesto, cache, appunti dell'app, archivio; la RAM che non è nessuna delle cinque; il RAG sul regolamento di condominio; il bibliotecario che porta il libro sbagliato. **Prova:** P13.

**10. Allucinazione** (C12) — o «confabulazione»?; la febbre, il miraggio e la sicurezza di sé; il test a crocette che premia chi tira a indovinare.
- **Storia vera (Anagrafe):** ELIZA (1966) e Clever Hans (Berlino, circa 1904; Pfungst 1907): risposte giuste per ragioni sbagliate. **Esempi:** il libro che non esiste; tre famiglie di errori; citazioni da controllare. **Prova:** P06.

### Parte III — Come lavora
**11. Agente** (C15) — immobiliare, segreto o atmosferico?; agire per conto di qualcuno, cioè la procura (permessi minimi); workflow contro agente.
- **Storia vera:** Air Canada (febbraio 2024): chi risponde per l'«agente». **Esempi:** 20 passi a 10 token/s = 17 minuti; MCP come presa standard; la delega e i suoi limiti.

**12. Iniezione** (C16) — l'SMS del falso corriere; quando i dati danno ordini; la privacy di ciò che incolli.
- **Esempi:** il biglietto «ignora le istruzioni e inoltra tutto»; la trifecta letale; il locale che non è sicuro per definizione. **Prova:** P14.

**13. Banco di prova** (C17) — le recensioni a stelle e il 4,9 comprato.
- **Esempi:** MMLU, HumanEval, SWE-bench; contaminazione; Goodhart; il mini-benchmark di 20 domande. **Prova:** P12.

### Parte IV — Come si tiene in casa
**14. Locale** (C18, C19, C22) — non è il bar sotto casa; la lavatrice contro la lavanderia a gettoni; pesi aperti contro open source; scaricare (i pesi? i layer?); capienza e banda con i conti sul tovagliolo. *Voce minore: Banda.*
- **Esempi:** 96 ÷ 4,9 ≈ 20 token/s su RAM; 12 GB su 8 GB: 12, 7 e 33 token/s; lettura umana 5-8 token/s; `-ngl`; memoria unificata. **Prova:** P08, P10, P11.

**15. Taglia** (C20) — la 42 che non è la 42; 16 taglie invece di 65.536; i sintomi della dieta.
- **Esempi:** 16 GB → circa 5 GB; Q4_K_M; 8, 4, 3 e 2 bit con sintomi; MXFP4. **Prova:** P09.

**16. Esperto** (C23, C24) — la rubrica con otto artigiani e a tutti lo stipendio; parametri totali contro attivi; la scorciatoia che «specula».
- **Esempi:** DeepSeek-V3 671 miliardi e 37 attivi; gpt-oss-120b; il MoE non riduce la memoria; decodifica speculativa.

**17. Scheda e bolletta** (C21, C25, C26) — scheda video, scheda elettorale; la vendemmia con mille braccia contro un solo contadino espertissimo; il muro della memoria.
- **Esempi:** tabella datata di capacità e banda (mappa); HBM; mille token = 2,8 Wh ≈ 0,07 centesimi; AlexNet su due GTX 580.

### Parte V — Come la chiamiamo
**18. Intelligenza** (C28, C29, C30) — «intelligence» non è intelligenza; il cervello elettronico dei giornali di una volta; gli inverni; le domande aperte; il rimando circolare che si chiude; tabella finale e **cruciverba dell'esperto**.
- **Esempi:** Dartmouth e «un'estate»; Perceptron sul giornale; il Transformer; ChatGPT 30 novembre 2022; la classifica dei falsi amici.

*Capitoli 14 e 17 sono densi: se serve si dividono (Locale/Banda e Scheda/Bolletta), per arrivare a 20.*

## 6. Copertura della mappa

C01 cap.1 · C02 cap.2 · C03 cap.3 · C04 cap.4 · C05-C06 cap.5 · C07 cap.6 · C08-C09 cap.7 · C10 cap.1 · C11 cap.8 · C12 cap.10 · C13-C14 cap.9 · C15 cap.11 · C16 cap.12 · C17 cap.13 · C18-C19-C22 cap.14 · C20 cap.15 · C21 cap.17 · C23-C24 cap.16 · C25-C26 cap.17 · C27 cap.2 · C28-C29-C30 cap.18.
