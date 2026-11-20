# ShipperFast: 180-second video script ("Vibe to Production")

Follows the submission guideline's five segments exactly. Every number below was read off the
live site (https://shipper-fast.vercel.app) on 20 Nov 2026; numbers on real-data screens change
with the data, so **read them off the screen when recording**. Scenario numbers are fixed.

Format per row: **screen → what to do** (cursor) → **say** (≈ 150 words per minute).

---

## 0:00–0:30 · Problem (the vibe): "This problem matters"

| Time | Screen → do | Say |
|---|---|---|
| 0:00 | `/welcome` (landing) for 2 s, then log in | "Garments are Bangladesh's biggest export, and they leave through one crowded port: Chattogram, about three and a half million containers a year." |
| 0:08 | **Control Tower**, data selector = *Today (estimated)*. Hover the KPI **Median time in port** | "Ships queue for days. Add a cyclone, a strike or a full yard, and orders miss their dates." |
| 0:16 | Hover **Yard occupancy** (NCT bar in red, ~196 %), then the **Brief** card | "Today, from public port data: about fifty hours median in port, one terminal at nearly double capacity. Exporters in Gazipur and pharma importers hear about it late, from a phone call." |

## 0:30–1:00 · Solution: "This is how we solve it"

| Time | Screen → do | Say |
|---|---|---|
| 0:30 | Still Control Tower. Slowly move the cursor down the left menu | "ShipperFast is an AI control tower for the Chattogram–Dhaka corridor. It reads news, hazard alerts, ship tracking and official tariff schedules…" |
| 0:42 | Point at the **LIVE / REPLAY** badges on the cards | "…maps which suppliers and orders depend on what, and recommends actions with a cost and a confidence." |
| 0:50 | Point at the **Data:** selector (top right) | "What makes it different: one place for port, suppliers, routes, factory quality and tariffs, and every number says where it came from. Live, replay, or synthetic. Never guessed." |

## 1:00–2:00 · Demo: "This is how it works" (input → AI → output)

| Time | Screen → do | Say |
|---|---|---|
| 1:00 | Data selector → **Cyclone shuts Chattogram + denim mill flood**. Control Tower: hover **Orders at risk: 96 orders, US$40M** | "Now a what-if, badged synthetic, fictional firms: a cyclone closes Chattogram and a denim mill floods. Ninety-six orders at risk." |
| 1:10 | **Disruption Radar** → click the event **Chattogram port suspends cargo handling…**. Hover **Confidence 67% → 86% fused**, then the green **HAZARD** chip, then a highlighted evidence span | "Input: five news reports. The AI turns them into one event. Alone that's sixty-seven percent confidence. The cyclone alert agrees, so fusion raises it to eighty-six. Every highlighted word is the evidence it used." |
| 1:25 | Scroll to **Export via BDMGL (recommendation)**. Hover **Expected value US$34.7K · Confidence 86 %**. *Do not click Accept on the live site* | "Output: a decision. Export through Mongla port: about thirty-five thousand dollars of expected value, after the extra freight." |
| 1:33 | **Supplier Network** → hover row **1 Chattogram port · HIGH · sole path for 140 orders · TTS < TTR** → click it → show **What if Chattogram port is disrupted?** | "The supplier graph finds single points of failure. Chattogram is the only path for a hundred and forty orders, and the network runs out of stock before the port recovers." |
| 1:44 | **Quality Lab** → hover lot **REJECTED**, then the **Lines** chart with the **ALARM** point (see note Q) | "On the factory floor, a vision model flags defects, the lot fails its inspection standard, and the order it blocks becomes a risk automatically." |
| 1:52 | Data selector → **Today**. **Tariff Monitor** → click the **26.5 %** cell (T-shirt → United States) | "And real tariff data: a cotton T-shirt from Bangladesh pays twenty-six and a half percent into the US, traced to the legal line." |

## 2:00–2:30 · AI approach: "This is real AI thinking"

| Time | Screen → do | Say |
|---|---|---|
| 2:00 | **Data & Models** → scroll to **Models** | "Each capability is its own AI pipeline, and each one must beat a simple baseline on held-out data before it ships." |
| 2:08 | **Ports & Vessels** → scroll to **C4 dwell and queue model** (the forecast fan) | "Port waits: LightGBM quantile models with conformal intervals, trained on twenty-six thousand real port calls. Eighteen percent better than the baseline for cargo ships." |
| 2:17 | Back to **Disruption Radar** evidence, or **Quality Lab** heatmaps | "News: an extractor checked by a local LLM that must quote its source. Defects: a DINOv2 vision model on CPU. A graph model and evidence fusion tie it together." |
| 2:25 | Point at **Noto Bangla labels on the map** (e.g. আনোয়ারা near Chattogram) | "Built for Bangladesh: local ports, rules and data, and the interface already renders Bangla." |

## 2:30–3:00 · Impact and next step: "We can build and scale this"

| Time | Screen → do | Say |
|---|---|---|
| 2:30 | Data selector → cyclone scenario. **Scenario Studio**: hover **Orders saved 2.2 · OTIF +1.6 pts · Net value US$98.4K** | "Same cyclone, with and without ShipperFast: two orders saved, on-time delivery up one point six, and ninety-eight thousand dollars net after the cost of acting." |
| 2:42 | Hover **Export one page (PDF)** | "On real 2023 to 2026 data, our alerts came thirty-four to fifty-three hours before Chattogram's worst day, and we publish the false alarms too." |
| 2:50 | Back to `/welcome` | "Next: Bangla news and interface, pilots with garment and pharma shippers, and more ports. ShipperFast: see the delay before it reaches your orders." |

Narration ≈ 450 words, just under 3 min at 150 words per minute: speak briskly. If you run long, cut the 1:52 tariff row
first (it can be a 3-second cut with no words) and then the 2:25 Bangla row.

---

## Guideline checklist (each mandatory item and where it is covered)

| Requirement | Where |
|---|---|
| 180 s, structured | Five segments with the guideline's own time boxes |
| Clear problem and user | 0:00–0:30: Chattogram, garment exporters in Gazipur, pharma importers |
| AI-native approach (LLM / RAG / Graph / ML) | 2:00–2:30: LLM-checked extraction, supplier graph, LightGBM + conformal, DINOv2 vision, evidence fusion |
| Basic system flow (input → AI → output) | 1:10–1:33: news reports (input) → fused event (AI) → costed reroute (output) |
| Demo / prototype | 1:00–2:00 on the deployed site |
| Bangla / localisation | 2:25 (Bangla map labels, local ports and rules) and 2:50 (Bangla news and UI next). Say only this: today Bangla is supported in rendering, not in news extraction |
| Impact (KPIs / outcomes) | 2:30–2:50: orders saved, OTIF, net value, alert lead time (K-03) |

## Facts behind the narration (be ready if asked)

| Claim | Source |
|---|---|
| ~3.41 M TEU in 2025 | Lloyd's List ranking via Dhaka Tribune (`docs/brief/01-product.md`) |
| 67 % → 86 % fused; Mongla EV US$34.7K; 96 orders / US$40M | Live site, cyclone scenario (synthetic) |
| 2.2 orders, +1.6 pts OTIF, US$98.4K net | Scenario Studio (synthetic), `docs/model-cards/nexus-studio.md` |
| 26,008 port calls; MAE 17.8 % better for cargo; 80 % band covers 81 % | `docs/model-cards/c4-port-dwell.md` (real GFW data, 2026 holdout) |
| 34–53 h lead (2 storm episodes, median 43.5 h); 3 of 7 alerts matched, 4 were false alarms | `docs/model-cards/nexus-backtest.md` |
| DINOv2-S on ONNX, CPU; ISO 2859-1 AQL | `docs/model-cards/c5-defect-intel.md` |
| US T-shirt 26.5 % = 16.5 % MFN + 10 % surcharge | Tariff Monitor (USITC, DS-TRADE-05) |

## Before you record (found while checking the live site)

1. **Refresh live data first** (port data showed "as of 17 Nov, stale"):
   `make cloud-refresh` (Docker), or record the real-data part right after the teammate's worker runs.
2. **Quality Lab images do not load on the live site** (note Q). The MVTec images are non-commercial and are
   kept off Render on purpose, and live upload is off there (512 MB). Options: record the Quality Lab clip from
   a local run (`make demo`), or cut to `docs/screenshots/quality-lab-v2-light.png` for the heatmaps. The lot
   board and the SPC chart do work live.
3. **Do not click Accept on the live site.** It writes to the shared database and cannot be reset there. To
   show the click, record locally and run `make golden` afterwards.
4. **Check Route Planner once** (Plan routes) before recording; it was not checked live. It is not in the
   main flow; use it only as extra footage.
5. **Use the scenario, not the real news list, for the radar.** A few real headlines are misclassified (e.g.
   a profit report tagged as a fire), which would distract.
6. **Wake the API 2 minutes before recording** (Render's free tier sleeps): open
   https://cportal-api.onrender.com/health.
7. Light theme, 1280 px window, browser zoom 100 %, bookmarks bar hidden, cursor highlight on.
