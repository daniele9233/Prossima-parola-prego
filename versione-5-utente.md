# Prossima parola, prego

### Viaggio tra le allucinazioni d’autore di un’IA ignorante ma straordinariamente eloquente

Tutto cominciò molto prima che qualcuno pronunciasse le parole *intelligenza artificiale*.

E, soprattutto, cominciò in maniera decisamente meno affascinante di quanto Hollywood avrebbe desiderato.

Niente robot coscienti.

Niente laboratorio sotterraneo.

Nessun ricercatore che, durante un temporale, alza una leva, osserva una creatura attraversata da scariche elettriche e grida:

«È viva!»

C’era invece un matematico russo che contava lettere.

Che, bisogna ammetterlo, come scena iniziale vende decisamente meno biglietti.

La cosa buffa è che bisogna tornare addirittura al **1913**, quando Andrej Andreevič Markov decise di prendere un capolavoro della letteratura russa e sottoporlo a un trattamento che nessun poeta avrebbe probabilmente gradito:

trasformarlo in statistica.

Il testo era *Eugenio Onegin* di Aleksandr Puškin.

Markov prese un campione di **20.000 lettere** e cominciò ad analizzare il modo in cui vocali e consonanti si susseguivano.

Ventimila.

Lettere.

Una per una.

Oggi probabilmente scriverebbe venti righe di Python, aprirebbe un Jupyter Notebook e chiamerebbe il file:

`analisi_finale_v3_VERAMENTE_FINALE.ipynb`

Nel 1913 lo fece sostanzialmente a mano.

Voleva verificare una cosa precisa: la probabilità che comparisse una vocale dipendeva da ciò che era apparso immediatamente prima?

La risposta era sì.

Le lettere non si susseguivano come palline estratte casualmente da un sacchetto.

C’era una struttura.

Il presente conteneva informazioni sul futuro.

Non abbastanza per prevederlo con certezza, ma abbastanza per assegnargli delle probabilità.

Era una delle applicazioni concrete di quelle che oggi chiamiamo **catene di Markov**.

E qui compare già una delle idee che attraverserà tutta la nostra storia:

> *Prevedere non significa sapere cosa accadrà. Significa sapere cosa ha più probabilità di accadere.*

Sembra una distinzione filosofica.

Tra qualche pagina scopriremo che è anche la ragione per cui un'intelligenza artificiale può spiegare perfettamente la fisica quantistica e, cinque minuti dopo, inventare con grande dignità accademica un libro che non è mai stato scritto.

Ma non anticipiamo.

Nel **1948**, trentacinque anni dopo Markov, entrò in scena uno dei personaggi più straordinari dell’intera storia dell’informatica.

**Claude Shannon.**

Matematico.

Ingegnere.

Crittografo.

Fondatore della teoria dell’informazione.

E, apparentemente, persona incapace di avere un hobby normale.

Ai Bell Labs Shannon era noto per attraversare i corridoi in **monociclo mentre faceva il giocoliere**.

Non è una metafora.

Lo faceva davvero.

Questo significa che mentre altri ricercatori stavano probabilmente andando a una riunione con una cartellina sotto il braccio, uno degli uomini che avrebbe posto le fondamenta matematiche del mondo digitale poteva superarli su una ruota sola lanciando palline in aria.

C’è qualcosa di rassicurante in tutto questo.

Shannon costruiva anche macchine per giocoleria, dispositivi eccentrici, giocava a scacchi e sperimentava continuamente con oggetti meccanici.

Nel 1950 costruì persino **Theseus**, un piccolo topo elettromeccanico capace di muoversi attraverso un labirinto e ricordare il percorso corretto dopo averlo trovato.

Uno dei primi esempi di macchina capace di mostrare un rudimentale comportamento di apprendimento.

L’uomo che contribuì a fondare la teoria dell’informazione costruì quindi anche un topo che imparava i labirinti.

A questo punto possiamo probabilmente perdonargli il monociclo.

Nel 1948 Shannon pubblicò *A Mathematical Theory of Communication*, uno dei lavori più importanti della storia dell’informatica.

Non stava cercando di costruire ChatGPT.

Non stava nemmeno cercando di costruire un’intelligenza artificiale conversazionale.

