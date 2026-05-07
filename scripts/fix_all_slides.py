
import os
import re

base_path = "/Users/halmayyof/Test3/test3/ذد/cv-for-developers-ultralytics/"
docs_slides_dir = os.path.join(base_path, "docs/slides")

html_files = [f for f in os.listdir(docs_slides_dir) if f.endswith(".html") and not f.endswith("speaker-view.html")]

def fix_matching_game(content):
    # Remove <pre><code> surrounding the matching game
    pattern = r'<div class="matching-game">\s*<div class="matching-columns">\s*<pre><code>(.*?)\s*</code></pre>\s*</div>'
    
    def unescape(match):
        inner = match.group(1)
        inner = inner.replace('&lt;', '<').replace('&gt;', '>')
        return f'<div class="matching-game"><div class="matching-columns">{inner}</div>'
        
    return re.sub(pattern, unescape, content, flags=re.DOTALL)

def fix_qa_slide_generic(content):
    # Find any section containing "شكراً لاهتمامكم ووقتكم"
    # We want to catch the whole <section ...> ... </section>
    pattern = r'<section\s+[^>]*>.*?(?:شكراً لاهتمامكم ووقتكم|شكراً جزيلاً لاهتمامكم).*?</section>'
    
    replacement = """<section id="شكرا" class="title-slide slide level1 sdaia-dark center" data-background-gradient="linear-gradient(135deg, #1C355E, #00C9A7)" data-state="sdaia-bg">
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 80vh; text-align: center; margin: 0 auto;">
<h1 style="font-size: 3.5rem; font-weight: 800; color: white; margin-bottom: 1rem;">شكراً لاهتمامكم ووقتكم</h1>
<p style="font-size: 1.8rem; color: #00C9A7; font-weight: 600; opacity: 0.9;">يُسعدني الإجابة على استفساراتكم ومناقشاتكم</p>
</div>
</section>"""
    
    # We use re.DOTALL to match across newlines
    # But be careful: the .*? might match too much if not restricted.
    # A safer way is to find the indices of the text and then find the nearest <section and </section>
    
    new_content = content
    matches = list(re.finditer(r'(?:شكراً لاهتمامكم ووقتكم|شكراً جزيلاً لاهتمامكم)', content))
    
    # Process in reverse to avoid index issues
    for match in reversed(matches):
        start_idx = match.start()
        # Find the start of the section containing this match
        section_start = content.rfind('<section', 0, start_idx)
        # Find the end of the section containing this match
        section_end = content.find('</section>', start_idx)
        
        if section_start != -1 and section_end != -1:
            section_end += len('</section>')
            new_content = new_content[:section_start] + replacement + new_content[section_end:]
            
    return new_content

for filename in html_files:
    full_path = os.path.join(docs_slides_dir, filename)
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = fix_matching_game(content)
    new_content = fix_qa_slide_generic(new_content)
    
    if new_content != content:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filename}")
    else:
        print(f"No changes for {filename}")
