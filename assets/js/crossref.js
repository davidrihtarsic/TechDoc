//ta test dela
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
