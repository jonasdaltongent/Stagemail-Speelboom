# Handleiding voor de leraar — Les 3: Professionele e-mail aan een stageplaats

**Vak:** Toegepaste Informatica
**Doelgroep:** klas 3MWb — 2de graad Maatschappij en welzijn, dubbele finaliteit
**Lesduur:** 1 × 50 minuten: 10 minuten instructie + 40 minuten keuzewerktijd
**Context:** De Speelboom, een fictieve buitenschoolse opvang
**Lokaal:** 18 — Windows 11, Google Workspace in Chrome
**Lesdag:** maandag 12 oktober 2026, 9de lesuur (rooster van 25-09-2026)
**Kernleerplandoel:** `BV2_04.01` — digitaal communiceren (toepassen; summatief via het portfolio)
**Opdracht in Classroom:** *Les 3 — Professionele e-mail aan een stageplaats*, deadline vrijdag 16 oktober 2026, 20.00 uur

<!-- Beginvragen (stap 1 van CONTEXT.md), beantwoord door Jonas op 09-10-2026:
     klas 3MWb · les 3 van het lessenplan, ma 12-10 9de uur · les 2 is gegeven (lesstart: ophalen) ·
     geen Gmail ("Ze hebben jammer genoeg geen toegang tot gmail in hun schoolaccount. We werken dus best
     in een werkdocument, een zelfgebouwde tool die gmail na-aapt voor de lay out of in smartschool"):
     gekozen voor het werkdocument met een venster dat Gmail nabootst · lokaal 18, Windows 11 ·
     AI-hulp: "Ik denk het wel, ik zie het in ieder geval toch staan." -->

## 1. Inhoud van het pakket

```text
W07 - Les 03 - MW - Professionele e-mail aan een stageplaats/
├── index.html              de lespagina: startpagina in beelden · route · één stap · checklist
├── presentatie.html        8 dia's; dia 1 is de vaste startdia "Zo start je"
├── css/style.css           lespagina (uit het sjabloon, met .nodig, .vast, .mail, .ccb, .bouwplan, de mascotte)
├── css/slides.css          dia's (uit het sjabloon, met .startroute en .met-mascotte)
├── js/script.js, js/slides.js
├── assets/                 logo's De Speelboom en GO! Dalton Gent, lettertypes (OFL), mascotte Dalton
├── werkdocument/
│   ├── Stagemail.docx              het werkdocument dat de leerling INLEVERT
│   └── maak_werkdocumenten.py      maakt het opnieuw (python-docx)
├── lesvoorbereiding.md     de lesvoorbereiding (28 punten)
├── dalton-lesfiche.html    de Dalton-lesfiche in de kleurcode: openen, Kopieer de fiche, plakken
├── lesdoelen.json          de doelen voor je jaaroverzicht
├── classroom.json          de opdracht voor de Classroom-koppeling
├── ai-bron.txt             de volledige tekst van de lespagina: de bron van de AI-hulp
└── README.md               deze handleiding
```

**Geen zip en geen Gmail.** De leerlingen hebben geen Gmail met hun schoolaccount, en 3MWb werkt per les in
één werkplek (`_afspraken/didactiek.md`). Alles gebeurt in het werkdocument; er wordt niets verstuurd.

**Adressen.** In het werkdocument en op de lespagina staan twee verzonnen adressen die eindigen op
`.example`, een domein dat nooit echt bestaat. Zo staat er geen echte organisatie of persoon in het pakket.

### 1b. Hoe de lespagina werkt

- **Startpagina** (nieuw, 09-10-2026): *Wat heb je nodig?* in drie beelden (de opdracht, de lespagina, het
  werkdocument), *Na deze les kan je*, en *Vast?* als genummerde rij.
- **Route** links, **één stap** in het midden, **checklist** rechts (20 taken). Op een smal scherm staat
  alles onder elkaar.
- De **titel van de pagina** begint met *Lespagina · Les 3*: zo heet de link in de opdracht en het tabblad
  in Chrome, naast het tabblad *Stagemail*.
- **AI-hulp**: aan (`data-ai-hulp="aan"` op `<body>`), want de Gemini Notebook hangt aan de opdracht
  (`_afspraken/ai-hulp.md`). Zonder notebook zet je hem op `"uit"`.
- `?leraar` achter het adres toont de screenshot-plaatsen (deze les heeft er geen: de beelden zijn
  tekeningen).

## 2. Klaarzetten

### Stap 1 — Publiceren via GitHub Pages ✅ *gebeurd op 09-10-2026*

Repository [`jonasdaltongent/Stagemail-Speelboom`](https://github.com/jonasdaltongent/Stagemail-Speelboom), Pages op branch `main`, map `/ (root)`. De lespagina:
<https://jonasdaltongent.github.io/Stagemail-Speelboom/>, de dia's: <https://jonasdaltongent.github.io/Stagemail-Speelboom/presentatie.html>. Dat adres staat ook op dia 7, in
`classroom.json` en in `lesdoelen.json`. Live bestanden nagekeken: gelijk aan de lokale.

### Stap 2 — De opdracht in Classroom, met de koppeling ✅ *concept op 09-10-2026*

Als **concept** in [3MWb - Informatica](https://classroom.google.com/c/MjUzNTk0NjYzMTJa) (teruggelezen: onderwerp, deadline,
20 punten, de link heet *Lespagina · Les 3 · …*, *Stagemail* als `STUDENT_COPY`). Toewijzen doe je zelf met
**Toewijzen**.

| | Opdracht: **Les 3 — Professionele e-mail aan een stageplaats** |
|---|---|
| **Onderwerp** | Module 1 — Organiseren en professioneel communiceren |
| **Bijlage 1** | de link naar de lespagina |
| **Bijlage 2** | `Stagemail` (Google-document) — **Een kopie maken voor elke leerling** |
| **Punten** | 20 |
| **Deadline** | vrijdag 16 oktober 2026, 20.00 uur |

```bash
python3 "/Volumes/Littlecisboy/Google drive/Toegepaste Informatica/_tools/zet_opdracht_klaar.py" "/Volumes/Littlecisboy/Google drive/Toegepaste Informatica/2026-2027/W07 - Les 03 - MW - Professionele e-mail aan een stageplaats" --proef
```

Instructietekst (het script vult de deadline in; er is geen e-mailadres nodig):

```text
Open de lespagina en werk stap 1 tot 7 af.
Je schrijft alles in je werkdocument Stagemail. Je hebt niets anders nodig.

Klik op Inleveren, ten laatste vrijdag 16 oktober 2026 om 20.00 uur.
```

### Stap 3 — Met de hand, als de koppeling niet werkt

1. Upload `werkdocument/Stagemail.docx` **in Drive zelf** (**Nieuw** › **Bestand uploaden**, met *Uploads
   converteren* aan).
2. Voeg het in de opdracht toe met **Bijvoegen** › **Drive**, met **Een kopie maken voor elke leerling**
   (alleen vóór je de opdracht post).
3. Voeg de lespagina toe met **Link**.

### De AI-hulp ✅ *klaargezet op 09-10-2026*

De Gemini Notebook **AI-hulp · Les 3 · Professionele e-mail aan een stageplaats** hangt aan het concept in
3MWb (teruggelezen via de API: nog `DRAFT`, met de bijlage `notebook`). Bron: `ai-bron.txt` (de volledige
tekst van de lespagina, gemaakt met `_tools/maak_ai_bron.py`). Bij **Chat instellen**: *Aangepast* met de
vaste instructie uit `_afspraken/ai-hulp.md`, reactielengte *Korter*. *Bovenaan de lesgroep plaatsen* staat
uit. Op de lespagina staat de AI-hulp aan (`data-ai-hulp="aan"`): in *Vast?* en op de theoriekaart.

**Getest** in de *Testklas AI-hulp (Claude)* met het testaccount demoleerling3: de leerling opent de
notebook vanuit de opdracht; jouw chatinstelling geldt ook voor de leerling; de antwoorden zijn kort, uit de
les en met bronnummers; de AI schrijft de e-mail niet ("Ik schrijf de e-mail niet in jouw plaats …"), vraagt
geen namen, en zegt bij een vraag buiten de les: "Dat staat niet in deze les." Jij hoeft niets meer te doen:
wijs de opdracht toe zoals altijd. Zie je bij een echte leerling een foutmelding, zeg het dan: dan zet ik de
AI-hulp weer uit op de lespagina.

### De demo klaarzetten (1 minuut)

Op dia 5 toon je het wisselen tussen de lespagina en *Stagemail*. Gebruik daarvoor je eigen kopie: in je map
*Demo voor schermafbeeldingen (Claude)* staat *Test Stagemail (Claude)* (Google-document, met niemand gedeeld).
Open het en de lespagina in twee tabbladen.

### Afvinklijst vóór de les

- [ ] De lespagina staat online en het adres op dia 7 klopt.
- [ ] De opdracht staat klaar in `3MWb - Informatica`, met de lespagina en *Stagemail* als **kopie per
      leerling**, en is toegewezen.
- [ ] Het wachtwoord van de computers staat op het bord (niet op de dia's: die zijn openbaar).
- [ ] *Test Stagemail (Claude)* en de lespagina staan open in twee tabbladen voor de demo.
- [ ] De Dalton-lesfiche staat in je planner (open `dalton-lesfiche.html`, klik op **Kopieer de fiche**, plak).
- [ ] `presentatie.html` opent op de beamer; `N` toont je notities, `F` is volledig scherm.

### 2b. Nagelezen klikpaden

| Handeling | Klikpad / naam | Bron |
|---|---|---|
| Naar de opdracht (dia 1) | classroom.google.com › **Inloggen** › de lesgroep › **Schoolwerk** › de opdracht › **Instructies bekijken** | [Classroom 6020285](https://support.google.com/edu/classroom/answer/6020285?hl=nl&co=GENIE.Platform%3DDesktop) (09-10-2026) |
| Inleveren | **Inleveren** · **Inleveren ongedaan maken** | idem |
| Aan, Cc, Bcc (uitleg) | de velden **Aan**, **Cc**, **Bcc**; Cc: "geen actie hoeven te ondernemen"; Bcc: adres verborgen | [Gmail 2819488](https://support.google.com/mail/answer/2819488?hl=nl&co=GENIE.Platform%3DDesktop) (09-10-2026) |

Er staan geen knopnamen van Gmail of Documenten in de stappen: de leerlingen typen alleen in een tabel van
hun werkdocument.

## 3. Het verloop van de les

| Fase | Tijd | Dia | Wat |
|---|---|---|---|
| Start | 0–2' | 1 | aanmelden met de vaste startdia, tot de lespagina open is |
| Lesstart | 2–5' | 2 | waar bewaar je je stagewerk? (vingers, dan →) |
| Ik doe | 5–10'30" | 3–6 | lesdoel · de zes delen · lezen hier, schrijven daar (twee tabbladen) · fout 1 van Kobe |
| Keuzewerktijd | 10'30"–50' | 7 | stap 1–7, *Zo werk je verder* blijft staan |
| Afsluiten | laatste minuut | 8 | de exitvraag; wie niet klaar is, levert toch in |

**Eerste rondgang:** heeft iedereen de lespagina én *Stagemail* open, in twee tabbladen? Dat is wat in les 2
het meest vastliep. **Tweede rondgang** (stap 4–5): Aan en Cc juist overgetypt, *u* in plaats van *je*?

## 4. Verbetersleutel

- **Deel 1**, de vijf fouten: geen onderwerp (voorbeeld) · *hey lien* (te los, voornaam, geen hoofdletter en
  komma) · Kobe zegt niet wie hij is en wanneer zijn stage is · chattaal (*??*, emoji) · *mvg* en geen
  volledige naam.
- **Deel 2**: a **Aan** · b **Cc** · c **Bcc**. Vraag 1: een e-mailadres is persoonlijke informatie; met Bcc
  ziet niemand de adressen van de anderen.
- **Deel 3**, de e-mail: zie de criteria in `lesvoorbereiding.md` §22 (20 punten).
- **Deel 5**: de mentor ziet meteen van wie de e-mail is en waarover; ze vindt hem later terug.

### Essentiële fouten — geef hier altijd feedback op

- Geen onderwerp, of een onderwerp als *stage*.
- *Hey* of de voornaam van de mentor.
- Geen naam onder de e-mail.
- De mentor in Cc, of de stagebegeleider in Aan.

## 5. Schermafbeeldingen

Niet nodig: de beelden op de startpagina, in stap 2 en op de dia's zijn tekeningen in HTML en CSS.

## 6. Het materiaal opnieuw maken

```bash
cd "/Volumes/Littlecisboy/Google drive/Toegepaste Informatica/2026-2027/W07 - Les 03 - MW - Professionele e-mail aan een stageplaats/werkdocument" && python3 maak_werkdocumenten.py
```

## 7. Leerplandoelen in je jaaroverzicht

`lesdoelen.json` (klasgroep `3 MW`): `BV2_04.01` kern · `BV2_02.07`, `BV2_02.07.02`, `BV2_02.12`
ondersteunend · `BV2_04.04` voorbereidend. De pre-push hook schrijft ze in `Leerplandoelen 2026-2027.xlsx`.

## 8. Wat nog moet blijken in de klas

- Helpen de vaste startdia en de startpagina in beelden om zonder hulp tot bij de opdracht, de lespagina
  en het werkdocument te geraken?
- Lukt het wisselen tussen de twee tabbladen na de demo op dia 5?
- Typen de leerlingen netjes in de vakken van het venster, of schuiven de tabellen in Google Documenten?
- Klopt de tijd van stap 5 (10 minuten) voor een eigen e-mail?
- Kunnen ook de echte leerlingen van 3MWb de AI-hulp openen (getest met demoleerling3)? Helpt hij, of vragen
  ze hem wat op de pagina staat zonder te lezen? Klikken ze op de bronnummers?
