// Small progressive enhancements: expandable texts and the year filter.
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.expandable').forEach(function (box) {
    var body = box.querySelector('.expandable-body');
    var button = box.querySelector('.expand-toggle');
    if (!body || !button) return;
    var label = button.firstChild.textContent;
    if (body.scrollHeight <= body.clientHeight + 4) return; // short text: no toggle
    box.classList.add('collapsed');
    button.addEventListener('click', function () {
      var open = box.classList.toggle('open');
      box.classList.toggle('collapsed', !open);
      button.setAttribute('aria-expanded', open ? 'true' : 'false');
      button.firstChild.textContent = open ? 'Show less ' : label;
    });
  });

  var filter = document.querySelector('.year-filter');
  if (filter) {
    filter.addEventListener('click', function (event) {
      var btn = event.target.closest('button');
      if (!btn) return;
      filter.querySelectorAll('button').forEach(function (b) { b.classList.toggle('active', b === btn); });
      var year = btn.dataset.year;
      document.querySelectorAll('#papers-list .paper-entry').forEach(function (li) {
        li.hidden = year !== 'all' && li.dataset.year !== year;
      });
    });
  }
});
