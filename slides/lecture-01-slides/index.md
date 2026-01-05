<section class="title">
  <div class="title-main">NLP and LLMs (CS40008.01)</div>
  <div class="title-sub">Lecture 01 – Introduction to NLP</div>

  <div class="title-meta">
    <div>Baojian Zhou</div>
    <div>NLP and LLMs (CS40008.01)</div>
    <div>School of Data Science, Fudan University</div>
    <div>03/05/2026</div>
  </div>
  <img
  src="media/ppt/media/image1.jpeg"
  alt="overlay"
  style="
    position: fixed;
    right: 18px;
    bottom: 18px;
    max-width: 60vw;
    max-height: 60vh;
    width: auto;
    height: auto;
    z-index: 9999;
    pointer-events: none;
    opacity: 0.95;
  "/>
</section>

---

<section class="ppt">

  <div class="ppt-title">About me</div>
  <div class="ppt-line"></div>

  <p><b>Email:</b> bjzhou@fudan.edu.cn</p>
  <p><b>Course Website:</b> <a href="https://baojian.github.io/llm-26/" target="_blank" rel="noopener">https://baojian.github.io/llm-26/</a></p>
  <p><b>Course Github:</b> <a href="https://github.com/baojian/llm-26" target="_blank" rel="noopener">https://github.com/baojian/llm-26</a></p>
  <p><b>Location:</b> South-401, Computing Center</p>
  <p><b>Office hour:</b> Wed. 10:00am–11:30am</p>
  <p><b>Research interests:</b> Machine learning on graphs, optimization, text mining (e.g., word embeddings), diffusion models, and in-context learning on LLMs.</p>
</section>

---

<section class="ppt">
  <div class="ppt-title">Outline</div>
  <div class="ppt-line"></div>
  
  <ul class="outline-bullets big">
  <li class="active">Course Overview</li>
  <li class="muted">Development of NLP & LLMs</li>
  <li class="muted">Basics for Text Preprocessing</li>
  <li class="muted">Text Tokenization</li>
  </ul>
</section>

---


<section class="ppt">
  <div class="ppt-title">What is natural language?</div>
  <div class="ppt-line"></div>
  
  **A structured system of communication used by humans**
  - 今天天气真好！
  - The weather is so nice today!
  - Le temps est vraiment beau aujourd’hui !

  **Formal Language (e.g., programming languages)**
  
  <div class="code-grid-3">
  <div class="cell">

  C<br>

  ```c
    #include<stdio.h>  
    int main(void){
      printf (“Hello, world!\n”);
      }
  ```
  </div>

  <div class="cell">

  Python<br>
  
  ```python
    def factorial(n: int) -> int:
      if n < 0:
          raise ValueError("n must be non-negative")
      result = 1
      for k in range(2, n + 1):
          result *= k
      return result
    print("5! =", factorial(5))
  ```
  </div>
  <div class="cell">

  Rust<br>

  ```rust
    fn factorial(n: u64) -> u64 {
      let mut result = 1;
      for k in 2..=n {
          result *= k;
      }
      result
    }
    fn main() {
        println!("5! = {}", factorial(5));
    }
  ```
  </div>
  
  </div>

</section>

---

<section class="ppt">
  <div class="ppt-title">Natural Language Processing (NLP)</div>
  <div class="ppt-line"></div>

  <div class="twocol" style="--left: 57%;">
    <div class="text">
      <div style="font-size:40px; line-height:1.35; font-weight:800;">
        NLP focuses on enabling computers to <span style="color:#d00;">understand</span> and <span style="color:#d00;">generate</span> text-based language in a way that is meaningful and useful: <span class="fudanblue">we care about language understanding and generation</span>.
      </div>
      <ul style="margin-top:20px; font-size:36px; line-height:1.45;">
        <li>Techniques developed in NLP can also be applied to code and other sequential data.</li>
      </ul>
    </div>
    <div class="fig">
      <img src="media/ppt/media/nlp-ai-ml-dl-nlp.png" alt="NLP figure"
           style="width:90%; max-width:450px; height:auto; border-radius:12px;">
    </div>
  </div>

  <div class="fragment" style="margin-top:10px; font-size:40px; font-weight:800;">
  <span style="color:#d00;">
    Modern LLMs are large neural models trained on massive text corpora to learn patterns in data and generalize across many NLP tasks.
  </span>
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">Example of LLMs – Ollama (Qwen3:1.7B)</div>
  <div class="ppt-line"></div>

  <iframe src="./ollama-demo.html"
          style="width:100%; height:620px; border:0; border-radius:12px;"></iframe>
</section>

---