Stava cercando di capire qualcosa di più fondamentale:

**che cos’è l’informazione?**

E soprattutto:

**quanto è prevedibile?**

Shannon studiò anche la struttura statistica della lingua inglese.

Se conosciamo alcune lettere precedenti, quanto possiamo indovinare quella successiva?

Se conosciamo alcune parole, quanto diventa prevedibile ciò che viene dopo?

Per mostrarlo propose persino un procedimento manuale che oggi sembra l’esperimento di qualcuno a cui è stato temporaneamente sequestrato il computer.

Si prende un libro.

Lo si apre a caso.

Si sceglie una lettera.

Poi si apre un’altra pagina, si cerca quella stessa lettera e si annota quella che la segue.

Poi si utilizza la nuova lettera e si ricomincia.

Ancora.

Ancora.

Ancora.

Shannon scrisse che sarebbe stato interessante spingersi verso approssimazioni ancora più sofisticate, ma che il lavoro necessario sarebbe diventato enorme.

Traduzione moderna:

**serviva un computer.**

Possibilmente grosso.

Molto grosso.

Ma il punto era ormai evidente.

**Il linguaggio possiede una struttura statistica.**

La cosa forse meno romantica — e quindi naturalmente più interessante — è che il linguaggio umano, per quanto ci piaccia immaginarlo intriso di anima, creatività, poesia e trascendenza, è terribilmente abitudinario.

Se qualcuno dice:

«Pane e…»

il nostro cervello non aspetta educatamente.

Ha già aperto un casinò clandestino.

*Burro* riceve parecchie puntate.

*Marmellata* può giocarsela.

*Termodinamica* viene accompagnata gentilmente all’uscita.

Non perché conosciamo il futuro.

Perché conosciamo abbastanza bene il passato.

Shannon aveva dato una forma matematica a qualcosa che il nostro cervello fa continuamente senza chiedere autorizzazione.

Ed eccolo lì, quasi settant’anni prima di ChatGPT, il principio che ancora oggi si nasconde dietro un modello linguistico:

**cosa viene dopo?**

---

Naturalmente c’era un problema.

Anzi, qualche miliardo.

Il linguaggio contiene un numero mostruoso di combinazioni possibili.

Per molto tempo uno degli strumenti più importanti furono gli **n-grammi**.

L’idea era relativamente semplice.

Se voglio prevedere una parola, guardo le ultime parole che la precedono e controllo statisticamente che cosa tende ad arrivare dopo.

Prendiamo:

**«Il gatto è sul…»**

Nel nostro archivio magari troviamo spesso:

*divano.*

*letto.*

*tetto.*

Molto più raramente:

*ministero dell’Economia.*

Il modello può quindi assegnare probabilità diverse.

Funziona.

Finché il contesto rimane piccolo.

Il problema è che aumentando il numero delle parole da ricordare aumenta vertiginosamente anche il numero delle combinazioni possibili.

Il linguaggio reagisce molto male a chi cerca di metterlo dentro una tabella.

Gli esseri umani continuano ostinatamente a inventare frasi che nessuno aveva mai pronunciato prima.

Un comportamento francamente poco collaborativo.

Serviva qualcosa capace di **generalizzare**.

Ed entrarono in scena le reti neurali.

---

Le **Reti Neurali Ricorrenti**, o RNN, sviluppate già negli anni Ottanta e poi utilizzate sempre più per elaborare sequenze, sembravano una soluzione naturale.

Funzionavano in modo intuitivo.

Una parola alla volta.

Da sinistra verso destra.

Ogni passaggio produceva uno stato interno che poteva influenzare quello successivo.

In un certo senso la rete portava con sé una piccola memoria di ciò che aveva appena letto.

Sembrava perfetto.

Solo che quella memoria aveva un piccolo difetto:

tendeva a essere quella di qualcuno alla fine di una riunione Teams di tre ore.

Le RNN tradizionali faticavano infatti a imparare relazioni tra eventi molto distanti all’interno di una sequenza.

Uno dei responsabili aveva un nome meravigliosamente drammatico:

**gradiente evanescente.**

