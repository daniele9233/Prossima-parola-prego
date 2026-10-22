# PROGETTO-LIBRO — memoria di lavoro

> **A cosa serve questo file.** È la memoria del progetto: contiene lo stato, le regole di voce, il protocollo sui numeri e la raccolta delle 110 curiosità con ID stabili. Va letto prima di scrivere qualsiasi capitolo nuovo. Non è il testo del libro: è la base dati (note di lavoro, dati ancora da verificare).
>
> **Regola d'oro:** ogni volta che un dato di questo file entra in un capitolo, si cita l'ID (es. «C13») nel registro d'uso in fondo. Così sappiamo sempre che cosa è già stato usato, dove, e con quale formulazione.

Ultimo aggiornamento: 22 ottobre 2026.

---

## 0. Stato del progetto

**Cartella di lavoro locale:** `C:\Users\kikkoderiso\Desktop\libro` · **Repo (copia di riferimento per riprendere il lavoro):** https://github.com/daniele9233/Prossima-parola-prego

**Nel repo**

| Percorso | Contenuto |
|---|---|
| `PROGETTO-LIBRO.md` | Questo file: **da leggere per primo** |
| `fonti/prima-della-prossima-parola.pdf` | **Fonte primaria della parte storica** (7 pagine, 9 quadri, da Lullo a ChatGPT) |
| `fonti/estratto.txt` | Testo del PDF (identico), per chi non può leggere PDF |
| `libro-1-la-nonna-e-il-forno/` | Prologo + Cap. 1, voce affettiva (rev 2): `prologo-e-capitolo-1.md` (sorgente), `.docx`, `.pdf` |
| `libro-2-luomo-che-faceva-indovinare-le-lettere/` | idem, voce saggistica |
| `libro-3-la-stanza-in-cui-non-ce-nessuno/` | idem, voce reportage |
| `strumenti/build_capitoli.py` | md → DOCX: `#` = titolo, `##` = sezione, `:::` = riquadro, `---` ignorato (richiede `python-docx`) |
| `strumenti/make_all.py` | rigenera i tre DOCX dalle cartelle dei libri |
| `strumenti/md_to_pdf_edge.py` | stampa i tre PDF con Edge/Chrome headless, stessa geometria del DOCX |

**Per rigenerare tutto:** `python strumenti/make_all.py`, poi `python strumenti/md_to_pdf_edge.py`. Si modifica sempre il `.md`; DOCX e PDF sono derivati. Verificato: da una copia pulita del repo i file rigenerati hanno testo e numero di pagine identici a quelli committati.

**Solo nella cartella locale (non nel repo: superati o non necessari):** `quattro-incipit.md` (contiene il vecchio memoir della nonna e dettagli non verificati), `archivio/`, `v1/v2/v4-prologo-capitolo1.md`, `l1-prologo-capitolo1.md` e i DOCX/PDF di Libro 1 senza «(rev 2)», `extract_pdf.py`, `test_bigram.py`. In locale i sorgenti dei tre libri si chiamano `l1-v2-prologo-capitolo1.md`, `v2-prologo-capitolo1.md`, `l3-prologo-capitolo1.md`: sono le stesse versioni del repo.

**Decisione aperta:** quale delle tre voci tenere. La 3 (ironica, seconda persona) è stata scartata.

**Vincoli già fissati dal committente:**
- La versione 1 **non** deve contenere una dedica alla nonna. La nonna può restare un personaggio, non una destinataria.
- Niente libro troppo tecnico: deve leggerlo un system engineer **e** qualcuno che non ha mai acceso un computer.
- Servono aneddoti, storie, aforismi, paragoni reali.
- Le formule sono ammesse solo se vecchie, raccontabili e non obbligatorie per la comprensione.
- **Stile di lavoro richiesto dall'autore:** onestà prima di tutto, niente fuffa, non assecondarlo: segnalare errori, cose inventate e punti deboli, anche scomodi. Il libro deve divertire e scorrere, essere pieno di esempi e curiosità, ed essere abbastanza tecnico da appassionare un ingegnere restando comprensibile a chi non conosce il campo.
- **Niente scene inventate presentate come viste, niente ricordi personali dell'autore:** la nonna del Libro 1 è un'immagine dichiarata, non un memoir.

**Formato del prodotto:** capitoli in Markdown → DOCX impaginato (15,24 × 22,86 cm, Palatino 10,5 pt, giustificato, numero di pagina nel footer) → PDF. I paragrafi interamente in grassetto diventano citazioni centrate in corsivo. I titoli `##` diventano paragrafi di sezione.

---

## 1. Le tre voci in gara

**V1 — Affettiva.** Apre su un gesto domestico, torna sempre a un'esperienza concreta, chiude con una battuta breve. Il sapere passa dalle mani. Adatta a chi legge poco e a chi vuole essere preso per mano. Rischio: il tono affettivo regge su un'esperienza vissuta. La nonna è stata dichiarata inventata: nel prologo è un'immagine («Immaginate una nonna…»), non un ricordo. Niente «mia nonna», niente date di vita, nei capitoli successivi.

**V2 — Saggistica (terza persona).** Storia delle idee, quadri cronologici, aforismi in corsivo come cesure. Dà autorevolezza e colloca il libro in una tradizione. Rischio: chiede al lettore un atto di fiducia iniziale.

**V4 — Reportage (presente).** Apre su un luogo e un'immagine sensoriale, poi tira il filo all'indietro. Chiude con un gancio. Rischio: il reportage va sostenuto, non si può aprire così e poi tornare alla lavagna.

**Regola trasversale:** qualunque voce si scelga, ogni numero va spiegato con un'immagine fisica prima di essere enunciato. «Quarantatré milioni di litri» non dice niente; «diciassette piscine olimpiche» dice tutto.

---

## 2. Protocollo sui numeri (non negoziabile)

Il libro vive di paragoni. I paragoni sono anche il modo più facile di mentire in buona fede. Regole:

1. **Dire sempre che cosa si sta contando.** L'acqua di raffreddamento in sito e quella della filiera elettrica sono due cose diverse, e la seconda è circa tre quarti del totale. Chi mostra solo la più piccola racconta metà verità.
2. **Dichiarazione ≠ misura.** Le cifre per prompt (0,24–0,34 Wh; 0,26–0,32 ml) sono dichiarazioni aziendali senza metodologia pubblica completa. Nel testo vanno attribuite («secondo Google», «secondo Altman»), mai presentate come misure.
3. **Previsione ≠ dato.** I 945 TWh del 2030 sono uno scenario IEA, non un fatto avvenuto. Stesso trattamento per qualunque «entro il 20XX».
4. **I calcoli miei si dichiarano.** Se divido, lo dico, mostro l'ipotesi e arrotondo: tre cifre significative al massimo. Un conto con quattro decimali sembra una misura ed è solo una divisione.
5. **Un paragone serve a far vedere una scala, non a dimostrare una tesi.** La mandorla non dimostra che l'AI consuma poco; dimostra che i confronti dipendono da dove si mette il confine.
6. **Niente numeri senza data.** Tutto invecchia: utenti, capitalizzazioni, benchmark, prezzi per token. Ogni cifra che va in stampa si ricontrolla.

---

## 3. Le 110 curiosità

**Legenda dei marcatori**
`(dich.)` dichiarazione aziendale o di un dirigente, non verificata indipendentemente · `(studio)` risultato pubblicato, valido nelle condizioni specificate · `(prev.)` previsione o scenario · `(bench)` risultato di benchmark, non capacità generale · `(fc)` verifica di terze parti · `(calc)` aritmetica su un dato dichiarato · `(storico)` fatto documentato

