---
type: stage
id: R.linalg
name: Linear Algebra Refresher
kind: refresher
multiplier: 1.2
topic: "[[VII-1-core-linear-algebra]]"
concepts: ["[[psd-covariance]]"]
roles: ["[[portfolio-construction]]", "[[signal-research]]"]
sprint: S15
status: ready-for-test
budget_h: 3
actual_h: 3.5
d4_due: 2026-08-15
baseline_closes: [VII.1, VII.2]
---

# Linear Algebra Refresher — Problem Set
`stage: R.linalg` · **Sprint 15, Day 10 (Thu 2026-07-30)** · **Budget: 3h in three blocks**

**Why this stage exists:** baseline VII.1 gave you `[[2,1],[1,2]]` and you produced the
*definition* of an eigenvalue but not the numbers (correct: 1 and 3). VII.2 (PSD) scored 1.
Those two gaps sit directly under PCA (S20), the covariance matrix in every risk model you
will ever touch, Cholesky sampling for correlated Monte Carlo, and the Markowitz derivation
you already met via Lagrange in R.calculus. This is the "computation forgotten" stage — you have
the concepts, you need the hands.

**Scope — three things only:**
1. Eigenvalues + eigenvectors by hand, 2×2 and 3×3, via the characteristic polynomial
2. Positive semi-definite: three equivalent definitions, and how to test
3. Why a covariance matrix is always PSD

Out of scope (they belong to later stages, do not chase them): SVD, QR, LU, Sherman-Morrison,
matrix exponentials, power iteration, condition numbers. PCA proper is S20 — you are building
its foundation here, not doing it. `topics/section_VII_linear_algebra.md` is the advanced
backlog, not this.

---

## Source — one book, one sitting

| Source | Covers | Time |
|---|---|---|
| **Green Book (Zhou), Ch. 2 — the Linear Algebra section** | All three topics, in interview register | **40 min, hard stop** |

Look for the headings on **eigenvalues/eigenvectors** and **positive definite/semi-definite
matrices**. Section numbering shifts between printings, so navigate by heading, not by number —
and note the real page range here once you find it: `pp. ____`.

**If Green Book's eigenvalue treatment is too terse** (it is written for people revising, not
learning), the single named fallback is **3Blue1Brown *Essence of Linear Algebra* ep. 14
("Eigenvectors and eigenvalues"), 17 min**. That is the *only* video in this stage. Do not
open ep. 1–13. If you find yourself queuing videos, that is the failure mode this stage was
restructured to kill.

**Input cap: 40 min.** Feynman Step 1 is ≤40% of stage time. Everything after that is your
own pen.

---

## The three-block shape

Your measured prime hours are 08–09 and the evening, with light-afternoon scrap. This stage is
built to break cleanly at the hour — no block depends on finishing the previous one mid-thought.

| Block | When | Do | Out |
|---|---|---|---|
| **1** | 08:00–09:00 | Read (40 min, hard stop) → close the book → start §1 teach-back | Teach-back drafted |
| **2** | afternoon scrap, 30–45 min | Tier A, on paper, closed-book | A1–A5 done |
| **3** | evening, 60 min | Gap-hunt §1 · Tier B · §3–§6 · numerical anchor | Note closed |

Note skeleton: `progress/feynman_notes/R_linear_algebra.md`

---

## Tier A — the floor (all five, unhinted, on paper)

**R.linalg-A1.** Find the eigenvalues of `A = [[2,1],[1,2]]` by hand. Write out `det(A − λI) = 0`
explicitly, expand to the characteristic polynomial, solve. Then find an eigenvector for each
eigenvalue.
*This is baseline VII.1. Answer: λ = 1, 3. If you cannot do this cold, the stage is not complete.*

**R.linalg-A2.** For a general `2×2` matrix `[[a,b],[c,d]]`, show that the characteristic polynomial
is `λ² − (a+d)λ + (ad−bc) = 0`. Name the two coefficients — you have met both before.
*Then use it to shortcut A1 in one line.*

**R.linalg-A3.** Find the eigenvalues of `B = [[4,1],[2,3]]`. Not symmetric, so check: are the
eigenvectors still orthogonal? Compare with A1 and say what changed.

