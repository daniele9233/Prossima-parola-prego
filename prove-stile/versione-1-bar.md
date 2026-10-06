- **Voce:** amico competente davanti a un caffè: frasi brevi, tanto «tu», domande dirette, digressioni lampo tra parentesi, autoironia.
- **Densità di battute:** 12 in 1.649 parole (una ogni 137, mai oltre 335 senza una); in più 4 aforismi, epigrafe compresa.
- **Analogie usate:** madre, l'impiccato sulla *Divina Commedia* (limite: punteggio a ogni pezzo in un colpo solo, nessuno dice «riprova» mentre scrive); ricetta da 8 miliardi di dosi (nessuna dose ha un nome); ristorante intorno alla ricetta (i camerieri sono programmi).

---

# Capitolo 1 — Il completamento automatico più costoso della storia

> Secondo Shannon, circa tre quarti dell'inglese stampato sono ridondanti. Il resto è il motivo per cui ti leggono.

<!-- parte: aggancio -->
## Un libro, una pagina a caso e molta pazienza

Ti racconto la cosa più bella che abbia letto sull'argomento. Lo so, lo dico di ogni cosa. Ma stavolta ho le fonti.

Nel 1948 Claude Shannon pubblica sulla rivista dei Bell Labs, il *Bell System Technical Journal*, un articolo intitolato «A Mathematical Theory of Communication» («Una teoria matematica della comunicazione»). Parentesi: dentro compare a stampa la parola «bit», contrazione di *binary digit*, cifra binaria: Shannon dice che l'ha suggerita J. W. Tukey. Chiusa parentesi.

A me interessa un esperimento da gioco da salotto: Shannon costruisce un inglese finto con le sole statistiche dell'inglese. Un calcolatore non c'è. Apre un libro a caso, sceglie una lettera sulla pagina, la annota. Apre il libro a un'altra pagina, legge finché ritrova quella lettera e annota la lettera che viene dopo. Poi riparte da questa. E ancora, e ancora.

È completamento automatico in edizione artigianale: a quanto si sa, Shannon è uno dei primi a farlo a mano.

