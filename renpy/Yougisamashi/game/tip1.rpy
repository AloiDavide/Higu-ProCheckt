style titolo is text:
        font "static/Caveat-VariableFont_wght.ttf"
        size 50
        xpos 960
        xalign 0.5
        textalign 0.5

style lista is text:

        size 30
        xpos 100
        line_leading 5
        line_spacing 5

style commento is text:
        font "static/Caveat-VariableFont_wght.ttf"
        size 45
        xpos 300
        line_leading 10
        yalign 0.7



define nv = Character(None, kind = nvl, what_style= "lista")
define title = Character(None, kind = nvl, what_style = "titolo")
define c = Character(None, kind = nvl, what_style = "commento")




image satok1 = im.Scale("satok1.png", 768, 576)
image satok2 = im.Scale("satok2.png", 768, 576)

image rika1 = im.Scale("rika1.png", 768, 576)
image rika2 = im.Scale("rika2.webp", 308, 480)

image kei1 = im.Scale("kei1.webp", 308, 480)
image kei2 = im.Scale("kei2.webp", 308, 480)

image rena1 = im.Scale("rena1.png", 640, 480)
image rena2 = im.Scale("rena2.png", 640, 480)

image mii1 = im.Scale("mii1.png", 640, 480)
image mii2 = im.Scale("mii2.png", 640, 480)

image shii1 = im.Scale("shii1.png", 640, 480)
image shii2 = im.Scale("shii2.png", 640, 480)

image chie = im.Scale("chie.png", 640, 480)

image irie1 = im.Scale("irie1.png", 640, 480)
image irie2 = im.Scale("irie2.png", 640, 480)



label tip1:
    stop music

    scene notes with newFade
    play music "audio/dancers5.mp3"

    play sound "audio/pageflip.mp3"
    call satoko from _call_satoko

    scene notes
    play sound "audio/pageflip.mp3"
    call mion from _call_mion

    scene notes
    play sound "audio/pageflip.mp3"
    call rena from _call_rena

    scene notes
    play sound "audio/pageflip.mp3"
    call kei from _call_kei

    scene notes
    play sound "audio/pageflip.mp3"
    call rika from _call_rika

    scene notes
    play sound "audio/pageflip.mp3"
    call shion from _call_shion

    scene notes
    play sound "audio/pageflip.mp3"
    call chie from _call_chie

    scene notes
    play sound "audio/pageflip.mp3"
    call irie from _call_irie

    scene notes
    "Mhh...{w} Sembrano solo un gruppo di amici molto affiatato.{w} Mi chiedo se veramente tutto ciò sia necessario per la missione."

    "Il capo non mi ha mai detto i dettagli ma so che è qualcosa di molto importante{w}, qualcosa sullo sventare una grande catastrofe..."

    "Non che cambi qualcosa se ci penso io da solo, piuttosto non vedo l'ora di vedere a cosa giocheranno domani."

    "Chiederò al capo se possiamo scommettere sul vincitore."

    "Sarà di nuovo Mion? {w}Forse Rika? {w}o Keiichi mostrerà finalmente di che pasta è fatto?"

    "Non sto nella pelle."

    scene black with newFade

    pause 4

    jump start

label satoko:

    show satok1:
        xalign 1.05
        yalign -0.1

    show satok2:
        xalign 1.05
        yalign 1.0

    title "{b}{color=#ffe674}Satoko Houjou / capelli biondi{/color}{/b}"



    nv """
- vanitosa

- perfida

- perfida+

- lettura del pensiero tramite osservazione facciale

- sessista

- perfida++

- astuta

- lettura a freddo

- prestigiatrice

- sessista+

- tsundere (che significa?)

- conosce la montagna come il palmo delle sue mani

- predittiva

- intelligente

- estremamente arrogante

- non sa gestire gli imprevisti"""



    c "Questa bambina si comporta in modo rocambolesco, ma credo sia solo il suo modo di venire a termini con la propria situazione familiare."


    nvl clear

    return