**R.linalg-A4.** Find the eigenvalues of the `3×3` matrix `C = [[2,0,0],[0,3,4],[0,4,9]]` by hand.
*Hint: it is block-diagonal — exploit that rather than expanding a full cubic. Recognising
structure before grinding is itself the skill being tested.*

**R.linalg-A5.** State three equivalent conditions for a symmetric matrix to be positive
semi-definite. Then test `[[2,1],[1,2]]` and `[[1,2],[2,1]]` — one is PSD, one is not. Say which,
and show it two different ways.

---

## Tier B — the target (≥3 of 5)

**R_linear_algebra-B1.** Prove that any covariance matrix `Σ` is PSD.
*Start from `xᵀΣx` and turn it into the variance of something. One line of algebra, and it is
the single most-asked linear-algebra question in a QR interview. If you get one thing from this
stage, get this.*

**R_linear_algebra-B2.** Show that a real symmetric matrix has real eigenvalues. Then show eigenvectors
belonging to distinct eigenvalues are orthogonal.
*The second half is two lines from `Av₁ = λ₁v₁`, `Av₂ = λ₂v₂`. The first half is harder — if
it stalls, note the stall and move on; the orthogonality result is the one that matters
downstream.*

**R_linear_algebra-B3.** `Σ = [[0.04, 0.01], [0.01, 0.09]]` — the covariance matrix from R_calculus-C2. Find its
eigenvalues by hand. What fraction of total variance does the largest explain?
*That fraction is the "explained variance ratio" of the first principal component. You have
now done PCA on two assets without calling it that.*

**R_linear_algebra-B4.** A correlation matrix for three assets with every pairwise correlation `ρ`. Write it
down. For which `ρ` is it a valid (PSD) correlation matrix?
*Answer is not `[−1,1]`. Worth knowing why: this is exactly the trap in hand-specified
correlation matrices, and why risk systems reject them.*

**R_linear_algebra-B5.** If `Σ` is PSD, show `Σ = BᵀB` for some `B`. Then say what this buys you when you
want to simulate correlated random variables.
*This is Cholesky's reason for existing. You will use it in S25 and in every multi-asset
Monte Carlo.*

---

## Tier C — only if A+B ran short

**R_linear_algebra-C1.** Trace and determinant equal the sum and product of eigenvalues. Verify on A1 and A4,
then explain why this gives a free sanity check on any hand computation.

**R_linear_algebra-C2.** `[[1,1],[0,1]]` has a repeated eigenvalue. How many linearly independent
eigenvectors does it have? What breaks?
*This is a defective matrix — the case where diagonalisation fails.*

---

## Deliverables

- [ ] `progress/feynman_notes/R_linear_algebra.md` — all 6 sections real, zero `⚠️ GAP`,
      napkin ≤200 words **said out loud once**
- [ ] Tier A A1–A5 unhinted, on paper
- [ ] ≥3 of 5 Tier B
- [ ] **Numerical anchor:** eigenvalues of `[[2,1],[1,2]]` by hand → verify with
      `np.linalg.eig`. Confirm you get `1` and `3`, and check the eigenvectors match yours up
      to scale *(numpy normalises to unit length and may flip the sign — if your answer differs
      by a factor, that is not an error; say why in the note)*
- [ ] **Unlock test:** re-answer baseline VII.1 and VII.2 cold. Both fully correct.

**No solver files this stage.** The `np.linalg.eig` check is three lines, inline in the note.
`src/solvers/` gets created when the Monte Carlo verifiers need it.

---
---

# ANSWER KEY — do not read until you have attempted

<details>
<summary>Tier A</summary>

**A1.** `det([[2−λ, 1],[1, 2−λ]]) = (2−λ)² − 1 = 0` → `λ² − 4λ + 3 = 0` → `(λ−1)(λ−3) = 0` →
**λ = 1, 3**.
For `λ=3`: `(A−3I)v = [[−1,1],[1,−1]]v = 0` → `v₁ = v₂` → **`v = (1,1)`**.
For `λ=1`: `[[1,1],[1,1]]v = 0` → `v₁ = −v₂` → **`v = (1,−1)`**.
Note `(1,1)·(1,−1) = 0` — orthogonal, as the spectral theorem guarantees for symmetric `A`.
Reading it geometrically: `A` stretches by 3 along `(1,1)` and leaves `(1,−1)` alone.

