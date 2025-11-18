"""
PunchIT Now - Smart Launcher with Auto-Update
Завантажує оновлення з GitHub та запускає New soft 3.0.py
"""

import os
import sys
import urllib.request
import json
import subprocess
import tkinter as tk
from tkinter import messagebox
import threading
from pathlib import Path

# GitHub Configuration
GITHUB_USER = "alexvlasov182"  # Твій GitHub username
GITHUB_REPO = "punchit-now"    # Назва репозиторію
GITHUB_BRANCH = "main"         # Гілка (main або master)

# Files to update from GitHub
FILES_TO_UPDATE = {
    "New soft 3.0.py": "New soft 3.0.py",
    "conversion_monitor.py": "conversion_monitor.py",
    "version.json": "version.json"
}

CURRENT_VERSION_FILE = "version.json"
LOCAL_VERSION_FILE = Path("version.json")

class UpdateLauncher:
    def __init__(self):
        self.current_dir = Path(__file__).parent
        self.version_info = self.load_local_version()
        
    def load_local_version(self):
        """Завантажує локальну версію"""
        version_file = self.current_dir / LOCAL_VERSION_FILE
        if version_file.exists():
            try:
                with open(version_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        return {"version": "0.0.0", "last_update": "Never"}
    
    def get_github_raw_url(self, filename):
        """Генерує URL для завантаження з GitHub"""
        return f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}/{filename}"
    
    def download_file(self, url, destination):
        """Завантажує файл з GitHub"""
        try:
            print(f"📥 Downloading: {url}")
            with urllib.request.urlopen(url, timeout=30) as response:
                content = response.read()
                with open(destination, 'wb') as f:
                    f.write(content)
            print(f"✅ Downloaded: {destination}")
            return True
        except Exception as e:
            print(f"❌ Download failed: {e}")
            return False
    
    def check_for_updates(self):
        """Перевіряє наявність оновлень на GitHub"""
        try:
            version_url = self.get_github_raw_url("version.json")
            with urllib.request.urlopen(version_url, timeout=10) as response:
                remote_version_data = json.loads(response.read().decode('utf-8'))
            
            remote_version = remote_version_data.get("version", "0.0.0")
            local_version = self.version_info.get("version", "0.0.0")
            
            print(f"🔍 Local version: {local_version}")
            print(f"🔍 Remote version: {remote_version}")
            
            # Порівнюємо версії (формат: major.minor.patch)
            local_parts = [int(x) for x in local_version.split('.')]
            remote_parts = [int(x) for x in remote_version.split('.')]
            
            if remote_parts > local_parts:
                return True, remote_version_data
            return False, None
            
        except Exception as e:
            print(f"⚠️ Can't check updates: {e}")
            return False, None
    
    def update_files(self, progress_callback=None):
        """Завантажує всі файли з GitHub"""
        success_count = 0
        total_files = len(FILES_TO_UPDATE)
        
        for i, (github_file, local_file) in enumerate(FILES_TO_UPDATE.items(), 1):
            if progress_callback:
                progress_callback(i, total_files, f"Downloading {local_file}...")
            
            url = self.get_github_raw_url(github_file)
            destination = self.current_dir / local_file
            
            if self.download_file(url, destination):
                success_count += 1
        
        return success_count == total_files
    
    def launch_app(self):
        """Запускає основну програму"""
        main_app = self.current_dir / "New soft 3.0.py"
        if main_app.exists():
            print(f"\n🚀 Launching: {main_app}")
            
            # Запускаємо Python скрипт
            python_exe = sys.executable
            subprocess.Popen([python_exe, str(main_app)])
            return True
        else:
            print(f"❌ Main app not found: {main_app}")
            return False