label mion:

    show mii1:
        xalign 1.05
        yalign 0.1

    show mii2:
        xalign 1.05
        yalign 1.0

    title "{b}{color=#23c076}Mion Sonozaki / capelli verdi{/color}{/b}"



    nv """
- estremamente competitiva

- perfida

- {s}leggermente sportiva{/s}

- subdolamente perfida

- sadica

- sconcia

- sadica+

- bluffatrice esperta

- esperta di fucili

- intuitiva

- determinata

- battitrice"""


    c "Molto competitiva ma anche competente. Sembra qualcuno di cui ci si puo fidare."

    nvl clear

    return

label rena:

    show rena1:
        xalign 1.05
        yalign 0.1

    show rena2:
        xalign 1.05
        yalign 1.0

    title "{b}{color=#ff8835}Rena Ryuuguu / capelli chiari{/color}{/b}"



    nv """
- compassionevole

- perfida

- probabile dipendenza da carineria

- più furba di quanto sembra

- cleptomane delle cose carine

- prestigiatrice

- limitless

- psicosi (?? boh io scrivo)

- investigatrice dilettante

- adulta

- incredibilmente percettiva

- perspicacie

- isterica della carineria"""


    c "Sicuramente più intelligente di quanto da a vedere. Una brava ragazza che tiene ai suoi amici."


    nvl clear

    return


label kei:

    show kei1:
        xalign 0.95
        yalign 0.1

    show kei2:
        xalign 0.95
        yalign 1.0

    title "{b}{color=#7b5252}Keiichi Maebara / capelli marroni / capelli chiari (pure lui){/color}{/b}"



    nv """
- intelligente e dalle mille risorse (uhm no)

- perfido

- cannibalismo

- eccessivamente compiaciuto e sicuro di se

- arrogante di livello divino

- feticista di gambe

- kirito moment coi fucili

- manipolatore

- draconiano (ah si?)

- campeggiatore e cuoco da campo

- incompetente cronico

- imbecille

- IMBECILLE

- fuori dagli schemi

- La sua casa è marcata per un'ispezione - codice AETAS

- esperto di baseball

- ufficialmente nella lista nera per codice TDDP"""

    c "La sua parlantina è a dir poco ammirevole ma si, è un imbecille."


    nvl clear

    return

label rika:

    show rika1:
        xalign 1.15
        yalign -0.1

    show rika2:
        xalign 0.95
        yalign 1.0

    title "{b}{color=#5c6ec3}Rika Furude / capelli blu{/color}{/b}"



    nv """
- perfida

- cannibalismo

- lettura del pensiero tramite osservazione facciale

- accondiscente in ogni situazione

- perfida+

- conosce la montagna come il palmo delle sue mani

- apprensiva verso Satoko

- estremamente leale verso gli amici

- non sa gestire gli imprevisti"""

    c "Decisamente imperscrutabile. Neanche il capo ha idea di cosa succede nella sua testa."

    nvl clear

    return


label shion:

    show shii1:
        xalign 1.05
        yalign 0.1

    show shii2:
        xalign 1.05
        yalign 1.0

    title "{b}{color=#23c076}Shion Sonozaki / ...oh no\nun'altra capelli verdi{/color}{/b}"



    nv """
- apparizione improvvisa

- sadismo perverso

- masochismo"""

    c "Sembra essere l'unico punto debole di Mion, ma siccome vive lontano sappiamo veramente poco di lei."

    nvl clear

    return


label chie:

    show chie:
        xalign 1.05
        yalign 0.5


    title "{b}{color=#4f88ca}maestra Chie / veste bianca{/color}{/b}"



    nv """
- credulona

- pazza se si nomina il curry"""

    c "Un'educatrice responsabile con una dieta opinionabile."

    nvl clear

    return


label irie:

    show irie1:
        xalign 1.0
        yalign 0.1

    show irie2:
        xalign 1.0
        yalign 1.0

    title "{b}{color=#efc281}coach Irie / Quattrocchi{/color}{/b}"



    nv """
- pervertito di declinazione ignota
    """

    c "Questa persona l'ho già vista da qualche parte... ma dove?"

    nvl clear

    return