### Blocco 1 — L'AI, l'elettricità e i paragoni che sorprendono

**C01 · Una domanda a ChatGPT e una lampadina** — 0,34 Wh per richiesta media (Altman, giugno 2025) ≈ lampadina LED da 10 W per poco più di 2 minuti. *(dich.)*
→ *Angolo:* chiedere all'AI come risparmiare energia, e consumarne per ricevere la risposta.

**C02 · Un milione di domande non è una piccola cosa** — 1.000.000 × 0,34 Wh = 340 kWh ≈ la stessa lampadina da 10 W accesa per 3,9 anni senza interruzione. *(calc)*
→ *Angolo:* l'operazione insignificante che diventa enorme quando si ripete.

**C03 · Nove secondi di televisione** — 0,24 Wh per prompt testuale mediano su Gemini (Google, maggio 2025), «meno di nove secondi di televisione da 100 W». La metodologia dichiarata include parte dell'infrastruttura, non solo il chip. *(dich.)*
→ *Angolo:* il paragone domestico come unità di misura del dibattito pubblico.

**C04 · Un milione di prompt Gemini** — 240 kWh, a consumo costante. Calcolo teorico, non misura del traffico reale. *(calc)*
→ *Angolo:* le piccole efficienze moltiplicate per miliardi.

**C05 · I data center consumano quanto un grande paese** — 415 TWh nel 2024, l'1,5% dell'elettricità mondiale. Non solo AI: cloud, archiviazione, servizi digitali. *(studio/IEA)*

**C06 · Entro il 2030 potrebbero superare il Giappone** — scenario di riferimento IEA 2025: ~945 TWh nel 2030, poco più del consumo elettrico nazionale giapponese usato nel rapporto. *(prev.)*

**C07 · In Irlanda quasi una presa su quattro** — nel 2025 i data center sono il 23% dell'elettricità misurata in Irlanda, contro il 5% del 2015. *(studio/CSO)*
→ *Angolo:* il paese piccolo come cartina di tornasole. Da usare con cautela: la quota è nazionale, non «più delle case», e va detta così.

**C08 · L'AI ha aiutato a ridurre i consumi dell'AI** — DeepMind, 2016: fino al 40% di energia in meno per il raffreddamento dei data center Google. *(dich.)*
→ *Angolo:* «un termostato molto, molto istruito».

**C09 · Le emissioni non dipendono solo dal modello** — due server identici con lo stesso modello possono avere emissioni diverse se l'elettricità viene da fonti diverse. *(studio)*
→ *Angolo:* due auto elettriche identiche: conta anche la corrente che le carica.

**C10 · Più efficiente, ma anche più usata** — Google: tra maggio 2024 e maggio 2025 l'energia per prompt testuale mediano su Gemini è calata di 33 volte. *(dich.)*
→ *Angolo:* effetto rimbalzo / paradosso di Jevons. Da presentare come ipotesi, non come legge: l'aumento dei consumi totali non è dimostrato da questo dato.

### Blocco 2 — L'AI, l'acqua e il caso delle mandorle

**C11 · Meno di una goccia grande** — ~0,32 ml per richiesta media (Altman): meno di un quindicesimo di cucchiaino. Nessuna metodologia pubblica completa. *(dich.)*

**C12 · Un milione di domande, 320 litri** — 1.000.000 × 0,32 ml = 320 L ≈ due vasche da bagno da 160 L. Esempio di scala, non misura reale. *(calc)*

**C13 · Una mandorla contro migliaia di conversazioni** — settembre 2026: Altman sostiene che una mandorla californiana equivale a ~38.000 domande. PolitiFact: «prevalentemente falso»; i 38.000 derivano dall'usare ~12 L per mandorla (inclusi acqua piovana e un indicatore di inquinamento idrico) e una stima molto bassa per ChatGPT. *(fc)*
→ *Angolo:* il caso esemplare del numero vero usato per dire una cosa fuori scala.

**C14 · Il numero che cambia tutto: da 1.000 a 10.000** — con criteri comparabili, le richieste necessarie a eguagliare i ~6 L di acqua dolce di una mandorla stanno tra ~1.000 e ~10.000. *(fc)*
→ *Angolo:* cambiare il metodo di misura cambia il confronto di decine di volte.

**C15 · Una vecchia AI poteva bere molto più acqua** — studio su GPT-3: una bottiglietta da 500 ml ogni 10–50 risposte di media lunghezza, in certe condizioni. Non descrive i modelli attuali. *(studio)*

**C16 · Addestrare GPT-3: 700.000 litri** — consumo diretto in sito, in specifici data center Microsoft statunitensi ≈ 4.700 vasche da 150 L. Simulazione scientifica, non lettura del contatore. *(studio/calc)*

**C17 · Se includi l'elettricità il conto cambia** — ~5,4 milioni di litri contando l'acqua indiretta per produrre energia: oltre sette volte il consumo diretto. *(studio)*
→ *Angolo:* perché due articoli seri sullo stesso modello riportano cifre diversissime.

**C18 · L'acqua consumata lontano dal data center** — le centrali elettriche raffreddano con acqua: un server che ne usa poca nel proprio edificio può averne consumata molta altrove. *(studio)*
→ *Angolo:* l'acqua di una tazza di caffè non è quella versata nella tazzina.

**C19 · Due richieste simili, impronte idriche diversissime** — Lawrence Berkeley National Laboratory, 2025: differenze teoriche superiori a 10.000 volte per carico di lavoro, al variare di temperatura, raffreddamento, elettricità, efficienza e utilizzo. *(studio)*

**C20 · Il paradosso acqua-energia** — il raffreddamento evaporativo consuma acqua ma poca elettricità; altri sistemi il contrario. Ridurre l'acqua locale non riduce automaticamente l'energia. *(studio)*
→ *Angolo:* un problema di ottimizzazione a più obiettivi, non una scelta morale.

### Blocco 3 — Il cervello umano, i neuroni e la natura

**C21 · Il cervello funziona con circa 20 watt** — a riposo, come una piccola lampadina, mentre sostiene percezione, linguaggio, memoria, emozioni e controllo del corpo. Confrontare i watt non misura l'intelligenza. *(studio)*

**C22 · Il 2% del peso, il 20% dell'energia** — un organo metabolicamente carissimo, che non si spegne di notte. *(studio)*

**C23 · 175 kWh all'anno** — 20 W medi → 0,48 kWh al giorno → 175,2 kWh l'anno. Paragone energetico, non cognitivo. *(calc)*

**C24 · 86 miliardi di neuroni** — la vecchia cifra di 100 miliardi era un'arrotondamento. GPT-3 ha 175 miliardi di parametri: circa il doppio, ma un parametro non è un neurone. *(studio)*
→ *Angolo:* l'errore da evitare in assoluto in tutto il libro.

**C25 · Le sinapsi sono molte più dei neuroni** — stime nell'ordine delle centinaia di migliaia di miliardi. La somiglianza tra rete artificiale e cervello è un'ispirazione matematica. *(studio)*

**C26 · Il moscerino della frutta** — 2024: mappa di ~139.000 neuroni e oltre 50 milioni di sinapsi di un esemplare adulto. *(studio)*
→ *Angolo:* l'animale che scacciamo dalla frutta.

**C27 · Anche i moscerini imparano e decidono** — orientamento, apprendimento, interazioni sociali con una rete minuscola. La dimensione, da sola, non racconta la sofisticatezza del comportamento. *(studio)*