<section class="ppt">
  <div class="ppt-title">Tasks – Sentiment Analysis</div>
  <div class="ppt-line"></div>

  <div class="twocol" style="--left: 40%;">
    <!-- LEFT: examples -->
    <div class="sa-left">
      <div class="sa-hint">Click an example:</div>
      <button class="sa-ex" data-text="Nice and compact to carry!">
        ✅ Nice and compact to carry!
      </button>
      <button class="sa-ex" data-text="Since the camera is small and light, I won't need to carry around those heavy, bulky professional cameras either!">
        ✅ Since the camera is small and light, I won't need to carry around those heavy, bulky professional cameras either!
      </button>
      <button class="sa-ex" data-text="The camera feels flimsy, is plastic and very light in weight you have to be very delicate in the handling of this camera.">
        ❌ The camera feels flimsy, is plastic and very light in weight you have to be very delicate in the handling of this camera.
      </button>
    </div>
    <!-- RIGHT: ollama demo -->
    <div class="sa-right">
      <iframe
        id="ollamaFrame"
        src="./ollama-sentiment-analysis.html?task=sentiment"
        style="width:100%; height:620px; border:0; border-radius:12px;">
      </iframe>
    </div>
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">Task – Machine Translation (ZH → EN)</div>
  <div class="ppt-line"></div>

  <div class="twocol" style="--left: 42%;">
    <!-- LEFT: examples -->
    <div class="mt-left">
      <div class="sa-hint">Click an example (Chinese source):</div>
      <button class="sa-ex" data-text="Google Translate支持249种语言。日均用户超过2亿人，2016年4月总用户数超过5亿人，每天翻译超过1000亿个单词。">
        Example 1: Google Translate (stats)
      </button>
      <button class="sa-ex" data-text="人工智能亦称智械、机器智能，指由人制造出来的机器所表现出来的智能。通常人工智能是指通过普通计算机程序来呈现人类智能的技术。该词也指出研究这样的智能系统是否能够实现，以及如何实现。同时，通过医学、神经科学、机器人学及统计学等的进步，常态预测则认为人类的很多职业也逐渐被其取代。">
        Example 2: AI definition (encyclopedic)
      </button>
    </div>
    <!-- RIGHT: ollama -->
    <div class="mt-right">
      <iframe
        id="ollamaFrameMT"
        src="./ollama-machine-translation.html?task=translate&src=zh&tgt=en"
        style="width:100%; height:620px; border:0; border-radius:12px;">
      </iframe>
    </div>
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">Task – Article Generation</div>
  <div class="ppt-line"></div>

  <div class="twocol" style="--left: 43%;">
    <!-- LEFT -->
    <div class="art-card">
      <div class="art-head">A · Blog</div>
      <div class="art-body">
        <div class="art-k">Title: Feeling unproductive? Maybe you should stop overthinking.</div>
        <div class="art-k" style="margin-top:10px;">Content:</div>
        <div class="art-v">
          In order to get something done, maybe we need to think less. Seems counter-intuitive,
          but I believe sometimes our thoughts can get in the way of the creative process.
          We can work better at times when we "tune out" the external world and focus on what's
          in front of us. I've been thinking about this lately, so I thought it would be good
          to write an article about it…
        </div>
      </div>
    </div>
    <!-- RIGHT -->
    <div class="art-card">
      <div class="art-head">B · News article</div>
      <div class="art-body">
        <div class="art-k">Title: United Methodists Agree to Historic Split</div>
        <div class="art-v"></div>
        <div class="art-k" style="margin-top:10px;">Content:</div>
        <div class="art-v">
          After two days of intense debate, the United Methodist Church has agreed to a historic split —
          one that is expected to end in the creation of a new denomination, one that will be
          “theologically and socially conservative,” according to The Washington Post. The majority of
          delegates attending the church‘s annual General Conference in May voted to strengthen a ban on
          the ordination of LGBTQ clergy and to write new rules that will “discipline” clergy who officiate
          at same-sex weddings. But those who opposed these measures have a new plan…
        </div>
      </div>
    </div>
  </div>

  <div class="quiz-row">
    <button class="quiz-btn">1) A: Human · B: Human</button>
    <button class="quiz-btn">2) A: Machine · B: Human</button>
    <button class="quiz-btn">3) A: Human · B: Machine</button>
    <button class="quiz-btn" data-fragment-index="1">4) A: Machine · B: Machine</button>
  </div>

  <div class="quiz-hint fragment" data-fragment-index="1">
    <b>Correct answer: 4)</b>. They are all generated by GPT-3!
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">Task – Image Understanding</div>
  <div class="ppt-line"></div>

  <div class="twocol" style="--left: 40%;">
    <!-- LEFT: images + model selector -->
    <div>
      <div style="display:flex; gap:10px; align-items:center; margin: 0 0 10px 0;">
        <div style="font-weight:900; font-size:22px;">Model:</div>
        <select id="vlModel" style="font-size:18px; padding:8px 10px; border-radius:10px; border:1px solid #cfcfcf;">
          <option value="qwen3-vl:2b">qwen3-vl:2b</option>
          <option value="qwen3-vl:4b">qwen3-vl:4b</option>
        </select>
      </div>
      <div class="vl-thumbs">
        <button class="vl-thumb selected" data-img="media/ppt/media/image41.jpg" aria-label="Select image 41">
          <img src="media/ppt/media/image41.jpg" alt="Image 41">
          <div class="cap">Click: Describe this image</div>
        </button>
        <button class="vl-thumb" data-img="media/ppt/media/image32.png" aria-label="Select image 32">
          <img src="media/ppt/media/image32.png" alt="Image 32">
          <div class="cap">Click: Describe this image</div>
        </button>
      </div>
    </div>
    <!-- RIGHT: ollama VLM UI -->
    <div class="sa-right">
      <iframe
        id="vlFrame"
        src="./ollama-vl-demo.html?img=media/ppt/media/image41.jpg&model=qwen3-vl:2b"
        style="width:100%; height:620px; border:0; border-radius:12px;">
      </iframe>
    </div>
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">Task – Text → Image (Stable Diffusion)</div>
  <div class="ppt-line"></div>

  <div class="twocol" style="--left: 38%;">
    <div>
      <div style="font-size:26px; font-weight:900; margin-bottom:10px;">Try prompts:</div>
      <ul style="font-size:22px; line-height:1.4;">
        <li>“A Shiba Inu wearing a graduation cap, studio lighting”</li>
        <li>“Fudan University campus at sunset, watercolor style”</li>
        <li>“A robot reading a book in a library, cinematic”</li>
      </ul>
      <div style="font-size:18px; opacity:.75; margin-top:10px;">
        (Right panel generates an image locally.)
      </div>
    </div>
    <div>
      <iframe
        src="./sd-txt2img-demo.html?p=A%20Shiba%20Inu%20wearing%20a%20graduation%20cap%2C%20studio%20lighting"
        style="width:100%; height:640px; border:0; border-radius:12px;"></iframe>
    </div>
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">Task – Text → Video</div>
  <div class="ppt-line"></div>

  <div class="twocol" style="--left: 49%; gap: 22px;">
    <!-- LEFT -->
    <div>
      <div style="font-size:22px; line-height:1.35; margin-top:6px;">
        <b>Creating video from text:</b><br>
        <span class="fudanblue">
          an old man wearing blue jeans and a white T-shirt taking a pleasant stroll in Antarctica during a winter storm
        </span>
      </div>
      <div style="height:40px;"></div>
      <video
        data-src="media/ppt/media/text-to-video.mp4"
        controls autoplay muted loop playsinline
        preload="metadata"
        style="width:100%; max-height:420px; height:auto; border-radius:12px; background:#000;">
      </video>
    </div>
    <!-- RIGHT -->
    <div>
      <div style="font-size:22px; line-height:1.35; margin-top:6px;">
        <b>Creating video from text:</b><br>
        <span class="fudanblue">
          a woman wearing purple overalls and cowboy boots taking a pleasant stroll in Johannesburg South Africa during a beautiful sunset
        </span>
      </div>
      <div style="height:40px;"></div>
      <video
        data-src="media/ppt/media/text-to-video-woman.mp4"
        controls autoplay muted loop playsinline
        preload="metadata"
        style="width:100%; max-height:420px; height:auto; border-radius:12px; background:#000;">
      </video>
    </div>
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">Many Other NLP Tasks & Products</div>
  <div class="ppt-line"></div>

  <!-- Row 1: wide image -->
  <div style="display:flex; justify-content:center; margin-top:10px;">
    <img src="media/ppt/media/image50.png"
         alt="Many NLP tasks and products"
         style="width:100%; max-width:1150px; height:auto; border-radius:12px;">
  </div>

  <div style="height:14px;"></div>

  <!-- Row 2: three images -->
  <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:14px; align-items:center;">
    <img src="media/ppt/media/image52.png"
         alt="Example 1"
         style="width:100%; height:200px; object-fit:contain; border-radius:12px; background:#fff;">
    <img src="media/ppt/media/image53.jpeg"
         alt="Example 2"
         style="width:100%; height:200px; object-fit:contain; border-radius:12px; background:#fff;">
    <img src="media/ppt/media/image54.jpeg"
         alt="Example 3"
         style="width:100%; height:200px; object-fit:contain; border-radius:12px; background:#fff;">
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">Many Other LLMs</div>
  <div class="ppt-line"></div>

  <div class="link-grid">
    <a class="link-card" href="https://chat.openai.com/" target="_blank" rel="noopener noreferrer">
      <div class="link-name">ChatGPT</div>
      <div class="link-url">https://chat.openai.com/</div>
    </a>
    <a class="link-card" href="https://www.deepseek.com/" target="_blank" rel="noopener noreferrer">
      <div class="link-name">DeepSeek</div>
      <div class="link-url">https://www.deepseek.com/</div>
    </a>
    <a class="link-card" href="https://www.kimi.com/" target="_blank" rel="noopener noreferrer">
      <div class="link-name">Kimi</div>
      <div class="link-url">https://www.kimi.com/</div>
    </a>
    <a class="link-card" href="https://chat.qwen.ai/" target="_blank" rel="noopener noreferrer">
      <div class="link-name">Qwen Chat</div>
      <div class="link-url">https://chat.qwen.ai/</div>
    </a>
    <a class="link-card" href="https://gemini.google.com/app" target="_blank" rel="noopener noreferrer">
      <div class="link-name">Gemini</div>
      <div class="link-url">https://gemini.google.com/app</div>
    </a>
    <a class="link-card" href="https://www.together.ai/" target="_blank" rel="noopener noreferrer">
      <div class="link-name">Together.ai</div>
      <div class="link-url">https://www.together.ai/</div>
    </a>
    <a class="link-card" href="https://claude.com/product/claude-code" target="_blank" rel="noopener noreferrer">
      <div class="link-name">Claude Code</div>
      <div class="link-url">https://claude.com/product/claude-code</div>
    </a>
    <a class="link-card" href="https://www.doubao.com/chat/" target="_blank" rel="noopener noreferrer">
      <div class="link-name">Dou Bao</div>
      <div class="link-url">https://www.doubao.com/chat/</div>
    </a>
  </div>
  <div class="link-tip">Click any card to open in a new tab.</div>
