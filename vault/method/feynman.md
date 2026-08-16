# The Feynman Protocol

The reason "I learned this before but forgot" happens: steps 1–2 (read, take notes) got done and
3–4 (explain, hunt gaps) got skipped. The gaps never found are exactly where memory decays first.

Encoding method only. The *schedule* that fights forgetting is the review ladder in
[[progression|progression.md]].

---

## The four steps

**1 — Learn.** One source, named chapter and page range. Cap input at ~40% of the topic's hours.
Sparse notes: formulas and one worked example, never a transcription.

**2 — Teach back, from memory.** Close the source. Write `progress/feynman_notes/<id>_<slug>.md`
as if teaching a smart 15-year-old. Define every term in the paragraph that uses it — "martingale"
is not an explanation, "a process whose expected future value given everything known now equals
its current value" is.

**3 — Hunt gaps.** Reread what was written. Every "obviously", "by symmetry", "it follows that",
and every place a concrete number wouldn't come → mark `⚠️ GAP:`. Fill *only* those, in place.

This is the step everyone skips and the only one that pays. `F1.5` closed after three rounds and
the finding was that every remaining gap was a derivation never done, not a page never read —
**recall errors come from unworked problems.**

**4 — Compress.** Napkin version, worked number, where it breaks.

---

## The note

Seven sections. §3 and §5 are what gets recalled cold in an interview, so errors there outrank
everything else in review.

| § | Section | What goes in it |
|---|---|---|
| 1 | Teach-back | From memory, no jargon shortcuts |
| 2 | Gaps found & filled | The `⚠️ GAP:` list, each one resolved |
| 3 | Napkin version | ≤200 words, speakable in 90 seconds |
| 4 | Where I'd actually meet this | The real interview question. **Not an analogy** — a supplied analogy is one more sentence to memorise; the user's own PCA/portfolio answers beat any of them |
| 5 | Summary table | The formulas, cold |
| 6 | Where this breaks | ≥2 assumptions + failure modes |
| 7 | Links | Related topics, solvers, problems solved |

## Done means

- [ ] All seven sections have real content, not `TODO`
- [ ] Zero remaining `⚠️ GAP` markers
- [ ] Napkin version ≤200 words, said out loud once
- [ ] The numerical example runs and produces the number it claims
- [ ] "Where this breaks" lists ≥2 items

Unchecked box = not complete, however many problems got solved. Grading honestly includes
grading "not finished" — `F1.4` closed as PARTIAL with 6 of 10 boxes failing, and saying so
plainly was worth more than a pass.

---

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Copying formulas out of the book | Close it first. From memory only. |
| "It's obvious" | It's a gap. Mark it. |
| Skipping step 4 because "I get it" | Then 200 words takes 10 minutes. Do it. |
| A 3000-word note | Transcribing, not teaching. Cut it. |
| Input exhausted, no next action | That's drift. Log the gap, switch to problems on paper. |
