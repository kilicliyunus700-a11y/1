# 🔥 Root - Team AutoExploit v1.0.0 💥

## 📌 Introduction

We are proud to announce the release of **Root - Team AutoExploit v1.0.0** — a powerful WordPress auto-exploitation tool built with a custom plugin for practical and effective penetration testing.

Unlike traditional vulnerability scanners that only detect potential issues, **Root - Team AutoExploit** is designed to actively exploit known WordPress CVEs and gain shell access when possible.  
This makes it a valuable tool for security professionals who need results, not just reports.  
Version 1.0.0 focuses exclusively on WordPress vulnerabilities and is optimized for Windows users, offering a simple user interface for configuration and execution.  
This is just the beginning—expect more CMS support and advanced modules in future versions.

---

## 🚀 Features – Root - Team AutoExploit v1.0.0

Root - Team AutoExploit is designed for offensive security professionals who want more than just scanning—it provides real-world exploitation capabilities, a modular plugin system, and an intuitive user interface.

### ✅ 1. Mass Exploitation Using `Target_Lists.txt`

Run exploitation against multiple targets listed in `Target_Lists.txt` (one URL per line).

> **INFO:**  
> To fully utilize the framework, enable the following in `ui_config`:
> - CVE Exploiter  
> - LFI Scanner  
> - Plugin Exploiter  

When combined, these modules provide powerful exploitation capabilities across multiple attack vectors.

---

### ✅ 2. Single Plugin with Bulk Targets

Select a specific plugin from `Plugin_Lists` and test it against a list of targets in `Lists.txt`.

> **Use Case:** Ideal for testing your favorite plugin against multiple websites (e.g., your own domains or local environments).

---

### ✅ 3. Single Plugin with Single Target

Test one specific plugin exploit against a single target domain.

> **Use Case:** 1-to-1 plugin testing — great for precision testing or local development.

---

### 🛠️ 4. Developer Mode – Build Your Own Plugins

Create and drop your own custom exploit plugins into the `Plugins_Exploiter/` directory.  
Simply run the tool using `install_plugin`, and your plugin will be:

- ✅ Loaded in real time  
- ✅ Validated for structure and errors  
- ✅ Debugged live with error notifications  

> **INFO:**
> - Supports WordPress CVEs and any other CVE-based web application exploits, including PHP, Laravel, etc.  
> - Use the `Plugin_BurnWP()` function as the entry point, similar to a `main()` function.  
> - Supports both GET and POST methods via prebuilt `Shell_Loader` forms.  

---

### ⚙️ 5. User-Friendly Interface for Configuration

Configure the tool via a simple UI or directly by editing `Config/config.json`.

> **INFO:**  
> Enable or disable features with:  
> ```json
> "Enable": True  
> "Disable": False
> ```
> All modules are toggleable via the `ui_config` interface for quick adjustments.

---

### 📚 6. CVE Database Overview (Built-In)

Root - Team AutoExploit includes a detailed CVE index that gives you full visibility into available exploits:

| **Field**       | **Description**                                      |
|------------------|------------------------------------------------------|
| ID               | Total number of available exploits                   |
| Title            | Name of the exploit                                  |
| CVE              | CVE ID (e.g., CVE-2024-XXXX)                         |
| Severity         | Rating (Critical, High, 7.5, etc.)                   |
| Public Date      | When the exploit was publicly released               |
| CVE Date         | Year the CVE was registered                          |
| Description      | Type of vulnerability (e.g., RCE, LFI, SQLi)         |
| Source           | Whether from core built-in tools or external plugins |
| Plugin CVE       | Shows if related to a plugin CVE                     |
| Technology       | Target platform (e.g., WordPress, Laravel, PHP, etc.)|


