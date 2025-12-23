
console.log("crossref.js LOADED");
document.addEventListener("DOMContentLoaded", () => {
  console.log("crossref.js DOMContentLoaded");
  // === FIGURE CROSS-REFERENCES =====================================
  let figCounter = 0;
  const figures = {};

  document.querySelectorAll("p").forEach(p => {
    const img = p.querySelector("img");
    if (!img) return;

    // Poiščemo {#fig:...}
    //const match = p.innerHTML.match(/\{#(fig:[^}]+)\}/);
    const match = p.innerHTML.match(/\{#fig:([^\s}]+)[^}]*\}/);
    if (!match) return;

    const id = match[1];
    figCounter++;
    figures[id] = figCounter;

    // ID damo sliki
    img.id = id;

    // odstranimo {#fig:...} iz HTML-ja
    p.innerHTML = p.innerHTML.replace(/\{#fig:[^}]+\}/, "");

    // dodamo napis
    const caption = document.createElement("div");
    caption.className = "figure-caption";
    caption.textContent = `Slika ${figCounter}: ${img.alt || ""}`;

    p.appendChild(caption);
  });

  // zamenjamo sklice [@fig:...]
  document.body.innerHTML = document.body.innerHTML.replace(
    /\[@(fig:[^\]]+)\]/g,
    (_, id) =>
      figures[id]
        ? `<a href="#${id}">sl. ${figures[id]}</a>`
        : `??`
  );


// === TABLE CROSS-REFERENCES =====================================

  let tblCounter = 0;
  const tables = {};

  document.querySelectorAll("div.table-wrapper").forEach(wrapper => {
    const table = wrapper.querySelector("table");
    if (!table) return;

    // napis tabele je v <p> ZA wrapperjem
    let captionP = wrapper.nextElementSibling;
    while (captionP && captionP.tagName !== "P") {
      captionP = captionP.nextElementSibling;
    }
    if (!captionP) return;

    // poiščemo {#tbl:...}
    const match = captionP.textContent.match(/\{#(tbl:[^}]+)\}/);
    if (!match) return;

    const id = match[1];
    tblCounter++;
    tables[id] = tblCounter;

    // ID damo tabeli
    table.id = id;

    // očistimo napis
    const captionText = captionP.textContent
      .replace(/\{#tbl:[^}]+\}/, "")
      .replace(/^Table:\s*/i, "")
      .trim();

    // nov napis
    captionP.textContent = `Tabela ${tblCounter}: ${captionText}`;
    captionP.classList.add("table-caption");

    // PREMAKNEMO NAPIS PRED TABELO
    wrapper.parentNode.insertBefore(captionP, wrapper);
  });

  // zamenjava sklicev [@tbl:...]
  document.body.innerHTML = document.body.innerHTML.replace(
    /\[@(tbl:[^\]]+)\]/g,
    (_, id) =>
      tables[id]
        ? `<a href="#${id}">tabela ${tables[id]}</a>`
        : `??`
  );
  console.log("TABLE DEBUG: tables found =", document.querySelectorAll("table").length);

// === EQUATION CROSS-REFERENCES ==================================

if (window.MathJax && MathJax.Hub) {
  MathJax.Hub.Queue(() => {

    let eqCounter = 0;
    const equations = {};

    document.querySelectorAll('script[type="math/tex"]').forEach(script => {
      const p = script.parentElement;
      if (!p || p.tagName !== "P") return;

      // poiščemo text node z {#eq:...}
      let labelNode = null;
      p.childNodes.forEach(node => {
        if (node.nodeType === Node.TEXT_NODE && /\{#eq:[^}]+\}/.test(node.textContent)) {
          labelNode = node;
        }
      });
      if (!labelNode) return;

      const match = labelNode.textContent.match(/\{#(eq:[^}]+)\}/);
      if (!match) return;

      const id = match[1];
      eqCounter++;
      equations[id] = eqCounter;

      // MathJax container
      const container = script.previousElementSibling;
      if (!container || !container.classList.contains("MathJax")) return;

      // ID damo na MathJax element
      container.id = id;

      // IZBRIŠEMO SAMO LABEL iz text node-a
      labelNode.textContent = labelNode.textContent.replace(/\{#eq:[^}]+\}/, "");

      // dodamo številko enačbe
      const tag = document.createElement("span");
      tag.className = "equation-number";
      tag.textContent = `(${eqCounter})`;

      // === WRAPPER ZA PORAVNAVO ======================================

      // ustvarimo wrapper
      const wrapper = document.createElement("div");
      wrapper.className = "equation-wrapper";

      // wrapper postavimo TJA, kjer je bila enačba
      container.parentNode.insertBefore(wrapper, container);

      // prestavimo MathJax element v wrapper
      wrapper.appendChild(container);

      // dodamo še številko
      wrapper.appendChild(tag);
    });

    // zamenjava sklicev [@eq:...]
    document.body.innerHTML = document.body.innerHTML.replace(
      /\[@(eq:[^\]]+)\]/g,
      (_, id) =>
        equations[id]
          ? `<a href="#${id}">en. ${equations[id]}</a>`
          : `??`
    );

  });
}
//konec DOMContentLoad-erja
});