Durante l’addestramento, il segnale matematico che permette alla rete di capire quanto gli eventi precedenti abbiano contribuito a un errore viene propagato all’indietro.

Ma attraversando molti passaggi può diventare sempre più piccolo.

E ancora più piccolo.

E ancora.

Finché praticamente scompare.

È un po’ come ricevere una telefonata:

«Abbiamo un problema causato da qualcosa successo sei mesi fa.»

«Cosa?»

«Non ricordo più.»

Nel **1997**, Sepp Hochreiter e Jürgen Schmidhuber pubblicarono una delle soluzioni più importanti al problema:

**Long Short-Term Memory.**

LSTM.

Un nome che sembra contemporaneamente una tecnologia di intelligenza artificiale e qualcosa che il medico potrebbe trovare nelle analisi del sangue.

Le LSTM erano particolari reti ricorrenti progettate proprio per rendere possibile l’apprendimento di dipendenze molto più lunghe e contrastare i problemi legati al flusso del gradiente.

Funzionavano molto meglio.

E per anni LSTM e altre architetture ricorrenti furono protagoniste del riconoscimento vocale, della traduzione automatica e dell’elaborazione del linguaggio.

Ma rimaneva un altro problema.

Questa volta non era la memoria.

Era il tempo.

Le reti ricorrenti avevano un carattere profondamente sequenziale.

Per elaborare il passaggio numero 100 bisognava prima calcolare il 99.

Per arrivare al 99 serviva il 98.

E prima ancora il 97.

Una parola dopo l’altra.

Una dopo l’altra.

Una dopo l’altra.

Per un essere umano leggere così è perfettamente normale.

Per una macchina dotata di migliaia di unità di calcolo è una situazione piuttosto frustrante.

È come assumere mille operai e poi comunicare:

«Perfetto. Adesso lavorate uno alla volta.»

---

Nel frattempo, nel **2003**, Yoshua Bengio, Réjean Ducharme, Pascal Vincent e Christian Jauvin pubblicarono *A Neural Probabilistic Language Model*.

Fu un altro passaggio fondamentale.

L’idea era elegante.

Invece di considerare ogni parola come un simbolo completamente isolato, una rete neurale poteva imparare delle **rappresentazioni numeriche distribuite**.

In parole semplici, ogni parola poteva essere rappresentata attraverso numeri che permettevano alla rete di catturare alcune somiglianze e regolarità.

La macchina non sapeva realmente che cosa fosse un cane.

Non ne aveva mai accarezzato uno.

Non aveva mai lanciato una pallina a un Labrador.

Ma poteva imparare che *cane* compariva in contesti più simili a *gatto* che a *cacciavite*.

Non è coscienza.

Ma considerando che eravamo partiti da qualcuno che contava vocali in Puškin, possiamo concederci un moderato entusiasmo.

Il problema continuava a essere lo stesso.

**Il calcolo.**

I modelli neurali richiedevano enormi quantità di moltiplicazioni tra matrici.

E le macchine dell’epoca, rispetto a ciò che sarebbe arrivato dopo, avevano mezzi limitati.

Le idee correvano più velocemente dell’hardware.

> *A volte una tecnologia non deve aspettare che qualcuno abbia l’idea giusta. Deve aspettare che costruire quell’idea smetta di essere impraticabile.*

E poi accadde qualcosa di meravigliosamente umano.

Arrivarono i videogiochi.

---

Per decenni l’industria informatica investì cifre gigantesche per rispondere a una necessità fondamentale della civiltà moderna:

**far esplodere le cose sullo schermo in maniera sempre più realistica.**

Ombre.

Texture.

Riflessi.

Milioni di triangoli.

Capelli mossi dal vento.

Pozzanghere che riflettono correttamente la luce.

Tutto questo richiedeva un tipo particolare di hardware:

la **GPU**.

La CPU tradizionale possiede relativamente pochi core molto potenti e versatili.

Una GPU segue una filosofia diversa: moltissime unità di calcolo capaci di eseguire contemporaneamente enormi quantità di operazioni simili.

Ed era esattamente ciò di cui avevano bisogno le reti neurali.

Perché dietro parole come *apprendimento*, *rete neurale* e *intelligenza artificiale* si nasconde una realtà assai meno mistica:

