#!/usr/bin/env python3
"""
maak_werkdocumenten.py
Genereert het werkdocument voor les 3 "Professionele e-mail aan een stageplaats" (De Speelboom, klas 3MWb):

  Stagemail.docx    het werkdocument dat de leerling INLEVERT (wordt in Classroom een Google-document)

Gebruik:  python3 maak_werkdocumenten.py     (vereist python-docx; huisstijl.py en go-dalton-gent.png
          staan ernaast, uit _sjablonen/lespakket/werkdocument/)

Waarom geen zip en geen Gmail: de leerlingen hebben met hun schoolaccount geen Gmail (Jonas, 09-10-2026),
en per les gebruiken ze één werkplek naast Classroom en de lespagina (_afspraken/didactiek.md). De e-mail
komt daarom in dit document, in een venster dat eruitziet als "Nieuw bericht" in Gmail.

12-10-2026: opgekuist naar Jonas' eigen versie (geen kopregel, geen *Zo werk je*, geen uitleg die op de
lespagina staat, geen knop Verzenden) en in de nieuwe huisstijl gezet: vakken in plaats van lijntjes, een
x in een vak in plaats van ☐, het puntenvak bovenaan en de punten per criterium in deel 4
(lesvoorbereiding § 22).

LET OP bij aanpassen:
 - Deel 1, rij 1 is het uitgewerkte voorbeeld: dat doet de leraar voor (dia 6). Laat het ingevuld.
 - De adressen eindigen op .example: dat domein bestaat nooit echt (RFC 2606). Geen echte organisatie.
 - Alle namen en gegevens zijn fictief (dat staat op de lespagina, niet in het werkdocument).
 - De punten in deel 4 komen uit lesvoorbereiding.md § 22. Verander je ze, doe het op beide plaatsen.
"""
import os
from huisstijl import *

HERE = os.path.dirname(os.path.abspath(__file__))

MENTOR = ("mevrouw Lien Verhoeven", "lien.verhoeven@despeelboom.example")
BEGELEIDER = ("mevrouw Ilse Wouters", "ilse.wouters@school.example")


HOOGTES = [1.0, 1.8, 2.2, 2.2, 1.2, 1.8]   # in cm, per vak van het bericht: genoeg plaats, niet meer


def venster(doc, delen):
    """Een venster dat eruitziet als 'Nieuw bericht' in Gmail.
    delen: de grijze labels links van de vakken in het bericht."""
    t = doc.add_table(rows=1 + 4 + len(delen), cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    randen(t, buiten="9AA0A6")
    breedtes(t, [3.2, BREEDTE - 3.2])

    kopcel = t.rows[0].cells[0].merge(t.rows[0].cells[1])
    schaduw(kopcel, "F2F6FC")
    celtekst(kopcel, "Nieuw bericht", vet=True, kleur=RGBColor(0x20, 0x21, 0x24))
    hoogte(t.rows[0], 0.8)
    kopcel.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER

    for i, veld in enumerate(["Aan", "Cc", "Bcc", "Onderwerp"], start=1):
        links, rechts = t.rows[i].cells
        celtekst(links, veld, kleur=GRIJS)
        vak(rechts)
        for c in (links, rechts):
            c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            cel_randen(c, "DADCE0", dikte=6, kanten=("bottom",))
        hoogte(t.rows[i], 0.85)

    for j, label in enumerate(delen):
        rij = t.rows[5 + j]
        celtekst(rij.cells[0], label, kleur=GRIJS, grootte=10)
        vak(rij.cells[1])
        hoogte(rij, HOOGTES[j])
    niet_splitsen(t)
    return t


def stagemail():
    doc = nieuw_document()
    kopblok(doc, "STAGEMAIL", punten=20)

    kader(doc, "Je stage", [
        "Je loopt stage in buitenschoolse opvang De Speelboom, van maandag 16 november tot vrijdag "
        "4 december 2026. Je kent daar nog niemand.",
        ("Je mentor:", f"{MENTOR[0]}  —  {MENTOR[1]}"),
        ("Je stagebegeleider van school:", f"{BEGELEIDER[0]}  —  {BEGELEIDER[1]}"),
        "Je opdracht: stuur je mentor een e-mail om kennis te maken. Vraag wanneer je eens kan "
        "langskomen. Je stagebegeleider wil meelezen.",
    ])

    # ---- Deel 1
    deel(doc, 1, "Wat is er mis met de e-mail van Kobe?")
    tabel(doc, ["", "Wat is er mis?", "Zo is het beter"], [
        ("1", "Er is geen onderwerp.", "Kennismaking stagiair Kobe Martens – stage vanaf 16 november"),
        ("2", "", ""),
        ("3", "", ""),
    ], [0.8, 7.4, BREEDTE - 0.8 - 7.4], invul=(1, 2), rijhoogte=1.3, voorbeeld_rij=1)

    # ---- Deel 2
    deel(doc, 2, "Aan, Cc of Bcc?")
    tabel(doc, ["Situatie", "Aan, Cc of Bcc?"], [
        ("a.  Je mailt je mentor. Zij moet je vraag beantwoorden.", ""),
        ("b.  Je stagebegeleider van school wil je e-mail lezen, maar moet zelf niets doen.", ""),
        ("c.  De Speelboom stuurt één e-mail naar de ouders van alle 20 kinderen. De ouders mogen "
         "elkaars e-mailadres niet zien.", ""),
    ], [12.6, BREEDTE - 12.6], invul=(1,), rijhoogte=1.0)
    vraag(doc, "Vraag 1. Waarom mogen de ouders in situatie c elkaars e-mailadres niet zien?")
    antwoordvak(doc, 1.8)

    # ---- Deel 3 (een eigen bladzijde: het venster breekt niet)
    deel(doc, 3, "Mijn e-mail aan mijn mentor", nieuwe_pagina=True)
    venster(doc, ["aanspreking", "wie ben je?", "waarom mail je?", "je vraag", "slotgroet",
                  "je naam, klas en school"])

    # ---- Deel 4: nalezen = de criteria van de beoordeling (lesvoorbereiding § 22)
    deel(doc, 4, "Nalezen", nieuwe_pagina=True)
    controletabel(doc, [
        ("Bij Aan staat het adres van mijn mentor, bij Cc dat van mijn stagebegeleider. Bcc is leeg.", 3),
        ("Mijn onderwerp zegt in een paar woorden wie ik ben en waarover mijn e-mail gaat.", 3),
        ("Ik begin met *Beste mevrouw Verhoeven,* en sluit af met *Met vriendelijke groeten,* met daaronder "
         "mijn voornaam en achternaam, klas en school.", 4),
        ("Ik zeg wie ik ben, waarom ik mail en wat ik vraag.", 5),
        ("Ik schrijf overal *u* en *uw*, niet *je* en *jij*. Geen emoji's, geen chattaal, geen afkortingen "
         "zoals *mvg*.", 3),
        ("Deel 1 en 2 zijn ingevuld.", 2),
    ])
    vraag(doc, "Je testlezer: laat je buur je e-mail lezen. Welke tip gaf je buur?")
    antwoordvak(doc, 1.2)
    vraag(doc, "Wat heb je daardoor aangepast?")
    antwoordvak(doc, 1.2)

    # ---- Deel 5
    deel(doc, 5, "Slotvraag")
    vraag(doc, "Je mentor krijgt elke dag veel e-mails. Waarom helpt een duidelijk onderwerp haar?")
    antwoordvak(doc, 1.8)

    doc.save(os.path.join(HERE, "Stagemail.docx"))


if __name__ == "__main__":
    stagemail()
    print("Gemaakt: Stagemail.docx")