**C28 · Il polpo è intelligenza distribuita** — circa due terzi dei neuroni sono nelle braccia: gran parte dell'elaborazione avviene fuori dal cervello centrale. *(studio)*
→ *Angolo:* analogia con il calcolo distribuito, suggestiva e non identitaria.

**C29 · Un neurone non è un interruttore** — cellula viva, elettrochimica, che modifica le proprie connessioni; il neurone artificiale è una funzione matematica. *(studio)*

**C30 · Il cervello consuma anche quando non pensa** — mantenimento dei potenziali, trasmissione sinaptica, salute cellulare. Non è un computer che va da zero a cento. *(studio)*

### Blocco 4 — Come funzionano davvero gli LLM

**C31 · Un token alla volta** — il compito di base è prevedere il token successivo; ripetendolo nascono racconti, codice, argomentazioni. *(studio)*
→ *Angolo:* la sorpresa centrale del libro.

**C32 · Un token non è una parola** — può essere una parola, un pezzo, un segno, pochi caratteri. Per questo contare le lettere non equivale a leggere carattere per carattere. *(studio)*
→ *Si aggancia a:* caso «strawberry», già usato nel cap. 1 di tutte e tre le versioni.

**C33 · Un milione di token ≈ 3.000 pagine** — 0,75 parole per token × 250 parole per pagina = 750.000 parole. Ricevere tutto quel testo non significa capirlo senza errori. *(calc)*

**C34 · La risposta nasce da una distribuzione** — il modello assegna punteggi alle continuazioni; la decodifica sceglie. Ridurlo a «tastiera predittiva» è comodo ma insufficiente. *(studio)*

**C35 · Un concetto in migliaia di numeri** — gli embedding trasformano testo in vettori; la configurazione standard di un modello OpenAI usa 3.072 dimensioni. *(studio)*
→ *Angolo:* un atlante matematico del significato.

**C36 · Non è una biblioteca di pagine web** — le informazioni stanno nei parametri, non come documenti consultabili: il modello può sapere una cosa e non sapere da dove viene. *(studio)*
→ *Angolo:* la radice strutturale delle citazioni inventate.

**C37 · Collegare documenti non è riaddestrare** — RAG: cerca fuori e mette il risultato nel contesto. *(studio)*
→ *Angolo:* lo studente che consulta gli appunti durante l'esame.

**C38 · 350 GB di pesi** — GPT-3, 175 miliardi di parametri × 2 byte, esclusi cache e memoria temporanea. *(calc)*
→ *Già usato nel cap. 1 v2.*

**C39 · 87,5 GB a 4 bit** — un quarto della dimensione a 16 bit: è il principio della quantizzazione. Solo pesi teorici; un modello reale chiede altra memoria e può perdere precisione. *(calc)*

**C40 · Non tutti i parametri si attivano** — Mixtral 8×7B: ~47 miliardi complessivi, ~13 miliardi usati per token (Mixture of Experts). *(studio)*
→ *Angolo:* l'azienda che non convoca tutti i dipendenti per ogni email.

### Blocco 5 — I paradossi matematici

**C41 · 10^100 sequenze** — dieci scelte per token, cento token: un googol. Il modello non le esplora: è lo spazio delle possibilità. *(calc)*

**C42 · 15,6 bit per scelta** — log₂(50.000) se i token fossero equiprobabili. Non lo sono: la struttura del linguaggio è ciò che rende possibile imparare. *(calc)*

**C43 · Il 99% non basta su una catena lunga** — 100 passaggi indipendenti al 99%: 0,99¹⁰⁰ ≈ 36,6%. Esempio matematico, non misura di un LLM. *(calc)*
→ *Angolo:* perché gli agenti che concatenano passaggi sono fragili.

**C44 · Un token sbagliato cambia tutto il resto** — ogni token generato diventa contesto del successivo: una premessa falsa viene sviluppata con coerenza. *(studio)*
→ *Angolo:* partire da un'ipotesi sbagliata in una dimostrazione.

**C45 · La maledizione dell'inversione (Reversal Curse)** — studio 2023, ICLR 2024: modelli addestrati su «A è B» non rispondono automaticamente a «chi è B?». *(studio)*
→ *Angolo:* ciò che per un umano è banale.

**C46 · Gli esempi nella domanda cambiano la prestazione** — few-shot learning: si sfruttano esempi nel contesto senza toccare i pesi. È una delle ragioni dell'importanza di GPT-3 nel 2020. *(studio)*

**C47 · 142 volte più piccolo, stessa soglia** — 2022: servivano 540 miliardi di parametri per superare una soglia MMLU; 2024: Phi-3-mini, 3,8 miliardi, la supera. Risultato di benchmark, non equivalenza generale. *(bench/AI Index)*

**C48 · Più parametri non significa più intelligenza** — contano dati, architettura, addestramento, risorse al momento della risposta. *(studio)*
→ *Angolo:* nemmeno il numero di neuroni ordina gli animali per intelligenza.

**C49 · Il costo è crollato di oltre 280 volte** — da ~20 $ per milione di token (novembre 2022) a 0,07 $ (ottobre 2024), a parità di soglia MMLU. *(bench/AI Index)*

**C50 · Specializzare senza riaddestrare tutto** — LoRA: fino a 10.000 volte meno parametri da addestrare rispetto a un fine-tuning completo di GPT-3, nella configurazione dello studio originale. *(studio)*

### Blocco 6 — Quando l'AI incontra biologia, chimica e scienza

**C51 · 200 milioni di proteine** — AlphaFold (DeepMind), 2022: strutture previste per oltre 200 milioni di proteine, rese accessibili a tutti i ricercatori. *(studio)*

**C52 · Previsione non è esperimento** — sono strutture previste, non misure sperimentali: la validazione in laboratorio resta necessaria. *(studio)*
→ *Angolo:* da usare ogni volta che si parla di «scoperte» dell'AI.

**C53 · Dalla sequenza alla forma** — AlphaFold 2: dalla sequenza di amminoacidi alla struttura tridimensionale. *(studio)*
→ *Angolo:* l'origami di cui conosci i componenti e prevedi la figura.

**C54 · Un Nobel per la Chimica con l'AI** — 2024: metà a David Baker (progettazione computazionale di proteine), metà a Demis Hassabis e John Jumper (previsione di strutture). Il premio è agli scienziati, non all'AI. *(storico)*

**C55 · E uno per la Fisica** — 2024: John Hopfield e Geoffrey Hinton, per i contributi fondamentali al machine learning con reti neurali artificiali. *(storico)*

**C56 · Halicin** — 2020, MIT: molecola individuata con il machine learning, attiva in laboratorio e su modelli animali contro batteri anche resistenti. Scoperta preclinica, non farmaco approvato. *(studio)*

**C57 · Il nome viene da HAL 9000** — l'antibiotico si chiama come il computer di *2001: Odissea nello spazio*. *(storico)*
→ *Angolo:* l'AI più inquietante del cinema dà il nome a una medicina.

**C58 · Previsioni meteo in meno di un minuto** — GraphCast, 2023: previsione globale a dieci giorni in meno di 60 secondi sull'hardware specificato. *(studio)*

**C59 · Meglio del sistema tradizionale sull'89,3%** — più accurato di HRES sull'89,3% delle combinazioni variabile/orizzonte. Non significa «indovina il meteo nel 90% dei casi». *(studio)*

**C60 · 2,2 milioni di strutture cristalline** — GNoME, 2023: strutture identificate computazionalmente, secondo il metodo di valutazione usato. *(studio)*