un numero indecente di moltiplicazioni.

Matrici.

Matrici ovunque.

A un certo punto divenne evidente che l’hardware costruito per renderizzare mostri, automobili e fucili virtuali poteva essere utilizzato anche per l’algebra lineare necessaria alle reti neurali.

Non fu una coincidenza improvvisa né un colpo di fortuna isolato: il calcolo general-purpose su GPU si stava sviluppando già negli anni Duemila.

Con strumenti come **CUDA di NVIDIA**, lanciato nel 2006 e reso disponibile agli sviluppatori nel 2007, sfruttare quella potenza divenne enormemente più pratico.

E nel **2012** arrivò uno dei momenti simbolici della rivoluzione del deep learning.

Alex Krizhevsky, Ilya Sutskever e Geoffrey Hinton presentarono **AlexNet** alla competizione ImageNet.

La rete ottenne risultati nettamente migliori rispetto agli approcci concorrenti basati sulle tecniche tradizionali di computer vision.

E sapete con cosa venne addestrata?

**Due NVIDIA GTX 580 da 3 GB.**

Il training durò circa **cinque o sei giorni**.

Due schede video.

Oggi una GTX 580 è il tipo di oggetto che un appassionato di hardware potrebbe trovare in garage e osservare per qualche secondo chiedendosi:

«La butto o magari serve ancora a mio cugino?»

Nel 2012 aveva contribuito a cambiare la direzione dell’intelligenza artificiale.

I videogiochi non inventarono il deep learning.

Ma l’enorme sviluppo delle GPU fornì alle reti neurali un motore straordinariamente adatto.

È una delle ironie più belle di tutta la storia.

Una parte della rivoluzione dell’intelligenza artificiale passò anche dalla nostra necessità di vedere ombre migliori in *Crysis*.

La civiltà avanza per strade misteriose.

---

E qui bisogna sfatare una leggenda.

**No, ChatGPT non esisteva già negli anni Novanta dentro un cassetto, in attesa che qualcuno comprasse una scheda video abbastanza potente.**

Le idee fondamentali erano sparse sul tavolo.

La probabilità.

Le catene di Markov.

I modelli linguistici.

Le reti neurali.

Le RNN.

Le LSTM.

Le rappresentazioni distribuite.

GPU sempre più potenti.

Mancavano però ancora parecchi ingredienti.

Grandi quantità di testo digitalizzato.

Hardware economicamente utilizzabile su larga scala.

Tecniche di ottimizzazione migliori.

Software.

Infrastrutture.

E soprattutto mancava un modo radicalmente migliore di elaborare le sequenze.

Poi arrivò il **2017**.

---

Otto ricercatori pubblicarono un paper dal titolo che oggi sembra quasi meno un articolo scientifico e più una provocazione:

# Attention Is All You Need

Ashish Vaswani.

Noam Shazeer.

Niki Parmar.

Jakob Uszkoreit.

Llion Jones.

Aidan Gomez.

Łukasz Kaiser.

Illia Polosukhin.

Otto nomi.

Una frase.

E una quantità considerevole di conseguenze.

Il **Transformer** abbandonava la ricorrenza utilizzata dalle RNN e si basava sui meccanismi di **attention**.

In particolare, attraverso la *self-attention*, il modello poteva mettere direttamente in relazione punti differenti della sequenza.

Consideriamo:

«Luca ha preso il portatile dalla scrivania perché **gli** serviva per lavorare.»

Per interpretare correttamente *gli*, il modello deve collegarlo a *Luca*.

Una parola può quindi avere importanza per un’altra che si trova parecchie posizioni più lontano.

L’attention consente al modello di stabilire quali parti della sequenza siano più rilevanti per interpretarne altre.

Naturalmente dietro la parola *attention* non c’è un piccolo omino dentro il computer che sottolinea le frasi con l’evidenziatore.

Ci sono matrici.

Di nuovo.

Mi dispiace.

La magia durerà pochissimo in questo libro.

Ma il Transformer aveva un vantaggio gigantesco.

Durante l’addestramento era molto più facilmente **parallelizzabile** rispetto alle architetture ricorrenti.

