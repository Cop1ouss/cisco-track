<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/readme/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset=".github/readme/banner-light.svg">
  <img alt="cisco-track" src=".github/readme/banner-dark.svg" width="100%">
</picture>

<p align="center">
  <a href="https://cop1ouss.github.io/cisco-track/"><img alt="Open the tracker →" src="https://img.shields.io/badge/Open%20the%20tracker%20%E2%86%92-89b4fa?style=for-the-badge&labelColor=1e1e2e"></a>
</p>
<p align="center">
  <img alt="CCNA 200-301" src="https://img.shields.io/badge/CCNA%20200--301-1e1e2e?style=flat-square&logo=cisco&logoColor=89dceb">
  <img alt="AZ-800" src="https://img.shields.io/badge/AZ--800-1e1e2e?style=flat-square&logo=microsoftazure&logoColor=89b4fa">
  <img alt="HTML" src="https://img.shields.io/badge/HTML-1e1e2e?style=flat-square&logo=html5&logoColor=fab387">
  <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-1e1e2e?style=flat-square&logo=javascript&logoColor=f9e2af">
  <img alt="MIT license" src="https://img.shields.io/badge/MIT%20license-1e1e2e?style=flat-square&logo=opensourceinitiative&logoColor=a6e3a1">
</p>

<p align="center">
  <img alt="Desktop view" src=".github/readme/screenshot-desktop.png" width="74%">
  &nbsp;
  <img alt="Phone view" src=".github/readme/screenshot-phone.png" width="21%">
</p>

A self-paced networking + systems administration curriculum tracker, built as a single-file interactive web app. Covers everything from home-network basics through enterprise switching/routing/automation to Windows Server Active Directory — aligned to **CCNA 200-301 v1.1**, **AZ-800**, and the **Cisco Junior Cybersecurity Analyst (JCA)** path.

## What's in here

| Course | Focus | Modules | Labs |
|---|---|---|---|
| **1. Networking Basics** | Home networks, Wi-Fi, IP fundamentals, basic security | 8 | 9 |
| **2. Networking Essentials** | OSI/TCP-IP, Ethernet, IPv4/IPv6 addressing & subnetting, DHCP, ARP, routing, TCP/UDP | 13 | 16 |
| **3. SRWE** (Switching, Routing & Wireless Essentials) | VLANs, inter-VLAN routing, Rapid PVST+, EtherChannel, HSRP, WLAN/WPA3, static routing | 16 | 22 |
| **4. Active Directory Foundations** | AD DS, DNS integration, OUs, GPOs, users/groups, domain-joined clients, helpdesk runbook | 9 | 9 |
| **5. ENSA** (Enterprise Networking, Security & Automation) | OSPFv2, AAA/VPN, ACLs, NAT, NTP/SNMP/Syslog, QoS, SDN, REST/Ansible automation | 10 | 13 |

**56 modules · 69 guided labs · ~269 hours** of self-paced content, each module with a written overview, learning objectives, key topics, and hands-on Packet Tracer / VirtualBox labs.

## Why a single HTML file

`index.html` is a self-contained progress tracker — no build step, no dependencies, no server. Open it in a browser, or use the live version on GitHub Pages:

- **Search & filter** every module by keyword, labs-only, CLI-only, or completion status
- **Per-lab completion tracking** saved to `localStorage` — progress persists across sessions on the same browser
- **Progress bars** per course and overall, updated live as labs are checked off
- Keyboard shortcuts: `/` to search, `1`-`4` to jump between courses, `0` for overview, `Esc` to close

Progress is stored locally in your browser only — nothing is sent anywhere, and clearing site data resets it.

## Using it

1. Open `index.html` directly, or visit the GitHub Pages link above.
2. Work through a course tab in order — each module has an overview, objectives, and one or more labs.
3. Click into a lab for the guided walkthrough, then mark it complete.
4. Courses 1–3 and 5 use **Cisco Packet Tracer** (free via the Cisco Networking Academy / Skills for All). Course 4 uses **VirtualBox** with a free 180-day Windows Server 2025 evaluation.

## Alignment

Content maps to **CCNA 200-301 v1.1** (the 2025+ exam blueprint — Rapid PVST+, WPA3, IaaS/PaaS/SaaS, cloud-managed networking) for courses 1–3 and 5, **AZ-800** (Windows Server hybrid administration) fundamentals for course 4, and the **Cisco Junior Cybersecurity Analyst (JCA)** Career Certificate.

> **AZ-800/AZ-801 were scheduled to retire on September 30, 2026** and consolidate into **AZ-802**. Course 4's content is still valid Windows Server hybrid-admin material either way; check Microsoft Learn for the current exam before you book.

> **CCNA 200-301 v1.1 retires February 2, 2027**, replaced by **v2.0** the next day. Confirmed against Cisco's own exam-topics PDF — v2.0 restructures the blueprint into five domains (not six) with a much heavier troubleshoot/diagnose emphasis, plus new topics (SFTP/SCP, storm control, RA guard, DNS-record troubleshooting, OSPFv3, agentic AI) not yet in courses 1–3/5. Courses 1–5 still target v1.1; a v2.0 content pass is a future project, not something in progress.

> **MS-900 (M365 Fundamentals) retired March 31, 2026** and can no longer be earned — dropped from the app's cert list entirely. Microsoft's loose successor is **AB-900** (Microsoft 365 Copilot and Agent Administration Fundamentals), confirmed live on Microsoft Learn but still in beta and scoped to Copilot/AI-agent admin, not general M365/Windows-Server fundamentals — not a direct swap-in for what MS-900 was doing here.

## Related

Same "Networking & Certs" category as [`ccna-tracker`](https://github.com/Cop1ouss/ccna-tracker)
(the hands-on/gamified test-prep companion to this repo's curriculum notes),
[`secplus-tracker`](https://github.com/Cop1ouss/secplus-tracker), and
[`subnet-calculator`](https://github.com/Cop1ouss/subnet-calculator).

## License

MIT — see [LICENSE](LICENSE).

---

<p align="center"><sub>Part of <a href="https://github.com/Cop1ouss">Uncook</a> · built off systems · © 2026 Dajoni Gomez</sub></p>
