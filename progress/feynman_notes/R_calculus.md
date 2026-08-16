---
type: feynman-note
stage: "[[R_calculus]]"
id: R.calculus
---

# R.calculus — Calculus & ODE Refresher

**Stage:** R.calculus · **Started:** 2026-07-25 · **Completed:** 2026-07-29
**Time spent:** 5.0h · **Source(s):** see `stage_maps/R_calculus.md` sources table

## Review log
- [ ] +1 week (2026-08-01): recall napkin version without opening file → pass/fail
- [ ] +1 month (2026-08-25): re-solve worked example from scratch → pass/fail
- [ ] +3 months (2026-10-25): re-take VIII.1 + VIII.3 → pass/fail

---

## 1. Teach-back (Step 2 — write from memory, source CLOSED)

<!-- Explain to a smart 15-year-old. Four things:
     (a) separable ODEs — why dy/dx = y gives e^x
     (b) linear first-order — what the integrating factor actually does
     (c) chain rule — the "inner times outer" picture
     (d) Lagrange multipliers — why ∇f = λ∇g, geometrically
     No jargon shortcuts. If you use a term, define it in the same paragraph. -->

(a) dy and dx are very small changes in y and x respectively. their ratio is saying how much does y change for a small nudge in x. dy/dx=y, it is saying that, the rate of change in y with x is dependent on the current level of y. the larger y the quicker the change. this type of change is exponential. the definition of e is a constant, such that e^x has derivative as e^x at every point of the curve. 
mechanically, when dy/dx = y, we can rearrange to be dy/y = dx, integrating both side gives us ln|y| + c = x -> y = exp(x-c) = e^(-c)*e^x = c*e^x, define c as the constant
separable ODEs are ODEs such that can be arranged in dy/dx = p(y)*q(x), and can then be solved in the way similar to above.
(b) linear first order: an ODE that can be arranged as y' + p(x)*y = q(x).
it's not directly separable. if we can make the LHS a single term, then this can be solved. first define a term that can make LHS be writter as d(I(x)*y)/dx. By differentiation by part, it can be written as dI/dx * y + I*dy/dx.
so when we multiple the ODE by I on both side, it becomes I*y'+I*p*y= I*q
already close to what we want, all we need is to get the expression for I such that I*p = dI/dx -> I = exp(integral(p(x)dx)) -> this should give us I
then I*y = integral (I(x) * q(x) dx), and we get y
(c) dy/dt = dy/dx * dx/dt
we can think of 2 functions, y(x) and x(t).change in value of x is dependent on change in t. change in y is dependent on change in x. if we shrink the change to small nudge, then rate of change of y with t can be expressed as rate of change in y wrt x times x wrt t: dy/dt = dy/dx * dx/dt. note here they are not fractions, dx cannot be canceled. this is just saying changes in variables at 'lower' level cascade up to higher levels. dx/dt is coupled with delta_t, their product is delta_x, which then couples to dy/dx
(d) we can start with a 2d plan - imagine we have contours on this plan with expression f(x,y), each contour line has a fixed value for f. then we have another expression g(x,y)=k. g goes through the plan and can cut through infinte numbers of contour. we want to find a point on g, such that at this point, the f value is largest. this is where g kisses a contour of f, where the local small portion are tangential to each other, so that whichever direction you go from that point, the change in value f is 0. so at this point the normal to both f and g are pointing to the same direction. therefore in vector form there exists lambda, such that scales normal vector of g to be equal to normal of f.

## 2. Gaps identified & filled (Step 3)

<!-- Re-read §1. Every "obviously", "by symmetry", "it follows that", or place you
     couldn't produce a number → mark it ⚠️ GAP: ... then go fill only those. -->
(a) when integrating there should be a constant term, as when differntiating it will disappear; int(1/y)dy = ln|y| + c;
(c) did not stress un-cancelability

## 3. Napkin version (≤200 words)

