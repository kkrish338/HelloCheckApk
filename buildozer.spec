[app]
title = HelloKivyApp
package.name = hellokivyapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,Pillow
orientation = portrait
fullscreen = 1
icon.filename = icon.png
android.permissions = INTERNET

# Android toolchain
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools = 33.0.0

# Use GitHub SDK instead of Buildozer downloading again
android.sdk_path = $ANDROID_SDK_ROOT
android.ndk_path = $ANDROID_NDK_HOME

# Packaging
android.archs = arm64-v8a, armeabi-v7a
android.package_format = apk
