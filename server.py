import http.server
import socketserver
import os
import json
import sys
from urllib.parse import urlparse, parse_qs

# Force flush prints
def print_flush(msg):
    print(msg)
    sys.stdout.flush()

PORT = 8123
ARTIFACT_DIR = r"C:\Users\huudu\.gemini\antigravity\brain\42e63b1a-6582-4aab-b3fa-6ee6475e6190"
WEB_DIR = r"d:\code\Data\novel_web"

NOVELS = {
    "daidao": {
        "id": "daidao",
        "title": "Đại Đạo Vô Tâm",
        "author": "Sát Trư Nhân",
        "tags": "Tiên Hiệp, Xuyên Không, Hài Hước, Hắc Ám",
        "status": "Đang ra",
        "summary": "Cứ nghĩ xuyên không vào môn phái tu tiên là sẽ phi thiên độn địa, ai dè lại phải vác cuốc đi cày linh điền, ăn cháo trắng cầm hơi. Ba kẻ hiện đại: Một nhân viên kế toán lười biếng 'vô tâm', một sát thủ trầm mặc cuồng sát, và một cô gái 'overthinking' cực đoan. Không có hào quang nhân vật chính, không có bàn tay vàng miễn phí. Chỉ có tư duy thực dụng, mưu hèn kế bẩn, và tình huynh đệ phũ phàng.",
        "cover": "cover.png",
        "prefix": "chapter_"
    },
    "khaithien": {
        "id": "khaithien",
        "title": "Khai Thiên (Quyển 1)",
        "author": "Cố Duy",
        "tags": "Hệ Thống, Cổ Đại, Xây Dựng Văn Minh, Độc Hành",
        "status": "Hoàn Thành",
        "summary": "Từ Bầy đàn Du mục đến Đế chế Sơ khai. Từ Công cụ Đá vỡ đến Kỷ nguyên Đồ sắt. Xuyên không về 800 năm trước để dẫn dắt sự tiến hóa của nhân loại. Một kiếp nhân sinh siêu phàm của kẻ kiến tạo văn minh, đập vỡ xiềng xích của tự nhiên.",
        "cover": "https://via.placeholder.com/200x300/1e293b/a78bfa?text=Khai+Thien",
        "prefix": "khaithien_chapter_"
    }
}

class NovelRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print_flush("%s - - [%s] %s" % (self.client_address[0], self.log_date_time_string(), format%args))

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        
        if path == '/':
            self.path = '/index.html'
            return super().do_GET()
            
        elif path == '/api/novels':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            novels_list = list(NOVELS.values())
            self.wfile.write(json.dumps(novels_list).encode('utf-8'))
            return
            
        elif path == '/api/files':
            query = parse_qs(parsed_url.query)
            novel_id = query.get('novel_id', [''])[0]
            
            # Nếu truyền sai hoặc không truyền, mặc định là truyện đầu tiên (daidao) để backward compatible
            novel_info = NOVELS.get(novel_id, NOVELS["daidao"])
            prefix = novel_info['prefix']
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            files = []
            if os.path.exists(ARTIFACT_DIR):
                for f in os.listdir(ARTIFACT_DIR):
                    if f.endswith('.md') and f.startswith(prefix):
                        files.append(f)
            
            files.sort()
            self.wfile.write(json.dumps(files).encode('utf-8'))
            return
            
        elif path.startswith('/files/'):
            filename = path[len('/files/'):]
            filepath = os.path.join(ARTIFACT_DIR, filename)
            if os.path.exists(filepath) and filename.endswith('.md'):
                self.send_response(200)
                self.send_header('Content-type', 'text/markdown; charset=utf-8')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                with open(filepath, 'r', encoding='utf-8') as f:
                    text_content = f.read()
                self.wfile.write(text_content.encode('utf-8'))
            else:
                self.send_error(404, "File not found")
            return
            
        return super().do_GET()

os.chdir(WEB_DIR)
Handler = NovelRequestHandler

print_flush(f"Starting Novel Web Server on 127.0.0.1:{PORT}")
print_flush(f"Web Directory: {WEB_DIR}")
print_flush(f"Artifact Directory: {ARTIFACT_DIR}")

# Bind to localhost specifically
with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    httpd.serve_forever()
