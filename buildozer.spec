[app]
title = Neo Launcher
package.name = neolauncher
package.domain = org.pritam
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.0,pillow

# --- Launcher Setting ---
android.manifest.intent_filters = <intent-filter><action android:name="android.intent.action.MAIN" /><category android:name="android.intent.category.HOME" /><category android:name="android.intent.category.DEFAULT" /></intent-filter>

orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,QUERY_ALL_PACKAGES

# --- SMART SETTINGS (Fast & Compatible) ---
# API 33 (Android 13) - नए कंप्यूटर पर चलता है
android.api = 33
# MINAPI 21 - Android 5+ (आपके Android 11 पर दौड़ेगा)
android.minapi = 21
# NDK 25b - यह सबसे जरूरी है ताकि नए कंप्यूटर पर क्रैश न हो
android.ndk = 25b
android.accept_sdk_license = True
p4a.branch = develop