| ID  | Title                                      | CVE            |
|-----|--------------------------------------------|----------------|
| 1   | File manager v6.9                          | CVE-2020-25213 |
| 2   | Cherry Plugin v1.2.7                       | Unknown        |
| 3   | Social Warfare 3.5.3                       | CVE-2019-9978  |
| 4   | ContactForm7_DND                           | CVE-2020-12800 |
| 5   | ContactForm7 5.1.6                         | CVE-2020-35489 |
| 6   | UserProfile Builder 3.11.7                 | CVE-2024-6366  |
| 7   | Slider Revolution Shell Upload             | CVE-2014-9735  |
| 8   | Bricks Builder 1.9.6                       | CVE-2024-25600 |
| 9   | Plugin Work The Flow 2.5.2                 | Unknown        |
| 10  | Plugin TheCartPress 1.5.3.6                | Unknown        |
| 11  | 3DPrint Lite <= 1.9.1.4                    | Unknown        |
| 12  | Cloudflare                                 | CVE-2017-9841  |
| 13  | DZS-videogaller                            | CVE-2017-9841  |
| 14  | MM-plugin                                  | CVE-2017-9841  |
| 15  | Affinipay-payment-gateway                  | CVE-2017-9841  |
| 16  | Aspose-pdf-importer                        | CVE-2017-9841  |
| 17  | Badgeup                                    | CVE-2017-9841  |
| 18  | Contact-form-7-to-database-extension       | CVE-2017-9841  |
| 19  | Jannes-mannes-social-media-auto-publisher  | CVE-2017-9841  |
| 20  | Jekyll-exporter                            | CVE-2017-9841  |
| 21  | Theme JS_Composer                          | CVE-2017-9841  |
| 22  | Message-Business                           | CVE-2017-9841  |
| 23  | MirAd-Network                              | CVE-2017-9841  |
| 24  | MM-plugin-inc                              | CVE-2017-9841  |
| 25  | Prh-api                                    | CVE-2017-9841  |
| 26  | Product-lister-walmart                     | CVE-2017-9841  |
| 27  | Realia-libraries-PayPal-PHP-SDK            | CVE-2017-9841  |
| 28  | Rollbar                                    | CVE-2017-9841  |
| 29  | Shortcode-tumblr-gallery                   | CVE-2017-9841  |
| 30  | Turtle-ad-network                          | CVE-2017-9841  |
| 31  | User-export-with-their-meta-data           | CVE-2017-9841  |
| 32  | Waves-ad-network                           | CVE-2017-9841  |
| 33  | Plugins-heyloyalty                         | CVE-2017-9841  |
| 34  | Wptimetoread                               | CVE-2017-9841  |
| 35  | Theme Divi-child                           | CVE-2017-9841  |
| 36  | Theme howto_wp                             | CVE-2017-9841  |
| 37  | Theme techmatters                          | CVE-2017-9841  |
| 38  | Upload 2018                                | CVE-2017-9841  |
---

## 📥 Requirements and Installation

1. ✅ Download and install **Python 3.12 or the latest version**:  
   👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. ✅ Clone this repository:
```bash
git clone https://github.com/kilicliyunus700-a11y/1.git
cd 1
```

<details>
<summary>🪟 How to Install on Windows</summary>

```bash
Option 1 — Manual installation
python3 -m pip install -r requirements.txt
python3 main.py

Option 2 — One-click installer
setup.bat
python3 main.py
```
</details>

<details>
<summary>🐧 How to Install on Linux</summary>

```bash
#Linux system dependencies
sudo apt update && sudo apt install -y \
    libxcb-xinerama0 libxkbcommon-x11-0 \
    libqt5gui5 libqt5widgets5 libqt5quick5 libqt5svg5

#Create a virtual environment
sudo apt install -y python3-venv

python3 -m venv .venv
source .venv/bin/activate    
python3 -m pip install --upgrade pip
pip install -r requirements.txt

python3 main.py
```
</details>

<details>
<summary>🍎 How to Install on macOS</summary>

```bash
python3 -m pip install -r requirements.txt
python3 main.py
```

</details>

---

## 🤝 Contributing

We welcome contributions! Feel free to fork this repository, make enhancements, and open pull requests. Please check the [issues](#) page for ongoing tasks or bug reports.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

> ⚠️ **Disclaimer**: This tool is for educational purposes only. 🏫 The creator (`zeproot`) and contributors are not responsible for any misuse or damages caused. Use responsibly, and only on systems you own or have permission for. ✅