</section>

---

<section class="ppt">
  <div class="ppt-title">What We Will Cover (Tentative)</div>
  <div class="ppt-line"></div>

  <div class="twocol" style="--left: 52%;">
    <!-- LEFT -->
    <div style="font-size:40px; line-height:1.5; margin-top:6px;">
      <div style="font-weight:900; color:#1f4e9a;">Basics</div>
      <div style="height:5px;"></div>
      <ul style="margin:0;">
        <li>Text pre-processing & tokenization</li>
        <li>Language models (N-grams)</li>
        <li>Word embeddings (word2vec)</li>
        <li>Neural networks for LMs</li>
        <li>RNNs for sequence labeling</li>
        <li>Self-attention mechanism</li>
        <li>Transformer architecture</li>
      </ul>
    </div>
    <!-- RIGHT -->
    <div style="font-size:40px; line-height:1.5; margin-top:6px;">
      <div style="font-weight:900; color:#1f4e9a;">LLMs</div>
      <div style="height:5px;"></div>
      <ul style="margin:0;">
        <li>Pretraining & fine-tuning</li>
        <li>Evaluation & benchmarking</li>
        <li>In-context learning</li>
        <li>Reasoning & agents</li>
        <li>Diffusion language models</li>
      </ul>
      <div style="height:14px;"></div>
      <div style="font-weight:900; color:#1f4e9a;">Applications</div>
      <div style="height:5px;"></div>
      <ul style="margin:0;">
        <li>Machine translation</li>
        <li>Syntactic analysis</li>
      </ul>
    </div>
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">Course Materials</div>
  <div class="ppt-line"></div>

  <div class="twocol" style="--left: 40%;">
    <!-- LEFT -->
    <div style="font-size:30px; line-height:1.55; margin-top:10px;">
      <div style="font-weight:900; color:#1f4e9a;">Where to find everything</div>
      <div style="height:5px;"></div>
      <ul style="margin:0;">
        <li>All lectures have slides + exercises</li>
        <li>Use GitHub to access source files</li>
        <li>Use the course website for learning</li>
      </ul>
    </div>
    <!-- RIGHT -->
    <div style="font-size:30px; line-height:1.45; margin-top:10px;">
      <div style="font-weight:900; color:#1f4e9a;">Course Materials Hub</div>
      <div style="height:5px;"></div>
      <div style="border:2px solid rgba(0,0,0,0.12); border-radius:14px; padding:14px 16px; background:#f6f7f9;">
        <div style="height:10px;"></div>
        <div style="font-weight:900;">GitHub Repo: <a href="https://github.com/baojian/llm-26" target="_blank" rel="noopener">https://github.com/baojian/llm-26</a>
        </div>
        <div style="height:10px;"></div>
        <div style="font-weight:900;">Course Website / Slides: <a href="https://baojian.github.io/llm-26/" target="_blank" rel="noopener">https://baojian.github.io/llm-26/</a>
        </div>
        <div style="height:10px;"></div>
        <div style="font-weight:900;">Jupyter Notebooks: (each lecture)</div>
      </div>
    </div>
  </div>
  <div style="height:100px;"></div>
  <div style="font-size:22px; line-height:1.45; opacity:0.9; border:2px solid rgba(0,0,0,0.12);
              border-radius:14px; padding:12px 14px; background:#f6f7f9;">
    <div style="font-weight:900; color:#1f4e9a;">Tip: weekly updates</div>
    <div style="height:5px;"></div>
    Each lecture will be updated weekly. You can fetch the latest materials by running:
    <div style="height:5px;"></div>
    <pre style="margin:0; padding:10px 12px; border-radius:12px; background:#fff; border:1px solid #ddd; font-size:18px; line-height:1.35;">
    cd llm-26
    git pull
    </pre>
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">How to Learn This Course Effectively</div>
  <div class="ppt-line"></div>

  <div class="twocol" style="--left: 62%;">
    <!-- LEFT -->
    <div style="font-size:40px; line-height:1.55; margin-top:8px;">
      <div style="font-weight:900; color:#1f4e9a;">Skills needed</div>
      <div style="height:5px;"></div>
      <ul style="margin:0;">
        <li><b>Linear algebra</b> (vectors, matrices)</li>
        <li><b>Basic statistics / ML</b> (probability, optimization)</li>
        <li><b>Python</b> (NumPy, PyTorch, Transformers)</li>
        <li><b>Communication</b> (team project, presentation)</li>
      </ul>
      <div style="height:10px;"></div>
      <div style="font-size:22px; opacity:0.75;">
        Strategy: <b>read → implement → experiment → explain</b>
      </div>
    </div>
    <!-- RIGHT: diagram -->
    <div class="skill-map">
      <div class="skill-center">NLP & LLMs</div>
      <div class="skill-node n1">Linear algebra</div>
      <div class="skill-node n2">Statistics / ML</div>
      <div class="skill-node n3">Python (NumPy / PyTorch)</div>
      <div class="skill-node n4">Communication</div>
    </div>
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">Outline</div>
  <div class="ppt-line"></div>
  
  <ul class="outline-bullets big">
  <li class="muted">Course Overview</li>
  <li class="active">Development of NLP & LLMs</li>
  <li class="muted">Basics for Text Preprocessing</li>
  <li class="muted">Text Tokenization</li>
  </ul>
