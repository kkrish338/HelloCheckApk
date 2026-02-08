# Buildozer Spec File for Kivy Hello App
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

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
#orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
#fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (str) Android NDK version to use
#android.ndk = 25b

# (str) Android SDK version to use
#android.sdk = 33

# (str) Android entry point, default is ok
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Supported architectures
#android.archs = armeabi-v7a, arm64-v8a, x86, x86_64

# (str) Path to a custom icon
icon.filename = icon.png

# (str) Presplash of the application
#presplash.filename = presplash.png

# (list) Pattern to whitelist for the whole project
#source.include_patterns = assets/*,images/*.png

# (str) Application versioning (method 1)
#version = 0.1

# (str) Application versioning (method 2)
#version.regex = __version__ = ['"]([^'"]*)['"]
#version.filename = %(source.dir)s/main.py

# (list) Application requirements
#requirements = python3,kivy

# (str) Custom source folders for requirements
# (Separate multiple paths with commas)
#requirements.source = 

# (str) Garden requirements
#garden_requirements = 

# (str) Custom source folders for garden requirements
#garden_requirements.source = 

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The format used to package the app for release mode (aab or apk or all)
#android.package_format = apk

# (bool) Copy the .so files instead of making a libpymodules.so (faster builds)
#android.copy_libs = 1

# (str) The entry point for your application
#entrypoint = main.py

# (str) The directory containing your application
#source.dir = .

# (str) The main .py file to use as the entry point
#source.main = main.py

# (str) The directory to store the build artifacts
#build.dir = .buildozer

# (str) The directory to store the dist artifacts
#dist.dir = bin

# (str) The directory to store the log files
#log.dir = .buildozer/log

# (str) The directory to store the cache files
#cache.dir = .buildozer/cache

# (str) The directory to store the virtualenv
#virtualenv.dir = .buildozer/venv

# (str) The directory to store the python-for-android build
#p4a.dir = .buildozer/p4a

# (str) The directory to store the python-for-android dist
#p4a.dist.dir = .buildozer/p4a/dist

# (str) The directory to store the python-for-android build cache
#p4a.cache.dir = .buildozer/p4a/cache

# (str) The directory to store the python-for-android build logs
#p4a.log.dir = .buildozer/p4a/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.dir = .buildozer/p4a/build

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log

# (str) The directory to store the python-for-android build artifacts
#p4a.build.artifacts.dir = .buildozer/p4a/build/artifacts

# (str) The directory to store the python-for-android build dist
#p4a.build.dist.dir = .buildozer/p4a/build/dist

# (str) The directory to store the python-for-android build cache
#p4a.build.cache.dir = .buildozer/p4a/build/cache

# (str) The directory to store the python-for-android build logs
#p4a.build.log.dir = .buildozer/p4a/build/log
