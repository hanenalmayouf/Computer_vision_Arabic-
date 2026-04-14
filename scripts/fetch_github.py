import urllib.request, json
url = 'https://api.github.com/repos/ultralytics/ultralytics/contents/docs/en/modes'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read())
        for img in data:
            if img['name'].endswith('.md'):
                print(f"{img['name'].replace('.md', '')}: {img['html_url']}")
except Exception as e:
    print(f"Error: {e}")
