---
name: stage-map
description: Write a stage map for a study topic — source, knowledge checklist, tiered problems, code problems, answer key, and the vault frontmatter that wires it into the capability graph. Use when the user names a topic to study ("stage map for Markov chains", "/stage-map Bayes"), or asks to revise or re-scope an existing stage map.
---

# Writing a stage map

A stage map is **what to do** for one topic. The companion Feynman note is **what the user
understood** — the user writes that, never you (see `.claude/CLAUDE.md` §7).

Output goes to `stage_maps/<id>_<slug>.md`. Read [reference.md](reference.md) for the full
template and the rules behind each section.

## The rules that matter most

**One topic, one file. Do not split.** A topic that spans several sessions gets **parts** inside
one file, with a line telling the user to stop at a part boundary. Splitting into `a`/`b`/`c`
files was tried and reversed — it fragmented the answer key and forced cross-file references.

**Build the checklist from the source's real `##` headings**, with section numbers attached —
never from what interviews tend to ask. Open the book's table of contents, or ask the user to.
Anything interview-critical but outside the chapter is named explicitly as not-here, with where
it actually comes from.

**Name the source once: one book, named chapter, page or section range.** Multiple sources per
topic cost more time choosing than studying. If the material crosses chapters, say so at the top
and say why — a stage whose material isn't in the chapter it claims is a known failure mode.

**No scheduling, no sizing multipliers, no per-block minute tables.** One `est_h` in frontmatter
and one line of rough breakdown is all the user wants; they study when they have time.

**No project-internal vocabulary.** No stage IDs in prose or problem labels (`A1`, not
`F1.1a-A1`), no baseline question numbers, no adjustment numbers, no `D1`/`D2`/`D4` labels, no
references to other stages by ID. Write "the geometric distribution's derivation", not "`F1.4`-B4".
The file should read as a real document about a real subject.

## Steps

1. **Identify the topic** in `vault/topics/` — the 59 notes there index `topics/` 1:1. Read the
   matching note for `concepts:` and any `deferred:` list already recorded.
2. **Find the source.** Ross, Green Book, Hull, CLM — the user owns these; never recommend a new
   textbook. Get the real section headings before writing the checklist.
3. **Write the file** per [reference.md](reference.md).
4. **Create missing vault stubs.** Any `[[concept]]` or `[[application]]` in the frontmatter that
   has no note gets one — see reference.md for the stub shapes. This is what keeps the graph
   connected.
5. **Regenerate the capability map:** `python vault/build_capability_map.py`. It prints any
   dangling link; the count must be zero when you finish.
6. **Report** the estimate, the concepts wired, and any stub you created.
