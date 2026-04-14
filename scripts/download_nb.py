import urllib.request
import json
import traceback

def main():
    try:
        url = 'https://raw.githubusercontent.com/ultralytics/ultralytics/main/examples/tutorial.ipynb'
        req = urllib.request.urlopen(url)
        content = req.read().decode('utf-8')
        nb = json.loads(content)
        
        with open('notebook_summary.txt', 'w', encoding='utf-8') as f:
            for i, cell in enumerate(nb.get('cells', [])):
                cell_type = cell.get('cell_type', '')
                f.write(f'\n--- CELL {i} ({cell_type}) ---\n')
                source = cell.get('source', [])
                if isinstance(source, str):
                    source = [source]
                
                # Write up to 10 lines of the cell
                for line in source[:10]:
                    f.write(line)
                if len(source) > 10:
                    f.write('\n... (truncated)')
                f.write('\n')
        print("Summary written to notebook_summary.txt")
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()

if __name__ == '__main__':
    main()
