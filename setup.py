from setuptools import setup

APP = ['app.py']
DATA_FILES = ['tomato.png']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['rumps'],
    'plist': {
        'CFBundleIconFile': 'tomato.png',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
