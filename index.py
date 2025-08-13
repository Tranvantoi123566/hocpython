import subprocess
import tkinter as tk
from tkinter import messagebox

def download_subtitle():
    url = url_entry.get().strip()
    lang = lang_entry.get().strip() or "en"
    
    if not url:
        messagebox.showerror("Lỗi", "Vui lòng nhập URL YouTube.")
        return

    # Thử phụ đề gốc
    command = [
        "yt-dlp",
        "--write-sub",
        "--sub-format", "srt",
        "--skip-download",
        f"--sub-lang={lang}",
        url
    ]
    
    try:
        print("📥 Đang thử tải phụ đề gốc...")
        subprocess.run(command, check=True)
        messagebox.showinfo("Thành công", "✅ Đã tải phụ đề gốc thành công.")
    except subprocess.CalledProcessError:
        print("⚠️ Không có phụ đề gốc. Thử phụ đề tự động...")
        # Thử phụ đề auto nếu phụ đề gốc không có
        command_auto = [
            "yt-dlp",
            "--write-auto-sub",
            "--sub-format", "srt",
            "--skip-download",
            f"--sub-lang={lang}",
            url
        ]
        try:
            subprocess.run(command_auto, check=True)
            messagebox.showinfo("Thành công", "✅ Đã tải phụ đề tự động thành công.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Lỗi", "❌ Không tải được phụ đề. Video có thể không có phụ đề cho ngôn ngữ đã chọn.")

# Giao diện tkinter
root = tk.Tk()
root.title("🔽 YouTube Subtitle Downloader")
root.geometry("500x200")

tk.Label(root, text="🔗 Link video YouTube:").pack(padx=10, pady=5)
url_entry = tk.Entry(root, width=60)
url_entry.pack(padx=10)

tk.Label(root, text="🌐 Ngôn ngữ phụ đề (ví dụ: en, vi):").pack(padx=10, pady=5)
lang_entry = tk.Entry(root, width=20)
lang_entry.pack(padx=10)

tk.Button(root, text="📥 Tải phụ đề", command=download_subtitle).pack(pady=15)

root.mainloop()
