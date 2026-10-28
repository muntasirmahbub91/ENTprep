# ENT Prep v7.2 — Release QA

## Changes
- Home starts a Professional Mock directly (10 questions: 5 MTF + 5 SBA, 15 minutes).
- Item Exams: Learning / Exam toggle at top, collapsible 3rd/4th phase lists, multi-item selection.
- Settings: saved defaults (both formats, 10 questions, all difficulties), inventory by clinical-card item, detailed mode descriptions.
- Learning Mode: untimed, app/tab switching allowed, immediate feedback on question completion; answer locks when feedback appears.
- Exam Mode: 90 seconds per question, deferred feedback, browser visibility-change detection and automatic finalization when hidden.
- Mock: unchanged marking, strict focus detection, original deadline retained after refresh.
- Corrected Item Exams review navigation and improved SBA answer review; detailed answer review collapsible.
- Kept existing question bank, eligibility filtering, local attempts, history and backup import/export.

## Testing
- `node --check app.js` succeeded.
- `npm test` 13 of 13 tests passed. These are question-bank and scoring/selection tests, not full browser E2E.
- Attempted browser E2E; local server request returned `net::ERR_BLOCKED_BY_ADMINISTRATOR` in the provided browser environment. Visual and device E2E testing **not completed**.
- Focus enforcement relies on `visibilitychange`; it cannot physically block apps, detect second devices or prevent tampering in a client-side application. Phone calls, notifications, tab changes and operating system actions may cause false-positive interruptions.
- Existing bank clinical content remains unchanged. No independent faculty approval is implied.

## Startup
`python3 -m http.server 8080` from the `ent-mbbs-app` directory, then open `http://localhost:8080`.
