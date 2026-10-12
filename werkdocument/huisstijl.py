"""
huisstijl.py — de bouwstenen van elk werkdocument (GO! Dalton Gent, Toegepaste Informatica)

Kopieer dit bestand ongewijzigd naar `werkdocument/` van een lesmap (uit `_sjablonen/lespakket/werkdocument/`),
met `go-dalton-gent.png` erbij. `maak_werkdocumenten.py` van de les doet `from huisstijl import *`.
Verbeter je iets, doe het dan hier in het sjabloon en kopieer het opnieuw.

Waarom zo (Jonas, 12-10-2026, na zijn eigen opkuis van Stagemail):
 - Alles waar de leerling typt, is een **vak**: een tabelcel met een lichtblauwe achtergrond. Typen in
   een vak schuift niets op; een te lang antwoord maakt het vak gewoon hoger. Nooit lijntjes van
   underscores (die schuiven mee met de tekst) en nooit een ☐ die de leerling moet wegtikken.
 - Geen kopregel met naam, klas en datum: Classroom zet de naam van de leerling in de titel van de
   kopie, de klas is de Classroom-klas en de datum is het moment van inleveren.
 - Geen *Zo werk je*, geen verwijzing naar de lespagina, geen "alles is verzonnen": dat staat op de
   lespagina en in de opdracht. Het werkdocument bevat alleen wat de leerling invult, en de feiten
   die hij daarvoor nodig heeft.
 - Bovenaan het logo van GO! Dalton Gent en het puntenvak (/20), zoals op een toets van de school.
 - A4, Calibri 12 voor de tekst (huisstijl Dalton: Calibri 11 of 12), Montserrat voor de titels (zoals
   de lespagina). Beide rendert Google Documenten (getest 12-10-2026).

Getest in Google Documenten na het omzetten van de .docx (12-10-2026): vakken, vaste kolombreedtes,
minimumhoogtes, kleuren, logo en lettertypes blijven behouden. Aanklikbare vinkjes (de checklist van
Google Documenten) kunnen niet uit een .docx komen: daarom typt de leerling een x in een vak.
"""
import os
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HIER = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HIER, "go-dalton-gent.png")

# huisstijl Dalton (_afspraken/vormgeving-en-techniek.md)
NAVY = RGBColor(0x3C, 0x51, 0xA0)
NAVY_DIEP = RGBColor(0x2A, 0x39, 0x73)
GRIJS = RGBColor(0x5F, 0x63, 0x68)
ZWART = RGBColor(0x1F, 0x1F, 0x1F)
WIT = RGBColor(0xFF, 0xFF, 0xFF)
HEX_NAVY = "3C51A0"
HEX_PERI = "A7B1DE"      # randen van vakken en tabellen
HEX_LIJN = "D5DAEE"      # lijnen binnenin een tabel
HEX_KOP = "E4E8F6"       # kopregel van een tabel
HEX_VAK = "F3F5FC"       # hier typt de leerling
HEX_KADER = "EEF0F9"     # een kader met feiten

TEKST = "Calibri"
TITEL = "Montserrat"
BREEDTE = 17.0           # bruikbare breedte in cm: A4 (21 cm) min 2 x 2 cm marge


# ---------- het document ----------
def nieuw_document():
    """A4, marges van 2 cm, Calibri 12."""
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = TEKST
    st.font.size = Pt(12)
    st.font.color.rgb = ZWART
    st.element.rPr.rFonts.set(qn("w:eastAsia"), TEKST)
    st.paragraph_format.space_after = Pt(4)
    st.paragraph_format.line_spacing = 1.1
    for s in doc.sections:
        s.page_width, s.page_height = Cm(21.0), Cm(29.7)
        s.top_margin = s.bottom_margin = Cm(1.8)
        s.left_margin = s.right_margin = Cm(2.0)
    return doc


def kopblok(doc, titel, punten=20):
    """Bovenaan: logo · titel · puntenvak (zoals de toets van de school)."""
    t = doc.add_table(rows=1, cols=3)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    randen(t)
    breedtes(t, [3.6, BREEDTE - 3.6 - 2.8, 2.8])
    logo, midden, score = t.rows[0].cells
    for c in (logo, midden, score):
        c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    p = logo.paragraphs[0]
    zonder_ruimte(p)
    if os.path.exists(LOGO):
        p.add_run().add_picture(LOGO, width=Cm(3.2))
    p = midden.paragraphs[0]
    zonder_ruimte(p)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(titel)
    stijl(r, TITEL, 22 if len(titel) <= 14 else 17, vet=True, kleur=NAVY_DIEP)
    if punten:
        puntenvak(score, punten, groot=True)
    hoogte(t.rows[0], 2.0)
    ruimte(doc, 10)
    return t