**C61 · 380.000 candidate stabili** — soddisfano criteri rigorosi di stabilità teorica; alcune potenzialmente utili per batterie e semiconduttori. Da realizzare, non ancora realizzate. *(studio)*

**C62 · Ordinare più in fretta** — AlphaDev: algoritmi fino al 70% più veloci in operazioni di ordinamento su sequenze piccolissime, nelle condizioni dei test. *(studio)*

**C63 · 25 problemi di geometria olimpica su 30** — AlphaGeometry, 2024, contro i 10 della soluzione automatica precedente. Combina rete neurale e deduzione simbolica: costruisce dimostrazioni. *(bench)*

**C64 · Argento alle Olimpiadi della Matematica** — IMO 2024: AlphaProof e AlphaGeometry 2 risolvono 4 problemi su 6, 28 punti su 42. Alcune soluzioni hanno richiesto giorni di calcolo; gli studenti avevano molto meno tempo. *(bench)*

**C65 · Duemila specie di uccelli** — Merlin Bird ID (Cornell Lab): riconosce oltre 2.000 specie dal canto; per insegnarne una nuova servono almeno 150 registrazioni. *(studio)*

### Blocco 7 — Le storie che hanno creato l'intelligenza artificiale

**C66 · La domanda è del 1950** — Turing propone il gioco dell'imitazione: non quanto velocemente calcola, ma se il comportamento linguistico è indistinguibile. *(storico)*

**C67 · Il nome nasce da un progetto estivo** — «intelligenza artificiale» compare nella proposta del 1955 per la scuola estiva di Dartmouth, tenuta nel 1956. *(storico)*
→ *Angolo:* la trasformazione tecnologica più importante del secolo prende il nome da un campus estivo.

**C68 · Una rete che voleva imitare un topo** — SNARC, 1951, Minsky e Edmonds: ~3.000 tubi elettronici per simulare una rete di 40 unità, topo in un labirinto. *(storico)*
→ *Angolo:* oggi reti enormemente più grandi su hardware da tasca.

**C69 · Il percettrone è del 1957** — Rosenblatt: classificazione modificando i pesi. *(storico)*

**C70 · Uno psicoterapeuta artificiale nel 1966** — ELIZA, Weizenbaum; la versione DOCTOR rimandava le frasi come domande. *(storico)*

**C71 · La segretaria voleva parlare con ELIZA in privato** — secondo il racconto dello stesso Weizenbaum, gli chiese di uscire dalla stanza. *(storico)*
→ *Angolo:* l'effetto ELIZA. Già usato nel cap. 1 v2.

**C72 · «Tre-otto anni»** — Minsky, 1970, indicava un orizzonte di 3–8 anni per capacità paragonabili a quelle umane generali. *(storico)*
→ *Angolo:* l'ottimismo come costante storica del settore.

**C73 · Gli inverni** — quando le promesse superano i risultati, fondi e interesse calano; il secondo inverno inizia alla fine degli anni Ottanta. *(storico)*

**C74 · 1986, la retropropagazione** — Rumelhart, Hinton, Williams: l'errore rispedito all'indietro negli strati. *(storico)*

**C75 · 200 milioni di posizioni al secondo** — Deep Blue batte Kasparov nel 1997 in un incontro di sei partite. *(storico)*
→ *Angolo:* la forza bruta vince, ma non spiega.

**C76 · Watson confonde Chicago con Toronto** — 2011: batte Jennings e Rutter a *Jeopardy!*, ma sbaglia una risposta. *(storico)*
→ *Angolo:* vincere una gara non immunizza dagli errori assurdi.

**C77 · Due GPU cambiano la visione artificiale** — AlexNet, 2012: 15,3% di errore top-5 contro 26,2% del secondo. Due schede. *(storico)*
→ *Già usato nel cap. 1 v1 e v2.*

**C78 · Il Transformer nasce per tradurre** — 2017, otto ricercatori: i risultati principali riguardano la traduzione automatica. *(storico)*

**C79 · GPT-2 rilasciato a tappe** — 2019, 1,5 miliardi di parametri, pubblicazione graduale per prudenza; versione completa a novembre. Oggi sembra piccolo. *(storico)*

**C80 · 30 novembre 2022** — ChatGPT come anteprima di ricerca. Non nasce l'AI: nasce la facilità di parlare con un modello. *(storico)*

### Blocco 8 — Aneddoti veri: quando l'AI sorprende, sbaglia o fa ridere

**C81 · La mossa 37** — AlphaGo contro Lee Sedol, marzo 2016: probabilità stimata che un professionista umano la giocasse ~1 su 10.000. Sembrò un errore, fu decisiva. *(storico)*

**C82 · E l'umano sorprese la macchina** — quarta partita, mossa 78 di Lee Sedol, anch'essa statisticamente improbabile: fu decisiva per la sua unica vittoria. *(storico)*
→ *Angolo:* la storia più bella del confronto: entrambe trovarono mosse straordinarie.

**C83 · 10^170 contro 10^80** — configurazioni del Go contro atomi dell'universo osservabile: circa 90 ordini di grandezza. AlphaGo non le esaminava: si concentrava sulle promettenti. *(calc)*
→ *Già usato nel cap. 1 v2.*

**C84 · 4-1 e un milione di dollari in beneficenza** — il premio andò a UNICEF, iniziative STEM e organizzazioni legate al Go. *(storico)*

**C85 · Tay, sedici ore** — 2016: chatbot su Twitter manipolato dagli utenti, messo offline in circa 16 ore. *(storico)*
→ *Angolo:* un esperimento su come far interagire una macchina con Internet.

**C86 · Insegnare a un'AI a dire «ehm»** — Google Duplex, 2018: esitazioni e intercalari inseriti per rendere il parlato più realistico. *(storico)*
→ *Angolo:* una macchina addestrata a sembrare meno perfetta per sembrare più umana.

**C87 · Chi risponde al telefono deve saperlo?** — le dimostrazioni di Duplex aprirono il dibattito; Google annunciò che avrebbe identificato le chiamate dell'assistente. *(storico)*
→ *Angolo:* una capacità tecnica che genera immediatamente un problema etico.

**C88 · Un quadro dell'AI a 432.500 dollari** — *Portrait of Edmond de Belamy*, Christie's 2018: stima massima 10.000 $, finale oltre 43 volte tanto. *(storico)*

**C89 · La firma era una formula** — al posto della firma d'artista, l'equazione della GAN usata dal collettivo Obvious. *(storico)*

**C90 · Sentenze che non esistono** — Mata v. Avianca, 2023: citazioni inventate da ChatGPT, sanzione complessiva di 5.000 dollari. *(storico)*
→ *Già usato nel cap. 1 v1.*

**C91 · Formaggio rosicchiato dai topi** — 2024, chatbot della città di New York per le imprese: risposte sbagliate e potenzialmente pericolose. *(storico)*
→ *Angolo:* un assistente creato per rispettare le regole che suggerisce di violarle.

**C92 · Il curriculum e le donne** — 2018, Reuters: sistema sperimentale Amazon addestrato su assunzioni storiche, sfavoriva curriculum associati a donne; abbandonato. *(storico)*
→ *Angolo:* imparare dal passato non significa imparare ciò che è giusto.

**C93 · Il collasso del modello** — Nature, 2024: addestramenti ricorsivi su dati sintetici possono degradare il modello. *(studio)*
→ *Angolo:* fotocopiare una fotocopia.

