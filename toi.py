import sys
import time
from rich.console import Console
import pygame

console = Console()

colors = [ "red", "green", "blue", "yellow", "magenta", "cyan"]

lines = [
    {"line": "Anh vui sao nước mắt cứ tuôn trào", "char_delay": 0.06},
    {"line": "Chẳng phải như thế quá tốt hay sao?", "char_delay": 0.06},
    {"line": "Anh ta đáng giá nhường nào", "char_delay": 0.06},
    {"line": "Ngược lại nhìn anh trông chẳng ra sao?", "char_delay": 0.05},
    {"line": "Cũng đúng thôi", "char_delay": 0.08},
    {"line": "Anh làm gì", "char_delay": 0.08},
    {"line": "Xứng đáng với em", "char_delay": 0.08}
]

delays = [0.60, 0.5, 0.9, 0.7, 1.7, 1.9, 1.6]

def rainbow_karaoke():
    for i, data in enumerate(lines):
        text = data["line"]
        char_delay = data["char_delay"]

        for j, char in enumerate(text):
            color = colors[j % len(colors)]
            console.print(char, style=f"bold {color}", end="")
            sys.stdout.flush()
            time.sleep(char_delay)
      
        print()

        time.sleep(delays[i])

# Khởi tạo pygame và phát nhạc nền
pygame.mixer.init()
pygame.mixer.music.load("nhac.mp3")  # Đường dẫn tới file nhạc của bạn
pygame.mixer.music.play()

rainbow_karaoke()

# Dừng nhạc khi kết thúc
pygame.mixer.music.stop()