def deel(doc, nr, titel, punten=None, nieuwe_pagina=False):
    """De kop van een deel: 'Deel 2 — Aan, Cc of Bcc?', met een lijn eronder. nr None: alleen de titel
    (bv. 'Extra — niet verplicht'). punten: zet rechts een puntenvak (bv. 4 -> '/ 4'), als de punten per
    deel gegeven worden."""
    kop = titel if nr is None else f"Deel {nr} — {titel}"
    if punten is None:
        p = doc.add_paragraph()
        p.paragraph_format.page_break_before = nieuwe_pagina
        p.paragraph_format.space_before = Pt(0 if nieuwe_pagina else 14)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(kop)
        stijl(r, TITEL, 14, vet=True, kleur=NAVY_DIEP)
        onderlijn(p)
        return p
    t = doc.add_table(rows=1, cols=2)
    randen(t)
    breedtes(t, [BREEDTE - 2.2, 2.2])
    links, rechts = t.rows[0].cells
    links.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    p = links.paragraphs[0]
    p.paragraph_format.page_break_before = nieuwe_pagina
    r = p.add_run(kop)
    stijl(r, TITEL, 14, vet=True, kleur=NAVY_DIEP)
    puntenvak(rechts, punten)
    ruimte(doc, 6)
    return t


def vraag(doc, s):
    """Een vraag in het vet, vlak boven haar antwoordvak."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(s)
    r.bold = True
    return p


def tekst(doc, s, klein=False, cursief=False, na=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(na)
    r = p.add_run(s)
    r.italic = cursief
    if klein:
        r.font.size = Pt(10)
        r.font.color.rgb = GRIJS
    return p


def antwoordvak(doc, hoogte_cm=1.4):
    """Het vak waarin de leerling typt. Het groeit mee als het antwoord langer is."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    randen(t, buiten=HEX_PERI)
    breedtes(t, [BREEDTE])
    vak(t.rows[0].cells[0])
    hoogte(t.rows[0], hoogte_cm)
    niet_splitsen(t)
    ruimte(doc, 4)
    return t


