---
type: feynman-note
stage: "[[R_linear_algebra]]"
id: R.linalg
---

# Linear Algebra Refresher
`stage: R.linalg` · **Started:** 2026-07-30 · **Completed:** ____
**Time spent:** __h · **Source(s):** Green Book Ch.2 linear algebra, pp. ____

## Review log
- [ ] +1 week (2026-08-06): recall napkin version without opening file → pass/fail
- [ ] +1 month (2026-08-30): re-solve `[[2,1],[1,2]]` eigenvalues from scratch → pass/fail
- [ ] +3 months (2026-10-30): re-take VII.1 + VII.2 → pass/fail

---

## 1. Teach-back (Step 2 — write from memory, source CLOSED)

<!-- Explain to a smart 15-year-old. Three things:
     (a) eigenvalues/eigenvectors — what Av = λv MEANS geometrically, then how you
         actually compute them (why does det(A − λI) = 0 find them?)
     (b) PSD — the three equivalent definitions, and why they are the same thing
     (c) why a covariance matrix is always PSD — the one-line argument
     No jargon shortcuts. If you use a term, define it in the same paragraph. -->

(a) for a matrix A, there exists a scalar lamda, such that when A as a transformation operation performed on a vector x, the resulting transformed vector is the same as applying the scalar to itself. i.e. Ax=lamda*x. In this case, lambda is the eigenvalue and x is the associated eigenvector. This is a very useful concept in linear algebra, as it can boil down a matrix into a combination of matrices that are linearly independent of each other. This is similar to having a system, where we can decouple a matrix A into combination of projections into these eigen vectors. 

For a symmetric matrix, we can prove that its eigenvectors are also perpendicular to each other. Let A be the matrix, ui be the ith unique eigenvalue and vi the ith eigenvector. i=1,2
Av1=u1*v1, Av2=u2*v2
take transpose:
(Av1)T = v1T*A = (u1*v1)T = u1*v1T
multiply v2 to both sides
v1t A v2 = u1 v1t v2
u2 v1t v2 = u1 v1t v2
rearrange: (u2-u1)*v1t v2 = 0
since u2 != u1, v1t v2 = 0 so they are normal to each other.

now back to main topic, to compute eigen value and vector.
for each pair of ui,vi, we can write Aui=viui;
we can aggregate these into matrix form
A[v1,...,vi] = I_u [v1,...,vi], where I_u is a matrix with main diagnal as ui
rearranging we get (A-uI)[v1,...,vi] = 0
since v is non trivial, we need A-uI as 0

(b) 3 conditions for positive definite:
1. quadratic form xTAx > 0
2. all eigenvalues are positive
3. all submatrices along the diagnoal have positive det

for PSD just replace the constraint as non negative

now prove why these 3 properties are the same. 
start from Av=uv
so vTAv=uvTv=u||v||, where ||v|| is the euclidean, which is sum of square of elements in v;
so when vTAv >0, since euclidean is positive, u has to be positive. this applies to all eigenvalues. so if 1 is true then 2 is true.

then for 3, this is a gap.

(c) ~~covariance matrix is just dot product of the variables matrix to itself. it is always symmetric and diagnal is variance. the elements are all euclidean. so 1,2 are always met. for 3, all submatrix is a mini version of the covariance matrix just with smaller set of variables, so they are all PSD, but pending gap on why det has to be non negative.~~
**SUPERSEDED** — this route went via the three conditions and stalled on the minors. The derivation below never needs them.

derivation:
let Y be a column vector (nx1) of n random variables yi
Mu be a column vector of same size, with mui being mean of that varible
so the deviation of all variable pairs: (Y-mu)(Y-mu)T
this gives a nxn matrix, with diagnal being square deviation of same variable
then variance matrix by definition is E((Y-mu)(Y-mu)T) — the E[.] IS the averaging, no extra divide by n
this is defined as the Sigma, variance matrix
let's get a vector x of constants, representing perturbations
the effect of applying the perturbation can be written as:
xT Sigma x = E(xT(Y-mu)(Y-mu)Tx)
let z = xT(Y-mu). z is a SCALAR — (1xn)(nx1) — so zT = z, and xT(Y-mu)(Y-mu)Tx = z*zT = z^2
so xT Sigma x = E(z^2) = Var(xT Y) >= 0, i.e. expected value of z^2, which already includes
expected value of Y, is just variance. A mean of squares can't be negative.
so the quadratic form is itself a variance, always non negative, meeting first criteria of PSD

and z = xT Y is just the portfolio return under weights x. So xT Sigma x IS that portfolio's
variance — Sigma cannot fail to be PSD because a portfolio cannot have negative variance.
PSD and not PD because a portfolio CAN have zero variance (perfectly hedged, or a redundant
asset) — the singular case that breaks Cholesky and naive Markowitz.

## 2. Gaps identified & filled (Step 3)