**C94 · Non tutti i dati sintetici fanno male** — 2025: contano qualità, diversità, provenienza e modalità di incorporazione. *(studio)*

**C95 · I delfini** — DolphinGemma (DeepMind): prevede quali vocalizzazioni potrebbero seguire. Trovare strutture ricorrenti non è tradurre. *(studio)*

### Blocco 9 — Le contraddizioni più incredibili

**C96 · Il genoma in meno di un gigabyte** — 3 miliardi di coppie di basi × 2 bit ≈ 750 MB. È un limite di codifica: la complessità di un organismo non sta nella conta dei bit. *(calc)*

**C97 · Oro alle Olimpiadi della Matematica** — IMO 2025: Gemini Deep Think risolve 5 problemi su 6, 35 punti su 42, fascia oro. *(bench)*

**C98 · E poi l'orologio** — ClockBench, AI Index 2026: il miglior sistema ~50,6% di risposte corrette, contro ~90% degli umani nel confronto riportato. *(bench)*
→ *Angolo:* medaglia d'oro in matematica, difficoltà con le lancette. È il cuore del «profilo irregolare».

**C99 · Robot bravissimi in laboratorio** — AI Index 2026: 89,4% in attività robotiche simulate, 12% in una valutazione di compiti domestici. Non è un confronto controllato dello stesso robot. *(bench)*

**C100 · Un compito su tre fallito al computer** — OSWorld, AI Index 2026: agenti intorno al 66%, sotto il riferimento umano. *(bench)*
→ *Angolo:* scrivere codice è una cosa, portare a termine un lavoro intero è un'altra.

**C101 · Gli incidenti aumentano** — 362 casi registrati nel 2025 contro 233 nel 2024. Aumentano anche diffusione e segnalazioni: il dato non prova da solo maggiore pericolosità. *(studio)*

**C102 · Prompt injection** — istruzioni nascoste in una pagina, un'email, un documento, sperando che il modello le scambi per comandi. *(studio)*
→ *Angolo:* il biglietto nascosto dentro il libro che l'assistente consulta.

**C103 · Pagine che cambiano il tono dell'assistente** — indagine Google 2026: istruzioni invisibili o nascoste destinate agli agenti che visitano la pagina. *(studio)*

**C104 · Pagine che provano a far cancellare file** — la stessa ricerca: comandi distruttivi, per lo più tentativi poco sofisticati. Il rischio cresce quando l'agente ha strumenti e permessi. *(studio)*
→ *Angolo:* la distinzione tra dati da leggere e istruzioni autorizzate.

**C105 · 232 millisecondi** — GPT-4o, documentazione OpenAI 2024: latenza audio minima ~232 ms, media ~320 ms. Conta anche il tempo: rispondere bene con tre secondi di ritardo è un'altra cosa. *(dich.)*

### Blocco 10 — Altri cinque fatti sul futuro

**C106 · Chinchilla batte Gopher** — 2022: 70 miliardi di parametri contro 280, stesso budget di addestramento ma più dati, risultati migliori su numerosi benchmark. *(studio)*
→ *Angolo:* non è solo la dimensione, è l'equilibrio tra dati e capacità.

**C107 · Quasi il 90% dei modelli viene dall'industria** — AI Index 2025: circa nove modelli di rilievo su dieci nel 2024. Le università restano centrali nella ricerca citata. *(studio)*

**C108 · Un'isola tiene in piedi l'AI mondiale** — TSMC fabbrica gran parte dei chip AI più avanzati progettati da altre imprese. *(studio)*
→ *Angolo:* una tecnologia distribuita via Internet che dipende da una catena fisica concentrata.

**C109 · Le emissioni crescono con i modelli** — AI Index 2025: ~588 t CO₂e per GPT-3, ~5.184 t per GPT-4, circa 8,8 volte. Stime di addestramento, non emissioni per domanda. *(studio)*

**C110 · Convincente non è vero** — un modello può scrivere in modo impeccabile partendo da dati falsi. Gli avvocati di New York, i chatbot istituzionali e i test di factualità dicono la stessa cosa: la qualità della scrittura non misura la verità. *(sintesi)*
→ *È la tesi-porta del libro: può chiudere il volume.*

---

## 4. I cinque paragoni guida

Da usare come colonna vertebrale argomentativa, non come curiosità sparse.

1. **Cervello contro data center.** Decine di watt contro megawatt, e modi di operare profondamente diversi. Non serve a dire chi è più intelligente: serve a mostrare quanto sono diverse le due architetture. → C21–C30
2. **Mandorla contro chatbot.** Due impronte idriche, confini di calcolo diversi. Un numero vero usato per comunicare un'idea fuorviante. → C11–C19
3. **Matematica difficile contro orologio.** Medaglia d'oro alle Olimpiadi e difficoltà con le lancette: l'AI non segue la progressione intuitiva delle abilità umane. → C97–C98
4. **Una sequenza di lettere e la complessità della vita.** 750 MB di genoma, miliardi di parametri: nessuna conta di bit racconta la complessità che ne deriva. → C96, C24–C25
5. **La macchina che scopre antibiotici e inventa sentenze.** È la contraddizione che riassume l'AI contemporanea. → C56, C90, C110

**Chiusura possibile del libro:** l'AI non è soltanto una rivoluzione informatica; è un esperimento su che cosa significhino intelligenza, apprendimento, creatività, conoscenza e affidabilità. Le sue curiosità più sorprendenti non riguardano i computer, ma ciò che insegnano su di noi. *(frase da rifinire, non da copiare)*

---

## 5. Dati in attesa di collocazione

**Non sono più nel capitolo 1**, che ora copre solo il periodo 1305-1843. Servono ai capitoli 4-6 (hardware, costi, cervello). Se si aggiornano, si aggiornano in tutti i file.

- Iowa, luglio 2022: ~43,5 milioni di litri (11,5 milioni di galloni) prelevati dai centri Microsoft di West Des Moines, il mese prima che OpenAI dichiarasse concluso l'addestramento di GPT-4 = ~6% dell'acqua del distretto (dati dell'acquedotto, riportati dall'AP, settembre 2023). L'AP non dice quanta sia servita al modello: non scrivere «durante l'addestramento». *(dich./stampa)*
- Supercomputer Microsoft per OpenAI (2020): 10.000 GPU, 285.000 core.
- Una singola GPU di ultima generazione: ~4,5 PFLOPS in FP8; un secondo = 142 milioni di anni per una persona; 6 giorni e 8 ore per tutta l'umanità; un'ora = ~63 anni di tutta l'umanità. *(calc — ipotesi dichiarate nel cap. 1 v4)*
- ENIAC, 1946: 27 tonnellate, 150 kW, 5.000 addizioni/s → una GPU moderna è ~7 miliardi di volte più veloce. *(calc)*
- Una scheda NVIDIA B200: ~1.000 W contro i ~20 W del cervello → 50 cervelli. → si sovrappone a C21
- GPT-3: 3,14×10²³ operazioni di addestramento; tutta l'umanità impiegherebbe ~1,2 milioni di anni. *(calc)*
- Modelli di frontiera: ~15.000 miliardi di token ≈ 11.000 miliardi di parole ≈ 250.000 anni di lettura a 250 parole/minuto, 8 ore al giorno. *(calc)*
- Transformer originale, 2017: ~900 $ di addestramento; GPT-4 ~78 milioni; Gemini Ultra ~191 milioni → oltre 200.000 volte in sei anni. *(AI Index)*
- Kenya, 2023 (inchiesta *TIME*): etichettatori pagati meno di 2 dollari l'ora per filtrare contenuti tossici.
- Turco meccanico, 1770 (Kempelen); «Mechanical Turk» di Amazon.
- Cauchy 1847 (discesa del gradiente), Leibniz (regola della catena), Shannon 1951 (*Prediction and Entropy of Printed English*).

