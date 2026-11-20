# ShipperFast: 180-second video script ("Vibe to Production")

Follows the submission guideline's five segments and time boxes. Every screen, label and number
below was checked on the live site (https://shipper-fast.vercel.app, logged in) on 20 Nov 2026.
Real-data numbers move with the data: **read them off the screen**. Scenario numbers are fixed.

**Pace:** about 375 words, roughly 135 words per minute: calm, with a short pause on each number.
That takes about 170 s of speech; the pauses fill the rest of the 180 s. Every row's words fit its time window.

**Labels used below:** the data picker at the top right is **Showing**; pages are in the left menu.

---

## 0:00–0:30 · Problem: "This problem matters"

| Time | Screen → do | Say |
|---|---|---|
| 0:00–0:10 | `/welcome` (landing page). Already logged in: no typing on camera | "Garments are Bangladesh's biggest export, and they leave through one crowded port: Chattogram, about three and a half million containers a year." |
| 0:10–0:17 | **Control Tower**, Showing = *Today (estimated)*. Hover the card **Median time in port, last 24 h** | "Ships queue for days. A cyclone, a strike or a full yard, and orders run late." |
| 0:17–0:30 | Hover the **LIVE** badge under the port map, then **Yard occupancy** (the red NCT bar, ~196 %), then the **Brief · Chattogram** card | "This is live, from the port authority's public data: fifty hours in port, one terminal near double capacity. Garment and pharma shippers hear about it late, by phone." |

## 0:30–1:00 · Solution: "This is how we solve it"

Quick montage, about 3 s per page, no clicks needed:

| Time | Screen → do | Say |
|---|---|---|
| 0:30–0:40 | Cut through **Ports & Vessels** → **Supplier Network** → **Disruption Radar** | "ShipperFast is an AI control tower for the Chattogram-to-Dhaka corridor. It reads news, hazard alerts, ship tracking and official tariff schedules," |
| 0:40–0:49 | Cut through **Tariff Monitor** → **Route Planner** (form only) → **Scenario Studio** | "maps which suppliers and orders depend on what, and recommends actions with a cost and a confidence." |
| 0:49–1:00 | Back on **Control Tower**: point at a **LIVE** and a **REPLAY** badge, then at **Showing** | "Port, suppliers, routes, quality and tariffs in one place, and every number shows its source: live, replay or synthetic. Never guessed." |

## 1:00–2:00 · Demo: "This is how it works" (input → AI → output)

| Time | Screen → do | Say |
|---|---|---|
| 1:00–1:10 | **Showing** → *Cyclone shuts Chattogram + denim mill flood*. Hover **Orders at risk (next 30 days): 96 orders, US$40M** and its **SYNTHETIC** badge | "Now a what-if, clearly marked synthetic: a cyclone closes Chattogram and a denim mill floods. Ninety-six orders at risk." |
| 1:10–1:25 | **Disruption Radar** → click **Chattogram port suspends cargo handling…**. The detail card opens below: scroll to it, hover **Confidence 67% → 86% fused**, the green **HAZARD** chip, then a highlighted word in **Evidence** | "Input: five news reports. The AI merges them into one event at sixty-seven percent confidence. A cyclone alert agrees, so fusion lifts it to eighty-six. Highlights show the evidence." |
| 1:25–1:34 | Scroll to **Export via BDMGL (recommendation)**; hover **Expected value US$34.7K** and **Confidence 86%**. Hover **Accept**, but don't click it on the live site | "Output: a decision. Export through Mongla: about thirty-five thousand dollars of expected value, after extra freight." |
| 1:34–1:47 | **Supplier Network** → hover row **1 · Chattogram port · HIGH · sole path for 140 orders · TTS < TTR** → click it; in the side panel hover **Survive vs recover if it fails**, then show **What if Chattogram port is disrupted?** Don't click **Run what-if** on the live site | "The supplier graph finds weak points. Chattogram is the only path for a hundred and forty orders worth fifty-eight million dollars, and stock runs out before the port recovers." |
| 1:47–2:00 | **Tariff Monitor** (works in any Showing mode) → click the **26.5%** cell (Men's knitted cotton T-shirt → United States); the detail card opens below: scroll to the rate bar, then **Compare origins** (Viet Nam 29%) | "Plus real tariffs: a Bangladeshi cotton T-shirt pays twenty-six and a half percent into the US, traced to its legal line. Vietnam pays twenty-nine, so that's an edge worth knowing." |

## 2:00–2:30 · AI approach: "This is real AI thinking"

| Time | Screen → do | Say |
|---|---|---|
| 2:00–2:07 | **Data & Models** → scroll to **Models** ("Each model ships with a baseline, a card and a time-based evaluation") | "Every model ships with a baseline, a model card and a test on held-out time." |
| 2:07–2:17 | **Ports & Vessels** → scroll to **C4 dwell and queue model**; hover **Departure windows that held: 85%** | "Port waits: LightGBM quantile models with conformal intervals, on twenty-six thousand real port calls. Eighty-five percent of departure windows held." |
| 2:17–2:26 | **Disruption Radar** (scenario) → the evidence highlights again | "News: rules plus a local LLM that must quote its source. A supplier graph and evidence fusion link it all." |
| 2:26–2:30 | Radar **Where** map: zoom on Bangladesh, where the label **বাংলাদেশ** shows | "Built for Bangladesh; it already renders Bangla." |

## 2:30–3:00 · Impact and next step: "We can build and scale this"

| Time | Screen → do | Say |
|---|---|---|
| 2:30–2:41 | **Scenario Studio** (cyclone scenario): hover **Orders saved 2.2**, **OTIF +1.6 pts**, **Net value of acting US$98.4K** | "Same cyclone, with and without ShipperFast: two orders saved, on-time delivery up one point six, ninety-eight thousand dollars net of costs." |
| 2:41–2:50 | Same page: hover the **With Nexus vs without** table, then **Export one page (PDF)** | "On real 2023-to-2026 data, alerts came thirty-four to fifty-three hours before Chattogram's worst day. We publish the false alarms too." |
| 2:50–3:00 | `/welcome`, then fade to an end card: **ShipperFast · shipper-fast.vercel.app** | "Next: Bangla news, pilots with garment and pharma shippers, more ports. ShipperFast: see the delay before it reaches your orders." |

If you run long, drop the tariff row's last sentence (1:47) and keep a 3-second silent cut of the matrix.

## On-screen captions (add in the editor; they help judges follow)

| Time | Caption |
|---|---|
| 0:00 | The problem: one port, every export |
| 0:30 | One AI control tower for the whole chain |
| 1:10 | INPUT: 5 news reports |
| 1:16 | AI: fusion 67% → 86% |
| 1:25 | OUTPUT: costed decision |
| 2:00 | Every model beats a baseline |
| 2:30 | Impact (synthetic scenario) |

---

## Guideline checklist (each mandatory item and where it is covered)

| Requirement | Where |
|---|---|
| 180 s, structured | Five segments with the guideline's time boxes |
| Clear problem and users | 0:00–0:30: Chattogram, garment exporters in Gazipur, pharma importers |
| AI-native approach (LLM / RAG / Graph / ML) | 2:00–2:26: LLM-checked extraction, supplier graph, LightGBM + conformal intervals, evidence fusion |
| Basic system flow (input → AI → output) | 1:10–1:34, with captions |
| Demo / prototype | 1:00–2:00, on the deployed site |
| Bangla / localisation | 2:26 (Bangla rendering) and 2:50 (Bangla news next). Claim only this: today Bangla is supported on screen, not in news reading |
| Impact (KPIs / outcomes) | 2:30–2:50: orders saved, OTIF, net value, alert lead time |
| Capabilities shown | C1 Network 1:34 · C2 Radar 1:10 · C3 Routes 0:40 · C4 Ports 2:07 · C6 Tariffs 1:47 · Nexus Studio 2:30. C5 Quality Lab cut by choice (its images can't be served on the live site) |

## Facts behind the narration (be ready if asked)

| Claim | Source |
|---|---|
| ~3.41 M TEU in 2025 | Lloyd's List ranking via Dhaka Tribune (`docs/brief/01-product.md`) |
| 96 orders / US$40M; 67% → 86% fused; Mongla EV US$34.7K; 140 orders via Chattogram | Live site, cyclone scenario (synthetic, fictional firms) |
| 2.2 orders, +1.6 pts OTIF, US$98.4K net | Scenario Studio (synthetic), `docs/model-cards/nexus-studio.md` |
| 26,008 real port calls; MAE 17.8% better than baseline for cargo; 80% band covers 81% on the test set | `docs/model-cards/c4-port-dwell.md` (GFW, 2026 holdout) |
| 85% of departure windows held (67 of 79) | Ports & Vessels, C4 replay snapshot (read off screen) |
| 34–53 h lead (2 storm episodes, median 43.5 h); 3 of 7 alerts matched, 4 were false alarms | `docs/model-cards/nexus-backtest.md` |
| US T-shirt 26.5% = 16.5% MFN + 10% surcharge; Viet Nam 29% | Tariff Monitor (USITC, DS-TRADE-05) |
| Chattogram sole path for 140 orders, US$57.7M | Supplier Network, cyclone scenario (synthetic) |

## Before you record

1. **Log in first**, so the video never shows typing.
2. **Don't click Accept or Run what-if on the live site.** Both write to the shared database and can't be
   reset there. To show the clicks, record locally and run `make golden` afterwards.
3. **Refresh live data first.** The port data showed "as of 17 Nov, stale". Run `make cloud-refresh`, or
   record right after the teammate's worker runs.
4. **Route Planner** appears only as the form in the montage. Test **Plan routes** once before using more of
   it; it wasn't checked live.
5. **Use the scenario for the radar**, not the real news list: a few real headlines are misclassified.
6. **Wake the API 2 minutes before recording** (Render's free tier sleeps):
   https://cportal-api.onrender.com/health
7. Light theme, 1280 px window, browser zoom 100%, bookmarks bar hidden, cursor highlight on.
