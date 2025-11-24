[app]
title = Neo Launcher
package.name = neolauncher
package.domain = org.pritam
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 1. Pillow हटा दिया (अक्सर एरर देता है और लॉन्चर में इसकी जरूरत नहीं है)
requirements = python3,kivy==2.2.0

# --- Launcher Setting ---
android.manifest.intent_filters = <intent-filter><action android:name="android.intent.action.MAIN" /><category android:name="android.intent.category.HOME" /><category android:name="android.intent.category.DEFAULT" /></intent-filter>

orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,QUERY_ALL_PACKAGES

# --- FINAL STABLE SETTINGS ---
# API 33 (Android 13) - Ubuntu 22.04 के साथ बेस्ट चलता है
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# 2. सबसे जरूरी बदलाव: Develop को हटाकर Master (Stable) कर दिया
p4a.branch = master
