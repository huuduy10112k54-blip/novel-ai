import os

def replace_in_file(filepath, replacements):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"C:\Users\huudu\.gemini\antigravity\brain\42e63b1a-6582-4aab-b3fa-6ee6475e6190"

replacements = {
    'chapter_03.md': [
        ('"Tao không thấy gì cả,"', '"Ta không thấy gì cả,"'),
        ('“Tao không thấy gì cả,”', '“Ta không thấy gì cả,”'),
        ('"Tao chỉ nói chuyện bình thường thôi."', '"Ta chỉ nói chuyện bình thường thôi."'),
        ('“Tao chỉ nói chuyện bình thường thôi.”', '“Ta chỉ nói chuyện bình thường thôi.”')
    ],
    'chapter_04.md': [
        ('"Tao tự luyện theo cách tao cảm thấy đúng,"', '"Đệ tử tự luyện theo cách đệ tử cảm thấy đúng,"'),
        ('“Tao tự luyện theo cách tao cảm thấy đúng,”', '“Đệ tử tự luyện theo cách đệ tử cảm thấy đúng,”'),
        ('"Tao cũng không hiểu tại sao họ đứng xem,"', '"Ta cũng không hiểu tại sao họ đứng xem,"'),
        ('“Tao cũng không hiểu tại sao họ đứng xem,”', '“Ta cũng không hiểu tại sao họ đứng xem,”'),
        ('"Tao luyện nhiều,"', '"Đệ tử luyện nhiều,"'),
        ('“Tao luyện nhiều,”', '“Đệ tử luyện nhiều,”')
    ],
    'chapter_06.md': [
        ('"Tao học về thảo dược,"', '"Ta học về thảo dược,"'),
        ('“Tao học về thảo dược,”', '“Ta học về thảo dược,”'),
        ('"Dẫn tao đi xem thử,"', '"Dẫn ta đi xem thử,"'),
        ('“Dẫn tao đi xem thử,”', '“Dẫn ta đi xem thử,”')
    ],
    'chapter_07.md': [
        ('"Tao đến tiễn."', '"Cháu đến tiễn."'),
        ('“Tao đến tiễn.”', '“Cháu đến tiễn.”'),
        ('cho tao mấy cái lông', 'cho cháu mấy cái lông'),
        ('Tao cần làm đuôi robot.', 'Cháu cần làm đuôi robot.'),
        ('"Tao không bế mày."', '"Anh không bế em."'),
        ('“Tao không bế mày.”', '“Anh không bế em.”'),
        ('"Tao không cần anh bế,"', '"Em không cần anh bế,"'),
        ('“Tao không cần anh bế,”', '“Em không cần anh bế,”')
    ],
    'chapter_09.md': [
        ('"Tao không có thói quen đó."', '"Ta không có thói quen đó."'),
        ('“Tao không có thói quen đó.”', '“Ta không có thói quen đó.”')
    ],
    'chapter_10.md': [
        ("nhắc nhở tao phải", "nhắc nhở tôi phải")
    ]
}

for filename, reps in replacements.items():
    replace_in_file(os.path.join(base_dir, filename), reps)

print("Replacements done.")
