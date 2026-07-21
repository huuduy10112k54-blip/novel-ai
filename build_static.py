import os
import json

dist_dir = r"d:\code\Data\novel_web\dist"
chapters_dir = os.path.join(dist_dir, "chapters")

# Create files.json
chapters = sorted([f for f in os.listdir(chapters_dir) if f.startswith("chapter_") and f.endswith(".md")])
with open(os.path.join(dist_dir, "files.json"), "w", encoding="utf-8") as f:
    json.dump(chapters, f)

# Update index.html
html_path = os.path.join(dist_dir, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("'/api/files'", "'files.json'")
html = html.replace("/files/", "/chapters/")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Build successful.")
