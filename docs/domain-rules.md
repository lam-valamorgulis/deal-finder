# Domain rules and invariants

Rules the app must always keep. Terms follow `GLOSSARY.md`.

Status values:
- **Decided Qn** — agreed in the grilling session, question n.
- **Research Rn** — wording comes from the research, accepted by the user (Q24).
- **From code** — kept from the old app, not reviewed again.
- **Unmeasured** — a default value, to be replaced by real data from the **Sổ giao dịch** or the **Tuần hiệu chỉnh**.

## Goal and scope

| # | Rule | Status |
|---|---|---|
| G1 | The main user is the **Người lướt hàng**. Build for them first. | Decided Q4 |
| G2 | **Khách dữ liệu giá** is a later product on the same data. Do not throw away data it would need. | Decided Q1, Q4 |
| G3 | iPhone is the main product line. The user adds other product lines in the app. | Decided Q7 |
| G4 | The project is first a learning project with a small income. Every step must be measurable. | Decided Q25 |
| G5 | The design must let a new **Phương án kinh doanh** (consignment, inbound buying, selling to shops, price data) be added without rewriting the core. | Decided Q25 |
| G6 | Build order: (1) price data collection and weekly price report, (2) call list and **Sổ giao dịch** for the **Tuần hiệu chỉnh**, (3) **Deal** alerts. | Decided Q26 |

## Actions outside the app

| # | Rule | Status |
|---|---|---|
| O1 | The app never sends anything to a seller and never posts on Chợ Tốt. The user does it. Reason: Chợ Tốt rules forbid spam and chat tools; automating a personal Zalo risks a ban. | Decided Q10, Research R1 |
| O2 | The app may draft a resale listing. The user decides to send it or not. | Decided Q10 |
| O3 | Alerts go only to the user's own channels. Telegram is the first channel. Zalo Bot Platform is tested as a second one. All channels sit behind one interface. | Decided Q10, Research R3 |

## Data collection

| # | Rule | Status |
|---|---|---|
| C1 | Only the public Chợ Tốt API (the data the website and app show), for the user's own use. No login. No private endpoints. No republishing or resale of raw tins. | Research R1 |
| C2 | One request at a time, at least 2 seconds apart. When blocked: slow down. After 5 blocks in a row: stop fully. | Research R1 |
| C3 | No rotating proxies. No CAPTCHA solving. No logged-in sessions. | Research R1 |
| C4 | Read only an allow-list of fields. Never read or store seller name, phone, avatar, account id, street address or GPS. Description text stays in memory only. Before text goes to an outside service, remove phone numbers and names. | Research R1 (personal data law, in force 2026-01-01) |
| C5 | Price data is collected nationwide, even outside the **Khu vực mua**. The buying area filters alerts, never collection. | Decided Q6 |
| C6 | Next to the keyword search, also collect all Apple phones with no keyword. Report weekly how many tins only one of the two found. | Research R4 |

## Comparing prices

| # | Rule | Status |
|---|---|---|
| P1 | A **Tin** is compared only with tins in its own **Nhóm so sánh**. | From code |
| P2 | A **Nhóm so sánh** needs at least 8 clean tins in the last 30 days before any alert. | From code |
| P3 | A tin with a sign of replaced parts, faults, bypass, lock or "đưa trước" goes to its own group and is never a **Deal**. A repair deal may come later as a separate, opt-in **Phương án kinh doanh**. | From code, Research R4 |
| P4 | "Cần mua" tins and tins with price 0 are never compared. | From code |

## Expected profit

| # | Rule | Status |
|---|---|---|
| E1 | **Giá bán lại**: the private tins first posted in the last 14 days, if there are 30 or more. Otherwise the older-tin price minus a cut (3% by default, 5% pessimistic). The dashboard shows which basis was used, how many tins, and the **Giá bỏ đi** in VND. | Research R4, cut Unmeasured |
| E2 | Cost = fixed amount per keyword (start 0.40M) + tax 1.5% of the sale price + holding cost 0.12% of the buying price per day + after-sale reserve 0.5–1% + hidden-risk reserve (2.4% if the **Checklist trước khi mua** is done, 5.9% if not or the seller has no history). | Research R4, all values Unmeasured |
| E3 | The **Sổ giao dịch** is the only source of real trade prices. After 20 closed trades its averages replace the defaults in E1 and E2. | Decided Q15, Research R4 |
| E4 | Lãi dự kiến is shown in three **Kịch bản lãi**: pessimistic, central, optimistic. Each uses three user-editable values: buy-side haggle, hidden-risk reserve, exit position. | Research R4 |

