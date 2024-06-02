label scene2_0:

    stop music fadeout 4

    scene night_hinamizawa with longFade


    n "Hinamizawa è di nuovo subbuglio per la seconda notte di fila."

    play sound "audio/sfx/cri cri.mp3"

    n "Con la scomparsa del sindaco ieri sera, e di quelle due ragazzine oggi, i residenti stanno rivoltando il villaggio come un calzino."


    n "Che diamine sta succedendo? Non doveva essere una morte e una sparizione all'anno? Abbiamo più che raddoppiato quelle cifre."



    play music "audio/sfx/rainy days.ogg"


    anon "R k -  a  !"


    n "Sento una voce avvicinarsi"

    play sound 'audio/sfx/bushes2.mp3'

    scene night_road with Dissolve(1)

    old1 "Rika-chamaaa!!!"

    old2 "Il bosco di notte è pericoloso! Vieni fuori! {w}Rika-chama!"

    n "Solo due anziani che cercano Rika?"

    n "Un momento, si sono fermati... uno dei due è caduto in ginocchio."

    old1 "O grande Oyashiro-sama. Ti prego calma la tua ira."

    old2 "Idiota! Non lo devi neanche pensare. {w}Oyashiro-sama non maledirebbe mai un membro delle stimate tre famiglie."

    old2 "Questo dev'essere un modo per mettere alla prova la nostra fede. Sia Kimiyoshi che Rika-chama sono al sicuro, ne sono convinto!"

    old2 "E poi i trasgressori non sono già stati puniti tutti?"

    old1 "Ma no, ma che dici. Dov'eri ieri quando Mion ha parlato a nome dei Sonozaki?"

    old1 "Nel magazzino rituale era entrato anche il figlio dei Maebara. Se qualcun altro merita di essere rapito dai demoni è quello screanzato."

    n "Non hanno tutti i torti."

    n "Capisco \"maledire\" gli stranieri che hanno rotto il taboo, ma queste sparizioni sono troppo strane."

    n "Ammesso che li abbiano giudicati responsabili del cambio del lucchetto. Perchè loro prima di Keiichi?"

    n "E poi c'è Satoko. {w}È scomparsa anche lei ma non sembra importare a nessuno."

    n "Oltre ai ragazzi non ho sentito un solo abitante chiamarla. È come se tutti accettassero la sua sparizione come qualcosa di ovvio."

    play sound 'audio/sfx/bushes1.mp3'

    pause 2

    old2 "Ehi! Mi pare che ho sentito qualcosa. Veniva da di là."

    old2 "Rika-chamaaaaa!"

    n "Dannazione mi hanno sentito."

    play sound 'audio/sfx/bushes3.mp3'
    scene night_small_shrine with Dissolve(2)

    n "Qua dovrei essere al sicuro per ora."

    n "Alla loro età non si addentreranno in un sentiero sterrato in salita,{w} per di più di notte, {w}ma potrebbero tornare con dei giovani appresso."

    n "E a quel punto probabilmente troverebbero il nostro nascondiglio... {w}Il nascondiglio dove ora sta riposando il capo."

    #qua compare larry
    show larry evil nope with dissolve

    n "......{w}Ho bisogno di raccogliere i miei pensieri. Devo fare mente locale."

    play music 'audio/higu/ancient times.mp3' fadein 4
    play sound 'audio/sfx/multiple pageflips.mp3'
    show larry notes tilt with dissolve

        
    pause 1

    lan """
    Per riassumere la mia situazione in poche parole. Non mi posso fidare di Check in questo momento.

    Lo so, sembra assurdo. Tra tutte le persone del BKG lui era l'ultimo da cui mi sarei aspettato un'insubordinazione.
    Eppure dopo che ho parlato sia con Terry che con un comandante in persona devo fare i conti con la realtà davanti ai miei occhi.

    Tante cose si spiegano nel momento in cui accettiamo un coinvolgimento del capo. Ad esempio il fatto che mi ha mentito sulla trasmittente.

    Da quando siamo partiti non siamo venuti in contatto con nessun altro capace di manometterla.
    Deve aver finto un guasto, così che non interferisse con le sue \"altre\" comunicazioni.
    """
    nvl clear

    play sound 'audio/sfx/pageflip.mp3'

    lan """
    Non è tutto quì.
    È palese che a distanza di minuti da quando quei quattro sono entrati nel magazzino rituale Mion ne fosse già al corrente.
    {w}Difatto quei due anziani lo avevano sentito dalla bocca di Mion.

    Secondo la nostra ricostruzione nessun altro si trovava nei paraggi in quel momento.{w}
    A meno che uno di loro non abbia vuotato il sacco di sua spontanea volontà, soltanto il capo avrebbe potuto diffondere l'informazione.

    E adesso abbiamo questa serie di omicidi e sparizioni su una scala completamente diversa da quelle degli altri anni...

    Possibile che la missione fosse una copertura, e che in realtà Check è venuto quì in qualità di spia e sicario per conto dei Sonozaki?

    """
    nvl clear

    show larry worried cry -tilt -notes with dissolve

    la "Questa è tutta colpa sua capo. {w}Perchè non mi ha detto niente? Io di lei mi fidavo."

    show larry evil with dissolve
    n "No, basta lamentele, devo concentrarmi. Non sono al sicuro quì."

    show larry nope notes tilt with dissolve

    play sound 'audio/sfx/pageflip.mp3'



    lan """
    Oggi come ieri, il capo mi ha incaricato di fare da vedetta, e di avvisarlo qualora si avvicinassero troppo al nascondiglio. {w}
    Questo sembrerebbe indicare che non si è ancora accorto della mia presa di coscienza. {w}
    Mi chiedo che effetto avrebbe farlo trovare dagli abitanti del villaggio.

    A meno che...

    Se Check è dalla loro parte significa che gli apici sono già al corrente della sua sua presenza, e per loro dovrebbe essere
    facile dirigere le ricerche lontano dalla sua posizione.

    Ma allora perchè assegnarmi questo ruolo? {w}Potrebbe essere un modo per distrarmi mentre porta a termine i suoi piani, o nel peggiore dei casi una trappola...

    A dire il vero.... {w}È da ieri notte che mi sento osservato.
    """





    n "This scene is about to end"

    n "In 3...."

    n "2...."

    n "2...."


    return