</section>

---

<section class="ppt">
  <div class="ppt-title">NLP history (1947-1969)</div>
  <div class="ppt-line"></div>

  <div class="twocol" style="--left: 65%;">
    <div class="text">
      <li><b>Warren Weaver wrote to Wiener in 1947</b></li>
        <ul>
            <li><span class="fudanblue"> ... When I look at an article in Russian, I say: "This is really written in English, but it has been coded in some strange symbols. I will now proceed to decode." ...</span></li>
        </ul>
        <li><b>Alan Turing wrote "Computing Machinery and Intelligence" in 1950 (proposed the Turing test)</b>
          <ul>
            <li><span class="fudanblue">... I propose to consider the question, "Can machines think?" This should begin with definitions of the meaning of the terms "machine" and "think." ...</span></li>
          </ul>
        </li>
    </div>
    <div class="fig">
      <img src="media/ppt/media/image6.jpeg" alt="Warren Weaver"  style="display:block; margin:0 auto 24px; width:220px; height:auto;" />
      <div class="cap" style="margin:0 auto 44px">Warren Weaver, 1894-1978</div>
      <img src="media/ppt/media/image7.jpeg" alt="Alan Turing"  style="display:block; margin:0 auto; width:220px; height:auto;" />
      <div class="cap">Alan Turing, 1912-1954</div>
    </div>
  </div>

  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">Outline</div>
  <div class="ppt-line"></div>
  
  <ul class="outline-bullets big">
  <li class="muted">Course Overview</li>
  <li class="muted">Development of NLP & LLMs</li>
  <li class="active">Basics for Text Preprocessing</li>
  <li class="muted">Text Tokenization</li>
  </ul>
</section>

---

<section class="ppt">
  <div class="ppt-title">Install Python & Tools</div>
  <div class="ppt-line"></div>
  <div class="twocol" style="--left: 40%;">
    <!-- LEFT: same content -->
    <div style="font-size:24px; line-height:1.5; margin-top:10px;">
      <div style="margin-bottom:4px;">
        <span style="font-weight:900; color:#1f4e9a;">Python & Jupyter Notebook</span>
        <div style="height:2px;"></div>
        <ul style="margin:8px 0 0 0;">
          <li><b>Python-3.12</b> —
            <a href="https://www.python.org/downloads/" target="_blank" rel="noopener">python.org/downloads</a> / <b>Jupyter Notebook</b> (Assignments submission) —
            <a href="https://jupyter.org/" target="_blank" rel="noopener">jupyter.org</a>
          </li>
        </ul>
      </div>
      <div style="margin-bottom:4px;">
        <span style="font-weight:900; color:#1f4e9a;">Python IDE / Notebook</span>
        <div style="height:2px;"></div>
        <ul style="margin:8px 0 0 0;">
          <li>PyCharm —
            <a href="https://www.jetbrains.com/pycharm/" target="_blank" rel="noopener">jetbrains.com/pycharm</a>
            / VS Code —
            <a href="https://code.visualstudio.com/" target="_blank" rel="noopener">code.visualstudio.com</a> / <b>Cursor (Claude Code)</b> —
            <a href="https://www.cursor.com/" target="_blank" rel="noopener">cursor.com</a>
          </li>
        </ul>
      </div>
      <div style="margin-bottom:4px;">
        <span style="font-weight:900; color:#1f4e9a;">Environment Manager</span>
        <div style="height:2px;"></div>
        <ul style="margin:8px 0 0 0;">
          <li><b>Anaconda</b> (recommended) —
            <a href="https://www.anaconda.com/download" target="_blank" rel="noopener">anaconda.com/download</a>
          </li>
        </ul>
        <div style="height:2px;"></div>
        <ul style="margin:8px 0 0 0;">
          <li><b>uv</b> (super fast) —
            <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank" rel="noopener">docs.astral.sh/uv</a>
          </li>
        </ul>
      </div>
      <div style="margin-bottom:4px;">
        <span style="font-weight:900; color:#1f4e9a;">Version Control</span>
        <div style="height:2px;"></div>
        <ul style="margin:8px 0 0 0;">
          <li>Git + GitHub (manage your code) —
            <a href="https://github.com/" target="_blank" rel="noopener">github.com</a>
          </li>
        </ul>
      </div>
      <div style="margin-top:10px; font-size:22px; opacity:0.75;">
        Tip: Install Python + Anaconda + Git + Notebook, then choose IDE (VS Code / PyCharm / Cursor with Claude Code).
      </div>
    </div>
    <!-- RIGHT: notebook link / embed -->
    <div style="margin-top:10px;">
      <div style="font-size:28px; font-weight:900; color:#1f4e9a; margin-bottom:8px;">
      <a href="https://baojian.github.io/llm-26/lecture-01/lecture-01-exercise-NLP-LLMs-introduction.html#section-0" target="_blank" rel="noopener" style="color:#1f4e9a; text-decoration:none;">Exercise Notebook (Section 0)</a>
      </div>
      <div style="height:2px;"></div>
      <iframe
        src="https://baojian.github.io/llm-26/lecture-01/lecture-01-exercise-NLP-LLMs-introduction.html"
        style="width:100%; height:520px; border:1px solid #d9d9d9; border-radius:12px;">
      </iframe>
      <div style="height:5px;"></div>
      <div style="font-size:18px; opacity:0.75;">
        If the embed is blocked, open in a new tab:
        <a href="https://baojian.github.io/llm-26/lecture-01/lecture-01-exercise-NLP-LLMs-introduction.html"
           target="_blank" rel="noopener">link</a>
      </div>
    </div>
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">RE: disjunctions</div>
  <div class="ppt-line"></div>
  <div class="re-bullet">• Letters inside square brackets <span class="dim">[ ]</span></div>
  <div class="re-row">
    <!-- LEFT: small table -->
    <div>
      <table class="re-table">
        <thead>
          <tr>
            <th>Pattern</th>
            <th>Matches</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="pattern">[wW]oodchuck</td>
            <td>Woodchuck, woodchuck</td>
          </tr>
          <tr>
            <td class="pattern">[1234567890]</td>
            <td>Any digit</td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- RIGHT: code -->
    <div class="re-code">
      <pre><code class="language-python">import re
