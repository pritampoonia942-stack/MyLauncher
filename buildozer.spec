[app]
title = Neo Launcher
package.name = neolauncher
package.domain = org.pritam
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Kivy 2.1.0 सबसे स्टेबल है
requirements = python3,kivy==2.1.0

# --- Launcher Setting ---
android.manifest.intent_filters = <intent-filter><action android:name="android.intent.action.MAIN" /><category android:name="android.intent.category.HOME" /><category android:name="android.intent.category.DEFAULT" /></intent-filter>

orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,QUERY_ALL_PACKAGES

# --- GOLDEN SETTINGS (100% Working) ---
# Android 12 (API 31) - यह एरर-फ्री है
android.api = 31
android.minapi = 21
# NDK 23b - यह Kivy के साथ मक्खन जैसा चलता है
android.ndk = 23b
android.accept_sdk_license = True
p4a.branch = master
