# Prossima parola, prego

### Viaggio tra le allucinazioni d’autore di un’IA ignorante ma straordinariamente eloquente

Il 21 maggio 2015 un ricercatore di nome **Andrej Karpathy** fece un esperimento che ogni genitore capisce al volo.

Prese una creatura che non sapeva niente.

Le diede da leggere un romanzo enorme.

E si mise a guardare cosa succedeva.

La creatura era una rete neurale.

Il romanzo era *Guerra e pace*.

Il compito, **uno solo**:

> *Dato quello che hai letto finora, qual è la lettera successiva?*

Non la parola.

La **lettera**.

La rete non sapeva cos'era una parola.

Non sapeva cos'era una frase.

Non sapeva che Tolstoj fosse russo, né che ci fosse una guerra.

Per lei il mondo era una fila di caratteri, e il suo mestiere era scommettere su quello dopo.

---

Karpathy ebbe la gentilezza di mostrare la rete a vari momenti dell'addestramento.

È uno dei documenti più commoventi della storia dell'informatica.

Un po' come guardare un bambino che impara a parlare, ma con la pazienza di chi non ha ancora un lavoro.

**Iterazione 100.**

Grovigli di lettere.

L'autore li chiama, con pudore anglosassone, *random jumbles*.

**Iterazione 300.**

Comincia a capire le virgolette e i punti.

Non sa cosa dicono.

Sa dove vanno.

**Iterazione 500.**

Le prime parole.

Cortissime.

*we*.

*He*.

*His*.

Il linguaggio degli uomini preistorici e dei programmatori in ritardo.

**Verso l'iterazione 2000.**

Parole scritte bene.

Virgolette.

Nomi propri.

E una frase che comincia così:

> *«Why do what that day,» replied Natasha, and wishing to himself the fact the…*

«Perché fare ciò che quel giorno», rispose Natasha, e desiderando a sé stesso il fatto il…

Si ferma lì, senza sostantivo, come l'ultima riga di un registro dopo un riavvio brusco. [DA VERIFICARE: il campione parola per parola, sul post di Karpathy]

Non vuol dire niente.

Ma è **formalmente perfetta**.

Ha l'aria di una conversazione.

Ha un personaggio.

Ha perfino un dolore sepolto da qualche parte.

Una frase così, in un romanzo ambizioso, si prende il premio.

---

La cosa più bella, però, è che nessuno aveva spiegato niente alla rete.

Non c'era un dizionario.

Non c'era una grammatica.

Non c'era un insegnante che dicesse: *le virgolette si chiudono*.

Era soltanto una macchina che cercava di sbagliare un po' meno a indovinare il carattere successivo.

E per sbagliare meno, **doveva scoprire le regole da sola**.

Karpathy provò con altri testi.

Con tutto Shakespeare, circa 4,4 milioni di caratteri: ne uscirono battute con il nome di chi parla, i due punti al posto giusto e parole inventate con grande disinvoltura.

Con un libro di geometria algebrica scritto in LaTeX, il linguaggio con cui i matematici impaginano le formule: il risultato, scrive lui, *quasi compila*, dopo qualche ritocco a mano.

Quando la rete si trova davanti a una dimostrazione difficile, a un certo punto decide di saltarla.

Scrive:

> *Proof omitted.*

Dimostrazione omessa.

Un comportamento che molti studenti di matematica riconoscerebbero con una certa commozione.

---

Poi arrivò il codice del **kernel di Linux**.

Mezzo gigabyte di C, il linguaggio con cui è scritto il cuore di mezzo mondo informatico.

La rete era minuscola, circa dieci milioni di parametri: il massimo che entrava nella scheda video di Karpathy.

Il suo campione cominciò con la licenza **GNU**, il testo legale del software libero, recitata carattere per carattere.

Poi generò inclusioni, macro, parentesi aperte e chiuse con precisione.

Karpathy ammette serenamente di non credere che quel codice compili.