<!-- Re-read §1. Every "obviously", "it follows that", or place you couldn't produce a
     number → mark it ⚠️ GAP: ... then go fill only those.
     Watch for: "det(A − λI) = 0 gives eigenvalues" stated without saying why a zero
     determinant means a non-trivial null space. That is the step everyone skips. -->

(a) why we need det(A-uI)=0 for A-uI=0? so first correction, the note above, v should be a single column vector. The rearragne method above is wrong, as we should get AV = VU; and bringing them to one side can't help us to get the form (A-U)V, as this is AV-UV;
instead we should look at it one by one. Av=uv; (A-u)v=0, for non trivial soltion, where v is non zero, A-U must be zero. which comes back to why we identified this gap.
for linear independency of a vector, it means we can make vector 1 to be the same as vector 2 by doing scaling and linear addition, and this can be extend to multiple vectors. let c be the vectors; this means we can express them as x1*c1+x2*c2=0, where x is the element in the eigenvector, and c is the column vector of (A-U); since we know eigenvector is nonzero, (A-U) must be linearly dependent, therefore we just need to solve for determinant(A-lambda I)=0

(b) what does it mean, or imply, that all upper and lower submatrix in PD is det positive? what does a negative det mean?
so we proved the relation between A and lambda -> A-U=0
det(A-uI) is the charactistic polynomial, and we can express it in its roots
det(A-uI) = (u1-u)(u2-u)...(un-u)
plug in u=0 -> det(A)= Pi(ui)
so determinant of A is product of all its eigenvalues. 
since upper or lower matrix is just sub slice of A, same analygy applies.

(c) same as above

## 3. Napkin version (≤200 words)

<!-- The 90-second spoken answer, covering all three of (a)(b)(c).
     Say it OUT LOUD once before ticking the checklist. -->

(a) for a matrix, a eigenvalue would achieve the same effect of transformation to its eigenvector as A does.
(b) a PSD matrix is a symmetric matrix with quadratic form as non-negative and eigenvalues all non-negative. effectively a positive number concept in higher dimension, but need more examples in later sprint to understand
(c) covariance between 2 variable a,b is (a-mu_a)(b-mu_b)



## 4. Analogy (non-mathematical)

<!-- One per topic. Non-mathematical — "some rearrangement of a formula" is not an analogy.
     Eigenvectors have a good physical one; PSD has one about which directions are "uphill". -->

1. eigenvector can be factors in PCA analysis of a stock return prediction, which can represent value, momemtun, fundmanetals etc.
2. real life system like energy, as its quardatic form is always non negative, so when we express the characteristic of a system A and give it perturbation x, xtAx is always non-negative
3. portfolio covariance matrix

## 5. Worked numerical example

<!-- Required: eigenvalues of [[2,1],[1,2]] by hand → verify with np.linalg.eig.
     Confirm 1 and 3. Check eigenvectors against yours up to scale — numpy normalises to
     unit length and may flip signs, so (1,1) may come back as (0.707, 0.707). Note why
     that is not a discrepancy. Inline is fine, no solver file this stage. -->
np.linalg.eig([[2,1],[1,2]])
## 6. Where this breaks

<!-- ≥2 items. Candidates you will meet in the problems:
     - orthogonal eigenvectors need SYMMETRY, not just squareness (A3)
     - repeated eigenvalues can leave you short of independent eigenvectors → defective,
       not diagonalisable (C2)
     - PSD ≠ PD: a singular covariance matrix is legal and it breaks Cholesky and naive
       Markowitz (B1, B5)
     - Sylvester's LEADING-minor test gives PD; PSD needs ALL principal minors (A5) -->
PD/PSD has to be symmetrical.

## 7. Links

- **Problems solved:** R.linalg-A1…A5, B__ (from `stage_maps/R_linear_algebra.md`)
- **Prereqs:** none (Tier 0)
- **Unlocks:** S1.6 joint/MVN · S7 PCA + covariance (S20) · S9.3 regression · S25 correlated MC
- **Baseline questions this closes:** VII.1 (eigenvalues of `[[2,1],[1,2]]`), VII.2 (PSD)
- **Deliberately deferred:** SVD, QR, LU, Cholesky implementation, condition numbers,
  power iteration, PCA proper → S7/S20. See the topic note in `vault/topics/` for the full split.

---

## Completion checklist (all must pass)

- [ ] All 6 template sections have real content
- [ ] Zero remaining ⚠️ GAP markers
- [ ] Napkin ≤200 words AND said out loud once
- [ ] Analogy is non-mathematical
- [ ] Numerical example runs and produces the claimed number
- [ ] "Where this breaks" lists ≥2 items
- [ ] Tier-A problems A1–A5 all solved unhinted
- [ ] ≥3 of 5 Tier-B solved
- [ ] Unlock test: VII.1 + VII.2 re-answered cold, both fully correct
