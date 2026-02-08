[app]
title = HelloKivyApp
package.name = hellokivyapp
package.domain = org.example

source.dir = .
source.main = main.py
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy,Pillow

orientation = portrait
fullscreen = 1
icon.filename = icon.png
android.permissions = INTERNET

# Architectures
android.archs = arm64-v8a, armeabi-v7a

# Output
android.package_format = apk

# CI stability
android.accept_sdk_license = True
log_level = 2
warn_on_root = 0