## Alerts

| # | Rule | Status |
|---|---|---|
| A1 | A **Deal** is only inside the **Khu vực mua**: a list of districts, each with the user's travel minutes. Alerts are ranked by travel minutes. Today: districts of TP Hồ Chí Minh. | Decided Q6, Research R4 |
| A2 | A **Deal** needs **Lãi dự kiến** in the central **Kịch bản lãi** ≥ the user's minimum per keyword. There is no fixed % threshold. A tin that pays only in the optimistic scenario goes to Gửi gộp as "có thể có lãi, chưa chắc". | Decided Q5, Research R4 |
| A3 | The **Rẻ bất thường** label only says the price is far too low (35% or more below). It never claims fraud. It always shows the **Checklist trước khi mua**. | Decided Q3, Research R4 |
| A4 | Only tins posted or pushed to the top in the last 6 hours can raise a new-tin alert. A re-pushed tin is marked **Đã đăng lâu**. | From code, Research R2 |
| A5 | Target: alert within 5 minutes of posting for hot models. The app logs the real alert delay and the first-call answer. Revisit after 30–50 real calls. Never faster than C2 allows. | Research R2, Unmeasured |
| A6 | **Gửi ngay**: a Deal with Lãi dự kiến ≥ 2 × the minimum, or a Rẻ bất thường tin, in the Khu vực mua. | Decided Q17 |
| A7 | **Gửi gộp**: other Deals in the Khu vực mua, as one summary every 1–2 hours. | Decided Q17 |
| A8 | **Chỉ lưu**: tins outside the Khu vực mua, or below the user's battery or cosmetic preference. Dashboard only. | Decided Q17 |
| A9 | The numbers in A6–A7 are set by the user in the app. | Decided Q17 |
| A10 | Every alert shows the **Checklist trước khi mua**. The selling checklist shows when a tin moves to Đã mua. | Research R4 |
| A11 | **Tin cũ — mặc cả** (experimental): a private, clean tin at least 5 days old, at or under the stale **Giá bỏ đi**, not Rẻ bất thường. Uses reserve 5.9% and 3 viewings. Goes to Gửi gộp and the weekly list, never Gửi ngay. Not called useful until 20 calls show how many stale tins are still for sale. | Research R4, Unmeasured |

## Listing stages

| # | Rule | Status |
|---|---|---|
| L1 | Stages: Mới → Đang theo dõi → Đã liên hệ → Đã mua → Đã bán. Any stage before Đã mua can go to Bỏ qua. | Decided Q18 |
| L2 | The app stores the price at every sighting of every tin in the Khu vực mua groups. It alerts on a **Tin theo dõi** when the price drops 5% or more, or when it is delisted. | Decided Q18, Research R2 |
| L3 | Moving to Đã liên hệ, Đã mua or Đã bán writes the **Sổ giao dịch**. | Decided Q18, Research R4 |

## AI boundary

| # | Rule | Status |
|---|---|---|
| I1 | Every money calculation (Lãi dự kiến, Giá bỏ đi, Mức ưu tiên) is done by fixed, tested code. No agent framework sits between the data and the Deal decision. | Decided Q19, Research R3 |
| I2 | AI may only read text (descriptions) and write text (resale drafts). It never decides a Deal. Text sent to an outside LLM has phone numbers and names removed. The LLM gets no tools and no database access. | Decided Q19, Research R3 |

## Price data product (later)

| # | Rule | Status |
|---|---|---|
| D1 | Keep the full history of asking prices, delisted tins and the **Sổ giao dịch**, nationwide. The raw tin history stays private. Selling price data needs written permission from Chợ Tốt or legal advice first. | Decided Q12, Research R1 |
