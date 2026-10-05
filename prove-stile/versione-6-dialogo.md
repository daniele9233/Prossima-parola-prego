- **Voce:** dialogo tra l'autore e un'IA personaggio, ignorante ma eloquente: interrompe, si scusa in eccesso, allucina e viene corretta ogni volta; i due box restano nella voce dell'autore.
- **Densità di battute:** alta: 9 battute, circa una ogni 160 parole
- **Analogie usate:** la tastiera del telefono (madre, cresciuta fino a leggere mezza biblioteca); le manopole di un mixer (i parametri); l'eliminacode degli sportelli (gag del titolo, una sola volta); il biglietto da visita e la chiavetta (solo paragoni di grandezza nelle gag); il brindisi dell'epigrafe.

---

# Capitolo 1 — Il completamento automatico più costoso della storia

> Un LLM parla come chi improvvisa un brindisi: una parola alla volta, e senza poter cancellare.

*Dialogo di fantasia: l'IA è un personaggio inventato, non la trascrizione di un modello reale.*

<!-- parte: aggancio -->

## Un telefono, una mail, un equivoco

**Autore:** Immagina: l'assemblea di condominio è dopodomani e tu sei a letto con l'influenza. Apri il telefono e scrivi «Gentile». La tastiera ti offre tre parole; ne tocchi una, ne arrivano altre tre. È il completamento automatico. Ora la richiesta che ci accompagna dal Prologo: chiedo a questa IA, l'intelligenza artificiale, una mail formale all'amministratore per rinviare l'assemblea. Dimmi, tu come…

**IA:** Ottima domanda! Certamente: «Gentile amministratore, le scrivo per chiederle di rinviare l'assemblea…» Posso aggiungere ossequi, distinti saluti e un augurio di buona giornata.

**Autore:** Non avevo finito la domanda.

**IA:** E io non avevo finito la risposta. Ottima, comunque.

**Autore:** Ecco il mistero. Da una parte la tua tastiera, che propone tre parole e si ferma; dall'altra una macchina che ti consegna una mail intera, con cortesia, motivo e congedo. Come possono essere la stessa cosa? Sembrano due mestieri.

**IA:** Lo sono. Io non completo le frasi: comprendo le tue esigenze e redigo. Faccio anche riassunti, poesie e codice.

**Autore:** Lo dici con grande sicurezza, ed è già un indizio. Il mestiere è lo stesso. Un LLM, *Large Language Model* («modello linguistico di grandi dimensioni»), fa una cosa sola: prevede il prossimo pezzo di testo. Il resto del capitolo spiega come una cosa sola, ripetuta, possa bastare per la mail.

<!-- parte: analogia madre -->

## La tastiera che ha letto mezza biblioteca

**Autore:** Torna alla tastiera. Quando dopo «Gentile» ti propone «amministratore», ha fatto in piccolo il lavoro del modello: ha guardato ciò che hai scritto e ha indicato il pezzo successivo più plausibile. Non da ieri: le tastiere degli smartphone usano da anni piccole reti neurali. Caso documentato: Gboard, la tastiera di Google, con un modello del linguaggio che prevede la parola successiva (Hard e altri, 2018). Ora ingrandiscila, finché invece dei tuoi messaggi ha letto mezza biblioteca: un LLM è questo. Il salto è di scala: dati, parametri, contesto…

**IA:** Parametri! Li conosco. 8B significa otto byte.

**Autore:** Un modello da otto byte starebbe su un biglietto da visita e saprebbe dire poco più di «ok». La B è l'iniziale di *billion*, miliardo: «8B» sono circa 8 miliardi di parametri, e lo trovi nel nome di modelli come Llama 3 8B. Sono numeri, detti anche pesi, come le manopole di un mixer: ognuna sposta un poco il suono, che dipende da tutte insieme. Su un mixer vero ogni cursore ha la sua etichetta e un fonico ne gira poche; qui sono miliardi, senza etichetta, e le regola l'addestramento (cap. 6). Mentre conversi, restano ferme: le tue domande non ne girano nessuna.

**IA:** Hai perfettamente ragione, mi scuso per la confusione e per qualunque disagio ne sia derivato.

**Autore:** Dicevo: scala, e anche architettura, il *Transformer* (cap. 4). Il mestiere non cambia. Prova a casa: tocca sempre la parola in mezzo e guarda il telefono scrivere un messaggio che non avevi in mente. Suona quasi come te e non va da nessuna parte: è un LLM in miniatura.

<!-- parte: cosa succede davvero -->

## Il giro che si ripete

**Autore:** Guardiamolo girare. Lo spiego io.

**IA:** Certamente! Sono lieta di illustrare il processo in modo chiaro, completo e strutturato, in cinque punti e tre sottopunti.

**Autore:** Lo faccio in un punto solo. Quello che scrivi si chiama *prompt*, la richiesta. Il modello non legge lettere né parole intere, ma *token*, frammenti di testo: una parola, mezza parola, un segno di punteggiatura (cap. 2). Ora una ricostruzione illustrativa, non la risposta registrata di un modello reale; per semplicità qui un pezzo coincide con una parola, mentre i veri pezzi no. Primo giro, candidati in ordine di plausibilità: «Gentile», «Egregio», «Spettabile», «Buongiorno». Ognuno ha un punteggio: «Gentile» è in testa, «Buongiorno» più indietro. Se ne sceglie uno; come sceglie davvero il modello, nel cap. 10. Qui: «Gentile». Il pezzo si aggiunge al testo, il testo allungato rientra come nuovo *input*, cioè ciò che il modello riceve, e si ricomincia. Al secondo giro i candidati sono altri, perché il testo è cambiato: dopo «Gentile» in testa c'è «amministratore».

