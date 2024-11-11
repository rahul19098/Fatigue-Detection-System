[app]

# (str) Title of your application
title = teat

# (str) Package name
package.name = teat

# (str) Package domain (needed for android/ios packaging)
package.domain = com.yourdomain

# (str) Source code where the main.py lives
source.dir = .

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = kivy, pygame, opencv-python

# (str) Custom source folders for requirements
source.include_exts = py,png,jpg,kv,xml

# (str) Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (bool) Indicate whether the application should be fullscreen or not


# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = CAMERA, INTERNET, RECORD_AUDIO

# (str) Android API to use
android.api = 28

# (bool) Use the RenPy REPL backend (limited python features)
# android.repl = 0

# (int) Android version code
android.version_code = 1

# (str) Android min API
android.minapi = 21

# (bool) Should the app be copy-protected?
# copylib = 0

# (bool) Should the app be in fullscreen mode?
fullscreen = 0