---

## 6. Conflitti e questioni aperte sui numeri

Da risolvere prima della stampa. **Sono i punti in cui il libro può essere smentito.**

1. **La mandorla ha tre valori diversi.** 3,56 L (studio USGS 2019, usato nel cap. 1 v1 e v4) · ~6 L di acqua dolce (fact-check 2026) · ~12 L includendo acqua piovana e indicatori di inquinamento (base del «38.000» di Altman). **Decisione:** adottare ~6 L come valore di riferimento e riscrivere il passo del cap. 1; il 3,56 L diventa «una stima più vecchia e più stretta». Il numero 11.125 va sostituito o accompagnato da un intervallo.
2. **CO₂ di GPT-3: 502 t o 588 t?** La stima Patterson 2021 dà ~502 t; l'AI Index 2025 riporta ~588 t. Sono stime diverse dello stesso addestramento. **Decisione:** citarne una sola e dire di chi è.
3. **Acqua di GPT-3: 700.000 L o 5,4 milioni?** Non è un conflitto: sono diretto e indiretto. Nel testo vanno sempre insieme, altrimenti il lettore pensa a un errore.
4. **Utenti di ChatGPT.** La cifra «900 milioni settimanali» è del febbraio 2026 ed è già nel cap. 1 v2. Non aggiornarla senza data.
5. **Wh e ml per prompt.** 0,34 Wh / 0,32 ml (ChatGPT, Altman) e 0,24 Wh / 0,26 ml (Gemini, Google) sono dichiarazioni, non misure. Nel cap. 1 v1 e v4 ho scritto «circa 0,3»: va bene, purché sia attribuito.
6. **Il 40% di DeepMind (C08)** riguarda il raffreddamento, non l'energia totale del data center. Non confonderli.
7. **L'Irlanda (C07):** 23% dell'elettricità misurata. Non «più delle case»: la formulazione del materiale originale è suggestiva ma va verificata prima di finire in pagina.

---

## 7. Mappa di impiego — capitoli previsti

Proposta di struttura, da confermare. Le curiosità sono assegnate per pertinenza, non in esclusiva.

| Cap. | Titolo di lavoro | Curiosità |
|---|---|---|
| 1 | Fatto (tre versioni in gara) | C05, C06, C11–C14, C16–C17, C21, C77 |
| 2 | Una parola alla volta: token, probabilità, embedding | C31–C40, C41–C44 |
| 3 | Come impara una macchina: dati, errori, gradienti | C45–C50, C106, C107 |
| 4 | Il carburante: GPU nate per i videogiochi | C75–C78, C83, C68 |
| 5 | Quanto costa: energia, acqua, bollette | C01–C20, C109 |
| 6 | Il cervello e il paragone impossibile | C21–C30, C96 |
| 7 | Quando sbaglia: allucinazioni, injection, agenti | C90–C92, C98–C104, C110 |
| 8 | Quando scopre: scienza, proteine, materiali | C51–C65, C97 |
| 9 | Le persone dietro il filtro | *(lacuna: il materiale non copre il lavoro di etichettatura, il copyright, le miniere)* |
| 10 | Che cosa resta aperto | C105, C108, C110, C95 |

**Lacune da colmare con nuova documentazione:** lavoro di etichettatura e moderazione; copyright e addestramento; catena dei materiali (litio, rame, terre rare); modelli open source e decentramento; agenti e sicurezza informatica; effetti sul lavoro d'ufficio; didattica e scuola. Nessuna di queste è coperta dalle 110 curiosità.

---

## 8. Come si aggiorna questo file

1. **Gli ID non si rinumerano mai.** Una curiosità nuova prende C111, C112, e così via, anche se tematicamente apparterrebbe a un blocco precedente: in quel caso si aggiunge in fondo con il blocco indicato tra parentesi.
2. **Ogni voce ha un marcatore di affidabilità.** Se non ce l'ha, non è pronta per entrare in un capitolo.
3. **Ogni voce che entra in un capitolo si registra qui sotto**, con capitolo e formulazione usata. Se un numero cambia, si sa dove andarlo a correggere.

### Registro d'uso

| ID | Capitolo | Formulazione usata | Stato |
|---|---|---|---|
| C05 | 1 (v1, v2, v4) | «415 TWh, l'1,5% dell'elettricità mondiale» | ok |
| C06 | 1 (v1) | «945 TWh nel 2030, poco più del Giappone» | ok, da attribuire a IEA |
| C11–C13 | 1 (v1, v4) | mandorla e Altman, con «Sam Almond» | **da rivedere**: valore mandorla |
| C16–C17 | 1 (v1) | 500 ml ogni 10–50 risposte | ok |
| C21 | 1 (v4) | 20 W contro 1.000 W | ok |
| C77 | 1 (v1, v2) | AlexNet, due GTX 580, 15,3% vs 26,2% | ok |
| C83 | 1 (v2) | 10^170 contro 10^80 | ok |
| C90 | 1 (v1) | avvocati di New York, 5.000 $ | ok |
| — | 1 (v2) | «900 milioni di utenti settimanali» | fuori raccolta, febbraio 2026 |

---

## 9. Impianto del libro

**Dimensioni:** 250-300 pagine, 70.000-90.000 parole, 4 parti, 16 capitoli, 15-20 pagine per capitolo (4.200-5.600 parole). Sotto le 200 pagine non c'è spazio per la parte tecnica; sopra le 350 il lettore non tecnico si perde a metà.

**Regola d'oro — due livelli separati, non una via di mezzo.**
Il testo principale è per tutti: nessuna formula, metafore ed esempi. Se una madre legge solo quello, deve capire tutto. I riquadri contengono formule, codice, dettagli: l'ingegnere li cerca, gli altri li saltano senza perdere il filo. Le derivazioni complete vanno in appendice.
Nel testo principale, al massimo **una formula per capitolo**, spiegata a parole (Hawking: ogni equazione dimezza le vendite; lui ne tenne una).

**Template fisso del capitolo — sette pezzi, in quest'ordine.**

1. **Aggancio** (~1 pagina): un aneddoto vero o una scena.
2. **La domanda del capitolo**, in una riga.
3. **Spiegazione** con una metafora quotidiana.
4. **Sotto il cofano**: la formula o il codice vero, dieci righe che girano.
5. **Provalo tu**: un esperimento da fare subito.
6. **Per chi ama pensare**: la domanda che resta aperta.
7. **In tre righe**: il riassunto finale.

Riquadro opzionale: **Curiosità**, per far respirare la pagina.

**L'esempio ricorrente:** «Il gatto ha mangiato il topo perché aveva fame.» Introdotta alla fine del cap. 1, va smontata capitolo per capitolo — i token nel 5, i vettori nel 6, l'attenzione nell'8. È l'appiglio del lettore non tecnico e il filo della pipeline per l'ingegnere.
**L'aggancio del prologo:** «buona» → «notte» sulla tastiera del telefono.

### Indice (proposta)

