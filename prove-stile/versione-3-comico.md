- **Voce:** il comico: battute e aforismi a ritmo da cabaret, ma sempre esatti; si ride delle macchine, dell'hype e di noi umani, mai del lettore.
- **Densità di battute:** altissima: 21 battute, circa una ogni 70 parole.
- **Analogie usate:** la tastiera del telefono che cresce fino a leggere mezza biblioteca (madre); le manopole di un mixer (i parametri); il brindisi dell'epigrafe, richiamato nella parte 3; l'eliminacode dello sportello (la gag del titolo).

---

# Capitolo 1 — Il completamento automatico più costoso della storia

> Un LLM parla come chi improvvisa un brindisi: una parola alla volta, e senza poter cancellare.

<!-- parte: aggancio -->

## Tre parole e una mail

Sul telefono scrivi «Ci vediamo». La tastiera, premurosa, ti offre tre parole: «domani», «alle», «presto». Ne tocchi una e ne arrivano altre tre. È il completamento automatico: un software che indovina cosa stai per scrivere. Di solito ci prende. Quando sbaglia, un «ti voglio bene» finisce nella mail al capo.

Ora immagina la sera prima dell'assemblea di condominio. L'unica cosa che vuoi è non andarci. Apri un'intelligenza artificiale (IA) e scrivi: «Scrivi una mail formale all'amministratore di condominio per rinviare l'assemblea.» È la richiesta del Prologo e ci seguirà per tutto il libro. Dopo pochi secondi hai una lettera intera: saluto, motivazione, scuse, proposta di una nuova data, distinti saluti. Burocratese impeccabile, senza il minimo imbarazzo: a un umano serve una carriera.

Ecco il mistero. La tastiera indovina una parola e poi si ferma ad aspettare te. L'IA scrive una lettera senza che tu tocchi niente, e sembra aver capito cos'è un condominio. Il resto del mondo la chiama rivoluzione; noi, per un capitolo, useremo il suo nome di battesimo: completamento automatico. Costosissimo, ma sempre completamento.

Possono essere la stessa cosa? Sì. La risposta è semplice, è vera, e a sentirla sembra una presa in giro. Non lo è: vediamo perché.

<!-- parte: analogia madre -->

## La tastiera che ha letto mezza biblioteca

Un *Large Language Model* (LLM, «modello linguistico di grandi dimensioni») fa una cosa sola: prevede il prossimo pezzo di testo. Una. Non ha un reparto mail, un reparto poesie e un reparto scuse al capo. Ha un mestiere solo, e lo svolge senza ferie.

Parti dalla tastiera. Da anni i suggerimenti degli smartphone sono piccole reti neurali, cioè modelli fatti di numeri regolabili, che hanno imparato da testi di esempio quali parole tendono a seguirne altre. Caso documentato: Gboard, la tastiera di Google, con un modello di linguaggio per predire la parola successiva (Hard e altri, 2018). Se scrivi «Ci vediamo», propone «domani» perché nei testi da cui ha imparato quella parola segue spesso: non sa cos'è un appuntamento. In questo assomiglia a certi amici. Un modello di linguaggio ce l'hai in tasca da anni, e noi lo usiamo soprattutto per rispondere «ok».

Adesso fallo crescere. Al posto di quattro chiacchiere da leggere, mezza biblioteca. Al posto di poche parole di contesto (il contesto è quanto testo ha davanti mentre prevede), pagine intere. Sotto, un'architettura nuova, il *Transformer* (cap. 4). Il mestiere non cambia; cambiano la scala (dati, parametri, contesto) e l'architettura. La tastiera ha fatto le elementari, l'LLM ha letto mezza biblioteca. Le differenze di cultura si notano.

Dentro il modello ci sono numeri, i parametri, detti anche pesi: pensali come le manopole di un *mixer* (il banco del tecnico del suono). «8B» vuol dire circa 8 miliardi di manopole (la B è *billion*, miliardo). Una sola non fa la canzone; conta l'insieme. Nessun tecnico del suono ne gira otto miliardi, e infatti non lo fa un tecnico: lo fa l'addestramento (cap. 6). Mentre conversi, restano ferme.

<!-- parte: cosa succede davvero -->

## Un giro, poi un altro, poi un altro ancora

Il ciclo ha quattro mosse. Il modello legge tutto il testo che ha davanti e dà un punteggio a ogni pezzo possibile. Ne sceglie uno (come, lo vedremo nel cap. 10). Lo attacca in coda al testo. Il testo allungato rientra come nuovo *input*, cioè ciò che il modello deve leggere, e si ricomincia fino alla fine.

Pezzo, in realtà, si dice *token*: un frammento di testo, che può essere una parola, mezza parola, un segno di punteggiatura. Il modello non legge lettere né parole intere (ne parliamo nel cap. 2). I punteggi si leggono come probabilità: sommano 1, cioè 100%, quindi se un candidato sale, gli altri scendono. Negli esempi useremo solo classifiche, «in testa» e «più indietro».

Ecco la mail. È una ricostruzione illustrativa, non la risposta registrata di un modello reale, e per semplicità qui un pezzo coincide con una parola, mentre i veri pezzi no (cap. 2). Il *prompt*, la richiesta che scrivi, entra. Primo giro, candidati in ordine di plausibilità: «Gentile», «Egregio», «Spettabile», «Buongiorno». Se ne sceglie uno, «Gentile», e si riparte:

