---

# 🚀 TheTimeMachine v3.0 - Weaponizing Wayback for Recon, BugBounties, OSINT & More!

![image](https://github.com/user-attachments/assets/e99eb95e-f46e-4b97-8d2a-83bac89d0447)

You’ve heard of time travel in movies and comics, right? Well, this isn’t fiction anymore 😎. *TheTimeMachine* lets you dig through the past of any web app by scraping archived URLs from the Wayback Machine — and helps you find sensitive, forgotten, or deprecated endpoints for further exploitation.

Whether you’re into bug bounty, red teaming, or just love good ol’ recon, this tool was built to make my recon workflow faster, cleaner, and more effective. No more juggling multiple scripts — TheTimeMachine does it all in one shot.

---

## 💡 What It Does

This isn't just another Wayback scraper. Here's what TheTimeMachine brings to the table:

- 🔎 **Archived URL Fetching** – Pull historical URLs from Wayback Machine.
- 💾 **Backup File Detection** – Find `.zip`, `.bak`, `.sql`, `.tar.gz`, `.old`, and other juicy files.
- ⚔️ **Attack Mode** – Scan for vulnerable endpoints using patterns/signatures:
  - XSS
  - SQLi
  - LFI
  - Open Redirects
  - WordPress Vulns
  - JIRA-based misconfig
- 🧠 **GET Parameter Mapping** – Map every GET parameter to where it appears. (Great for fuzzing automation.)
- 🧪 **JWT Detection** – Detect and decode JWTs embedded in archived URLs.
- 📁 **Directory Listing Detection** – Find open indexed directories.
- 🕵️ **Subdomain Enumeration** – Pull subdomains seen in archived data.
- 🔍 **Keyword Search** – Search custom keywords like `config`, `backup`, `.log`, etc.
- 🧩 **Custom Payload Lists** – Use your own fuzz list or signatures for custom scans.

---

## ⚙️ Installation

Tested on **Python 3** across Ubuntu/Kali/Windows.

```bash
git clone https://github.com/anmolksachan/TheTimeMachine
````
```bash
cd TheTimeMachine
````
```bash
pip3 install -r requirements.txt
````

---

## 🚀 Usage

```bash
python3 thetimemachine.py <target.com> [OPTIONS]
```

**Note:** Don't use `http://` or `https://` in the domain — just pass `domain.com` or `sub.domain.com`.

---

## 📋 Options

| Option            | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| `--fetch`         | Fetch archived URLs from Wayback                             |
| `--backups`       | Scan for exposed backup/config files                         |
| `--attack [type]` | Run attack mode (xss, sqli, lfi, redirect, jira, wp, custom) |
| `--jwt`           | Detect & decode JWT tokens                                   |
| `--subdomains`    | Extract subdomains from historical URLs                      |
| `--parameters`    | Extract GET parameters & map them to URLs                    |
| `--listings`      | Detect open directory listings                               |

---

## 🔁 Example Workflows


#### Fetch all Wayback URLs
```bash
python3 thetimemachine.py example.com --fetch
```
#### Look for exposed backup files
```bash
python3 thetimemachine.py example.com --backups
```
#### Look for directory listing
```bash
python3 thetimemachine.py example.com --listings
```
#### Scan for possible XSS points
```bash
python3 thetimemachine.py example.com --attack xss
```
#### Map parameters from archived data
```bash
python3 thetimemachine.py example.com --parameters
```
### Extract JWTs
```bash
python3 thetimemachine.py example.com --jwt
```
### And much more
```bash
usage: thetimemachine.py [-h] [--fetch] [--jwt] [--backups] [--subdomains] [--listings] [--attack {xss,sqli,lfi,redirect,jira,wp,fuzz}] [--menu]
                         [--parameters]
                         target
```
---

## 📁 Output Structure

All results are neatly saved under the `content/` directory:

```
content/
└── example.com/
    ├── example.com_URLs.txt
    ├── example.com_xss.txt
    ├── example.com_sqli.txt
    ├── example.com_parameters.txt
    ├── example.com_subdomain.txt
    └── ...
```

---

## ✍️ Add Your Own Payloads

You can fully customize the payloads for XSS, SQLi, fuzzing, etc. Just edit the respective `.txt` files inside the repo and fire away!

---

## 🧠 Why I Built This

I'm not a full-time bug bounty hunter, but I needed a tool that’d do fast recon, find juicy endpoints, and give me enough leads to manually dig deeper. Got my HOF on multiple VDPs and bugbounty, including **NOKIA**, **Mediatek**, and more. 

---

## 📸 Demo
<!--![GIF Demo](https://raw.githubusercontent.com/anmolksachan/anmolksachan.github.io/main/img/TTM.gif)-->
https://github.com/user-attachments/assets/e07155ed-52b5-45e4-91aa-297a5caeac3a

#### Note: This is just a demo and doesn't cover full potential of the tool.
---

## 🙌 Shoutouts

* [@nihitjain11](https://github.com/nihitjain11)
* [@Shivam Saraswat](https://github.com/shivamsaraswat)
* [@thecyberneh](https://github.com/thecyberneh$0)
* [PushkraJ99](https://github.com/PushkraJ99$0)

---

## 🌎 Community

1. [Simple Recon on Android using TheTimeMachine + Dirsearch (Medium)](https://alpinnnnnn13.medium.com/simple-recon-di-android-menggunakan-tools-thetimemachine-dan-dirsearch-3384aad17c15)
2. [Michel Kartner – YouTube](https://youtu.be/gh2DdRjK4BY?t=1888)
3. [@cyb\_detective’s Tweet](https://x.com/cyb_detective/status/1581324309108510721)

---

## 📬 Contact

DMs are open – reach out to me on [@FR13ND0x7F](https://twitter.com/fr13nd0x7f)

---

## ⭐️ Support

If this tool helped you, drop a star on the repo or follow me on Twitter — that’s all I ask 😄

---

## 👨‍💻 Author

Author: **Anmol K. Sachan** | Twitter/ X: [@FR13ND0x7F](https://x.com/fr13nd0x7f)
<br>Co-author: **Chaudhary\_S4h4b** | Twitter/ X: [@Chaudhary\_S4h4b](https://x.com/)

---

## ⚒️ Issues

Version 3.0 is under development. If you see any issues please open an issues and we are happy to take a look and fix that.
- `--menu` work is under progress you can directly use `--attack` instead.
- `--backup` needs to also output archieved URL simialr to [WayBackupFinder](https://github.com/anmolksachan/WayBackupFinder)

---
