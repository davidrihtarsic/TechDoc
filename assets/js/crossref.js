// === FIGURE CROSS-REFERENCES =====================================

console.log("crossref.js LOADED");
document.addEventListener("DOMContentLoaded", () => {
  console.log("crossref.js DOMContentLoaded");
  let figCounter = 0;
  const figures = {};

  document.querySelectorAll("p").forEach(p => {
    const img = p.querySelector("img");
    if (!img) return;

    // Poiščemo {#fig:...}
    const match = p.innerHTML.match(/\{#(fig:[^}]+)\}/);
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
        ? `<a href="#${id}">slika ${figures[id]}</a>`
        : `??`
  );
});

// === TABLE CROSS-REFERENCES =====================================

let tblCounter = 0;
const tables = {};

document.querySelectorAll("table").forEach(table => {
  const captionP = table.nextElementSibling;

  if (!captionP || captionP.tagName !== "P") return;

  const match = captionP.textContent.match(/\{#(tbl:[^}]+)\}/);
  if (!match) return;

  const id = match[1];
  tblCounter++;
  tables[id] = tblCounter;

  // ID damo tabeli
  table.id = id;

  // očistimo {#tbl:...}
  const captionText = captionP.textContent
    .replace(/\{#tbl:[^}]+\}/, "")
    .replace(/^Table:\s*/i, "")
    .trim();

  // nov napis
  captionP.textContent = `Tabela ${tblCounter}: ${captionText}`;
  captionP.classList.add("table-caption");
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

