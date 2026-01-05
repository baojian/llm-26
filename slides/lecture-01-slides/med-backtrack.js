(function(){
  const COST_INS = 1, COST_DEL = 1, COST_SUB = 2;

  function buildDP(s, t){
    const m = s.length, n = t.length;
    const dp = Array.from({length: m+1}, () => Array(n+1).fill(0));
    dp[0][0] = 0;
    for(let i=1;i<=m;i++) dp[i][0] = dp[i-1][0] + COST_DEL;
    for(let j=1;j<=n;j++) dp[0][j] = dp[0][j-1] + COST_INS;
    for(let i=1;i<=m;i++){
      for(let j=1;j<=n;j++){
        const sub = dp[i-1][j-1] + (s[i-1] === t[j-1] ? 0 : COST_SUB);
        const del = dp[i-1][j] + COST_DEL;
        const ins = dp[i][j-1] + COST_INS;
        dp[i][j] = Math.min(sub, del, ins);
      }
    }
    return dp;
  }

  // deterministic backtrack preference: diag > del > ins
  function backtrackOps(s, t, dp){
    let i = s.length, j = t.length;
    const ops = []; // from end->start
    while(i>0 || j>0){
      // diag (match/sub)
      if(i>0 && j>0){
        const c = (s[i-1] === t[j-1]) ? 0 : COST_SUB;
        if(dp[i][j] === dp[i-1][j-1] + c){
          ops.push({
            op: (c===0 ? "keep" : "sub"),
            a: s[i-1], b: t[j-1],
            i, j, ni: i-1, nj: j-1
          });
          i--; j--;
          continue;
        }
      }
      // delete
      if(i>0 && dp[i][j] === dp[i-1][j] + COST_DEL){
        ops.push({ op:"del", a:s[i-1], b:"*", i, j, ni:i-1, nj:j });
        i--;
        continue;
      }
      // insert
      if(j>0 && dp[i][j] === dp[i][j-1] + COST_INS){
        ops.push({ op:"ins", a:"*", b:t[j-1], i, j, ni:i, nj:j-1 });
        j--;
        continue;
      }

      // fallback (shouldn't happen)
      break;
    }
    ops.reverse(); // forward order
    return ops;
  }

  function renderDPTable(container, s, t, dp){
    // same square-cell look as your MED table, but simpler HTML
    const m = s.length, n = t.length;
    let html = `<table><tr><th></th><th>∅</th>`;
    for(let j=0;j<n;j++) html += `<th>${t[j]}</th>`;
    html += `</tr>`;

    for(let i=0;i<=m;i++){
      html += `<tr>`;
      html += (i===0) ? `<th>∅</th>` : `<th>${s[i-1]}</th>`;
      for(let j=0;j<=n;j++){
        html += `<td id="bt-${i}-${j}" class="${(i===0||j===0) ? "op-init" : ""}">${dp[i][j]}</td>`;
      }
      html += `</tr>`;
    }
    html += `</table>`;
    container.innerHTML = html;
  }

  function clearPath(slide){
    slide.querySelectorAll(".med-table td.path, .med-table td.active").forEach(td=>{
      td.classList.remove("path","active");
    });
  }

  function markCell(slide, i, j){
    const td = slide.querySelector(`#bt-${i}-${j}`);
    if(td){
      td.classList.add("active","path");
    }
  }

  function appendAlign(slide, step){
    const top = slide.querySelector("#alTop");
    const mid = slide.querySelector("#alMid");
    const bot = slide.querySelector("#alBot");

    const a = document.createElement("div");
    a.className = `align-cell ${step.op}`;
    a.textContent = step.a;

    const b = document.createElement("div");
    b.className = `align-cell ${step.op}`;
    b.textContent = step.b;

    const m = document.createElement("div");
    m.className = `align-cell ${step.op}`;
    // middle connector
    if(step.op === "keep") m.textContent = "|";
    else if(step.op === "sub") m.textContent = "≠";
    else m.textContent = " ";
    // show gaps more explicitly
    if(step.a === "*" || step.b === "*") m.textContent = " ";

    top.appendChild(a);
    mid.appendChild(m);
    bot.appendChild(b);
  }

  function popAlign(slide){
    ["#alTop","#alMid","#alBot"].forEach(sel=>{
      const row = slide.querySelector(sel);
      if(row && row.lastElementChild) row.removeChild(row.lastElementChild);
    });
  }

  function initBacktrackSlide(slide){
    if(slide.__bt) return;

    const s = slide.getAttribute("data-s") || "intention";
    const t = slide.getAttribute("data-t") || "execution";

    const dp = buildDP(s, t);
    const ops = backtrackOps(s, t, dp);

    // render table
    const tableHost = slide.querySelector("#btTable");
    renderDPTable(tableHost, s, t, dp);

    // auto-generate fragments
    const frags = slide.querySelector(".bt-frags");
    frags.innerHTML = "";
    for(let k=0;k<ops.length;k++){
      const sp = document.createElement("span");
      sp.className = "fragment btfrag";
      sp.setAttribute("data-fragment-index", String(k));
      frags.appendChild(sp);
    }
    Reveal.sync();

    slide.__bt = { s, t, dp, ops };
  }

  function onStepShown(slide, idx){
    const st = slide.__bt;
    if(!st) return;
    const step = st.ops[idx];

    // highlight current cell and the next cell along the path
    clearPath(slide);
    // show current (i,j) as we “arrive” there during forward alignment build
    markCell(slide, step.ni, step.nj);
    markCell(slide, step.i, step.j);

    appendAlign(slide, step);
  }

  function onStepHidden(slide, idx){
    const st = slide.__bt;
    if(!st) return;
    popAlign(slide);
    clearPath(slide);

    // highlight previous step cell (if exists)
    const prev = idx - 1;
    if(prev >= 0){
      const p = st.ops[prev];
      markCell(slide, p.ni, p.nj);
      markCell(slide, p.i, p.j);
    }
  }

  Reveal.on("slidechanged", e => {
    const slide = e.currentSlide;
    if(slide && slide.classList.contains("med-bt-slide")){
      initBacktrackSlide(slide);
    }
  });

  Reveal.on("ready", e => {
    const slide = e.currentSlide;
    if(slide && slide.classList.contains("med-bt-slide")){
      initBacktrackSlide(slide);
    }
  });

  Reveal.on("fragmentshown", e => {
    const slide = Reveal.getCurrentSlide();
    if(!slide || !slide.classList.contains("med-bt-slide")) return;
    const idx = parseInt(e.fragment.getAttribute("data-fragment-index") || "0", 10);
    onStepShown(slide, idx);
  });

  Reveal.on("fragmenthidden", e => {
    const slide = Reveal.getCurrentSlide();
    if(!slide || !slide.classList.contains("med-bt-slide")) return;
    const idx = parseInt(e.fragment.getAttribute("data-fragment-index") || "0", 10);
    onStepHidden(slide, idx);
  });
})();