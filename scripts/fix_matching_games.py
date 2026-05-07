
import os
import re

html_files = [
    "docs/slides/Ultralytics_Foundations_2_Real_World_Use_Cases.html",
    "docs/slides/Ultralytics_Foundations_3_Custom_Data_Training.html"
]

css = """
<style>
.matching-game {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
  padding: 15px;
  background: rgba(255,255,255,0.05);
  border-radius: 15px;
  margin-top: 20px;
}
.matching-columns {
  display: flex;
  justify-content: space-between;
  width: 100%;
  gap: 30px;
}
.scenarios-col, .solutions-col {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.match-item {
  padding: 12px;
  background: white;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s;
  text-align: center;
  font-weight: bold;
  color: #1e293b;
  font-size: 0.9rem;
}
.match-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
  border-color: #00C9A7;
}
.match-item.selected {
  border-color: #00C9A7;
  background: #f0fdfa;
  transform: scale(1.02);
}
.match-item.matched {
  background: #dcfce7;
  border-color: #22c55e;
  color: #166534;
  cursor: default;
  opacity: 0.8;
}
.match-item.wrong {
  background: #fee2e2;
  border-color: #ef4444;
  animation: shake 0.5s;
}
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-5px); }
  75% { transform: translateX(5px); }
}
</style>
"""

js = """
<script>
(function() {
  let currentScenario = null;
  let currentSolution = null;
  let totalMatches = 0;

  window.selectScenario = function(el, matchId) {
    if (el.classList.contains('matched')) return;
    el.closest('.matching-game').querySelectorAll('.scenarios-col .match-item').forEach(i => i.classList.remove('selected'));
    el.classList.add('selected');
    currentScenario = { el, matchId };
    if (currentSolution) checkMatch(el.closest('.matching-game'));
  };

  window.selectSolution = function(el, matchId) {
    if (el.classList.contains('matched')) return;
    el.closest('.matching-game').querySelectorAll('.solutions-col .match-item').forEach(i => i.classList.remove('selected'));
    el.classList.add('selected');
    currentSolution = { el, matchId };
    if (currentScenario) checkMatch(el.closest('.matching-game'));
  };

  function checkMatch(gameEl) {
    const feedback = gameEl.querySelector('#game-feedback');
    if (currentScenario.matchId === currentSolution.matchId) {
      currentScenario.el.classList.add('matched');
      currentSolution.el.classList.add('matched');
      feedback.innerHTML = '<span style="color: #22c55e;">أحسنت! إجابة صحيحة ✅</span>';
      totalMatches++;
      if (totalMatches % 4 === 0) {
        feedback.innerHTML = '<span style="color: #00C9A7; font-size: 1.4em;">🎉 مذهل! لقد أتممت التحدي بنجاح! 🎉</span>';
      }
    } else {
      currentScenario.el.classList.add('wrong');
      currentSolution.el.classList.add('wrong');
      feedback.innerHTML = '<span style="color: #ef4444;">حاول مرة أخرى ❌</span>';
      const s = currentScenario.el;
      const sol = currentSolution.el;
      setTimeout(() => {
        s.classList.remove('wrong', 'selected');
        sol.classList.remove('wrong', 'selected');
      }, 800);
    }
    currentScenario = null;
    currentSolution = null;
  }
})();
</script>
"""

base_path = "/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/"

for file in html_files:
    full_path = os.path.join(base_path, file)
    if not os.path.exists(full_path):
        print(f"File not found: {file}")
        continue
        
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Remove <pre><code> surrounding the matching game
    # We look for <div class="matching-game"> followed by <div class="matching-columns"> and then <pre><code>
    pattern = r'<div class="matching-game">\s*<div class="matching-columns">\s*<pre><code>(.*?)\s*</code></pre>\s*</div>'
    
    def unescape(match):
        inner = match.group(1)
        # Pandoc escapes < and > inside code blocks
        inner = inner.replace('&lt;', '<').replace('&gt;', '>')
        return f'<div class="matching-game"><div class="matching-columns">{inner}</div>'
        
    new_content = re.sub(pattern, unescape, content, flags=re.DOTALL)
    
    # 2. Inject CSS and JS before </body>
    if "</body>" in new_content:
        new_content = new_content.replace("</body>", f"{css}{js}</body>")
    
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Patched {file}")
