import os
import json
import shutil
import glob

# Cai dat thu muc
src_dir = os.getcwd()
docs_dir = os.path.join(src_dir, 'docs')
api_dir = os.path.join(docs_dir, 'api')
files_dir = os.path.join(docs_dir, 'files')

# Xoa docs cu
if os.path.exists(docs_dir):
    shutil.rmtree(docs_dir)
os.makedirs(docs_dir)
os.makedirs(api_dir)
os.makedirs(files_dir)

# 1. Copy files tinh
shutil.copy2(os.path.join(src_dir, 'index.html'), os.path.join(docs_dir, 'index.html'))
if os.path.exists(os.path.join(src_dir, 'cover.png')):
    shutil.copy2(os.path.join(src_dir, 'cover.png'), os.path.join(docs_dir, 'cover.png'))

# 2. Xay dung api/novels.json
NOVELS = [
    {
        'id': 'khaithien',
        'title': 'Khai Thiên (Quy?n 1)',
        'author': 'C? Duy',
        'tags': 'H? Th?ng, C? Ð?i, Xây D?ng Vãn Minh, Ð?c Hành',
        'status': 'Hoàn Thành',
        'summary': 'T? B?y ðàn Du m?c ð?n Ð? ch? Sõ khai. T? Công c? Ðá v? ð?n K? nguyên Ð? s?t. Xuyên không v? 800 nãm trý?c ð? d?n d?t s? ti?n hóa c?a nhân lo?i. M?t ki?p nhân sinh siêu phàm c?a k? ki?n t?o vãn minh, ð?p v? xi?ng xích c?a t? nhiên.',
        'cover': 'cover.png'
    },
    {
        'id': 'daidaovotam',
        'title': 'Ð?i Ð?o Vô Tâm',
        'author': 'Sát Trý Nhân',
        'tags': 'Tiên Hi?p, Hài Hý?c, H?c Ám',
        'status': 'Ðang ra',
        'summary': 'C? ngh? xuyên không vào môn phái tu tiên là s? phi thiên ð?n ð?a, ai dè l?i ph?i vác cu?c ði cày linh ði?n, ãn cháo tr?ng c?m hõi. Ba k? hi?n ð?i: M?t nhân viên k? toán lý?i bi?ng vô tâm, m?t sát th? tr?m m?c cu?ng sát, và m?t cô gái overthinking c?c ðoan. Ch? có tý duy th?c d?ng, mýu hèn k? b?n, và t?nh huynh ð? ph? phàng.',
        'cover': 'cover.png'
    }
]

with open(os.path.join(api_dir, 'novels.json'), 'w', encoding='utf-8') as f:
    json.dump(NOVELS, f, ensure_ascii=False)

# 3. Copy Markdown files va tao api/files_ID.json
all_mds = glob.glob(os.path.join(src_dir, '*.md'))
for novel in NOVELS:
    nid = novel['id']
    prefix = nid + '_' if nid != 'daidaovotam' else 'chapter_'
    
    novel_files = []
    for md in all_mds:
        basename = os.path.basename(md)
        if basename.startswith(prefix) and basename.endswith('.md'):
            # Copy to files_dir
            shutil.copy2(md, os.path.join(files_dir, basename))
            novel_files.append(basename)
    
    # Sort files naturally if possible, or simple sort
    novel_files.sort()
    
    with open(os.path.join(api_dir, f'files_{nid}.json'), 'w', encoding='utf-8') as f:
        json.dump(novel_files, f, ensure_ascii=False)

# 4. Sua index.html de dung Relative Path
index_path = os.path.join(docs_dir, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("fetch('/api/novels')", "fetch('api/novels.json')")
html = html.replace("fetch('/api/files?novel_id=' + novelId)", "fetch('api/files_' + novelId + '.json')")
html = html.replace("fetch('/files/' + filename)", "fetch('files/' + filename)")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Build success!')
