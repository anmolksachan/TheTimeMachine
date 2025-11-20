---

# 🚀 TheTimeMachine v3.0 - Weaponizing Wayback for Recon, BugBounties, OSINT & More!

![image](https://github.com/user-attachments/assets/e99eb95e-f46e-4b97-8d2a-83bac89d0447)

You’ve heard of time travel in movies and comics, right? Well, this isn’t fiction anymore 😎. *TheTimeMachine* lets you dig through the past of any web app by scraping archived URLs from the Wayback Machine — and helps you find sensitive, forgotten, or deprecated endpoints for further exploitation.

Whether you’re into bug bounty, red teaming, or just love good ol’ recon, this tool was built to make my recon workflow faster, cleaner, and more effective. No more juggling multiple scripts — TheTimeMachine does it all in one shot.

---

## 🧩 Featured At

| Conference        | Year | Track / Showcase         |    |
|-------------------|------|---------------------------|---|
| [Defcon33- Las Vegas, NV](https://defcon.org/html/defcon-33/dc-33-demolabs.html#content_60874) | 2025 | Demo Labs | <img width="225" height="224" alt="image" src="https://github.com/user-attachments/assets/74fc8406-70eb-4b50-a42b-60af6a62cd34" /> |
| [BSides Mumbai](https://www.linkedin.com/feed/update/urn:li:activity:7339908506176618497/) | 2025 | Tools Arsenal Showcase |<img width="225" height="224" alt="image" src="https://github.com/user-attachments/assets/b5c1937d-d7bb-49e1-9bc3-6166102a2781" />|
| [OSINT Conference](https://osintconference.com/speakers) | 2025 | OSINT Conference | <img width="225" height="224" alt="image" src="https://github.com/user-attachments/assets/eba9502f-047e-42b7-ab7d-c3154a4acc11" /> |
| [Null Bangalore × OWASP Bangalore](https://www.linkedin.com/feed/update/urn:li:activity:7389327666564263936/) | 2025 |  [Monthly Meetup](https://www.meetup.com/owasp-bangalore-chapter/events/311891197/?eventOrigin=group_past_events) | <img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/28ed864b-eb4d-48fe-8412-7da576e0e899" />|
| [Bsides Delaware](https://bsidesdelaware.com/) | 2025 |  Conference | <img width="225" height="224" alt="image" src="https://github.com/user-attachments/assets/e922c068-4e00-4a42-a871-cf720ba78aab" />|
| [Announcing Soon!](#) | 20XX | Announcing Soon! | <img width="225" height="224" alt="image" src="https://comb.io/p4hBRB.gif" />|


---

## 💡 What It Does

This isn't just another Wayback scraper. Here's what TheTimeMachine brings to the table:

- 🔎 **Archived URL Fetching** – Pull historical URLs from Wayback Machine.
- 💾 **Backup File Detection** – Find `.zip`, `.bak`, `.sql`, `.tar.gz`, `.old`, and other juicy files.
- ⚙️ **Historical Backups** - Looks for historical backups for the identified backup files.
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

## 📝 Blogs

1. [The Time Machine — Weaponizing WaybackUrls for Recon, BugBounties , OSINT, Sensitive Endpoints and what not v1.0](https://medium.com/@anmolksachan/the-time-machine-weaponizing-waybackurls-for-recon-bugbounties-osint-sensitive-endpoints-and-40889a03feeb)
2. [Time Traveling for Bugs: How The Time Machine v3.0 Uncovered an XSS on REDACTED.com](https://medium.com/@anmolksachan/time-traveling-for-bugs-how-the-time-machine-uncovered-an-xss-on-redacted-com-92e3662a50e4)
3. [How “The Time Machine v3.0” Landed Me in the CERT-In Hall of Fame](https://anmolksachan.medium.com/how-the-time-machine-v3-0-landed-me-in-the-cert-in-hall-of-fame-5d356ad34911)

---


## 🌎 Community

1. [Simple Recon on Android using TheTimeMachine + Dirsearch (Medium)](https://alpinnnnnn13.medium.com/simple-recon-di-android-menggunakan-tools-thetimemachine-dan-dirsearch-3384aad17c15)
2. [Michel Kartner – YouTube](https://youtu.be/gh2DdRjK4BY?t=1888)
3. [@cyb\_detective’s Tweet](https://x.com/cyb_detective/status/1581324309108510721)
4. [@cyb\_detective’s Tweet v3.0](https://x.com/cyb_detective/status/1943789270726324606)
5. [The Ultimate Guide to the Time Machine Way Back URL Crawler for OSINT](https://www.youtube.com/watch?v=eguWHDfV-W0)
6. [OSINT resources](https://sizeof.cat/post/osint-resources/)
7. [Cyber Detective's OSINT tools collection](https://github.com/cipher387/osint_stuff_tool_collection)
8. [Unlock the Full Potential of the Wayback Machine for Bug Bounty](https://infosecwriteups.com/unlock-the-full-potential-of-the-wayback-machine-for-bug-bounty-8b6f57e2637d)
9. [TheTimeMachine for Bug Bounties & OSINT](https://medium.com/@XEyeSecurity/thetimemachine-for-bug-bounties-osint-39bded4bc78f)

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
- `listings` enhanced detection capability with aggresive mode.

---