- **Prologo** — la tastiera che suggerisce «notte» dopo «buona».
- **Parte I, Da dove viene:** 1. Il sogno di calcolare il pensiero; 2. Markov e le vocali di Puškin; 3. Shannon, l'informazione è sorpresa; 4. Turing, i neuroni di carta, gli inverni.
- **Parte II, Come funziona:** 5. I token; 6. Gli embedding; 7. La discesa del gradiente; 8. L'attenzione e il Transformer; 9. Pre-training, dati, GPU; 10. Fine-tuning e RLHF; 11. La temperatura e il sampling.
- **Parte III, Ignorante ma eloquente:** 12. Le allucinazioni; 13. Bias e figuracce; 14. Usarla bene: prompt, contesto, agenti, modelli in locale.
- **Parte IV, Che cosa significa:** 15. Capisce davvero?; 16. E adesso?
- **Epilogo + appendici:** glossario, formule, cronologia, letture.

La Parte III è quella che i lettori racconteranno agli amici. Il cap. 14 è il punto in cui l'esperienza da sistemista vale più che altrove (VRAM, quantizzazione, agenti su infrastruttura vera): quasi nessun libro divulgativo lo sa spiegare dall'interno.

### Il PDF come fonte storica

`prima-della-prossima-parola.pdf` (7 pagine) contiene nove quadri:

1. Il sogno di calcolare il pensiero (1305-1843) — Lullo, Leibniz, Swift, Lovelace
2. Una formula scolpita su una tomba (1870-1906) — Boltzmann, l'entropia, la softmax
3. Il matematico ribelle (1906-1913) — Markov, Nekrasov, le 20.000 lettere dell'*Onegin*
4. Turing (1936-1952) — macchina universale, Enigma, gioco dell'imitazione
5. Neuroni di carta e il gioco della prossima lettera (1943-1951) — McCulloch, Pitts, Shannon, Theseus
6. Nasce l'«intelligenza artificiale» (1955-1990) — Dartmouth, percettrone, inverni, ELIZA, Searle, retropropagazione, Jelinek
7. Le parole diventano luoghi (1953-2013) — Wittgenstein, Harris, Firth, Bengio, word2vec
8. *Attention Is All You Need* (2014-oggi) — Bahdanau, Transformer, GPT, ChatGPT, Nobel 2024
9. Epilogo e cronologia essenziale

