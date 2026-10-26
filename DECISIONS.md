# Decisions, deviations and faculty review

1. The developer prompt prioritizes a **frontend-only** app. The rulebook's server-authentication, server clock, centralized exam audit and answer-key withholding requirements cannot be guaranteed without a server. This app performs all grading in the browser, with a clear honesty disclaimer.
2. The preferred React/Vite/Dexie stack in the prompt is advisory. This implementation uses native ES modules, vanilla JavaScript and IndexedDB to remain zero-dependency, immediately executable, easy to deploy and review. It still includes distinct engine/storage/UI modules.
3. All 100 pilot items remain **draft**. Demonstration mode is labeled; published mode deliberately has no eligible questions until explicit approval and `published:true`.
4. The published-student mode toggle is available for evaluation, not restricted by authentication; it filters content, not access to browser keys.
5. The ENT-only 5 MTF / 5 SBA / 15-minute mock is a proposed educational approximation, not claimed as a separate official university rule.
6. Question order is 5 MTF then 5 SBA. Questions cannot repeat their concept or variation groups in the same exam. Soft novelty prioritizes groups not used in the most recent three completed mocks. Selected versions and keys are frozen inside attempt snapshots.
7. Scoring uses integer fifths, with no negative marks. Topic practice has its own denominator equal to the selected number of stems; practice does not count in mock averages.
8. The mock timer persists its start and deadline as wall-clock timestamps. This is good for ordinary refresh/recovery but does not resist deliberate system clock tampering. Multi-tab coordination is best-effort only.
9. Browser storage uses IndexedDB. User export and import validate basic structure; imports preserve existing IDs rather than overwriting. Imports are not faculty-approved content releases.
10. Automated unit tests cover bank format, seed determinism, selected concept uniqueness and exact scoring. Automated browser E2E infrastructure is not bundled; verify critical journeys on real mobile Safari/Chrome before broad release.
11. The student-facing bank is not independently clinically audited by this build. Faculty must validate keys, explanations, ambiguous stems and curricular blueprint before a published launch.


## v2.0 update
Selected `candidate_questions_draft.json` rather than `master_all_records_v2.json` for live demo selection; 309 quarantined records excluded. No draft record was promoted to approved. Original candidate fields and IDs retained. Updated topic labels to match revised topic taxonomy; existing saved exam snapshots remain unchanged. Bumped offline cache to v2 to reduce risk of stale bank.

## v2.1 mobile UI changes
Only presentation and navigation elements changed. No question keys, eligibility rules, grading weights, attempt formats or storage schemas were altered. A service-worker cache version bump forces an update of cached UI assets after reload. Small-screen exam navigation uses a collapsible question navigator and sticky bottom actions.
