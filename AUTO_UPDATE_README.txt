═══════════════════════════════════════════════════════════════════════
  🔄 СИСТЕМА АВТООНОВЛЕНЬ PUNCH IT NOW
═══════════════════════════════════════════════════════════════════════

🎯 ЩО ДОДАНО:

1. Кнопка "🔄 Перевірити оновлення" в Settings Tab
2. Автоматична перевірка версії на GitHub
3. Завантаження .exe файлу
4. Автоматична заміна старої версії
5. Оновлення конфігурацій (опціонально)
6. Перезапуск програми після оновлення

═══════════════════════════════════════════════════════════════════════

📁 СТРУКТУРА ФАЙЛІВ НА GITHUB:

Створіть у своєму репозиторії такі файли:

1. version.json (у корені репозиторію):
   {
     "version": "9.3.0",
     "download_url": "https://github.com/USERNAME/REPO/releases/download/v9.3.0/PunchITNow.exe",
     "config_url": "https://raw.githubusercontent.com/USERNAME/REPO/main/config_update.json",
     "changelog": "🎉 Що нового...",
     "required": false,
     "min_version": "9.0.0"
   }

2. config_update.json (якщо треба оновити конфіги):
   {
     "features_config.json": { ... },
     "hotkeys_config.json": { ... }
   }

3. Release на GitHub з .exe файлом

═══════════════════════════════════════════════════════════════════════

⚙️ НАЛАШТУВАННЯ:

1. Відкрийте файл "New soft 3.0.py"

2. Знайдіть метод check_for_updates() (біля рядка 13472)

3. Замініть YOUR_USERNAME та YOUR_REPO:
   VERSION_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/version.json"
   
   Приклад:
   VERSION_URL = "https://raw.githubusercontent.com/AlexFarmPunch/PunchITNow/main/version.json"

4. Оновіть CURRENT_VERSION на актуальну версію вашого софту:
   CURRENT_VERSION = "9.2.0"

═══════════════════════════════════════════════════════════════════════

📦 ЯК СТВОРИТИ RELEASE НА GITHUB:

1. Зберіть .exe файл через PyInstaller:
   pyinstaller --onefile --windowed "New soft 3.0.py"

2. Перейдіть на GitHub → Ваш репозиторій → Releases

3. Натисніть "Create a new release"

4. Tag version: v9.3.0 (відповідає версії в version.json)

5. Release title: Punch IT Now v9.3.0

6. Завантажте .exe файл в Assets

7. Скопіюйте URL завантаження та вставте в version.json:
   https://github.com/USERNAME/REPO/releases/download/v9.3.0/PunchITNow.exe

═══════════════════════════════════════════════════════════════════════

🔄 ПРОЦЕС ОНОВЛЕННЯ:

1. Користувач натискає "Перевірити оновлення"
2. Софт перевіряє version.json на GitHub
3. Порівнює версії (9.2.0 vs 9.3.0)
4. Якщо є оновлення → показує діалог з changelog
5. Користувач натискає "Завантажити та встановити"
6. Софт завантажує .exe файл
7. Завантажує config_update.json (якщо є)
8. Створює bat-скрипт для заміни файлу
9. Перейменовує старий .exe в PunchITNow_old.exe (backup)
10. Копіює новий .exe
11. Запускає нову версію
12. Видаляє bat-скрипт

═══════════════════════════════════════════════════════════════════════

🛡️ БЕЗПЕКА:

1. Backup створюється автоматично (PunchITNow_old.exe)
2. Якщо щось піде не так - можна запустити старий .exe
3. Тимчасові файли видаляються після оновлення
4. Користувач може відмовитись від оновлення
5. Перевірка версій через порівняння (packaging.version)

═══════════════════════════════════════════════════════════════════════

📝 ПРИКЛАД version.json:

{
  "version": "9.3.0",
  "download_url": "https://github.com/AlexFarmPunch/PunchITNow/releases/download/v9.3.0/PunchITNow.exe",
  "config_url": "https://raw.githubusercontent.com/AlexFarmPunch/PunchITNow/main/config_update.json",
  "changelog": "🎉 Що нового у версії 9.3.0:\n\n✨ Нові функції:\n• Додано систему автооновлень\n• Покращено парсинг Google Sheets\n\n🐛 Виправлення:\n• Виправлено помилку з CVV полем\n• Покращено стабільність x4 режиму",
  "required": false,
  "min_version": "9.0.0"
}

═══════════════════════════════════════════════════════════════════════

🔧 ПОЛЯ version.json:

• version - нова версія (обов'язково)
• download_url - посилання на .exe (обов'язково)
• config_url - посилання на конфіги (опціонально)
• changelog - опис змін (опціонально)
• required - чи обов'язкове оновлення (не реалізовано)
• min_version - мінімальна підтримувана версія (не реалізовано)

═══════════════════════════════════════════════════════════════════════

📋 ПРИКЛАД config_update.json:

{
  "features_config.json": {
    "features": {
      "email_validator": true,
      "auto_refresh": true,
      "new_feature": true
    }
  },
  "hotkeys_config.json": {
    "minimize_restore": "f3",
    "octo_browser": "f"
  },
  "sheets_parsing_config.json": {
    "profile_name": "Название",
    "email": "Почта",
    "password": "Пароль"
  }
}

Кожен файл конфігурації оновиться відповідно.

═══════════════════════════════════════════════════════════════════════

⚠️ ВАЖЛИВО:

1. Встановіть модулі:
   pip install requests packaging

2. URL має бути публічним (raw.githubusercontent.com)

3. Тестуйте на тестовій версії перед публікацією

4. Використовуйте семантичне версіонування (X.Y.Z)
   X - major (великі зміни)
   Y - minor (нові функції)
   Z - patch (виправлення)

5. Завжди створюйте backup перед оновленням

═══════════════════════════════════════════════════════════════════════

🚀 ШВИДКИЙ СТАРТ:

1. Замініть YOUR_USERNAME/YOUR_REPO в коді
2. Створіть version.json у репозиторії
3. Створіть Release з .exe файлом
4. Оновіть version у version.json
5. Готово! Користувачі зможуть оновлюватись

═══════════════════════════════════════════════════════════════════════

💡 ПОРАДИ:

• Завжди тестуйте оновлення локально
• Пишіть детальний changelog
• Робіть backup конфігів перед оновленням
• Використовуйте GitHub Actions для автозбірки
• Створюйте pre-release для тестування

═══════════════════════════════════════════════════════════════════════

📞 ПІДТРИМКА:

Telegram: @Alex_FarmPunch

═══════════════════════════════════════════════════════════════════════
