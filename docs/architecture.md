# Architecture

How the app is built. Words follow `GLOSSARY.md`. Rule ids (C1, E2, A11…) point to `docs/domain-rules.md`.

## Decisions

| # | Decision | Why | Change later? |
|---|---|---|---|
| Q27 | Python | Price statistics and Vietnamese text reading. Research R3 found no tool that does this better. | Hard |
| Q28 | SQLite, reached only through one storage layer | One user, one machine, a few hundred tins a day. The storage layer lets us move to Postgres for the price-data product (G2). | Easy, if only the storage layer touches SQL |
| Q29 | Five modules with small interfaces (below) | Each rule has one owner. A new **Phương án kinh doanh** plugs into one place (G5). | Medium |
| Q30 | Telegram buttons to log calls; web dashboard for reports | The user logs a call on the phone, seconds after it ends. | Easy |
| Q31 | Run on the user's Mac while building. Then Oracle Cloud Always Free. Then a Vietnam VPS if Oracle has no capacity. | Free first (G4). Step 1 runs fine on a Mac. | Easy |
| I1–I2 | No agent framework. An LLM call, if any, only reads or writes text. | Money rules must be fixed and tested. | Hard |

## The system

```
Chợ Tốt                    App                                         User
───────                    ───                                         ────
public API ──▶ Collector ──▶ Catalog ──▶ Pricing ──▶ Alerts ──────────▶ Telegram
                   │            │           ▲           │
                   ▼            ▼           │           ▼
               ┌──────────────── Store (SQLite) ──────────────┐
               │ sightings · groups · ledger · settings · alerts│
               └──────────────────────────────────────────────┘
                   ▲                        │
                   │                        ▼
               Ledger ◀── Telegram buttons  Reports ──▶ web dashboard
               (còn / đã bán / giá chốt)    (weekly price report)
```

## Modules

Each module hides its details behind a small interface. Other modules call only that interface.

### 1. Collector — talks to Chợ Tốt

- **Job:** fetch tins, nationwide (C5), by keyword and by brand with no keyword (C6).
- **Owns rules:** C1–C4, C6. It is the only module that makes network calls to Chợ Tốt.
- **Interface:** `fetch(query) -> list[RawTin]`. A `RawTin` holds only allow-listed fields (C4).
- **Must not:** store a seller name, phone, account id or address; keep description text after the Catalog has read it.

### 2. Catalog — turns a tin into a Nhóm so sánh

- **Job:** read title, structured codes and description. Output the **Nhóm so sánh**, the condition flags (replaced parts, lock, bypass, "đưa trước"), battery %, cosmetic %, seller type (private / shop).
- **Owns rules:** P1, P3, P4.
- **Interface:** `classify(raw: RawTin) -> CatalogEntry`.
- **Note:** first version uses written rules, tested with real sentences. An LLM reader may be added later behind the same interface (I2). The old repo's rules have no license, so they are rewritten, not copied.

### 3. Pricing — all money calculations

- **Job:** **Giá bán lại** (E1), costs (E2), **Lãi dự kiến** in three **Kịch bản lãi** (E4), **Giá bỏ đi**, the Deal decision (A2), Rẻ bất thường (A3).
- **Owns rules:** E1–E4, A2, A3, P2. This is where I1 lives.
- **Interface:** `evaluate(entry, group_stats, settings) -> Evaluation`. Pure functions: no network, no database writes. Every rule has a test.
- **Business options (G5):** each **Phương án kinh doanh** is one `ProfitModel` with the same interface: `expected_profit(entry, group_stats, settings) -> Scenarios`. Flipping is the first model. Consignment uses a fee instead of a buying price. Adding an option = adding one model and its tests.

### 4. Alerts — who hears about it, and when

- **Job:** choose the **Mức ưu tiên** (A6–A9), the Khu vực mua filter and travel-time ranking (A1), new-tin vs stale-tin windows (A4, A11), the pre-buy checklist (A10). Send through a channel.
- **Owns rules:** A1, A4–A11, O3.
- **Interface:** `decide(evaluation, settings) -> Priority`, and `Channel.send(message)`. Telegram is the first `Channel`; Zalo is a second one later.

### 5. Ledger — the Sổ giao dịch and listing stages

- **Job:** keep each tin's **Trạng thái tin** (L1), the price at every sighting (L2), and every call, viewing, purchase and sale (L3, E3). Feed real numbers back to Pricing after 20 trades.
- **Owns rules:** L1–L3, E3, O1, O2.
- **Interface:** `record(event)` for button presses and stage changes; `calibration_report()` for the **Tuần hiệu chỉnh**.

### Shared parts (not domain modules)