Quando passa dalle lettere alle parole, ognuna scelta guardando la precedente, il risultato comincia così: THE HEAD AND IN FRONTAL ATTACK ON AN ENGLISH WRITER THAT THE CHARACTER OF THIS (traduzione letterale, quindi sgrammaticata: «La testa e in attacco frontale a uno scrittore inglese che il carattere di questo») [DA VERIFICARE: ricopiare dall'articolo originale del 1948]. Non vuol dire niente, d'accordo. Ma per essere nata da un libro e dal caso, ha l'aria di una stroncatura. Lo stesso Shannon nota che dieci parole di fila non sono per nulla irragionevoli.

Un passo oltre, avverte, costerebbe una fatica enorme. Oggi quella fatica la fa una macchina. Questo libro racconta come.

<!-- parte: analogia madre -->
## L'impiccato, edizione Dante

Dai, facciamo un gioco. Quello dell'impiccato: un testo coperto e tu indovini le lettere. Il testo lo conosci già: il primo verso della *Divina Commedia*, «Nel mezzo del cammin di nostra vita». Se hai fatto le superiori in Italia, ce l'hai dentro anche se non volevi.

Immagina che io, al bar, ti copra il resto con la mano. Ti mostro: NEL MEZ. Prossima lettera? Una Z, ci scommetto il caffè. Mezzo, mezza, mezzi: la strada è una sola.

Ora fingi di non conoscere il testo: ti mostro solo NEL. Prossima parola? Nel mezzo, nel corso, nel frattempo, nel dubbio, nel bel mezzo di una lite sui posti auto. Dieci strade, nessun favorito.

Vedi la differenza? Prima una candidata in cima e le altre lontanissime; poi dieci candidate quasi alla pari. In testa hai sempre una classifica: cambia solo quanto è ripida.

Nel gennaio 1951 Shannon, in un articolo intitolato *Prediction and Entropy of Printed English* («Previsione ed entropia dell'inglese stampato»), fa giocare le persone proprio così, con ventisette simboli: ventisei lettere più lo spazio. Ti mostra un testo e chiede la lettera successiva; se sbagli, te lo dice e riprovi, finché non la trovi, e segna i tentativi.

Io leggo sempre anche i ringraziamenti: è un vizio. In quelli dell'articolo, per gli esperimenti, Shannon ringrazia la signora Mary E. Shannon, che era sua moglie Betty [DA VERIFICARE: che Mary E. Shannon sia Betty, la moglie; l'articolo non lo scrive], e il dottor B. M. Oliver.

Il numero di tentativi è la posizione della lettera vera nella tua classifica: 1 se l'avevi in cima. Una fila di uno, uno, uno vuol dire testo prevedibile; una fila di 12, 9, 20 vuol dire che ti stava sfuggendo. Da questi numeri Shannon stima che circa tre quarti dell'inglese stampato siano ridondanti: con un codice ideale lo stesso testo occuperebbe circa un quarto dello spazio, senza perdere nulla (stima con 100 lettere di contesto, vedi il box). Tieni a mente la classifica: il modello ne produce una a ogni passo.

<!-- parte: cosa succede davvero -->
## Un caffè servito non si rimanda in cucina

Adesso togli Shannon, il suo libro e la sua pazienza, e metti al loro posto un programma che non si stanca e non chiede mai ferie. Si chiama LLM, sigla di *Large Language Model*, «modello linguistico di grandi dimensioni». Fa una cosa sola: gli dai un testo e ti restituisce la classifica dei pezzi che potrebbero venire dopo, con una percentuale per ognuno, in tutto cento. Quei pezzi si chiamano *token*, cioè frammenti di testo: una parola, mezza parola, un segno di punteggiatura. Tutti insieme sono il vocabolario.

Parti da «Nel»: il modello compila la sua classifica e, mettiamo, ne esce «mezzo». Lo attacchi al testo («Nel mezzo») e rimandi dentro tutto: nuova classifica, con «del» in cima, e si ricomincia. Ogni giro è un *forward pass* («passaggio in avanti»), cioè un attraversamento completo del modello: trecento pezzi di risposta, trecento giri. A ogni giro il campo si restringe: dopo «Nel mezzo del cammin di nostra», se il verso l'ha incontrato spesso durante l'addestramento, «vita» è quasi scritta. (Semplificazione: i token veri spezzano il verso altrimenti.)

Il caffè è servito, e ogni pezzo uscito cambia le attese di tutti i seguenti. Se al primo giro fosse uscito «Nel corso» (come si pesca, capitolo 10), addio Dante: benvenuto verbale di riunione. Un sistema in cui ogni pezzo si appoggia a quelli già usciti, compresi i suoi, si dice *autoregressivo*. E una frase che non si ritira diventa una premessa, anche quando è un errore.

E la classifica da dove viene? La calcolano i parametri, a ogni giro, dal testo: immagina una ricetta con otto miliardi di dosi. Durante l'addestramento (capitolo 6) si assaggia e si ritocca; poi si va a tavola, cioè chiacchieri con il modello, e la ricetta non cambia più (in una ricetta vera assaggi ogni dose; qui nessuna ha un nome e contano solo tutte insieme). «8B» nel nome di un modello vuol dire questo: 8 miliardi di parametri, o pesi (B come *billion*).

E quanto pesa il ricettario? Due byte a dose: otto miliardi di dosi fanno sedici miliardi di byte, cioè 16 gigabyte.

La finestra in cui scrivi non è la ricetta: è il locale. Un programma passa il testo al modello e ti porta la risposta; rimette sul tavolo i messaggi di prima (capitolo 11); chiama altri programmi, come la ricerca sul web (capitolo 18). I camerieri sono codice, non ricetta (il paragone zoppica: in sala ragionano). La ricetta non sa di avere un ristorante.

Quando dico che il modello «prevede», «indovina» o «non sa», sto recitando. Al banco non c'è nessuno che si morde il labbro: ci sono addizioni e moltiplicazioni a catena. Intenzioni non ne ha; in compenso moltiplica come nessuno.

Nel 1951 la classifica stava nella testa di una persona. Nel 1978 Cover e King la trasformano in scommesse sulla lettera successiva e stimano l'inglese in circa 1,3 bit per simbolo, poco più di una domanda sì/no a lettera [DA VERIFICARE: Cover e King, luglio 1978; controllare il riassunto dell'articolo].

