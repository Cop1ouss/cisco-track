# PRD: NETOPS IT Track

| | |
| --- | --- |
| **Owner** | Dajoni Gomez |
| **Status** | Ship → Maintain |
| **Phase color** | Ruby (in daily use) |
| **Live** | https://cop1ouss.github.io/cisco-track/ |

## Problem

Networking and sysadmin study material is scattered across Cisco NetAcad, Jeremy's IT Lab, Microsoft Learn and lab guides. Without one map, it's easy to skip topics, lose track of finished labs, and lose sight of how the pieces connect: home network → enterprise switching and routing → Active Directory.

## Goal

One self-paced curriculum that shows every module and lab in order, tracks what's done, and maps to the exams that matter: **CCNA 200-301 v1.1**, **AZ-800** fundamentals and **Cisco JCA**.

## Users

- **Me**, working toward CCNA and a sysadmin role.
- Anyone else on the same path who wants a free, structured tracker.

## Scope

**In:**
- 5 courses, 56 modules and 69 guided labs.
- Per-lab completion stored in `localStorage`.
- Search and filters.
- Keyboard shortcuts.

**Out:**
- Accounts or sync.
- Video hosting.
- A v2.0 CCNA content pass. That's a separate project after Feb 2027.

## Requirements

1. Runs from a single `index.html`, with no build step, no dependencies and no server.
2. Every module has an overview, objectives, key topics and at least one lab.
3. Progress persists across sessions in the same browser and never leaves the device.
4. Works on a phone and with the keyboard only (`/`, `0`–`4`, `Esc`).
5. Exam-retirement notices stay accurate. Each one is checked against the vendor's page before it's edited.

## Finish line

- Every lab in courses 1–3 and 5 checked off before I book CCNA.
- Course 4 labs reproduced in the [home lab](https://github.com/Cop1ouss/homelab).

## Risks

- **CCNA v1.1 retires Feb 2, 2027.** Mitigation: flag v2.0 differences in the README and plan the content pass separately.
- **Microsoft exams change.** AZ-800/801 → AZ-802. Mitigation: the README notice gets checked during the monthly project check-in.

---

<sub>© 2026 Dajoni Gomez · Uncook™ · part of the [journey log](https://cop1ouss.github.io/Cop1ouss/)</sub>
