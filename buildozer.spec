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

# --- Fixing the Crash (NDK Version Lock) ---
# हम मशीन को जबरदस्ती NDK 25b इस्तेमाल करने को कह रहे हैं
android.ndk = 25b
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.accept_sdk_license = True
p4a.branch = develop
