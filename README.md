# ENT Prep — Final Professional MBBS

A working **static, browser-only ENT mock exam and practice app**. All 100 supplied draft questions are included in **demonstration mode**, not faculty-validated public examinations. No backend, login, remote database, tracking, or paid libraries.

## Run

Unzip the archive. In the `ent-mbbs-app` folder run:

```bash
python3 -m http.server 8080
```

Then open **http://localhost:8080** in your browser. Do not double-click `index.html` directly: browsers restrict loading JSON modules from `file://` URLs.

Node.js is required only to run the included automated tests:

```bash
node --test tests/*.test.mjs
```

Or `npm test`. No `npm install` required. Static deployment: upload the contents of the folder to Netlify, GitHub Pages, Cloudflare Pages, Vercel static hosting, or any ordinary static server. This application uses URL hash routes (`/#/exam/setup`) for compatibility with static hosts. Initial browser load must be online, but its service worker caches application files for subsequent offline use when served over HTTPS or localhost.

## Features

- Timed 15-minute mock with 5 MTF and 5 SBA stems; 10 marks total
- MTF individual statement True/False/blank, 0.2 per correct statement; SBA single correct option, 1 mark
- Draft demo mode and safe published-only mode (currently empty)
- Random seeded questions, no shared concept or variation group within an attempt
- Topic/difficulty/type filtered untimed practice, optional immediate feedback
- Question flags, navigator, partially answered states, review-before-submit
- Countdown persists across reload, resumes saved attempt, submits after expiry
- IndexedDB persistence of entire question/answer snapshots
- Results, explanations, topic performance, history and backup export/import
- Mobile-first layout and keyboard-friendly form controls

## Faculty approval and publication

`content/questions.json` is the static release source. To publish, review every relevant stem, key, option and explanation against current accepted references. Change only faculty-validated items to `"status":"approved"` and add `"published":true`. Update `content/manifest.json` with a new release ID, approved count and hash. Publish a separate build; published mode includes only items meeting **both** requirements. Keep old completed attempt snapshots unchanged.

To reconvert the originally supplied TXT pilot, run:

```bash
python3 scripts/convert-pilot.py /absolute/path/to/pilot.txt
```

This resets the package to the draft source; it is **not** an approval process.

## Operational limitations

All files, grading keys and code are browser-inspectable. This is not proctored or secure assessment; timers can be manipulated by advanced users. Browser data may be erased on site-data clearing, private mode or storage eviction. Export backups regularly; no cross-device sync. The proposed 10-question ENT-only format is **not** asserted to be an officially mandated separate exam. The source rulebook's future server-centric instructions are intentionally not implemented. See `DECISIONS.md`.


## Question bank revision v2.0
The included `content/questions.json` contains 1,191 structurally filtered draft candidates: 465 MTF and 726 SBA. `content/quarantined-questions.json` contains 309 excluded records for editorial investigation. The source revision preserved 1,500 original IDs, but did not medically verify any item. Published mode remains empty. Existing local exam attempts retain their frozen question snapshots. Because the web app uses a service worker, close other existing app tabs and reload after replacing deployed files; the cache name is updated to v2.

## v2.1 smartphone interface update
- Collapsible navigation menu on phones, rather than an overflowing navigation strip.
- Larger touch targets (minimum approximately 44–48px) for answers and navigation.
- Compact sticky examination timer and a progress indicator.
- Sticky Previous/Next controls near the bottom of the phone viewport.
- Collapsible question-number navigator to leave more room for question text.
- Refined layouts for 360–430px screen widths; safe-area support for modern phones.
- Preserves the 1,191 draft-candidate question bank, exam scoring, offline cache, and local history.


## v2.2 interface refresh
Removed repetitive alert banners and decorative blocks, simplified the home page and About page, and corrected checkbox sizing and topic-grid alignment. Underlying question bank status remains draft (not faculty approved).