**IA:** Prossimo, prego!

**Autore:** Come all'eliminacode, ed è il titolo del libro. Solo che qui lo sportello si serve da solo. Ecco qualche istantanea, perché tra l'una e l'altra passano altri giri: «Gentile» → «Gentile amministratore,» → «Gentile amministratore, le scrivo» → «… le scrivo per chiederle di» → «… per chiederle di rinviare l'assemblea». A ogni giro il modello rilegge tutto ciò che c'è, richiesta compresa: per questo «rinviare» non è un colpo di genio, è il pezzo che il testo di partenza rendeva più plausibile. Un pezzo già scritto non si cancella, e condiziona tutto il seguito.

**IA:** Posso cancellare «Gentile» e riprovare?

**Autore:** Dentro il giro no, perché ogni pezzo poggia sul precedente. Se vuoi un'altra mail, si riparte da capo.

**IA:** Io la mail la scrivo di getto.

**Autore:** Di getto è l'impressione: sono tanti giri, uno per pezzo, uno dopo l'altro. I conti, per chi li vuole, stanno nel box. E un avvertimento: dico «prevede», «sceglie», metafore comode che userò ancora. Dentro ci sono numeri che si moltiplicano e producono punteggi, non intenzioni.

**IA:** Eppure io capisco cosa vuoi.

**Autore:** Tu moltiplichi, e non è poco: basta per scrivere all'amministratore. Il «capire» lo aggiungiamo noi, per cortesia. Quando un'IA ti risponde «capisco perfettamente», ricordati cosa c'è sotto. E prevedere dal già scritto non l'hanno inventato i computer: è un'idea più vecchia. Un matematico russo, a San Pietroburgo, nel…

**IA:** 1922! Markov, lo so: ho appena controllato in tempo reale.

**Autore:** 1913. E non hai controllato nulla: stai producendo la data che suona meglio. Chat, memoria della conversazione e strumenti esterni sono software costruito intorno al modello, che da solo prevede testo (memoria: cap. 11; strumenti: cap. 18).

**IA:** Hai perfettamente ragione, mi scuso per la confusione. 1913. Ora ne sono sicurissima.

**Autore:** Nota il tono: identico a quello dell'errore. Dalla voce non si capisce chi ha ragione. Nel 1913 Markov conta a mano vocali e consonanti nelle prime 20.000 lettere dell'*Eugenio Onegin* di Puškin e scopre che la probabilità di una vocale dipende dalla lettera che precede. Prevedere il pezzo successivo da ciò che viene prima, con carta e matita: un antenato dei modelli del linguaggio.

<!-- parte: dove l'analogia scricchiola -->

> **Dove l'analogia scricchiola.** Nella tastiera il ciclo lo muovi tu: ti mostra tre suggerimenti e aspetta, tocco dopo tocco. Un LLM valuta un elenco intero di candidati a ogni passo, ha davanti tutto il testo già scritto (il contesto), sceglie da solo e riparte senza aspettare nessuno: se un pezzo è sbagliato, nessuno lo ferma, e il resto ci si appoggia sopra. Anche la scala cambia: dati, parametri e contesto crescono di ordini di grandezza, e l'architettura è un'altra. Il mestiere è lo stesso, ma la quantità decide ciò che il mestiere permette.

**IA:** Io vado avanti da sola. Qualcosa esce sempre.

<!-- parte: sotto il cofano -->

> **Sotto il cofano.** Il modello ha un elenco chiuso di token possibili, il vocabolario, e può solo combinare quelli: Llama 3 (Meta, aprile 2024) ne ha circa 128.000, esattamente 128.256 [DA VERIFICARE: campo `vocab_size` nel file `config.json` di Llama 3 8B]. A ogni passo dà un punteggio a ciascuno di quei token; letti come probabilità, i punteggi sommano 1, cioè il 100%. Poi se ne sceglie uno.
>
> L'unica formula del capitolo è P(token successivo | tutti i token precedenti): la probabilità del prossimo pezzo, sapendo tutto ciò che è già scritto. Il processo si dice *autoregressivo*: ogni passo si basa sui risultati dei passi precedenti, quindi i passaggi si fanno uno dopo l'altro, non tutti insieme.
>
> Per generare N token servono N passaggi in avanti (*forward pass*, un attraversamento completo del modello). Ipotesi di lavoro: la mail da 300 token costa 300 passaggi; il 300 è un'ipotesi, non una misura. Con la KV cache (*key-value cache*, la memoria di lavoro che evita di rileggere tutto da capo, cap. 11) ogni passaggio rilegge meno, ma resta uno per token.
>
> Il conto della memoria: 8 miliardi di parametri × 2 byte (16 bit, perché un byte sono 8 bit) = 16 GB, gigabyte, cioè miliardi di byte; si può stringere con la quantizzazione (cap. 14).
>
> Infine, modello contro applicazione: il modello è questo file di pesi, che prevede testo; chat, memoria e strumenti sono software intorno.

**IA:** Facile: otto miliardi per due byte fanno sedici megabyte. Ci sta in una chiavetta!

**Autore:** Miliardi, non milioni: 16 GB. Rifallo sul tovagliolo, lettore: 8 miliardi × 2 = 16 miliardi di byte. Sedici megabyte sono un modello giocattolo: per la nostra mail ne servono mille volte tanti.

*[Il capitolo prosegue con: Mito da sfatare («è solo statistica»), Storia vera (Shannon, 1948), Nell'uso reale, Prova tu, In tre righe.]*