class LauncherUI:
    def __init__(self):
        self.launcher = UpdateLauncher()
        self.root = tk.Tk()
        self.root.title("PunchIT Now - Launcher")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        
        # Center window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.root.winfo_screenheight() // 2) - (300 // 2)
        self.root.geometry(f"500x300+{x}+{y}")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Header
        header = tk.Label(self.root, text="🚀 PunchIT Now Launcher", 
                         font=("Arial", 18, "bold"), fg="#2196F3")
        header.pack(pady=20)
        
        # Version info
        version = self.launcher.version_info.get("version", "Unknown")
        self.version_label = tk.Label(self.root, 
                                      text=f"Current version: {version}", 
                                      font=("Arial", 11))
        self.version_label.pack(pady=5)
        
        # Status label
        self.status_label = tk.Label(self.root, 
                                     text="Checking for updates...", 
                                     font=("Arial", 10), 
                                     fg="gray")
        self.status_label.pack(pady=10)
        
        # Progress bar (simple)
        self.progress_frame = tk.Frame(self.root)
        self.progress_frame.pack(pady=10)
        
        self.progress_label = tk.Label(self.progress_frame, 
                                       text="", 
                                       font=("Arial", 9))
        self.progress_label.pack()
        
        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        self.update_btn = tk.Button(button_frame, 
                                    text="🔄 Check Updates", 
                                    command=self.check_updates,
                                    font=("Arial", 11, "bold"),
                                    bg="#4CAF50", fg="white",
                                    width=15, height=2,
                                    cursor="hand2")
        self.update_btn.pack(side=tk.LEFT, padx=5)
        
        self.launch_btn = tk.Button(button_frame, 
                                    text="▶️ Launch App", 
                                    command=self.launch_app,
                                    font=("Arial", 11, "bold"),
                                    bg="#2196F3", fg="white",
                                    width=15, height=2,
                                    cursor="hand2")
        self.launch_btn.pack(side=tk.LEFT, padx=5)
        
        # Auto-check updates on start
        self.root.after(500, self.check_updates)
        
    def check_updates(self):
        """Перевіряє оновлення в окремому потоці"""
        self.status_label.config(text="🔍 Checking for updates...", fg="orange")
        self.update_btn.config(state=tk.DISABLED)
        
        def check_thread():
            has_update, remote_info = self.launcher.check_for_updates()
            
            if has_update:
                remote_version = remote_info.get("version", "Unknown")
                self.root.after(0, lambda: self.show_update_dialog(remote_version, remote_info))
            else:
                self.root.after(0, lambda: self.status_label.config(
                    text="✅ You have the latest version", fg="green"))
                self.root.after(0, lambda: self.update_btn.config(state=tk.NORMAL))
        
        threading.Thread(target=check_thread, daemon=True).start()
    
    def show_update_dialog(self, new_version, remote_info):
        """Показує діалог про доступне оновлення"""
        changelog = remote_info.get("changelog", "New version available")
        
        msg = f"🎉 New version available: {new_version}\n\n"
        msg += f"Changes:\n{changelog}\n\n"
        msg += "Download update now?"
        
        response = messagebox.askyesno("Update Available", msg)
        
        if response:
            self.download_update()
        else:
            self.status_label.config(text="⏭️ Update skipped", fg="gray")
            self.update_btn.config(state=tk.NORMAL)
    
    def download_update(self):
        """Завантажує оновлення"""
        self.status_label.config(text="📥 Downloading updates...", fg="blue")
        self.progress_label.config(text="Starting download...")
        
        def download_thread():
            def progress_callback(current, total, message):
                percentage = int((current / total) * 100)
                self.root.after(0, lambda: self.progress_label.config(
                    text=f"[{current}/{total}] {message} ({percentage}%)"))
            
            success = self.launcher.update_files(progress_callback)
            
            if success:
                # Оновлюємо версію в UI
                new_version_info = self.launcher.load_local_version()
                new_version = new_version_info.get("version", "Unknown")
                
                self.root.after(0, lambda: self.version_label.config(
                    text=f"Current version: {new_version}"))
                self.root.after(0, lambda: self.status_label.config(
                    text="✅ Update completed successfully!", fg="green"))
                self.root.after(0, lambda: self.progress_label.config(
                    text="All files updated!"))
                
                # Пропонуємо запустити програму
                self.root.after(500, lambda: messagebox.showinfo(
                    "Success", "Update completed! Click 'Launch App' to start."))
            else:
                self.root.after(0, lambda: self.status_label.config(
                    text="❌ Update failed", fg="red"))
                self.root.after(0, lambda: messagebox.showerror(
                    "Error", "Failed to download some files. Check internet connection."))
            
            self.root.after(0, lambda: self.update_btn.config(state=tk.NORMAL))
        
        threading.Thread(target=download_thread, daemon=True).start()
    
    def launch_app(self):
        """Запускає основну програму"""
        if self.launcher.launch_app():
            self.root.after(1000, self.root.destroy)
        else:
            messagebox.showerror("Error", 
                               "Main application not found!\nPlease download updates first.")
    
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    print("="*60)
    print("🚀 PunchIT Now - Smart Launcher")
    print("="*60)
    
    app = LauncherUI()
    app.run()
