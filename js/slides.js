/**
 * Klassikale dia's · De Speelboom · Les 3 Professionele e-mail aan een stageplaats
 * presentatie.html — één reeks dia's voor de fase "Ik doe".
 * →/spatie: volgende (eerst onthullingen), ←: vorige, F: volledig scherm, N: sprekersnotities
 */
(function () {
  'use strict';
  var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var notesBox = document.getElementById('notes');
  var counter = document.getElementById('counter');
  var i = 0;

  // schaal het 1280x720-podium naar het scherm
  var stage = document.querySelector('.stage');
  function fit() {
    var s = Math.min(window.innerWidth / 1280, window.innerHeight / 720);
    stage.style.transform = 'scale(' + s + ')';
  }
  window.addEventListener('resize', fit);
  fit();

  /* ---------- Kloktijden op de dia Zo werk je verder (sinds 11-10-2026) ----------
   * De lesmomenten van deze les en de beltijden staan op .kloklijst (data-lesmomenten, data-beltijden),
   * gezet door _tools/zet_lesmomenten.py uit de planning (_afspraken/presentatie.md).
   * 1. Nu is een gepland lesmoment van deze les: van nu tot de bel, min 1 minuut voor de exitvraag.
   * 2. Anders (voorbereiden, 's avonds, een tussenuur): de uren van het volgende geplande lesmoment, met de
   *    dag erbij: begin van het lesuur + de instructie (data-instructie, standaard 10) + de stap die samen
   *    gebeurt.
   * 3. Geen lesmoment bekend: tijdens een lesuur van nu tot de bel, anders de geplande minuten.
   * De tijd verdeelt zich over de stappen volgens hun minuten (data-min); data-samen = al samen gedaan.
   * T rekent opnieuw, en tijdens een lesuur vanaf nu (een les die verschoven is, of de dia te vroeg getoond). */
  var BEL_LEF = '8.25-9.15 9.15-10.05 10.25-11.15 11.15-12.05 12.05-12.55 13.45-14.35 14.35-15.25 15.25-16.15 16.15-17.05';
  var DAGEN = ['zo', 'ma', 'di', 'wo', 'do', 'vr', 'za'];
  function minuut(t) { var d = t.split('.'); return parseInt(d[0], 10) * 60 + parseInt(d[1], 10); }
  function klok(min) { var h = Math.floor(min / 60), m = min % 60; return h + '.' + (m < 10 ? '0' : '') + m; }
  function twee(n) { return (n < 10 ? '0' : '') + n; }
  function kloktijden(slide, opnieuw) {
    var lijst = slide.querySelector('.kloklijst');
    if (!lijst || (slide.hasAttribute('data-tijden') && !opnieuw)) return;
    var nu = new Date(), nuMin = nu.getHours() * 60 + nu.getMinutes();
    var vandaag = nu.getFullYear() + '-' + twee(nu.getMonth() + 1) + '-' + twee(nu.getDate());
    var items = Array.prototype.slice.call(lijst.querySelectorAll('[data-min]'));
    var open = items.filter(function (li) { return !li.hasAttribute('data-samen'); });
    var samen = items.filter(function (li) { return li.hasAttribute('data-samen'); })
      .reduce(function (som, li) { return som + parseInt(li.getAttribute('data-min'), 10); }, 0);
    var plan = open.reduce(function (som, li) { return som + parseInt(li.getAttribute('data-min'), 10); }, 0);
    var kop = slide.querySelector('.eindtijd');

    var huidig = null;
    (lijst.getAttribute('data-beltijden') || BEL_LEF).split(' ').forEach(function (b) {
      var x = b.split('-'), van = minuut(x[0]), tot = minuut(x[1]);
      if (nuMin >= van && nuMin < tot) huidig = tot;
    });
    var momenten = (lijst.getAttribute('data-lesmomenten') || '').split(';').filter(Boolean).map(function (m) {
      var x = m.split('/');
      return { datum: x[0], van: minuut(x[1]), tot: minuut(x[2]), klas: x[3], uur: x[4] };
    });
    var nuGepland = momenten.filter(function (m) { return m.datum === vandaag && nuMin >= m.van && nuMin < m.tot; })[0];
    var schooldag = nu.getDay() >= 1 && nu.getDay() <= 5;
    var start = null, eind = null, dag = '';
    if (nuGepland) {
      start = nuMin; eind = nuGepland.tot - 1;
    } else if (huidig && schooldag && (opnieuw || !momenten.length)) {
      start = nuMin; eind = huidig - 1;
    } else if (momenten.length) {
      var komend = momenten.filter(function (m) { return m.datum > vandaag || (m.datum === vandaag && m.tot > nuMin); });
      var m = komend[0] || momenten[momenten.length - 1];
      start = m.van + parseInt(lijst.getAttribute('data-instructie') || '10', 10) + samen;
      eind = m.tot - 1;
      var d = new Date(m.datum + 'T12:00:00');
      dag = DAGEN[d.getDay()] + ' ' + m.datum.slice(8, 10) + '-' + m.datum.slice(5, 7) + ', ' + m.klas + ', ' + m.uur + 'de uur · ';
    }
    if (start === null || eind <= start) {
      open.forEach(function (li) { li.querySelector('.tijd').textContent = li.getAttribute('data-min') + "'"; });
      if (kop) kop.textContent = plan + ' minuten';
      slide.setAttribute('data-tijden', '1');
      return;
    }
    var factor = (eind - start) / plan, som = 0, t = start;
    open.forEach(function (li, k) {
      som += parseInt(li.getAttribute('data-min'), 10);
      t = (k === open.length - 1) ? eind : start + Math.round(som * factor);
      li.querySelector('.tijd').textContent = 'tot ' + klok(t);
    });
    if (kop) kop.textContent = dag + 'tot ' + klok(t);
    slide.setAttribute('data-tijden', '1');
  }

  function show(n) {
    i = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach(function (s, k) { s.classList.toggle('active', k === i); });
    kloktijden(slides[i], false);
    var note = slides[i].querySelector('template.note');
    notesBox.innerHTML = '<h3>Dia ' + (i + 1) + ' / ' + slides.length + '</h3>' + (note ? note.innerHTML : '<p>Geen notities.</p>');
    if (counter) counter.textContent = (i + 1) + ' / ' + slides.length;
    try { sessionStorage.setItem('dia_speelboom_stagemail', String(i)); } catch (e) {}
  }

  function next() {
    var s = slides[i];
    var hidden = s.querySelector('.reveal-item:not(.shown)');
    if (hidden) { hidden.classList.add('shown'); return; }
    if (s.hasAttribute('data-answer') && !s.classList.contains('revealed')) { s.classList.add('revealed'); return; }
    show(i + 1);
  }
  function prev() { show(i - 1); }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') { e.preventDefault(); next(); }
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); prev(); }
    else if (e.key === 'f' || e.key === 'F') {
      if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(function () {});
      else document.exitFullscreen();
    }
    else if (e.key === 'n' || e.key === 'N') { document.body.classList.toggle('show-notes'); }
    else if (e.key === 't' || e.key === 'T') { kloktijden(slides[i], true); }
  });
  document.querySelector('.deck').addEventListener('click', function (e) {
    if (e.target.closest('a')) return;
    if (e.clientX < window.innerWidth / 4) prev(); else next();
  });

  var start = 0;
  try { start = parseInt(sessionStorage.getItem('dia_speelboom_stagemail') || '0', 10) || 0; } catch (e) {}
  show(start);
})();
