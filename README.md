# ENT Prep v7.2

A static, mobile-friendly ENT MBBS question practice app organized into 19 clinical-card items.

## Start
From this folder:

```sh
python3 -m http.server 8080
```

Then open http://localhost:8080. Use a local web server rather than opening index.html directly.

## Modes
- Professional Mock: one tap from Home; 10 questions (5 MTF + 5 SBA), 15 minutes, 10 marks.
- Item Learning Mode: choose phase/item(s); untimed, immediate feedback that locks answered questions.
- Item Exam Mode: same item selection; 90 seconds per question, feedback after submission, detects when the tab becomes hidden and automatically submits.
- Item exam question format, count and difficulty preferences are saved in Settings. Default: both MTF and SBA, 10 questions, all difficulty levels.

## Safety and privacy
All progress stays within this browser. Export a backup in Settings before deleting browser data. Focus enforcement is a deterrent only and may be triggered by phone calls or other OS interruptions. Not a secure proctoring product.

See `QA_REPORT_v7_2.md` for validation and testing limitations.