- «Gentile»
- «Gentile amministratore,»
- «Gentile amministratore, le scrivo»
- «Gentile amministratore, le scrivo per chiederle di»
- «Gentile amministratore, le scrivo per chiederle di rinviare l'assemblea»

Rileggi l'elenco: ogni riga è un'istantanea, e tra l'una e l'altra passano più giri, ciascuno con in mano soltanto il testo scritto fin lì. Mancano le scuse, la nuova data e i distinti saluti, ma è lo stesso giro con altre voci: tra scrivere «Gentile» e scrivere il resto cambia solo il numero di giri. Gli scartati non fanno ricorso. È l'eliminacode degli sportelli che chiama «prossimo, prego», con una differenza: invece dei numeri chiama le parole, e non chiude mai per pausa pranzo.

Ora il brindisi dell'epigrafe. Una volta scritto «Gentile», non lo cancelli: resta sul tavolo e condiziona tutto il seguito. Se hai aperto con «Egregio», devi finire in modo coerente con «Egregio». Non esiste il tasto Annulla, e nemmeno la zia che ti tira la manica.

Quando dico che il modello «sa», «sceglie», «prevede», uso metafore comode. Cosa succede davvero: il testo diventa numeri, i numeri attraversano il modello e si moltiplicano per i parametri, e all'uscita c'è un punteggio per ogni pezzo possibile. Nessuna intenzione: solo moltiplicazioni. Tante.

Chat, memoria della conversazione e strumenti esterni sono software costruito intorno al modello (la memoria nel cap. 11, gli strumenti nel cap. 18). Il modello, in sé, prevede testo. Per lui sei un testo da continuare. Non è niente di personale.

L'idea ha un antenato che lavorava con carta e matita. Nel 1913, a San Pietroburgo, il matematico russo Markov contò a mano vocali e consonanti nelle prime 20.000 lettere dell'*Eugenio Onegin* di Puškin e scoprì che la probabilità di trovare una vocale dipende dalla lettera che precede. Prevedere un pezzo da ciò che viene prima: senza scheda video, senza bolletta, con un'idea più vecchia di un secolo. Da lì a un LLM il passo è di scala e di motore, non di mestiere: dalla vocale che segue una lettera al pezzo che segue un intero testo.

<!-- parte: dove l'analogia scricchiola -->

> **Dove l'analogia scricchiola.** La tastiera guarda di solito poche parole, il modello un'intera conversazione (cap. 11). La tastiera ha letto quattro chiacchiere, il modello «mezza biblioteca», che è un modo di dire: la scala vera si misura in dati e in manopole senza etichetta, non in scaffali. E soprattutto la tastiera ti consulta: propone tre parole e aspetta il tuo tocco, mentre il modello sceglie, si rilegge e riparte da solo, e il tuo contributo sta tutto nel prompt, prima del primo giro. Non aspetta la tua scelta, come quei colleghi che ti chiedono un parere a lavoro già consegnato.

<!-- parte: sotto il cofano -->

> **Sotto il cofano.** Un LLM è una funzione sui token: prende la sequenza scritta finora e restituisce un punteggio per ogni token del vocabolario, l'elenco chiuso dei pezzi possibili. Llama 3 (Meta, aprile 2024) ne ha circa 128.000; il valore esatto è 128.256 [DA VERIFICARE: campo `vocab_size` nel file `config.json` di Llama 3 8B]. Quindi a ogni passo 128.256 punteggi, anche per i pezzi che con un condominio non c'entrano niente: il modello è metodico, e anche il punteggio più basso è un punteggio.
>
> L'unica formula del capitolo è P(token successivo | tutti i token precedenti), dove P sta per probabilità e la barra verticale si legge «sapendo che». A parole: la probabilità del prossimo pezzo, sapendo tutto ciò che è già scritto. Il modello la calcola, ne sceglie uno, lo aggiunge e ricomincia: per questo si dice *autoregressivo*, ogni passo si basa sui risultati dei precedenti.
>
> Per generare N token servono N passaggi in avanti (*forward pass*, un attraversamento completo del modello). Ipotesi di lavoro, non una misura: una mail da 300 token, quindi 300 passaggi. Con la *KV cache* (da *key-value*, chiave-valore; cap. 11) ogni passaggio rilegge meno, ma ne resta uno per token. Trecento attraversamenti completi per una mail che nessuno leggerà con la stessa cura con cui è stata prodotta.
>
> Il conto della memoria: 8 miliardi di parametri × 2 byte (16 bit) = 16 GB, dove GB sta per gigabyte, miliardi di byte: quanto la memoria di una buona scheda video per videogiochi. Si può stringere con la quantizzazione (cap. 14). Infine, modello e applicazione sono cose diverse: il modello è un file di numeri che prevede token; l'applicazione è il programma che lo fa girare, gli rimette in ingresso il testo e ci costruisce intorno chat, memoria e strumenti.

*[Il capitolo prosegue con: Mito da sfatare («è solo statistica»), Storia vera (Shannon, 1948), Nell'uso reale, Prova tu, In tre righe.]*