**A2.** `det([[a−λ, b],[c, d−λ]]) = (a−λ)(d−λ) − bc = λ² − (a+d)λ + (ad − bc)`.
The coefficients are **trace** (`a+d`) and **determinant** (`ad−bc`). So for any 2×2:
`λ² − tr(A)λ + det(A) = 0`.
A1 in one line: `tr = 4`, `det = 3` → `λ² − 4λ + 3 = 0` → `λ = 1, 3`. ✓
Consequence worth keeping: `λ₁ + λ₂ = tr`, `λ₁λ₂ = det`.

**A3.** `tr = 7`, `det = 4·3 − 1·2 = 10` → `λ² − 7λ + 10 = 0` → **`λ = 2, 5`**.
Eigenvectors: for `λ=5`, `[[−1,1],[2,−2]]v = 0` → `v = (1,1)`. For `λ=2`,
`[[2,1],[2,1]]v = 0` → `v = (1,−2)`.
`(1,1)·(1,−2) = −1 ≠ 0` — **not orthogonal**. Orthogonality of eigenvectors is a consequence
of *symmetry*, not of being a matrix. Lose symmetry, lose the guarantee (and in general lose
the guarantee of real eigenvalues too).

**A4.** Block-diagonal: the `1×1` block `[2]` and the `2×2` block `[[3,4],[4,9]]`. Eigenvalues
of a block-diagonal matrix are the union of the blocks' eigenvalues, so `λ = 2` plus the roots
of `λ² − 12λ + (27−16) = λ² − 12λ + 11 = 0` → `(λ−1)(λ−11) = 0`.
**λ = 1, 2, 11.** Sanity check: sum `= 14 = tr(C) = 2+3+9`. ✓
Expanding the full cubic gets the same answer and takes five times as long.

**A5.** For symmetric `A`, these are equivalent:
1. `xᵀAx ≥ 0` for all `x` *(the definition)*
2. all eigenvalues `≥ 0`
3. `A = BᵀB` for some `B`
*(and for PSD specifically, all principal minors `≥ 0` — note Sylvester's leading-minors test
gives positive **definite**; PSD needs all principal minors, not just leading ones. A common
interview trip-up.)*

`[[2,1],[1,2]]`: eigenvalues `1, 3` — both `> 0`, so **PD** (hence PSD). Second way:
`xᵀAx = 2x₁² + 2x₁x₂ + 2x₂² = (x₁+x₂)² + x₁² + x₂² ≥ 0`. ✓

`[[1,2],[2,1]]`: `tr = 2`, `det = 1−4 = −3` → `λ² − 2λ − 3 = 0` → `λ = −1, 3`. Negative
eigenvalue → **not PSD**. Second way: `x = (1,−1)` gives `xᵀAx = 1 − 4 + 1 = −2 < 0`. ✓
*(Fast tell: `det < 0` for a 2×2 means eigenvalues have opposite signs, so it cannot be PSD.)*

</details>

<details>
<summary>Tier B</summary>

**B1.** Let `Σ = Cov(R)` for a random vector `R`, and let `x` be any fixed vector. Then

`xᵀΣx = xᵀE[(R−μ)(R−μ)ᵀ]x = E[xᵀ(R−μ)(R−μ)ᵀx] = E[(xᵀ(R−μ))²] = Var(xᵀR) ≥ 0`

because a variance is a mean of squares. **`xᵀΣx` is the variance of the portfolio with weights
`x`** — that is the whole content of the result. A covariance matrix cannot fail to be PSD,
because a portfolio cannot have negative variance. It is PSD rather than PD because a portfolio
can have *zero* variance (perfectly hedged, or a redundant asset) — which is exactly the
degenerate case that makes `Σ` singular and blows up naive Markowitz.

**B2.** *Real eigenvalues:* take `Av = λv` with possibly complex `v`. Then
`v*ᵀAv = λ(v*ᵀv)`. Conjugate-transpose it: `v*ᵀAᵀv = λ̄(v*ᵀv)`, and `Aᵀ = A` real symmetric, so
the left sides agree → `λ(v*ᵀv) = λ̄(v*ᵀv)`. Since `v*ᵀv > 0`, `λ = λ̄`, so `λ` is real.