<!-- The 90-second spoken answer. Say it OUT LOUD once before ticking the checklist. -->
(a) separable ode: a form of ode that can be rearrange to a clean form dy/p(y)=q(x)dx;
(b) a more complex form comparing to separable ode, y'+py=q, but we can rearrange it by finding a expression, called integration factor, such that it can be written as (i*y)dx = i*q
(c) chain rule: it's like a system of cogs, moves in lower level cascade up, and each cog has their ratio. say there are 3 levels, y,x,t. to find change in y wrt to t, we can use delta_y = dy/dt*delta_t = dy/dx * dx/dt * delta_t; and dx/dt * delta_t = delta_x;
(d) we are looking for a point on f along a constraint g, such that, at this point, whichever direction we go from this point along the constraint, the change in f is 0. therefore at this point, g is tangential to f, meaning their normal is pointing to the same direction. 


## 4. Analogy (non-mathematical)
(a) some arrange of a formula. but on exponential it's a system common in natural, where rate of change is dependent on current level. like how animals/herds grow/decay
(b) some arrange of a formula
(c) system of cogs
(d) hiking on a mountain with trail.

## 5. Worked numerical example

<!-- Required: solve A1 by hand → verify e^1 ≈ 2.71828 numerically.
     3-line Euler scheme or scipy.integrate.solve_ivp. Inline is fine, no solver file this stage. -->

Pseudocode (not run — Euler on the ODE itself, not the series for e):

// we know dy/dx = y, so dy = dx * y
y = 1
dx = 1e-5
for _ in range(1e5)        // steps = 1/dx, so x travels 0 -> 1
     y += dx * y

Each step multiplies y by (1+dx), over 1/dx steps, so this returns exactly
(1+dx)^(1/dx) = 2.718268... — NOT e. It is the compound-interest definition
of e with 1e5 compounding periods; e is only the dx -> 0 limit.
Error ≈ e·dx/2 ≈ 1.4e-5, first-order in dx: halve dx, halve the error.
The check that passes is agreement to a tolerance set by dx, not equality.

## 6. Where this breaks

<!-- ≥2 items. e.g. separation of variables fails when g(y) has a zero;
     Lagrange needs ∇g ≠ 0 and finds stationary points, not necessarily minima. -->
(a) ln|y| as integral of 1/y
(b) has to be arranged to this certain form first for IF to apply
(c) not fractions, can't just cancel terms
(d) gradient field of constraint cannot be 0, i.e. g must exist in the space. what we find need to be sorted to see which one is max/min
(e) numerical: Euler never returns e for any finite dx — it returns (1+dx)^(1/dx).
    Accuracy is a tolerance question, not an equality question. Smaller dx is not
    free either: truncation error falls like dx but float roundoff accumulates over
    1/dx additions, so there is a floor (~dx=1e-8 in float64) past which smaller
    steps get worse.

## 7. Links

- **Problems solved:** R.calculus-A1…A6 (Tier A complete). Tier B not logged individually.
  Also `inventory/section_VIII` §1: *Exponential Growth/Decay* and *Logistic Growth*.
- **Prereqs:** none (Tier 0)
- **Unlocks:** R.linalg linear algebra · `F1.5` continuous RVs · S4.x SDEs · S9.3 regression
- **Baseline questions this closes:** VIII.1 (`dy/dx=y`), VIII.3 (Lagrange)
- **Deferred to post-S4/S6 (2026-07-29):** `inventory/section_VIII` §2 PDEs (heat equation,
  BS PDE, Feynman-Kac), 2nd-order ODEs, and §3 Kelly criterion. Useful framing, but they
  need the finance first — revisit when S4 (BM/Itô) and S6 (BS/Greeks) are in hand.

---

## Completion checklist (all must pass)

- [ ] All 6 template sections have real content
- [ ] Zero remaining ⚠️ GAP markers
- [ ] Napkin ≤200 words AND said out loud once
- [ ] Analogy is non-mathematical
- [ ] Numerical example runs and produces the claimed number
- [ ] "Where this breaks" lists ≥2 items
- [ ] Tier-A problems A1–A6 all solved unhinted
- [ ] ≥4 of 7 Tier-B solved