Gli stessi autori mostrarono che poteva ottenere risultati migliori riducendo notevolmente i tempi di training.

Finalmente potevamo dire a migliaia di unità di calcolo:

«Lavorate tutte insieme.»

E loro, essendo processori e non colleghi d’ufficio, lo facevano realmente.

---

Un anno dopo, nel **2018**, OpenAI prese quell’architettura e la combinò con un’altra idea fondamentale:

il **pre-training**.

Nacque il primo **GPT**.

*Generative Pre-trained Transformer.*

Tre parole che presto sarebbero diventate piuttosto importanti.

L’idea di fondo era quasi offensivamente semplice.

Dargli moltissimo testo.

Mostrargli una sequenza.

Nascondere ciò che viene dopo.

E chiedergli di indovinarlo.

Prendiamo:

**«Roma è la capitale…»**

Il modello deve assegnare delle probabilità alle possibili continuazioni.

*d’Italia.*

*italiana.*

*del paese.*

*di Saturno.*

Durante l’addestramento confronta la propria previsione con ciò che nel testo veniva realmente dopo.

Se sbaglia, i suoi parametri vengono modificati leggermente.

Poi riprova.

E riprova.

E riprova.

Milioni.

Miliardi.

Miliardi di miliardi di calcoli.

Parametri che vengono continuamente aggiustati di quantità minuscole.

Finché la rete comincia a catturare una quantità impressionante di regolarità.

Grammatica.

Sintassi.

Stile.

Relazioni tra parole.

Strutture del codice.

Schemi logici.

Informazioni sul mondo presenti nei testi.

E qui la storia assume una forma quasi comica.

Perché dopo più di un secolo di matematica, probabilità, neuroscienze computazionali, informatica, miliardi di dollari in hardware, data center grandi come capannoni industriali e alcune delle menti più brillanti del pianeta, il compito fondamentale poteva ancora essere sintetizzato così:

**«Prossima parola, prego.»**

Anzi.

Per essere precisi:

**«Prossimo token, prego.»**

Solo che, ripetendo quel gioco un numero sufficientemente assurdo di volte, era emerso qualcosa che nessuno dei primi esperimenti di Markov avrebbe potuto mostrare.

La macchina riusciva a scrivere.

Tradurre.

Riassumere.

Programmare.

Rispondere a domande.

Spiegare la relatività.

Imitare Shakespeare.

Scrivere una query SQL.

Correggere una configurazione Kubernetes.

Probabilmente anche spiegare perché quella configurazione Kubernetes non funzionava.

Il che, in alcuni ambienti professionali, è già molto vicino alla definizione operativa di intelligenza.

Eppure mancava qualcosa.

Qualcosa di enormemente importante.

Il modello poteva parlare di Roma senza esserci mai stato.

Descrivere il sapore di una pesca senza averne mai assaggiata una.

Scrivere del dolore senza aver mai sofferto.

Spiegare la paura senza aver mai avuto nulla da perdere.

E soprattutto poteva rispondere a una domanda senza possedere, nel senso umano del termine, un archivio interno dove andare a controllare:

**«Questa cosa è vera?»**

Perché un modello linguistico non nasce con l’obiettivo fondamentale di dire la verità.

Nasce imparando quale continuazione sia plausibile.

Ed ecco il secondo piccolo aforisma che conviene tenere a mente prima di proseguire:

> *L’eloquenza è la capacità di sembrare convincenti. La verità è un problema completamente diverso.*

Gli esseri umani lo avevano già dimostrato abbondantemente molto prima dell’arrivo dell’intelligenza artificiale.

Gli LLM hanno semplicemente automatizzato il processo.

Ed è qui che appare la caratteristica più affascinante, divertente e pericolosa di queste macchine.

Quando sanno una cosa, possono raccontarla magnificamente.

Quando non la sanno…

possono raccontarla magnificamente lo stesso.

Tra:

**«questa risposta è vera»**

e

**«questa risposta sembra esattamente quella che dovrebbe venire dopo»**

esiste una distanza minuscola quando tutto funziona.

E un abisso quando non funziona.

Quell’abisso ha un nome.

**Allucinazione.**

Ed è proprio lì dentro che comincia questo libro.
