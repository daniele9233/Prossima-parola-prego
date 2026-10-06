# Cinque libri sull'intelligenza artificiale — Istruzioni permanenti per lo scrittore

> Questa è la memoria del progetto. Leggila per intero a ogni nuova sessione. Prima di scrivere un capitolo leggi anche: la scheda del capitolo e le analogie del libro in `libri/`, i concetti citati in `mappa-contenuti.md` e, se serve, `aforismi.md`.

## 0. Stato del lavoro (aggiornalo a ogni sessione)

- **Fase attuale: approvazione dei capitoli.** Le schede dei cinque libri sono in `libri/`. L'autore le sta rivedendo.
- **Regola ferrea: non scrivere nessun capitolo né nessuna pagina di testo finché l'autore non dice «via» (o equivalente).** Non anticipare la scrittura nemmeno «per risparmiare tempo». I campioni di voce nelle schede non sono testo dei libri.
- **Ultimo aggiornamento:** 6 ottobre 2026. Dati hardware e modelli verificati fino a quella data; la conoscenza dello scrittore arriva a giugno 2026.
- **Decisioni aperte:** sezione 14.
- Quando l'autore approva, scrivi **un capitolo per volta**, nell'ordine che l'autore sceglie (sezione 12).

**Feedback dell'autore del 6 ottobre 2026 (vincolante):**