str1 = "This string contains Woodchuck and woodchuck."
result = re.search(pattern=r"[wW]oodchuck", string=str1)
print(result)
result = re.search(pattern=r"[wW]ooodchuck", string=str1)
print(result)</code></pre>
    </div>
  </div>
  <div style="height:18px;"></div>
  <div class="re-bullet">• Ranges <span class="dim">[A-Z]</span></div>
  <table class="re-table" style="font-size:26px;">
    <thead>
      <tr>
        <th style="width:18%;">Pattern</th>
        <th style="width:32%;">Matches</th>
        <th>Example String</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="pattern">[A-Z]</td>
        <td>An upper case letter</td>
        <td><span class="hl">D</span>renched Blossoms</td>
      </tr>
      <tr>
        <td class="pattern">[a-z]</td>
        <td>A lower case letter</td>
        <td><span class="hl">m</span>y beans were impatient</td>
      </tr>
      <tr>
        <td class="pattern">[0-9]</td>
        <td>A single digit</td>
        <td>Chapter <span class="hl">1</span>: Down the Rabbit Hole</td>
      </tr>
    </tbody>
  </table>
  <div style="height:20px;"></div>
    <div style="font-size:20px; line-height:1.35; opacity:0.9;
            border:2px solid rgba(0,0,0,0.12);
            border-radius:14px; padding:10px 12px; background:#f6f7f9;">
            <span style="font-weight:900; color:#1f4e9a;">Tip:</span>Try the code in <b>Section 2</b> of the exercise notebook:
            <a href="https://baojian.github.io/llm-26/lecture-01/lecture-01-exercise-NLP-LLMs-introduction.html#20" target="_blank" rel="noopener">lecture-01-exercise-NLP-LLMs-introduction.html</a>
    </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">RE: negation in disjunction</div>
  <div class="ppt-line"></div>

  <div class="re-bullet">• Negations: e.g., <span class="dim">[^Ss]</span></div>
  <div class="re-bullet">• <b>Caret (脱字符)</b>: negation only when first in <span class="dim">[ ]</span></div>

  <div style="height:10px;"></div>

  <table class="re-table" style="font-size:26px;">
    <thead>
      <tr>
        <th style="width:20%;">Pattern</th>
        <th style="width:35%;">Matches</th>
        <th>Example String</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="pattern">[^A-Z]</td>
        <td>Not an upper case letter</td>
        <td>O<span class="hl">y</span>fn pripetchik</td>
      </tr>
      <tr>
        <td class="pattern">[^Ss]</td>
        <td>Neither ‘S’ nor ‘s’</td>
        <td><span class="hl">I</span> have no exquisite reason</td>
      </tr>
      <tr>
        <td class="pattern">[^e^]</td>
        <td>Neither e nor ^</td>
        <td><span class="hl">L</span>ook here</td>
      </tr>
      <tr>
        <td class="pattern">a\^b</td>
        <td>The pattern <span class="dim">a^b</span></td>
        <td>Look up <span class="hl">a^b</span> now</td>
      </tr>
    </tbody>
  </table>

  <div style="height:14px;"></div>

  <div class="re-row" style="grid-template-columns: 1.15fr 0.85fr;">
    <!-- LEFT: code -->
    <div class="re-code">
      <pre><code class="language-python">import re
str1 = "Look up a^b now"
result = re.search(pattern=r"a\^b", string=str1)
print(result)</code></pre>
    </div>
    <!-- RIGHT: output -->
    <div class="re-out">
    Output:
      <pre><code>&lt;re.Match object; span=(8, 11), match='a^b'&gt;
