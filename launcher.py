import os, sys, shutil, subprocess, platform
HTML_FILE = "cats_cradle (4).html"
BROWSERS = {
    "Linux": ["firefox", "brave-browser", "brave", "google-chrome", "chromium"],
    "Windows": [
        r"C:\Program Files\Mozilla Firefox\firefox.exe",
        r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    ],
}

def open_html():
    system = platform.system()
    candidates = BROWSERS.get(system, [])
    for browser in candidates:
        path = shutil.which(browser) if system != "Windows" else (browser if os.path.exists(browser) else None)
        if path:
            subprocess.Popen([path, HTML_FILE])
            return True
    return False

def install_linux():
    installers = [
        (["pacman"], ["sudo", "pacman", "-Sy", "--noconfirm", "firefox", "brave", "chromium"]),
        (["apt"], ["sudo", "apt", "update"]),
        (["dnf"], ["sudo", "dnf", "install", "-y", "firefox", "chromium"]),
        (["zypper"], ["sudo", "zypper", "--non-interactive", "install", "MozillaFirefox", "chromium"]),
        (["xbps-install"], ["sudo", "xbps-install", "-Sy", "firefox", "chromium"]),
    ]
    for checks, cmd in installers:
        if shutil.which(checks[0]):
            try:
                subprocess.run(cmd, check=False)
                if checks[0] == "apt":
                    subprocess.run(["sudo", "apt", "install", "-y", "firefox", "chromium-browser"], check=False)
            except Exception:
                pass
            return

def install_windows():
    if shutil.which("winget"):
        subprocess.run(["winget", "install", "-e", "--id", "Mozilla.Firefox"], check=False)
        subprocess.run(["winget", "install", "-e", "--id", "Brave.Brave"], check=False)
        subprocess.run(["winget", "install", "-e", "--id", "Google.Chrome"], check=False)

if not open_html():
    if platform.system() == "Linux":
        install_linux()
    elif platform.system() == "Windows":
        install_windows()
    open_html()
