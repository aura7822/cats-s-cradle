import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
subprocess.check_call([
    sys.executable, "-m", "PyInstaller",
    "--onefile", "--name", "launcher", "launcher.py"
])
print("Built dist/launcher.exe")