- **Store:** the only code that knows SQL. Tables for sightings, groups, ledger, settings, alerts.
- **Scheduler:** runs the collect loop and the Gửi gộp summary on time.
- **Web:** dashboard pages for reports and settings (keywords, Khu vực mua, minimum profit, scenario values).

## Data kept

| Data | What it is | Rule |
|---|---|---|
| Sightings | Each time a tin is seen: price, time, group, seller type, district. No personal data. | L2, C4, D1 |
| Group stats | Daily median, P25, count per Nhóm so sánh; fresh (14-day) and older tins apart. | E1, P2 |
| Ledger | Calls, answers, prices said on the phone, prices at the meeting, purchases, sales, losses. | L3, E3 |
| Settings | Keywords, Khu vực mua with travel minutes, minimum profit per keyword, scenario values. | A1, A2, A9, E4 |
| Alerts | What was sent, when, at what priority, and the alert delay. | A5 |

## Tech stack (Q33)

| Job | Library | Why |
|---|---|---|
| Call the Chợ Tốt API | `httpx` | Small, enough for one request at a time (C2) |
| Dashboard | `FastAPI` + server-rendered HTML (Jinja) + `htmx` | No JavaScript build step. Easy for one person to change. |
| Telegram with buttons | `python-telegram-bot` | Inline buttons and multi-step replies built in |
| Scheduling | Own collect loop + `APScheduler` for the Gửi gộp summary | Simple |
| Styling | `Pico.css` as the base, plus our own design tokens | Clean defaults; our tokens make it look like one product |
| Tests, packaging | `pytest`, `uv` | Python standard |

## UI and UX (Q34–Q36)

### Principles

- **Phone and desktop both** (Q35). Phone: the user acts (reads an alert, logs a call). Desktop: the user studies (weekly report, ledger, settings).
- **Clean and good-looking, without a custom design phase** (Q36). Pico.css base. One accent colour. Light and dark mode.
- **Numbers first.** Prices use tabular figures, right-aligned, in VND with dot separators (14.450.000đ). Profit is green when positive, red when negative.
- **Vietnamese UI.** Domain words exactly as in `GLOSSARY.md`.
- **Tables become cards on a phone.** A desktop table row turns into one card with the 4 most important values on top.

### Telegram alert (Q34)

```
🟢 DEAL · Gửi ngay
iPhone 15 Pro Max 256GB VN/A · Pin 89% · Ngoại hình 98%
Giá rao 14.450.000đ · Giá bỏ đi 15.130.000đ
Lãi: xấu −0,9tr · giữa +0,67tr · tốt +2,0tr
📍 Quận 7 · ~25 phút · Cá nhân · đăng 12 phút trước
☑ iCloud · linh kiện · pin · khóa mạng · không cọc
[Mở tin] [Còn] [Đã bán] [Không nghe] [Bỏ qua]
```

(Example numbers.) Pressing **[Còn]** asks "Giá chốt qua điện thoại?". The user types `14200`; the bot writes the Ledger. One or two taps per log.

### Dashboard pages, by phase (Q35)

| Phase | Page | Phone view | Desktop view |
|---|---|---|---|
| 1 | Báo cáo giá tuần | One card per Nhóm so sánh: median, P25, count, trend arrow | Table of all groups, sortable, with a small trend line |
| 1 | Cài đặt từ khóa | Simple list with add / remove | Same, with filters per keyword |
| 2 | Báo cáo hiệu chỉnh | Median haggle, "còn" share, calls left to reach 20 | Same, plus the list of calls |
| 3 | Danh sách deal | Cards sorted by travel minutes | Table with the three scenarios |
| 3 | Sổ giao dịch | Cards per tin with its stage | Table with filters by stage and outcome |
| 3 | Cài đặt | Khu vực mua, minimum profit, scenario values | Same |

## Build phases (G6)

Each phase ends with something the user can see and measure (G4).

| Phase | Builds | Done when |
|---|---|---|
| 1. Price data | Collector, Catalog, Store, weekly price report | 7 days of nationwide iPhone data; the report shows median, P25 and count for each big group, fresh vs older; no personal data in the database. |
| 2. Calibration | Ledger, Telegram buttons, call list | The user logs 20 numeric `lowest_price` answers from the call list in one week; the report shows median haggle and the "còn" share. |
| 3. Deal alerts | Pricing, Alerts, settings pages | Alerts arrive with three scenarios and the checklist; alert delay is logged; first trades go into the Ledger. |

## Open items

- Does Chợ Tốt block requests from foreign servers (Oracle, GitHub)? Test before moving off the Mac.
- Zalo Bot: can it push messages after the first chat? (research open question 7)
- Oracle Always Free: free capacity is hard to get, and the free size was cut in 2026.
- All money values in E1, E2, A11 are **Unmeasured** until phase 2 and 20 trades.
