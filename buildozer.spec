[app]
title = Neo Launcher
package.name = neolauncher
package.domain = org.pritam
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# हम Kivy का पुराना और भरोसेमंद वर्ज़न यूज़ करेंगे
requirements = python3,kivy==2.1.0,pillow

# --- Launcher Setting ---
android.manifest.intent_filters = <intent-filter><action android:name="android.intent.action.MAIN" /><category android:name="android.intent.category.HOME" /><category android:name="android.intent.category.DEFAULT" /></intent-filter>

orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,QUERY_ALL_PACKAGES

# --- SAFE & STABLE SETTINGS ---
# API 31 (Android 12) कभी फेल नहीं होता
android.api = 31
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True
p4a.branch = master