Il PDF usa già tre tipi di riquadri (CURIOSITÀ, PER L'INFORMATICO, PER CHI AMA PENSARE) che corrispondono al template. Le formule del PDF vanno nei «Sotto il cofano».

**Attenzione a un dettaglio:** per Turing, il PDF scrive che l'interrogatore avrebbe indovinato nel 70% dei casi; altre fonti dicono che la macchina avrebbe ingannato nel 30%. È la stessa previsione letta dai due lati: scegliere una formulazione e non alternarle.

### Stato al 22 ottobre 2026

**Cambio di impianto:** non sono tre stesure dello stesso libro, sono **tre libri diversi**. Stessa cronologia di fondo (scoperta → nascita → funzionamento → evoluzioni), ma capitoli, protagonisti e tagli differenti. Vedi §10.

Fatto: **prologo + capitolo 1 di tutti e tre i libri**, impaginati.
- Libro 1: 13 pagine (3.202 parole)
- Libro 2: 14 pagine (3.594 parole)
- Libro 3: 15 pagine (3.475 parole)
(conteggi aggiornati al 22 ottobre 2026, dopo le correzioni del §11)

I capitoli sono ancora sotto le 15-20 pagine: manca una scena per ciascuno. Da fare quando si sceglie (o se si vogliono tutti e tre).

### Come si scrive un capitolo nuovo

1. Rileggere il quadro corrispondente del PDF e le curiosità assegnate nella mappa (§7).
2. Scegliere l'aggancio: una scena, non un concetto.
3. Scrivere la domanda in una riga. Se non sta in una riga, il capitolo non è pronto.
4. Buttare giù il testo principale senza formule.
5. Aprire il cofano: una formula o dieci righe di codice, verificate.
6. Progettare il «Provalo tu» in modo che fallisca in modo istruttivo.
7. Chiudere con la domanda aperta e con «In tre righe».
8. Passare ogni numero al protocollo del §2.

---

## 10. Tre libri, non tre stesure

Stessa cronologia di fondo — **scoperta → nascita → funzionamento → evoluzioni** — ma ogni libro ha capitoli, protagonisti e taglio propri. Cambia la porta d'ingresso sulla stessa storia, e cambia la misura dei capitoli.

### Libro 1 — *La nonna e il forno* (voce affettiva)
**Il libro delle mani.** Filo conduttore: il sapere che sta nelle dita e quello che sta nei libri. Ogni capitolo ruota intorno a un gesto: impastare, contare, indovinare, sbagliare, correggere, scegliere.

- **Prologo — Il pane** ✅ (una nonna dichiarata immagine, non memoir; «quanto basta», le mani)
- **Parte I, Le mani:** 1. Scrivere le regole (Lullo) ✅ · 2. Calculemus (Leibniz) · 3. Il riso di Swift e l'obiezione di Ada · 4. Il professore che contava le vocali (Markov) · 5. L'uomo che faceva indovinare le lettere (Shannon)
- **Parte II, Il mestiere:** 6. Il dado e la farina (Boltzmann, temperatura) · 7. Fare a pezzi le parole (token) · 8. Le parole diventano posti (embedding) · 9. Imparare sbagliando (gradiente) · 10. Guardare indietro (attenzione) · 11. Il forno (dati, GPU) · 12. Diventare gentili (RLHF)
- **Parte III, Quando la ricetta non riesce:** 13. La ricetta perfetta per il forno sbagliato (allucinazioni e pregiudizi) · 14. Cucinare con l'aiuto (uso, agenti)
- **Parte IV, Le mani della macchina:** 15. Che cosa sa una macchina che non ha mani · 16. Domani

### Libro 2 — *L'uomo che faceva indovinare le lettere* (voce saggistica)
**Il libro delle idee.** Filo conduttore: la staffetta. Chi ha aggiunto quale pezzo, e senza sapere che cosa stava costruendo.

- **Prologo — Tre parole** ✅ (la tastiera, «buona» → «notte»)
- **Parte I, Il sogno:** 1. Il sogno di calcolare il pensiero (Lullo, Leibniz, Swift, Lovelace) ✅ · 2. Una formula scolpita su una tomba (Boltzmann) · 3. Il matematico ribelle (Markov) · 4. L'informazione è sorpresa (Shannon) · 5. Le macchine possono pensare? (Turing, McCulloch-Pitts, inverni, ELIZA)
- **Parte II, La macchina:** 6. I token · 7. Gli embedding · 8. Imparare dagli errori (retropropagazione) · 9. L'attenzione è tutto ciò che serve · 10. La scala (dati, parametri, GPU) · 11. Diventare educati (RLHF e sampling)
- **Parte III, Ignorante ma eloquente:** 12. Le allucinazioni d'autore · 13. Bias e figuracce · 14. Usarla bene
- **Parte IV, Che cosa significa:** 15. Capisce davvero? · 16. E adesso?

### Libro 3 — *La stanza in cui non c'è nessuno* (voce reportage)
**Il libro dei luoghi.** Filo conduttore: le stanze. Ogni capitolo si apre in un posto e da lì tira il filo.

- **Prologo — La stanza** ✅ (l'Iowa, il calore, i cavi turchesi, l'acqua)
- **Parte I, Le stanze:** 1. La macchina di Lagado (Swift e Lullo) ✅ · 2. Vienna, cimitero centrale (Boltzmann) · 3. San Pietroburgo 1913 (Markov) · 4. Bletchley Park (Turing) · 5. La soffitta (inverni, ELIZA, stanza cinese)
- **Parte II, Le macchine:** 6. La catena di montaggio (token) · 7. La mappa (embedding) · 8. La discesa (gradiente) · 9. La sala macchine (Transformer) · 10. Il capannone (GPU, dati) · 11. Il collaudo (RLHF)
- **Parte III, I processi:** 12. Il tribunale (allucinazioni) · 13. Lo specchio (bias) · 14. Il banco di lavoro (uso)
- **Parte IV, Le stanze vuote:** 15. La stanza vuota (capisce?) · 16. Domani

### Regole di coerenza fra i tre libri
- **Le stesse verità di fondo, mai le stesse frasi.** Se un aneddoto serve a due libri, va raccontato da un'altra angolazione e con altre parole.
- **La frase ricorrente** («Il gatto ha mangiato il topo perché aveva fame») resta in tutti e tre: cambia il capitolo in cui viene smontata.
- **I numeri vengono dal §3 e dal §5**, non reinventati. Le cifre già usate restano quelle.
- **Ogni libro ha il suo capitolo 1**: Lullo per il 1, il sogno intero per il 2, Lagado per il 3. Non si sovrappongono.

---

## 11. Correzioni del 22 ottobre 2026 e punti ancora aperti

**Primo giro (errori verificati)** in Libro 2 e 3: 10.000⁵ = 10²⁰; «Volontà» e non «Amore»; Lullo laico, non frate; regola della catena 1676 e binario 1703; cronologie (Swift 10 anni dopo Leibniz, «quasi due secoli» fino a Markov, Turing poco più di un secolo dopo Lovelace, Deep Blue oltre 150 anni dopo); Terza Figura di 36 caselle; Boltzmann difensore degli atomi; cavi turchesi (multimodali OM3/OM4); probabilità sulla parola successiva e non su ogni frase; Borges senza «cieco».

**Secondo giro (ripasso dei dubbi)**
- Libro 1: aggressione dello schiavo «intorno al 1274» (prima: 1276), «poco più che quarantenne», «più di trent'anni dopo», tolto «Poteva comprarla, e l'ha comprata» (ora: «Doveva averla in casa… e quella persona, in quel caso, non era libera»); Miramar (1276) ora presentato come fondazione successiva. Turing riportato come nel testo del 1950 (confessione: conti fatti in fretta e male; errore dei filosofi: credere di conoscere subito tutte le conseguenze di un fatto).
- Libro 2 e 3: l'*Ars* iniziata nel 1274, forma definitiva 1305-08; Lullo propose anche una crociata (dal 1290, *Liber de passagio*); «una ne ha sette» → «la più antica ha più di tre secoli» (anche Libro 1); tolta la frase «Ho scritto le stesse cose due volte…»; riquadro «in otto righe»; «Provalo tu» senza previsioni sulle risposte dei modelli.
- Libro 2: ELIZA «quattrocento righe» (420 nel MAD-SLIP originale); I Ching: il disegno arriva da Pechino nel 1703, fu Bouvet ad accorgersi della corrispondenza.
- Libro 3: Iowa attribuito all'AP e ai dati dell'acquedotto (luglio 2022, 6%, mese prima della fine dell'addestramento di GPT-4), «una parte evapora»; tolti il rumore che sale a ogni richiesta, «un'altra stanza, vera», le dimensioni della sala e l'intera sezione «La bottega»; «e a volte le due cose coincidono» al posto dell'umanità che chiede l'ordine.
- Impaginatore: `build_capitoli.py` salta la riga `---`; `make_all.py` costruisce Libro 1 da `l1-v2-prologo-capitolo1.md` (rev 2).

**Ancora aperti — da decidere o verificare**
1. L1 — memoir: risolto. La nonna è inventata (confermato dall'autore il 22 ottobre 2026); il prologo è riscritto in seconda persona («Immaginate una nonna…»), senza ricordi personali né date.
2. L1 — coltello e suicidio dello schiavo: fonte unica (*Vita coaetanea*, 1311), da controllare sul testo critico. «Intorno al 1274» viene da una sola fonte secondaria (schiavo morto nel 1274), non dal testo.
3. L1/L2/L3 — Turing: parafrasi dalla sezione sull'obiezione di Lady Lovelace (1950) fatta a memoria; verificare sul testo.
4. L2/L3 — «Provalo tu»: previsioni tolte, ma l'esperimento va provato su 3-4 modelli e datato (§2.6). L1 «La macchina che sostiene tutto» conserva una previsione («Vi darà tre argomenti…»).
5. L3 — prologo: la sala resta una scena composita (armadi neri, ventole, due file); decidere se dichiararlo.
6. L2 — segretaria di ELIZA: da Weizenbaum a memoria, non verificata dalla ricerca.
7. L3 — «una parte evapora»: l'AP non dice quanta; la quota di acqua usata dall'addestramento resta ignota.
8. File superseduti, solo nella cartella locale: `l1-prologo-capitolo1.md` e i suoi DOCX/PDF senza «(rev 2)». Non rigenerarli.

**PDF:** stampati da Edge dall'HTML con `strumenti/md_to_pdf_edge.py`, con la stessa geometria del DOCX (15,24 × 22,86 cm), non convertiti dal DOCX: sulla macchina di lavoro LibreOffice e Word non c'erano. Edge va lanciato da una shell normale (dal sandbox di alcuni strumenti non scrive il PDF).

---

## 12. Valutazione critica e decisioni (22 ottobre 2026)

**Giudizio onesto sui tre prologhi + cap. 1** (circa il 4% del libro finale: giudicati voce, attacco e affidabilità, non il libro intero).
- Per il lettore doppio (non tecnico + ingegnere): **L1 > L2 > L3**.
  - **L1:** l'unica con una tesi (regole contro esempi), la più accurata, con umorismo vero. Debolezze: il tono sullo schiavo (corretto nel secondo giro) e il rischio memoir (risolto: la nonna è un'immagine).
  - **L2:** l'aggancio «buona → notte» è il più universale, ma il capitolo si ripete (Ada raccontata due volte, aforismi in grassetto vuoti) e aveva più errori.
  - **L3:** la prima pagina migliore, ma la scena è composita e la promessa (acqua, energia, hardware) non è mantenuta nel capitolo, che è storia pura.
- **Sovrapposizione:** nel cap. 1, L2 e L3 condividono circa il 45% delle frasi (82 su ~180); L1 il 12-16%. Viola §10 («mai le stesse frasi»): finché non cambia, sono due voci sullo stesso testo, non due libri.
- **Problema strutturale dei tre cap. 1:** circa 3.000 parole di storia antica (Lullo, Leibniz, Swift, Ada) prima che una macchina faccia qualcosa; poco umorismo; esempi quasi solo storici. Da valutare: anticipare la demo (il bigramma su Collodi) o il «quanto basta», e comprimere la storia.
- Gli errori verificati del §11 erano quasi tutti in L2 e L3; L1 era il più affidabile. Per l'ingegnere un errore numerico costa più di quanto rendano le curiosità.
- **Test consigliato prima di scegliere la voce:** le prime due pagine di ciascun libro, senza titoli, a 5 non tecnici e 3 ingegneri.

**Decisioni dell'autore:** la nonna è inventata (prologo di L1 in seconda persona, «Immaginate una nonna…»); i tre libri sono nel repo pubblico; la scelta fra le tre voci resta aperta.

**Prima di scrivere il prossimo capitolo:** rileggere §2 (protocollo numeri), §9 («Come si scrive un capitolo nuovo») e i punti ancora aperti del §11; verificare ogni fatto e ogni numero su fonte, non a memoria.
