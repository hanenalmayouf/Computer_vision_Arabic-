import os
import json
import re

# Mapping of filenames to their current repository locations
# This can be dynamically populated by searching, but for the common ones I'll prefill
path_map = {
    "horse.png": "slides/assets/horse.png",
    "parking_slots.mp4": "slides/assets/parking_slots.mp4",
    "Cars.mp4": "slides/assets/Cars.mp4",
    "Pull_ups.mp4": "docs/slides/assets/Pull_ups.mp4"
}

def find_file_in_repo(filename):
    if filename in path_map:
        return path_map[filename]
    
    # Generic search if not in map (excluding weights .pt)
    if filename.endswith(".pt"):
        return None
        
    for root, dirs, files in os.walk("."):
        if filename in files:
            path = os.path.relpath(os.path.join(root, filename), ".").replace("\\", "/")
            path_map[filename] = path
            return path
    return None

def migrate_notebook(file_path):
    print(f"Checking {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            nb = json.load(f)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return
            
    base_url = "https://raw.githubusercontent.com/NaifMersal/cv-for-developers-ultralytics/main/"
    legacy_patterns = [
        r"https://raw\.githubusercontent\.com/NaifMersal/cv-for-developers-ultralytics/main/labs/",
        r"https://github\.com/NaifMersal/cv-for-developers-ultralytics/raw/main/labs/"
    ]
    
    changed = False
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            source_lines = cell.get("source", [])
            new_source = []
            for line in source_lines:
                new_line = line
                for pattern in legacy_patterns:
                    if re.search(pattern, line):
                        # 1. Handle variable-based f-strings: url = f".../labs/{variable}"
                        var_match = re.search(r'\{(video_path|video_file|image_file_path|filename)\}', line)
                        if var_match:
                            # We can't easily resolve the variable here without more logic, 
                            # but we know most of these belong in slides/assets/ or docs/slides/assets/
                            # The user's pattern was specific. Let's assume we map the variable to a search.
                            # However, for simplicity and safety, let's see if we can just update the segment
                            # or if we need to replace the f-string with a more explicit search.
                            
                            # Actually, most of these moved to slides/assets/
                            # Let's try to find if the variable was assigned in the same cell
                            source_text = "".join(source_lines)
                            assignment_match = re.search(rf'{var_match.group(1)}\s*=\s*(?:f?["\'])([^"\']+)(?:["\'])', source_text)
                            if assignment_match:
                                filename = assignment_match.group(1)
                                if filename.endswith(".pt"):
                                    print(f"  Skipping weights: {filename}")
                                    continue
                                repo_path = find_file_in_repo(filename)
                                if repo_path:
                                    new_line = re.sub(pattern, f"{base_url}{os.path.dirname(repo_path)}/", line)
                                    print(f"  Fixed {var_match.group(0)} -> {repo_path}")
                                else:
                                    print(f"  Could not find location for {filename}")
                            else:
                                # Fallback if assignment not found: use slides/assets/ as a likely candidate
                                new_line = re.sub(pattern, f"{base_url}slides/assets/", line)
                                print(f"  Fallback fix for variable: {line.strip()}")
                                
                        # 2. Handle hardcoded filenames
                        else:
                            hardcoded_match = re.search(rf"{pattern}([A-Za-z0-9_\-\.]+)", line)
                            if hardcoded_match:
                                filename = hardcoded_match.group(1)
                                if filename.endswith(".pt"):
                                    print(f"  Skipping weights: {filename}")
                                    continue
                                repo_path = find_file_in_repo(filename)
                                if repo_path:
                                    new_line = re.sub(pattern + filename, f"{base_url}{repo_path}", line)
                                    print(f"  Fixed hardcoded: {filename} -> {repo_path}")
                                else:
                                    print(f"  Could not find location for {filename}")
                        
                if new_line != line:
                    changed = True
                new_source.append(new_line)
            cell["source"] = new_source

    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1)
        print(f"  Saved {file_path}")

def run_migration():
    labs_dir = "labs"
    for root, dirs, files in os.walk(labs_dir):
        for file in files:
            if file.endswith(".ipynb"):
                migrate_notebook(os.path.join(root, file))

if __name__ == "__main__":
    run_migration()