def kader(doc, titel, inhoud):
    """Een kader met de feiten die de leerling nodig heeft (bv. 'Je stage').
    inhoud: lijst van regels; een regel is een tekst, of (label, tekst) voor een vet label."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    randen(t, buiten=HEX_PERI)
    breedtes(t, [BREEDTE])
    cel = t.rows[0].cells[0]
    schaduw(cel, HEX_KADER)
    marges(cel, boven=0.2, onder=0.2, links=0.3, rechts=0.3)
    p = cel.paragraphs[0]
    r = p.add_run(titel)
    stijl(r, TITEL, 11, vet=True, kleur=NAVY_DIEP)
    p.paragraph_format.space_after = Pt(4)
    for regel in inhoud:
        p = cel.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        if isinstance(regel, tuple):
            r = p.add_run(regel[0] + "  ")
            r.bold = True
            p.add_run(regel[1])
        else:
            p.add_run(regel)
    niet_splitsen(t)
    ruimte(doc, 4)
    return t


def tabel(doc, kop, rijen, cm, invul=(), rijhoogte=1.0, voorbeeld_rij=None, vet=(), klein=()):
    """Een tabel met een kopregel. invul: de kolommen (0, 1, …) waarin de leerling typt: die cellen
    worden een vak. voorbeeld_rij: de rij (1 = de eerste na de kop) die al ingevuld is (de demo).
    vet / klein: kolommen in het vet / in 10 pt (bv. citaten)."""
    t = doc.add_table(rows=1 + len(rijen), cols=len(kop))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    randen(t, buiten=HEX_PERI, binnen=HEX_LIJN)
    breedtes(t, cm)
    for i, h in enumerate(kop):
        c = t.rows[0].cells[i]
        schaduw(c, HEX_KOP)
        celtekst(c, h, vet=True, kleur=NAVY_DIEP, grootte=11)
    for r, rij in enumerate(rijen, start=1):
        for k, waarde in enumerate(rij):
            c = t.rows[r].cells[k]
            c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            if waarde:
                celtekst(c, waarde, kleur=GRIJS if r == voorbeeld_rij else None,
                         cursief=(r == voorbeeld_rij and k in invul), vet=k in vet,
                         grootte=10 if k in klein else None)
            elif k in invul:
                vak(c)
        hoogte(t.rows[r], rijhoogte)
    niet_splitsen(t)
    ruimte(doc, 4)
    return t


def controletabel(doc, rijen, kop=("Klopt?", "Wat moet kloppen?", "Punten")):
    """Nalezen en beoordelen in één tabel. De leerling typt een x in het vak links; de leraar zet de punten
    rechts. rijen: lijst van (tekst, punten); punten None = geen puntenkolom voor die rij."""
    met_punten = any(p for _, p in rijen)
    cm = [1.6, BREEDTE - 1.6 - 2.0, 2.0] if met_punten else [1.6, BREEDTE - 1.6]
    t = doc.add_table(rows=1 + len(rijen), cols=len(cm))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    randen(t, buiten=HEX_PERI, binnen=HEX_LIJN)
    breedtes(t, cm)
    for i in range(len(cm)):
        c = t.rows[0].cells[i]
        schaduw(c, HEX_KOP)
        celtekst(c, kop[i], vet=True, kleur=NAVY_DIEP, grootte=11)
        if i != 1:
            c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    for r, (s, punten) in enumerate(rijen, start=1):
        rij = t.rows[r]
        vak(rij.cells[0])
        rij.cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        rij.cells[0].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        rij.cells[1].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        celtekst(rij.cells[1], s)
        if met_punten:
            c = rij.cells[2]
            c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
            if punten:
                stijl(c.paragraphs[0].add_run(f"/ {punten}"), TEKST, 12, kleur=GRIJS)
        hoogte(rij, 0.9)
    niet_splitsen(t)
    ruimte(doc, 4)
    return t


def mailvenster(doc, delen):
    """Een venster dat eruitziet als 'Nieuw bericht' in Gmail (MW en MWW les 3), zonder knop Verzenden: er
    wordt niets verstuurd. delen: (grijs label, hoogte in cm) per vak van het bericht."""
    t = doc.add_table(rows=1 + 4 + len(delen), cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    randen(t, buiten="9AA0A6")
    breedtes(t, [3.2, BREEDTE - 3.2])
    kopcel = t.rows[0].cells[0].merge(t.rows[0].cells[1])
    schaduw(kopcel, "F2F6FC")
    celtekst(kopcel, "Nieuw bericht", vet=True, kleur=RGBColor(0x20, 0x21, 0x24))
    kopcel.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    hoogte(t.rows[0], 0.8)
    for i, veld in enumerate(["Aan", "Cc", "Bcc", "Onderwerp"], start=1):
        links, rechts = t.rows[i].cells
        celtekst(links, veld, kleur=GRIJS)
        vak(rechts)
        for c in (links, rechts):
            c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            cel_randen(c, "DADCE0", dikte=6, kanten=("bottom",))
        hoogte(t.rows[i], 0.85)
    for j, (label, cm) in enumerate(delen):
        rij = t.rows[5 + j]
        celtekst(rij.cells[0], label, kleur=GRIJS, grootte=10)
        vak(rij.cells[1])
        hoogte(rij, cm)
    niet_splitsen(t)
    return t


def puntenvak(cel, punten, groot=False):
    """Een kader met '/ 20' rechts: de leraar typt het cijfer vóór de schuine streep."""
    cel.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    cel_randen(cel, HEX_NAVY, dikte=12 if groot else 8)
    p = cel.paragraphs[0]
    zonder_ruimte(p)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    stijl(p.add_run(f"/ {punten}"), TITEL, 18 if groot else 12, vet=True, kleur=NAVY)


def nieuwe_pagina(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


# ---------- kleine hulpfuncties (python-docx kan dit niet zelf) ----------
def stijl(r, lettertype=None, grootte=None, vet=False, kleur=None, cursief=False):
    if lettertype:
        r.font.name = lettertype
        r._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), lettertype)
    if grootte:
        r.font.size = Pt(grootte)
    r.bold = vet
    r.italic = cursief
    if kleur is not None:
        r.font.color.rgb = kleur
    return r


def celtekst(cel, s, vet=False, kleur=None, grootte=None, cursief=False):
    """Tekst in een cel. Tussen *sterretjes* komt cursief: voor letterlijke woorden, zoals
    'Ik begin met *Beste mevrouw Verhoeven,*'."""
    cel.text = ""
    p = cel.paragraphs[0]
    zonder_ruimte(p)
    r = None
    for i, stuk in enumerate(s.split("*")):
        if stuk:
            r = p.add_run(stuk)
            stijl(r, None, grootte, vet=vet, kleur=kleur, cursief=cursief or i % 2 == 1)
    return r


def zonder_ruimte(p):
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)


def ruimte(doc, pt):
    """Een lege regel van pt punten hoog (tussen twee tabellen zet Google er anders een gewone regel)."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = Pt(pt)
    rpr = p._p.get_or_add_pPr()
    rr = OxmlElement("w:rPr")
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), str(max(2, int(pt))))
    rr.append(sz)
    rpr.append(rr)
    return p


