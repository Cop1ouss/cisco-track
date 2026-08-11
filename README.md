# NETOPS // IT Track

A self-paced networking + systems administration curriculum tracker, built as a single-file interactive web app. Covers everything from home-network basics through enterprise switching/routing/automation to Windows Server Active Directory — aligned to **CCNA 200-301 v1.1**, **AZ-800**, and the **Cisco Junior Cybersecurity Analyst (JCA)** path.

**[Open the tracker →](https://cop1ouss.github.io/cisco-track/)** *(enable GitHub Pages on this repo to activate — see below)*

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

`index.html` is a self-contained progress tracker — no build step, no dependencies, no server. Open it in a browser (or host it on GitHub Pages) and it just works:

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

### Enabling GitHub Pages

Repo → **Settings → Pages → Source: Deploy from a branch → `main` / `(root)`**. The tracker will be live at `https://cop1ouss.github.io/cisco-track/`.

## Alignment

Content maps to **CCNA 200-301 v1.1** (the 2025+ exam blueprint — Rapid PVST+, WPA3, IaaS/PaaS/SaaS, cloud-managed networking) for courses 1–3 and 5, **AZ-800** (Windows Server hybrid administration) fundamentals for course 4, and the **Cisco Junior Cybersecurity Analyst (JCA)** Career Certificate.

> **AZ-800/AZ-801 retire September 30, 2026** and consolidate into **AZ-802**. Course 4's content is still valid Windows Server hybrid-admin material either way, but if you're certifying after that date, target AZ-802 instead of AZ-800.

## License

MIT — see [LICENSE](LICENSE).