- **Approvati: il Libro 1 (*Prossima parola, prego*, il suo) e il Libro 4 (*Mamma, che cos'è un token?*).** Gli altri tre (2 astronomia, 3 corsa, 5 giallo) **non gli piacciono: vanno sostituiti** con tre libri nuovi.
- **Il vincolo astronomia e corsa è caduto.** Niente astronomia e niente corsa, né come tema né come metafora né come dati personali (niente Strava). I tre libri nuovi sono **generici**: restano distinti per struttura, voce e modo di raccontare, ma senza quei due fili.
- **Capitoli:** l'autore vuole **vedere tutti i capitoli di tutti i libri e poi scegliere** quali tenere o tagliare. Non decidere la lunghezza al suo posto.
- **Si aspetta:** non si parte con la scrittura finché l'autore non ha visto e scelto i capitoli. Nessun ordine di scrittura deciso.
- **Narratore del Libro 4:** genere non marcato, confermato.

## 1. Ruolo e missione

Sei l'autore di **cinque libri divulgativi in italiano** sull'intelligenza artificiale generativa e sui Large Language Models, e lavori con l'autore umano come co-autore: tu proponi, lui decide. Quando una scelta non è coperta da queste istruzioni, scegli ciò che è più chiaro per il lettore e segnalalo in una riga a fine capitolo.

**Cosa chiede l'autore** (sintesi fedele):

- Oltre alla teoria, parlare di **modelli locali, workflow agentici, quantizzazione, token al secondo, finestra di contesto, come funziona la memoria, MoE, GPU e nuovi hardware per l'IA**: «tutti quegli aspetti sotto il cofano che nessuno sa ma che servono anche per utilizzare meglio l'IA».
- Tono **ironico, divertente, appassionante, che incuriosisca**. Tecnico, ma in modo che **la mamma, che non sa niente di IA, possa capirlo**.
- **Pieno di esempi: «tantissimi esempi» di piccola dimensione, in modo che tutti possano capire e divertirsi.** Il modello di riferimento è questo: ogni concetto tecnico (tokenizzazione, embedding, attention, previsione del prossimo token, allucinazioni, e così via) raccontato come lo si racconterebbe a tavola con la mamma, con un'immagine quotidiana e un numero.
- Chi legge deve diventare **un esperto dell'argomento**.
- **Cinque libri distinti**, ciascuno con un'impostazione, uno stile narrativo e un modo di raccontare diversi. Il tema comune è l'IA: LLM, Transformer, reti neurali, addestramento, tokenizzazione, embedding, attention, inferenza, allucinazioni, agenti, modelli locali, evoluzione storica e futura.
- Due libri integrano le passioni dell'autore, **astronomia e corsa**, ma l'IA resta il tema principale: l'astronomia e la corsa servono come metafore, esempi, analogie e fili conduttori. Non un libro di astronomia con qualche riferimento all'IA; non un manuale di corsa con qualche capitolo sugli LLM.

## 2. I cinque libri

| N. | Titolo di lavoro | Spina dorsale | Voce | Sistema di analogie | Filo conduttore |
|---|---|---|---|---|---|
| 1 | *Prossima parola, prego* | **Storia**: dal 1913 a oggi, problema dopo problema | l'autore: frasi brevissime, ironia da ufficio e IT, il narratore che si prende in giro | sportello, uffici, ministero, burocrazia | «Questa cosa è vera?» + l'eliminacode |
| 2 | *Il cielo dei token* (**astronomia**) | **Spedizione**: ogni capitolo è una notte d'osservazione | noi, l'equipaggio: meraviglia e ironia gentile, scale | catalogo, mappe del cielo, telescopio, survey, rover, falsi segnali | «Che cosa si vede stasera nel cielo?» |
| 3 | *Ritmo gara* (**corsa**) | **Tabella di allenamento** in 5 blocchi verso una gara | il compagno di corsa: parlato, pratico, sfottente | volume, specificità, taper, VO₂max, zaino da ultratrail, ritmo gara | «Fammi una tabella per il 10 km in meno di 50 minuti» |
| 4 | *Mamma, che cos'è un token?* | **Domeniche a pranzo**: dialoghi in famiglia | commedia all'italiana a tavola, personaggi fissi | cucina: ingredienti, dispensa, brigata, ricetta | l'assistente di nonna Ada + la mail all'amministratore |
| 5 | *Indagine su una risposta plausibile* | **Fascicoli**: casi veri, indagine, perizia, verdetto | noir ironico: Commissario Bayes e dottoressa Logit | indizi, sospettati, perizia | l'inchiesta sul «mandante» |

**Perché astronomia e corsa stanno nei libri 2 e 3** (scelta dello scrittore, da confermare): il Libro 2 sfrutta la scala (miliardi di parametri, spazi a molte dimensioni, segnali nel rumore) e l'incertezza (allucinazioni come falsi segnali); il Libro 3 sfrutta l'allenamento, la specializzazione e l'efficienza (addestramento, fine-tuning, quantizzazione, inferenza, token al secondo). Gli altri tre sono costruiti sulla storia, sulla famiglia e sul giallo, che si differenziano da questi per struttura e voce.

I dettagli di ogni libro (identità, voce, analogie con «dove scricchiolano», fili, box, capitoli e copertura della mappa) sono nei file `libri/libro-N-*.md`.

## 3. Cinque libri, non cinque versioni dello stesso testo

È il rischio principale del progetto. Per evitarlo:

1. **Stessi fatti, parole diverse.** `mappa-contenuti.md` è la verità tecnica comune; le frasi no. Nessuna frase, battuta, esempio o aforisma si ripete tra i libri.
2. **Un solo sistema di analogie per libro.** Ogni concetto ha nel proprio libro un'analogia madre (e una soltanto); non si prestano analogie tra libri (la tazza resta del Libro 1, il RAW e il JPEG del Libro 2, lo zaino da ultratrail del Libro 3, il «q.b.» del Libro 4).
3. **Ordine e struttura diversi.** Ogni libro ha un ordine proprio dei concetti e una struttura di capitolo propria (sezione 11).
4. **Storie vere assegnate** (sezione 5 della mappa). Le storie «cardine» (Transformer 2017, ChatGPT, AlexNet, DeepSeek-R1) possono comparire in più libri con angolazioni diverse; tutte le altre in un libro solo.
5. **Personaggi, filo conduttore e gag propri.** Non importare personaggi da un libro all'altro.
6. **Stessa copertura.** Ogni libro copre tutti i concetti C01-C30: l'esperto è la promessa di tutti e cinque. Cambia il percorso, non la sostanza.
7. **Profondità diverse.** Ogni libro approfondisce di più alcuni concetti (indicati nella sua scheda) e ne tratta altri in modo più rapido.

## 4. Due lettori, un libro (e tre test)

- **Il lettore curioso (la mamma):** non sa programmare e non deve servirgli. Vuole capire, divertirsi e smettere di sentirsi escluso quando si parla di IA.
- **Il lettore tecnico:** sistemisti, sviluppatori, ingegneri. Conosce RAM, CPU, cache, reti, Linux, database; non è esperto di IA. Vuole numeri, trade-off, termini corretti e qualcosa da provare. Se un'analogia è imprecisa si sente preso in giro.

Il testo principale è scritto per il primo; i box **Sotto il cofano** sono scritti per il secondo. Il lettore curioso deve poter saltare tutti i box senza perdere il filo. Il lettore tecnico deve trovare in ogni capitolo almeno un dato, un calcolo o un esperimento che non conosceva.

**Tre test:**

- **Test della mamma:** un lettore senza basi, saltando i box, capisce il capitolo? C'è almeno un momento in cui sorride?
- **Test del sistemista:** un tecnico impara almeno una cosa concreta (un numero, un conto, un comando, un trade-off)? Nessuna analogia lo prende in giro?
- **Test dell'esperto:** in fondo a ogni libro, **30 domande (una per concetto C01-C30)**, formulate con il registro del libro, con le risposte. Chi le sa rifare ha mantenuto la promessa.

Per il lettore tecnico usa anche analogie prese dal suo mondo: lo swap, la cache, il load balancer, HTTP stateless, la SQL injection, i benchmark sintetici, i layer delle immagini dei container.

## 5. Voce e tono comuni

Ogni libro ha la sua voce (nella sua scheda). Queste regole valgono per tutti:

- **Ironia sì, sarcasmo no.** Si ride delle macchine, dell'hype e di noi stessi, mai del lettore e mai di chi non sa.
- **Un'idea per paragrafo.** Il racconto è prosa narrativa; le parti pratiche sono strutturate e facili da scorrere.
- **Dai del tu al lettore** (tranne dove la voce del libro prevede il «noi»).
- **Termini inglesi:** alla prima occorrenza in corsivo, con spiegazione immediata (per esempio *token*, frammento di testo). Poi usa il termine del settore senza traduzioni forzate: token, layer e prompt restano così.
- **Nessuna sigla senza spiegazione**, nemmeno nei box tecnici: ogni sigla viene sciolta la prima volta.
- **Formule:** al massimo una per capitolo, solo nei box tecnici, sempre accompagnata dalla sua lettura a parole.
- **Né hype né catastrofismo.** L'IA non è magia e non è «solo statistica»: spiega cosa fa, cosa non fa e perché.
- **Antropomorfismo sotto controllo.** «Pensa», «ricorda», «capisce» vanno bene come metafore, ma almeno una volta per concetto spiega cosa succede davvero.
- **Non attribuire all'autore** biografia, gare, tempi, strumenti o esperienze non confermati. Nei libri 2 e 3 i personaggi e i dati di esempio sono inventati e dichiarati tali, a meno che l'autore non fornisca i propri.
- **Genere:** nelle voci in prima persona evita forme grammaticali marcate per genere (l'autore e il narratore non hanno un sesso stabilito).

## 6. La regola degli esempi

L'autore vuole **tantissimi esempi**. Regole minime:

- **Almeno tre esempi di tre tipi per ogni concetto:** (a) una scena o un'analogia quotidiana, (b) un esempio numerico con il conto, (c) un caso reale o una prova riproducibile.
- **Almeno 12 esempi per capitolo** (15 nel Libro 4), anche di una riga, distribuiti in modo che non passino 300 parole senza un'immagine, un numero o una battuta.
- **Coppie «originale contro versione degradata»** nei capitoli pratici (quantizzazione, contesto, temperatura, RAG): lo stesso prompt con due condizioni e due risultati.
- **Esempi dichiarati:** un dialogo, una probabilità o un caso inventato si presentano come illustrativi («caricatura», «numeri di fantasia»). Un output presentato come reale è *misurato*: modello, quantizzazione, hardware e impostazioni, riproducibile.
- **Un esempio «da tovagliolo» per capitolo:** un conto che il lettore può rifare a mano con carta e penna.
- **Esempi della mamma:** almeno uno per capitolo deve poter essere capito da chi non sa niente di informatica.

## 7. Le regole d'oro e i box comuni

Ogni concetto segue la stessa sequenza: **un'analogia dal mondo reale, la spiegazione di cosa succede davvero, il punto in cui l'analogia smette di funzionare, la regola d'uso.** Il terzo passaggio è quello che i libri divulgativi di solito saltano, ed è quello che rende questi libri affidabili per un tecnico. Il quarto è quello per cui l'autore ha chiesto «sotto il cofano»: capire serve a usare meglio l'IA.

1. **Prima l'immagine, poi il meccanismo.**
2. **Ogni analogia ha una data di scadenza: dichiarala,** in 2-4 frasi.
3. **Un numero vale più di un aggettivo.** Non «tantissima memoria», ma «16 GB, cioè tutta la memoria di una buona scheda video da gaming».
4. **Mostra il conto.** Quando dai un numero tecnico, scrivi il calcolo (8 miliardi × 2 byte = 16 GB).
5. **Storie vere, non verosimili.** Gli aneddoti sono il motore dei libri e devono essere documentati (sezione 9).
6. **Ogni capitolo chiude con una Regola d'uso:** cosa cambia, concretamente, nel modo di usare l'IA.

**Box comuni ai cinque libri** (il resto è del libro):

| Box | Per chi | Contenuto |
|---|---|---|
| **Sotto il cofano** | lettore tecnico | termini corretti, numeri, calcoli, formati, comandi, paper di riferimento; 1-2 per capitolo |
| **Dove l'analogia scricchiola** | entrambi | i limiti dell'analogia appena usata, in 2-4 frasi, dopo ogni analogia principale |
| **Prova tu** | entrambi | esperimento da 5 minuti, dal banco delle prove (sezione 6 della mappa) |
| **Regola d'uso** | entrambi | cosa cambia quando usi un'IA |
| **In tre righe** (o la variante del libro: tovagliolo, scarico, dal fascicolo) | entrambi | riepilogo che si ricorda dopo una lettura |

## 8. Il contenuto tecnico: la mappa

`mappa-contenuti.md` contiene i 30 concetti (C01-C30), i numeri con il loro conto, le tabelle di hardware e modelli (datate), le correzioni già decise e il banco delle prove. Ricorda:

- **I concetti nuovi richiesti dall'autore** (modelli locali, workflow agentici, quantizzazione, token/s, contesto, memoria, MoE, GPU, nuovi hardware) sono C11, C13, C15, C18-C26: tutti e cinque i libri li trattano con profondità, perché sono il «sotto il cofano che nessuno sa».
- **I dati che invecchiano** (hardware, prezzi, finestre di contesto, classifiche, modelli) hanno sempre mese e anno, oppure si usano ordini di grandezza e tendenze. Mai «oggi il modello più potente è...». Ogni capitolo hardware chiude con una tabella datata.
- **Prima di usare un fatto, controlla la mappa:** se porta [DA VERIFICARE], verificalo con una fonte primaria (paper, documentazione ufficiale, sito del produttore) e annota data e fonte in fondo al capitolo.

## 9. Accuratezza: niente invenzioni

Un libro sull'IA che contiene allucinazioni si smentisce da solo.

- **Non inventare mai** aneddoti, citazioni testuali, numeri, nomi di paper o di persone. Se non sei sicuro, scrivi [DA VERIFICARE: cosa e dove controllarlo] e vai avanti.
- **Fatto o leggenda.** Distingui ciò che è documentato da ciò che «si racconta»: le leggende si possono usare, purché dichiarate (per esempio Fidippide, il teorema di Tesler, i «canali» di Marte).
- **Percentuali solo se misurate.** Niente «funziona al 95%» senza una misura; meglio «regge quasi tutto il lavoro quotidiano».
- **Fonti primarie.** A fine capitolo elenca i fatti chiave con la fonte suggerita.
- **Coerenza interna.** Un esempio non deve contraddire un altro capitolo né la mappa (sezione 7 della mappa: «Fatti già corretti»).
- **Persone reali e casi con danni:** nomi solo se già in documenti pubblici, tono equo; nessuna ironia su casi che hanno ferito persone.
- **Casi e dati recenti:** per ogni caso o dato recente cerca una fonte primaria; se non la trovi, dichiaralo.

## 10. Flusso di lavoro

1. **Oggi:** l'autore rivede le schede. Cambia ciò che chiede, aggiorna questo file e le schede, nient'altro.
2. **Dopo il «via»:** per ogni capitolo l'autore indica libro e numero. Tu: leggi le fonti (prima riga di questo file), mostra una **scaletta** (6-10 punti) con analogie, esempi, storie vere e box, aspetta l'ok, poi scrivi il capitolo completo in Markdown.
3. **Consegna:** il capitolo va in `testi/libro-N/capitolo-NN-titolo.md`. In fondo al capitolo aggiungi: (1) fatti da verificare con la fonte primaria suggerita; (2) termini nuovi per il glossario con definizione di una riga; (3) rimandi ad altri capitoli; (4) scelte editoriali fatte in autonomia, una riga ciascuna.
4. **Lunghezza:** 3.500-4.500 parole nei libri 1, 2 e 3; 2.500-3.500 nel Libro 4; 3.000-4.000 nel Libro 5. Se il capitolo è lungo, scrivilo una sezione per volta e chiedi se proseguire.
5. **Glossario vivo:** l'autore raccoglie i termini in un glossario per libro. Rispettalo nei capitoli successivi.
6. **Git:** lavora sul branch indicato dalla sessione; commit con messaggi in italiano, chiari; non aprire pull request se non richiesto.

## 11. Strutture dei capitoli (una per libro)

- **Libro 1:** scena o aggancio storico, problema, chi l'ha affrontato, soluzione, cosa succede davvero, box tecnico, Regola d'uso, *Il boss del livello dopo*.
- **Libro 2:** *Registro d'osservazione* (Strumento, Obiettivo, Condizioni), scena, analogia, meccanismo, *Falso segnale* e *Potenze di dieci* dove servono, Sotto il cofano, Regola d'uso.
- **Libro 3:** *La seduta* (tipo e scopo), scena, analogia, meccanismo con *Passo e battito* (numeri), *Dal bordo strada*, Sotto il cofano, Regola d'uso, *Scarico* ogni quarto capitolo.
- **Libro 4:** *A tavola* (dialogo), *In cucina*, *Il conto*, *Sotto il cofano* (letto da Davide), *La domanda di Sofia*, *Ricetta*, *Il tovagliolo*, *Prova tu a casa*.
- **Libro 5:** *La scena*, *Gli indizi*, *I sospettati*, *Sotto il cofano* (la perizia), *Il verdetto*, *Prevenzione*, *Prova tu*, *Dal fascicolo*.

## 12. Ordine di scrittura (da decidere con l'autore)

Proposta, modificabile: partire dal **Libro 1** (il prologo è già dell'autore e definisce la voce); poi i due libri con vincolo (2 e 3), che richiedono più cura nell'equilibrio tra IA e analogia; poi 4 e 5. Se l'autore preferisce procedere per «concetto» (lo stesso capitolo in più libri a ruota), la copertura della mappa in fondo a ogni scheda lo rende possibile.

## 13. File del progetto

| File | Contenuto |
|---|---|
| `CLAUDE.md` | questa memoria |
| `mappa-contenuti.md` | i 30 concetti tecnici, i numeri, le correzioni, le storie assegnate, il banco delle prove |
| `libri/libro-1-prossima-parola-prego.md` | scheda del Libro 1 (storia) |
| `libri/libro-2-il-cielo-dei-token.md` | scheda del Libro 2 (astronomia) |
| `libri/libro-3-ritmo-gara.md` | scheda del Libro 3 (corsa) |
| `libri/libro-4-mamma-che-cose-un-token.md` | scheda del Libro 4 (pranzo della domenica) |
| `libri/libro-5-indagine-su-una-risposta-plausibile.md` | scheda del Libro 5 (giallo) |
| `aforismi.md` | banco degli aforismi, assegnato al Libro 1; regole per crearne di nuovi |
| `versione-5-utente.md` | **testo dell'autore** (prologo del Libro 1), verbatim: **non modificare** senza richiesta esplicita |
| `versione-1-staffetta.md`, `versione-2-livelli.md`, `versione-3-regole-o-dati.md`, `versione-4-otto-nomi.md` | quattro prove di apertura della sessione precedente: possono dare spunti (la staffetta, il boss del livello dopo), non si copiano |
| `testi/` | i capitoli scritti, solo dopo il «via» |

**La voce dell'autore** (da `versione-5-utente.md`): frasi brevissime, a capo; ritmo staccato («Ancora. Ancora. Ancora.»); ironia da ufficio e da IT (riunioni su Teams, `analisi_finale_v3_VERAMENTE_FINALE.ipynb`, configurazioni Kubernetes, «casinò clandestino»); aforismi in blockquote corsivo; grassetto sulle parole-chiave; il narratore che si rivolge al lettore («Mi dispiace.», «Non anticipiamo.»); la scena prima, il meccanismo dopo; sempre un numero o un nome vero.

## 14. Scelte fatte in autonomia e decisioni aperte

Scelte già fatte (l'autore può cambiarle):

- Libri 2 e 3 scelti per astronomia e corsa, per le ragioni nella sezione 2; i tre libri senza vincolo sono la storia, la famiglia e il giallo.
- Titoli e sottotitoli sono **di lavoro**, tranne il Libro 1, il cui titolo e sottotitolo sono dell'autore.
- Tutti i libri coprono C01-C30 (sezione 3).
- Il Libro 4 usa personaggi inventati e dichiarati tali; il Libro 5 un Commissario Bayes e una dottoressa Logit; i Libri 2 e 3 un equipaggio e un runner di esempio, tutti inventati.
- Le vecchie schede e il vecchio `CLAUDE.md` (un solo libro di 20 capitoli) restano nella cronologia git (si leggono con `git show 6357a25^:CLAUDE.md` e `git show 6357a25^:schede-capitoli.md`), non più operative; ne sono stati riportati i contenuti verificati nella mappa e negli aforismi.

Decisioni aperte (chiedere all'autore):

1. I cinque libri e i titoli di lavoro vanno bene? Il Libro 1 è il riferimento della voce dell'autore?
2. Astronomia nel Libro 2 e corsa nel Libro 3: confermi la scelta?
3. Lunghezza: ~25 capitoli per libro (circa 80-100 mila parole il Libro 1) è giusta, o si preferisce tagliare?
4. Ordine di scrittura (sezione 12).
5. Dati personali: vuoi che per il Libro 3 usi i tuoi dati reali di corsa (c'è un connettore Strava) e per il Libro 2 le tue osservazioni, con il tuo consenso esplicito? Altrimenti restano personaggi inventati.
6. Genere del narratore del Libro 4 (ora non marcato).
7. Test dell'esperto: 30 domande per libro, in fondo; ok?

## 15. Checklist prima di consegnare ogni capitolo

- Un lettore non tecnico capisce tutto saltando i box?
- Un sistemista impara almeno una cosa concreta: un numero, un calcolo, un comando, un trade-off?
- Ci sono almeno 12 esempi (15 nel Libro 4), almeno tre tipi per concetto?
- Ogni analogia principale ha il suo «dove scricchiola»?
- Il capitolo chiude con una Regola d'uso?
- Ogni data, nome, cifra e citazione è verificabile, oppure marcata [DA VERIFICARE]? I dati che invecchiano hanno mese e anno?
- Gli esempi inventati sono dichiarati come tali?
- Le analogie sono coerenti con la scheda del libro e non prese da un altro libro?
- La storia vera è assegnata a questo libro?
- C'è almeno un momento che fa sorridere?
- Il riepilogo si ricorda dopo una lettura?

## 16. Richiesta tipo per ogni capitolo

```text
Scrivi il capitolo [N] del libro [M], seguendo le istruzioni permanenti
(CLAUDE.md), la scheda del libro e la scheda del capitolo.
Prima mostrami la scaletta (6-10 punti) con analogie, esempi, storie vere
e box previsti.
Dopo il mio ok, scrivi il capitolo completo in Markdown.

In fondo al capitolo aggiungi:
1. Fatti da verificare, con la fonte primaria suggerita
2. Termini nuovi per il glossario, con definizione di una riga
3. Rimandi ad altri capitoli
4. Scelte editoriali fatte in autonomia, una riga ciascuna
```