def vak(cel):
    """Maakt van een cel een vak waarin de leerling typt."""
    schaduw(cel, HEX_VAK)
    zonder_ruimte(cel.paragraphs[0])


def schaduw(cel, kleur):
    tcPr = cel._tc.get_or_add_tcPr()
    for oud in tcPr.findall(qn("w:shd")):
        tcPr.remove(oud)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), kleur)
    tcPr.append(shd)


def randen(tabel, buiten=None, binnen=None, dikte=6):
    """Randen van een tabel: niets (standaard), een kader rondom, en/of lijnen binnenin."""
    tblPr = tabel._tbl.tblPr
    for oud in tblPr.findall(qn("w:tblBorders")):
        tblPr.remove(oud)
    b = OxmlElement("w:tblBorders")
    for kant in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement("w:" + kant)
        kleur = buiten if kant in ("top", "left", "bottom", "right") else binnen
        if kleur:
            e.set(qn("w:val"), "single")
            e.set(qn("w:sz"), str(dikte))
            e.set(qn("w:space"), "0")
            e.set(qn("w:color"), kleur)
        else:
            e.set(qn("w:val"), "nil")
        b.append(e)
    tblPr.append(b)


def cel_randen(cel, kleur, dikte=8, kanten=("top", "left", "bottom", "right")):
    tcPr = cel._tc.get_or_add_tcPr()
    b = tcPr.find(qn("w:tcBorders"))
    if b is None:
        b = OxmlElement("w:tcBorders")
        tcPr.append(b)
    for kant in kanten:
        e = OxmlElement("w:" + kant)
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), str(dikte))
        e.set(qn("w:space"), "0")
        e.set(qn("w:color"), kleur)
        b.append(e)


def marges(cel, boven=0.1, onder=0.1, links=0.19, rechts=0.19):
    tcPr = cel._tc.get_or_add_tcPr()
    m = OxmlElement("w:tcMar")
    for kant, cm in (("top", boven), ("left", links), ("bottom", onder), ("right", rechts)):
        e = OxmlElement("w:" + kant)
        e.set(qn("w:w"), str(int(cm * 567)))
        e.set(qn("w:type"), "dxa")
        m.append(e)
    tcPr.append(m)


def onderlijn(p, kleur=HEX_PERI):
    pPr = p._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    e = OxmlElement("w:bottom")
    e.set(qn("w:val"), "single")
    e.set(qn("w:sz"), "6")
    e.set(qn("w:space"), "3")
    e.set(qn("w:color"), kleur)
    bdr.append(e)
    pPr.append(bdr)


def breedtes(tabel, cm):
    """Vaste kolombreedtes, zodat Google Documenten de tabel niet zelf herschikt."""
    tabel.autofit = False
    tblPr = tabel._tbl.tblPr
    lay = OxmlElement("w:tblLayout")
    lay.set(qn("w:type"), "fixed")
    tblPr.append(lay)
    for kol, w in zip(tabel.columns, cm):
        kol.width = Cm(w)
    for rij in tabel.rows:
        for cel, w in zip(rij.cells, cm):
            cel.width = Cm(w)


def hoogte(rij, cm):
    """Minimumhoogte van een rij: het vak is nooit kleiner, en groeit mee met een langer antwoord."""
    trPr = rij._tr.get_or_add_trPr()
    for oud in trPr.findall(qn("w:trHeight")):
        trPr.remove(oud)
    h = OxmlElement("w:trHeight")
    h.set(qn("w:val"), str(int(cm * 567)))
    h.set(qn("w:hRule"), "atLeast")
    trPr.append(h)


def niet_splitsen(tabel):
    """Een rij breekt niet over twee bladzijden."""
    for rij in tabel.rows:
        trPr = rij._tr.get_or_add_trPr()
        trPr.append(OxmlElement("w:cantSplit"))