Process finished with exit code 0</code></pre>
    </div>
  </div>

  <div style="height:5px;"></div>

  <div style="font-size:20px; line-height:1.35; opacity:0.9;
              border:2px solid rgba(0,0,0,0.12);
              border-radius:14px; padding:10px 12px; background:#f6f7f9;">
    <span style="font-weight:900; color:#1f4e9a;">Tip:</span>
    Try the code in <b>Section 2</b> of the exercise notebook:
    <a href="https://baojian.github.io/llm-26/lecture-01/lecture-01-exercise-NLP-LLMs-introduction.html#section-1"
       target="_blank" rel="noopener">
      lecture-01-exercise-NLP-LLMs-introduction.html
    </a>
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">RE: more disjunction</div>
  <div class="ppt-line"></div>

  <div class="re-bullet">• <b>Woodchucks</b> is another name for <b>groundhog</b>!</div>
  <div class="re-bullet">• The pipe <b>|</b> for disjunction</div>

  <div style="height:18px;"></div>

  <div style="display:flex; justify-content:center;">
    <table class="re-table" style="width:78%; font-size:28px;">
      <thead>
        <tr>
          <th style="width:55%;">Pattern</th>
          <th>Matches</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="pattern">groundhog|woodchuck</td>
          <td>groundhog and woodchuck</td>
        </tr>
        <tr>
          <td class="pattern">yours|mine</td>
          <td>yours mine</td>
        </tr>
        <tr>
          <td class="pattern">a|b|c</td>
          <td>= [abc]</td>
        </tr>
        <tr>
          <td class="pattern">[gG]roundhog | [wW]oodchuck</td>
          <td><b>???</b></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div style="height:40px;"></div>

  <div style="font-size:20px; line-height:1.35; opacity:0.9;
              border:2px solid rgba(0,0,0,0.12);
              border-radius:14px; padding:10px 12px; background:#f6f7f9;">
    <span style="font-weight:900; color:#1f4e9a;">Question:</span>
    What does <b>[gG]roundhog | [wW]oodchuck</b> match?
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">RE: ? * + .</div>
  <div class="ppt-line"></div>

  <div style="height:6px;"></div>

  <div style="display:flex; justify-content:center;">
    <table class="re-table" style="width:92%; font-size:26px;">
      <thead>
        <tr>
          <th style="width:20%;">Pattern</th>
          <th style="width:35%;">Matches</th>
          <th>Matched examples</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="pattern">colou?r</td>
          <td>Optional previous char</td>
          <td><span class="hl">color</span> &nbsp;&nbsp; <span class="hl">colour</span></td>
        </tr>
        <tr>
          <td class="pattern">oo*h!</td>
          <td>0 or more of previous char</td>
          <td>
            <span class="hl">oh!</span> &nbsp; <span class="hl">ooh!</span> &nbsp;
            <span class="hl">oooh!</span> &nbsp; <span class="hl">ooooh!</span>
          </td>
        </tr>
        <tr>
          <td class="pattern">o+h!</td>
          <td>1 or more of previous char</td>
          <td>
            <span class="hl">oh!</span> &nbsp; <span class="hl">ooh!</span> &nbsp;
            <span class="hl">oooh!</span> &nbsp; <span class="hl">ooooh!</span>
          </td>
        </tr>
        <tr>
          <td class="pattern">baa+</td>
          <td>1 or more of previous char</td>
          <td>
            <span class="hl">baa</span> &nbsp; <span class="hl">baaa</span> &nbsp;
            <span class="hl">baaaa</span> &nbsp; <span class="hl">baaaaa</span>
          </td>
        </tr>
        <tr>
          <td class="pattern">beg.n</td>
          <td>any char</td>
          <td>
            <span class="hl">begin</span> &nbsp; <span class="hl">begun</span> &nbsp;
            <span class="hl">beg0n</span> &nbsp; <span class="hl">beg3n</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <div style="height:14px;"></div>

  <div class="re-row" style="grid-template-columns: 1.1fr 0.9fr;">
    <!-- code -->
    <div class="re-code">
      <pre><code class="language-python">import re