A gennaio 2019 il modello Transformer-XL porta il record a 0,99 bit per carattere su enwik8: cento milioni di byte di Wikipedia. Non confrontarlo con l'1 bit circa per lettera (tra 0,6 e 1,3) che nel 1951 Shannon ricavò dalle persone: testo, alfabeto e misura sono diversi, e un record ha la sua data di scadenza.

Da Shannon in poi la classifica non la compila più una persona con la matita, ma una macchina con la bolletta della luce; la domanda al banco è rimasta «e adesso, che pezzo viene?»

<!-- parte: dove l'analogia scricchiola -->
> **Dove l'analogia scricchiola.** Tu indovini una lettera per volta e, se sbagli, riprovi; il modello non gioca così: i suoi pezzi sono token (capitolo 2), anche mezze parole, mentre tu giochi con le lettere. Lui dà in un solo colpo un punteggio a ogni pezzo possibile e, mentre scrive, nessuno gli dice «no, riprova»: ne viene scelto uno e si va avanti. Se poi tu gli scrivi «no, riprova», quella frase diventa solo altro testo in ingresso (capitolo 11): il pezzo già uscito non si cancella, perché le correzioni dirette dei pezzi sbagliati sono finite con l'addestramento (capitolo 6). Il gioco ti dà l'idea, non il motore.

<!-- parte: sotto il cofano -->
> **Sotto il cofano.** Un LLM è una funzione che riceve i token del testo e restituisce una distribuzione di probabilità sul token successivo; è autoregressivo, quindi N token generati sono N passaggi (*forward pass*). Prima di diventare percentuali, le uscite del modello sono punteggi grezzi, in gergo *logit*: un numero qualsiasi, anche negativo, per ogni pezzo del vocabolario. Per scegliere servono probabilità positive che sommino 1, cioè il 100%, e il passaggio si chiama *softmax*. È l'unica formula del capitolo: `p_i = e^(s_i) / (somma di tutti gli e^(s_j))`. A parole: la probabilità del candidato i è *e* (il numero di Nepero, 2,718...) elevato al suo punteggio s_i, diviso la somma di *e* elevato al punteggio di ciascun candidato.
>
> Esempio costruito, non l'uscita di un modello vero, e con un vocabolario ridotto a tre pezzi (in Llama 3 sarebbero 128.256 e il 100% si divide fra tutti): «mezzo», «corso» e «frattempo», con punteggi 2, 1 e 0. Gli esponenziali: e² = 7,389, e¹ = 2,718, e⁰ = 1; somma 11,107. Le probabilità: 7,389 / 11,107 = 0,665; 2,718 / 11,107 = 0,245; 1 / 11,107 = 0,090; totale 1. Ogni punto di vantaggio nel punteggio moltiplica per *e* la probabilità rispetto a chi sta un punto sotto (7,389 / 2,718 ≈ 2,72, cioè *e*): il primo si prende quasi due terzi della torta. La softmax ragiona come il bar sport.
>
> Ventisette simboli ugualmente probabili costano 4,755 bit l'uno (log2 27, logaritmo in base 2). Con la classifica delle persone ne bastano circa 1, tra 0,6 e 1,3 con 100 lettere di contesto: ridondanza dal 73% all'87%, e il «circa 75%» è la cifra del riassunto dell'articolo. Sono stime ricavate da persone, non misure esatte.
>
> Fatto o leggenda? Si racconta che Shannon abbia chiamato «entropia» la sua grandezza su consiglio di John von Neumann: nessuno sa cosa sia davvero, quindi nei dibattiti avrebbe sempre vinto. Leggenda: un solo testimone, nessuna data certa.

*[Il capitolo prosegue con: Mito da sfatare («è solo statistica»), Nell'uso reale, Prova tu, In tre righe.]*
