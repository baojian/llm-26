(function(){
  // Only run if the slide exists
  function isBpeSlideActive(){
    const s = Reveal.getCurrentSlide();
    return !!(s && s.dataset && s.dataset.bpeDemo === "1");
  }

  // Initial corpus (exactly from the toy example slide)
  const corpus0 = [
    { count: 5, tokens: ["l","o","w","_"] },
    { count: 2, tokens: ["l","o","w","e","s","t","_"] },
    { count: 6, tokens: ["n","e","w","e","r","_"] },
    { count: 3, tokens: ["w","i","d","e","r","_"] },
    { count: 2, tokens: ["n","e","w","_"] },
  ];

  const initVocab = ["_","d","e","i","l","n","o","r","s","t","w"];

  // Merge list following your slides
  const merges = [
    ["e","r","er"],
    ["er","_","er_"],
    ["n","e","ne"],
    ["ne","w","new"],
    ["l","o","lo"],
    ["lo","w","low"],
    ["new","er_","newer_"],
    ["low","er_","low_"]
  ];

  let step = 0;
  let corpus = null;
  let vocab = null;
  let done = false;

  function cloneCorpus(c){
    return c.map(x => ({count: x.count, tokens: x.tokens.slice()}));
  }

  function applyMerge(pairA, pairB, merged){
    corpus.forEach(row => {
      const out = [];
      const t = row.tokens;
      for(let i=0;i<t.length;i++){
        if(i < t.length-1 && t[i]===pairA && t[i+1]===pairB){
          out.push(merged);
          i++; // skip next
        }else{
          out.push(t[i]);
        }
      }
      row.tokens = out;
    });
    if(!vocab.includes(merged)) vocab.push(merged);
  }

  function render(){
    const elV = document.getElementById("bpeVocab");
    const elC = document.getElementById("bpeCorpus");
    const elS = document.getElementById("bpeStep");

    if(!elV || !elC || !elS) return;

    elV.textContent = "{ " + vocab.join(", ") + " }";

    elC.textContent = corpus.map(r => {
      return String(r.count).padStart(2," ") + "  " + r.tokens.join(" ");
    }).join("\n");

    if(step < merges.length){
      const [a,b,m] = merges[step];
      elS.innerHTML = `Merge <code>${a} ${b}</code> → <code>${m}</code>   <span style="opacity:.65;font-weight:800;">(${step+1}/${merges.length})</span>`;
    }else{
      elS.innerHTML = `<b>Done.</b> (Press → to continue)`;
    }
  }

  function reset(){
    step = 0;
    done = false;
    corpus = cloneCorpus(corpus0);
    vocab = initVocab.slice();
    render();
  }

  function nextStep(){
    if(done) return false;
    if(step >= merges.length){
      done = true;
      render();
      return false;
    }
    const [a,b,m] = merges[step];
    applyMerge(a,b,m);
    step++;
    render();
    if(step >= merges.length){
      // allow next → to leave slide
      done = true;
    }
    return true; // consumed
  }

  // Reset when we enter this slide
  Reveal.on("slidechanged", () => {
    if(isBpeSlideActive()) reset();
  });

  // Intercept → while we are on this slide
  document.addEventListener("keydown", (e) => {
    if(!isBpeSlideActive()) return;
    if(e.key === "ArrowRight" || e.key === "PageDown" || e.key === " "){
      if(!done){
        e.preventDefault();
        e.stopPropagation();
        nextStep();
      }
      // if done=true, reveal handles it normally (next slide)
    }
  }, true);
})();