str1 = "oh! ooh! oooh! ooooh!"
result = re.search(pattern=r"oo+h!", string=str1)
print(result)</code></pre>
    </div>
    <!-- output -->
    <div class="re-out">
      <pre><code>&lt;re.Match object; span=(4, 8), match='ooh!'&gt;</code></pre>
    </div>
  </div>
  <div style="height:50px;"></div>
  <div style="font-size:20px; line-height:1.35; opacity:0.9;
              border:2px solid rgba(0,0,0,0.12);
              border-radius:14px; padding:10px 12px; background:#f6f7f9;">
    <span style="font-weight:900; color:#1f4e9a;">Tip:</span>
    Try the code in <b>Section 2</b> of the exercise notebook:
    <a href="https://baojian.github.io/llm-26/lecture-01/lecture-01-exercise-NLP-LLMs-introduction.html#section-1"
       target="_blank" rel="noopener">
      lecture-01-exercise-NLP-LLMs-introduction.html
    </a>
  </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">Task – Tokenization with Regular Expression</div>
  <div class="ppt-line"></div>

  <!-- TOP: task description -->
  <div style="font-size:30px; line-height:1.45; margin-top:10px;">
    Use the regex <span class="pattern">[A-Za-z]+(?:'[A-Za-z]+)?</span> to tokenize the following sentence. Observe what is kept, what is dropped, and why.
  </div>
  <div style="height:14px;"></div>
  <!-- BOTTOM: code (left) + output (right) -->
  <div class="re-row" style="grid-template-columns: 1fr 1fr;">
    <!-- LEFT: code -->
    <div class="re-code">
      <pre><code class="language-python">import re
word_re = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
text = """Senjō no Valkyria 3 : Unrecorded \
Chronicles ( Japanese : 戦場のヴァルキュリア3 ,\
lit . Valkyria of the Battlefield 3 ) , commonly\
 referred to as Valkyria Chronicles III outside \
 Japan , is a tactical role @-@ playing video \
 game developed by Sega and Media.Vision\
  for the PlayStation Portable . \
Released in January 2011 in Japan , \
it is the third game in the Valkyria series .\
 Employing the same fusion of tactical \
and real @-@ time gameplay as its predecessors"""
tokens = word_re.findall(text)
print(len(tokens))
print(tokens)</code></pre>
    </div>
    <!-- RIGHT: output -->
    <div class="re-out">
      <pre><code>Output tokens:
['Senj', 'no', 'Valkyria', 'Unrecorded', 
'Chronicles', 'Japanese', 'lit', 'Valkyria', 
'of', 'the', 'Battlefield', 'commonly', 'referred',
 'to', 'as', 'Valkyria', 'Chronicles', 'III', 
 'outside', 'Japan', 'is', 'a', 'tactical', 'role',
  'playing', 'video', 'game', 'developed', 'by', 
  'Sega', 'and', 'Media', 'Vision', 'for', 'the',
   'PlayStation', 'Portable', 'Released',  'in', 
   'January', 'in', 'Japan', 'it', 'is', 'the', 
  'third', 'game', 'in', 'the', 'Valkyria', 'series',
   'Employing', 'the', 'same', 'fusion', 'of', 
   'tactical', 'and', 'real', 'time', 'gameplay', 
   'as', 'its', 'predecessors']</code></pre>
    </div>
  </div>
  <div style="height:40px;"></div>
  <div style="font-size:20px; opacity:0.85;">
    Discussion: Why do we get <b>Senj</b> (not Senjō), <b>firstgame</b>, and <b>senseof</b>?
  </div>
</section>

---

<section class="ppt med-slide"
         data-src="intention"
         data-tgt="execution"
         data-ins="1"
         data-del="1"
         data-sub="2">

  <div class="ppt-title">Minimum Edit Distance (MED): fill the DP table</div>
  <div class="ppt-line"></div>

  <div class="med-meta">
    <span><b>Source:</b> <span class="mono" id="medSrcLabel"></span></span>
    <span style="margin-left:18px;"><b>Target:</b> <span class="mono" id="medTgtLabel"></span></span>
    <span class="med-hint">Press <b>→</b> to fill the next cell</span>
  </div>

  <div style="height:5px;"></div>

  <div class="med-wrap">
    <div class="med-table" id="medTable"></div>
    <div class="med-legend">
      <div class="leg"><span class="dot keep"></span> match (0)</div>
      <div class="leg"><span class="dot sub"></span> substitute (sub)</div>
      <div class="leg"><span class="dot ins"></span> insert (ins)</div>
      <div class="leg"><span class="dot del"></span> delete (del)</div>
      <div style="height:5px;"></div>
      <div style="opacity:.75; font-size:18px; line-height:1.3;">
        Default costs: ins=1, del=1, sub=2 (edit if needed).
      </div>
    </div>
  </div>

  <!-- Invisible fragments to “trap” → and reveal steps on the same slide -->
  <div class="med-frags" aria-hidden="true"></div>
  <div class="med-eq">
  $$
D[i,j] = \min \left\{
\begin{aligned}
& D[i-1,j]   + \mathrm{Del}(x_i)  \\
& D[i,\,j-1] + \mathrm{Ins}(y_j) \\
& D[i-1,j-1] + \mathrm{Sub}(x_i,y_j)
\end{aligned}
\right.
$$
  </div>
</section>

---

<section class="ppt med-bt-slide" data-s="intention" data-t="execution">
  <div class="ppt-title">MED – Backtracking (Alignment)</div>
  <div class="ppt-line"></div>

  <div class="med-wrap">
    <!-- LEFT: (optional) show the DP table again, and we highlight the path while backtracking -->
    <div class="med-table">
      <div class="med-table-inner" id="btTable"></div>
    </div>
    <!-- RIGHT: alignment being built -->
    <div class="med-legend">
      <div style="font-weight:900; margin-bottom:10px;">Alignment (press →)</div>
      <div class="align-box">
        <div class="align-row" id="alTop"></div>
        <div class="align-row mid" id="alMid"></div>
        <div class="align-row" id="alBot"></div>
      </div>
      <div style="margin-top:10px; font-size:18px; opacity:.75;">
        Gap symbol: <b>*</b> &nbsp;|&nbsp; Match: <span class="legend-chip keep">green</span>
        Sub: <span class="legend-chip sub">red</span>
        Ins: <span class="legend-chip ins">blue</span>
        Del: <span class="legend-chip del">orange</span>
      </div>
    </div>
  </div>

  <!-- fragments auto-created by JS into this container -->
  <div class="bt-frags" style="display:none;"></div>
</section>

---

<section class="ppt">
  <div class="ppt-title">Outline</div>
  <div class="ppt-line"></div>
  
  <ul class="outline-bullets big">
  <li class="muted">Course Overview</li>
  <li class="muted">Development of NLP & LLMs</li>
  <li class="muted">Basics for Text Preprocessing</li>
  <li class="active">Text Tokenization</li>
  </ul>
</section>

---

<section class="ppt bpe-slide">
  <div class="ppt-title">Subword Tokenization – BPE</div>
  <div class="ppt-line"></div>

  <div class="bpe-wrap">
    <div class="bpe-left">
      <ul class="bpe-bullets">
        <li><b>Step 0 (word boundary):</b> append an end-of-word symbol <code>_</code> to each word.</li>
        <li><b>Step 1 (init vocab):</b> vocabulary = all characters appearing in the corpus (including <code>_</code>).</li>
        <li><b>Step 2 (repeat K times):</b>
          <ol>
            <li>count adjacent symbol pairs in the corpus</li>
            <li>merge the <b>most frequent</b> pair into a new symbol</li>
            <li>update the corpus representation + vocabulary</li>
          </ol>
        </li>
      </ul>
      <div class="bpe-note">
        Intuition: BPE learns frequent character patterns (subwords) like <code>er</code>, <code>new</code>, <code>low</code>, ...
      </div>
    </div>
    <div class="bpe-right">
      <div class="bpe-card">
        <div class="bpe-card-title">Why “subwords”?</div>
        <div class="bpe-card-body">
          <ul>
            <li>handles <b>rare / new words</b> by composing from pieces</li>
            <li>keeps a <b>compact vocabulary</b></li>
            <li>works well for <b>morphology</b> (prefix/suffix patterns)</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

---

<section class="ppt bpe-slide">
  <div class="ppt-title">BPE Toy Example</div>
  <div class="ppt-line"></div>

  <div class="bpe-wrap">
    <div class="bpe-left">
      <div class="bpe-block">
        <div class="bpe-block-title">Training corpus</div>
        <div class="bpe-mono">
          low low low low low
          lowest lowest
          newer newer newer newer newer newer
          wider wider wider
          new new
        </div>
      </div>
      <div class="bpe-block">
        <div class="bpe-block-title">After adding end-of-word <code>_</code> and splitting into letters</div>
        <div class="bpe-mono">
          Vocab: { _, d, e, i, l, n, o, r, s, t, w }<br/>
          Corpus (counts × symbols):<br/>
          5  l o w _<br/>
          2  l o w e s t _<br/>
          6  n e w e r _<br/>
          3  w i d e r _<br/>
          2  n e w _
        </div>
      </div>
    </div>
    <div class="bpe-right">
      <div class="bpe-block">
        <div class="bpe-block-title">First few merges</div>
        <div class="bpe-mono">
          Merge <b>e r</b> → <b>er</b><br/>
          Merge <b>er _</b> → <b>er_</b><br/>
          Merge <b>n e</b> → <b>ne</b><br/>
          Next merges (summary):<br/>
          (ne, w)→new,</b><br/> 
          (l, o)→lo, </b><br/> 
          (lo, w)→low, </b><br/> 
          (new, er_)→newer_, </b><br/> 
          (low, er_)→low_
        </div>
      </div>
    </div>
  </div>
</section>

---

<section class="ppt bpe-dyn-slide" data-bpe-demo="1">
  <div class="ppt-title">BPE in Action (press →)</div>
  <div class="ppt-line"></div>

  <div class="bpe-wrap"  style="--left:80%;">
    <!-- LEFT: corpus + vocab -->
    <div class="bpe-left">
      <div class="bpe-block">
        <div class="bpe-block-title">Vocabulary</div>
        <div id="bpeVocab" class="bpe-mono"></div>
      </div>
      <div class="bpe-block">
        <div class="bpe-block-title">Corpus representation</div>
        <div id="bpeCorpus" class="bpe-mono"></div>
      </div>
    </div>
    <!-- RIGHT: merge controller -->
    <div class="bpe-right">
      <div class="bpe-card">
        <div class="bpe-card-title">Next merge</div>
        <div class="bpe-card-body">
          <div id="bpeStep" class="bpe-step"></div>
          <div class="bpe-small">Press <b>→</b> to merge the next most frequent pair.</div>
          <div class="bpe-small">After the last merge, <b>→</b> will go to the next slide normally.</div>
        </div>
      </div>
    </div>
  </div>

  <div class="bpe-final fragment">
  <div class="bpe-final-title">Final state (after all merges)</div>

  <div class="bpe-final-row">
    <!-- LEFT -->
    <div class="bpe-final-col">
      <div class="bpe-final-sub">Original text</div>
      <div class="bpe-mono">
        low low low low low lowest lowest
        newer newer newer newer newer newer
        wider wider wider
        new new
              </div>
              <div style="height:2px;"></div>
              <div class="bpe-final-sub">Vocabulary V</div>
              <div class="bpe-mono">
        { _, d, e, i, l, n, o, r, s, t, w,
          er, er_, ne, new, lo, low, newer_, low_ }
              </div>
            </div>
            <!-- RIGHT -->
            <div class="bpe-final-col">
              <div class="bpe-final-sub">Final Tokenization</div>
              <div class="bpe-mono"><pre><code class="language-python">['low', '_', 'low', '_', 'low', '_', 'low', '_', 
'low', '_', 'low', 'e', 's', 't', '_', 'low', 
'e', 's', 't', '_', 'newer_', 'newer_', 'newer_', 
'newer_', 'newer_', 'newer_', 'w', 'i', 'd', 
'er_', 'w', 'i', 'd', 'er_', 'w', 'i', 'd',
 'er_', 'new', '_', 'new', '_']</code></pre></div>
            </div>
          </div>
        </div>
</section>

---

<section class="ppt">
  <div class="ppt-title">Exercises & Readings</div>
  <div class="ppt-line"></div>

  <div class="twocol" style="--left: 52%;">
    <!-- LEFT -->
    <div class="text">
      <ul class="outline-bullets big" style="font-size:28px; line-height:1.45; margin-top:8px;">
        <li><b>TODO 1: Setup your course environmnet (github)</b>
        <div style="height:6px;"></div>
        <a href="https://github.com/baojian/llm-26" target="_blank" rel="noopener">
              https://github.com/baojian/llm-26
            </a>
      </ul>
      <ul class="outline-bullets big" style="font-size:28px; line-height:1.45; margin-top:8px;">
        <li><b>TODO 2: Install anaconda and ollama</b>
        <div style="height:6px;"></div>
        <a href="https://www.anaconda.com/download" target="_blank" rel="noopener">
              https://www.anaconda.com/download
            </a>
        <a href="https://ollama.com/download" target="_blank" rel="noopener">
              https://ollama.com/download
            </a>
      </ul>
      <ul class="outline-bullets big" style="font-size:28px; line-height:1.45; margin-top:8px;">
        <li style="color:#d00;"><b>Exercise: do our first exercise</b></li>
        <div style="height:6px;"></div>
        <a href="https://baojian.github.io/llm-26/lecture-01/lecture-01-exercise-NLP-LLMs-introduction.html" target="_blank" rel="noopener">
              https://baojian.github.io/llm-26/lecture-01/lecture-01-exercise-NLP-LLMs-introduction.html
            </a>
      </ul>
    </div>
    <!-- RIGHT -->
    <div class="fig">
      <div style="font-size:28px; line-height:1.5; margin-top:6px;">
        <div style="font-weight:900; color:#1f4e9a;">Studying and Reading Links</div>
        <div style="height:8px;"></div>
        <ul style="margin:0; padding-left:1.1em;">
          <div style="height:8px;"></div>
          <li>
            For NLP/Python beginners (video):<div style="height:2px;"></div>
            <a href="https://www.youtube.com/watch?v=xvqsFTUsOmc&t=1607s" target="_blank" rel="noopener">
              Alice Zhao — NLP in Python
            </a>
          </li>
          <div style="height:8px;"></div>
          <li>
            Histroy of LLMs (by Gregory Gundersen):<div style="height:2px;"></div>
            <a href="https://gregorygundersen.com/blog/2025/10/01/large-language-models/" target="_blank" rel="noopener">
            blog: large-language-models</a>
          </li>
          <li>
            Our reading materials:<div style="height:2px;"></div>
            <a href="https://www.nltk.org/book/ch02.html" target="_blank" rel="noopener">
              nltk.org/book/ch02.html
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <div style="height:40px;"></div>
      <div style="font-size:40px; opacity:0.85;">
        <b>Next lecture:</b> Simple Language Models (N-grams)
      </div>
</section>