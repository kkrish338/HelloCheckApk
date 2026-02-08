# Minimal Kivy Hello App

This is a minimal cross-platform Kivy app that runs on Windows (desktop) and Android (APK built via GitHub Actions).

## Features
- Text input for name
- Submit button
- Displays "Hello <Name>" with colored background and icon

## Local Desktop Test (Windows)

1. Install Python 3.8+ and Git
2. Clone repo:
   ```sh
   git clone <your-repo-url>
   cd hello_world_apk
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run app:
   ```sh
   python main.py
   ```
5. Build Windows executable:
   ```sh
   pip install pyinstaller
   pyinstaller --onefile main.py
   dist\main.exe
   ```

## Android APK Build (Cloud)

- Push to GitHub. The workflow in `.github/workflows/android-apk.yml` will build the APK and upload it as an artifact.
- Download APK from the Actions tab after the workflow completes.

## Troubleshooting
See the end of this README for common issues and fixes.