Un difetto ricorrente: **non riusciva a tenere traccia dei nomi delle variabili**.

Come un collega che ti ha spiegato tutto nella riunione, e al ritorno alla scrivania non ricorda come si chiama il progetto.

Ma tieni a mente la licenza.

Recitata a memoria.

Quasi senza esitazioni.

Perché per una macchina addestrata a indovinare il carattere successivo, dopo le prime parole di quella licenza il seguito è praticamente obbligato.

La previsione è facile.

La frase la conosce.

> *Prevedere bene è ricordare che il resto, di solito, viene dopo.*

---

Il momento che mi piace di più, però, è nascosto in mezzo al post, quasi di passaggio.

Karpathy addestrò una rete anche su Wikipedia.

Il campione che ne uscì conteneva un indirizzo web.

Perfetto.

Con il prefisso giusto, il dominio giusto, la dignità di un indirizzo vero.

E scrisse, quasi di passaggio, una frase che oggi ha il sapore di una profezia:

> *L'indirizzo non esiste. Il modello se l'è semplicemente allucinato.*

(L'originale dice *the model just hallucinated it*.)

Siamo nel **maggio 2015**.

La parola *allucinazione* è già lì.

Sette anni prima di ChatGPT.

Quando nessuno, a parte qualche ricercatore, sapeva cosa fosse un modello linguistico.

Una macchina che inventa un indirizzo, perfettamente verosimile, per un posto che non esiste.

E lo fa con la stessa naturalezza con cui ricorda la licenza GNU.

È quasi una delle idee fondamentali di questo libro:

> *Per un modello, ricordare e inventare sono la stessa mossa. Cambia soltanto se il seguito, per caso, è vero.*

---

Passarono due anni.

Nel 2017 **Alec Radford, Rafal Jozefowicz e Ilya Sutskever** addestrarono una rete con lo stesso compito, a indovinare il carattere successivo, ma su oltre **82 milioni di recensioni di prodotti** di Amazon.

Un mese di calcolo su quattro schede video.

Facciamo il conto, perché è bello.

12.500 caratteri al secondo.

Per 30 giorni, cioè 2.592.000 secondi.

Fa **32,4 miliardi di caratteri**: più o meno una passata sull'intero archivio di circa 38 miliardi di byte.

Una passata.

Dopo un mese.

E a quel punto, dentro la rete, accadde una cosa che nessuno aveva chiesto.

Tra le **4.096 unità** interne, ne comparve una, la numero 2388 nel codice di dimostrazione, che si comportava in modo diverso a seconda che la recensione fosse **positiva o negativa**.

Nessuno le aveva insegnato che cos'è un sentimento.

Nessuno le aveva insegnato niente.

Le era stato chiesto soltanto:

*che lettera viene dopo?*

E per rispondere bene a questa domanda, in mezzo a milioni di recensioni, **era comodo capire se il cliente fosse contento**.

---

Qui la storia diventa interessante.

E, per un sistemista, un po' preoccupante.

Perché nessuno ha *programmato* quella unità.

È comparsa.

Come una abitudine dentro una persona che nessuno aveva deciso di addestrare.

Un modello che impara a prevedere qualcosa finisce per costruirsi dentro un po' di mondo.

Non tutto.

Non per forza quello giusto.

Ma abbastanza da stupire chi lo ha costruito.

Ed è per questo che la frase «è *solo* statistica» è metà verità e metà alibi.

Sì, dentro ci sono moltiplicazioni.

Un numero indecente.

Ma moltiplicando abbastanza, per abbastanza tempo, su abbastanza testo, escono cose che somigliano alla comprensione.

E a volte, invece, escono cose che somigliano soltanto a un indirizzo web inventato.

Con la stessa identica sicurezza.

Prossima lettera, prego.

> *Un modello non distingue ciò che ricorda da ciò che gli suona giusto. È una dote che gli umani riconoscono subito: la usano da sempre al bar.*

E da qui, davvero, comincia questo libro.
