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
   * Bij het eerste tonen: de tijd tot het belsignaal (min 1 minuut voor de exitvraag)
   * wordt verdeeld over de stappen, volgens hun geplande minuten (data-min).
   * Een stap met data-samen is al samen gedaan. Buiten een lesuur: de geplande minuten vanaf nu.
   * T rekent opnieuw. Beltijden campus LEF: _afspraken/school-en-klassen.md. */
  var BEL = [[8, 25, 9, 15], [9, 15, 10, 5], [10, 25, 11, 15], [11, 15, 12, 5], [12, 5, 12, 55],
             [13, 45, 14, 35], [14, 35, 15, 25], [15, 25, 16, 15], [16, 15, 17, 5]];
  function klok(min) { var h = Math.floor(min / 60), m = min % 60; return h + '.' + (m < 10 ? '0' : '') + m; }
  function kloktijden(slide, opnieuw) {
    var lijst = slide.querySelector('.kloklijst');
    if (!lijst || (slide.hasAttribute('data-tijden') && !opnieuw)) return;
    var nu = new Date(), nuMin = nu.getHours() * 60 + nu.getMinutes(), eind = null;
    BEL.forEach(function (b) {
      var van = b[0] * 60 + b[1], tot = b[2] * 60 + b[3];
      if (nuMin >= van && nuMin < tot) eind = tot - 1;
    });
    var open = Array.prototype.filter.call(lijst.querySelectorAll('[data-min]'), function (li) { return !li.hasAttribute('data-samen'); });
    var plan = open.reduce(function (som, li) { return som + parseInt(li.getAttribute('data-min'), 10); }, 0);
    var factor = (eind && eind > nuMin) ? (eind - nuMin) / plan : 1;
    var t = nuMin, som = 0;
    open.forEach(function (li, k) {
      som += parseInt(li.getAttribute('data-min'), 10);
      t = (eind && k === open.length - 1) ? eind : nuMin + Math.round(som * factor);
      li.querySelector('.tijd').textContent = 'tot ' + klok(t);
    });
    var kop = slide.querySelector('.eindtijd');
    if (kop) kop.textContent = 'tot ' + klok(t);
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