*Orthogonality:* `Av₁ = λ₁v₁`, `Av₂ = λ₂v₂`, `λ₁ ≠ λ₂`. Then
`v₂ᵀAv₁ = λ₁(v₂ᵀv₁)` and also `v₂ᵀAv₁ = (Av₂)ᵀv₁ = λ₂(v₂ᵀv₁)` using symmetry.
Subtract: `(λ₁ − λ₂)(v₂ᵀv₁) = 0`, and `λ₁ ≠ λ₂` forces **`v₂ᵀv₁ = 0`**.
This is the spectral theorem's engine, and it is why PCA's components come out orthogonal for
free rather than by construction.

**B3.** `tr = 0.13`, `det = 0.04·0.09 − 0.01² = 0.0036 − 0.0001 = 0.0035`.
`λ² − 0.13λ + 0.0035 = 0` → `λ = (0.13 ± √(0.0169 − 0.014))/2 = (0.13 ± √0.0029)/2`.
`√0.0029 ≈ 0.05385` → **`λ ≈ 0.09193, 0.03807`**.
Largest explains `0.09193 / 0.13 ≈ **70.7%**` of total variance.
*(Total variance = sum of eigenvalues = trace. That identity is why "explained variance ratio"
is `λₖ/Σλ` — a fact you now have from first principles rather than from a scikit-learn
docstring.)*

**B4.** `R = [[1,ρ,ρ],[ρ,1,ρ],[ρ,ρ,1]]`. This is `(1−ρ)I + ρ𝟙𝟙ᵀ`, whose eigenvalues are
`1 + 2ρ` (once, eigenvector `(1,1,1)`) and `1 − ρ` (twice, the plane orthogonal to it).
PSD needs both `≥ 0`: `ρ ≤ 1` and `ρ ≥ −1/2`. So **`ρ ∈ [−1/2, 1]`**.
Three assets cannot all be strongly mutually negatively correlated — if A and B both move
against C, A and B must move *together*. Generally for `n` assets the floor is `−1/(n−1)`,
tightening toward 0 as `n` grows. This is why risk systems reject hand-typed correlation
matrices, and why practitioners "repair" them by flooring negative eigenvalues at zero.

**B5.** Diagonalise: `Σ = QΛQᵀ` with `Λ ≥ 0`, so `√Λ` is real. Take `B = √ΛQᵀ`, then
`BᵀB = Q√Λ√ΛQᵀ = QΛQᵀ = Σ`. ✓
*Use:* if `Z ~ N(0, I)` are independent standard normals, then `X = BᵀZ` has
`Cov(X) = BᵀIB = Σ`. So **one matrix multiply turns independent noise into correlated
samples with the covariance you asked for.** Cholesky (`Σ = LLᵀ`, `L` lower-triangular) is the
cheap way to get such a `B` — half the cost of LU, and it exists precisely when `Σ` is PD.
A PSD-but-singular `Σ` is where Cholesky fails and you fall back to the eigendecomposition
above.

</details>

<details>
<summary>Tier C</summary>

**C1.** `tr(A) = Σλᵢ`, `det(A) = Πλᵢ`. A1: `tr = 4 = 1+3` ✓, `det = 3 = 1·3` ✓.
A4: `tr = 14 = 1+2+11` ✓, `det = 2·11 = 22 = 1·2·11` ✓.
Free check: after any hand computation, sum your eigenvalues and compare to the diagonal sum.
Costs five seconds and catches most sign errors.

**C2.** `[[1,1],[0,1]]`: `det(A−λI) = (1−λ)²` → `λ = 1` twice. But
`(A−I) = [[0,1],[0,0]]`, whose null space is spanned by `(1,0)` alone — **one** independent
eigenvector for an algebraic multiplicity of 2. Geometric multiplicity < algebraic multiplicity,
so the matrix is **defective** and cannot be diagonalised (you need Jordan form).
A shear: it fixes the horizontal axis and tilts everything else, so there is no second
independent direction that merely scales. Note this never happens for real symmetric matrices —
the spectral theorem rules it out, which is why covariance matrices are always diagonalisable.

</details>
