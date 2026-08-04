# Plan: Strengthening the Trial and Prospective-Study Focus
*2026-08-03 19:02 PDT*

> **Status, 2026-08-03.** All items in sections 1 through 4 and section 6
> have been implemented across eight chapters (+694/-47 lines). The full
> book renders; every citation and cross-reference resolves; the
> US-spelling gate passes. The two chapters marked "no action" (3 and 9)
> were left untouched, as were the passages listed in section 5. The
> bibliography gap described in section 7 remains open and is the natural
> next piece of work.

A chapter-by-chapter plan for increasing the book's focus on clinical
trials and prospective epidemiological studies, using the 93 references
merged into `references.bib` today. Line numbers refer to the files as of
this date.

## 0. Summary of findings

Three findings shaped this plan, and two of them contradict the premise
the plan started from.

**The clinical-trial thread is already strong.** The trial ledger is the
book's declared running case study (`00-intro.qmd:227-256`) and it is
genuinely carried through: ch. 2 commits a locked dataset, ch. 3 sets
confirmation depth as a significance level, ch. 8 maps front-running onto
allocation concealment, ch. 9 maps correlated slashing onto shared
frailty. The trial material does not need more volume. It needs
supporting evidence at the points where it currently asserts.

**The prospective-epidemiology thread is the actual gap.** The word
"cohort" appears zero times in chapters 0, 1, and 2, and only in ch. 6
and ch. 10 thereafter. This matters technically, not just thematically: a
prospective study with periodic data freezes is the natural motivation
for consistency proofs, which the book cites (`@rfc6962` at
`02-cryptographic-primitives.qmd:969-975`) but never explains, and for
sequential rather than one-shot commitment. A cohort is not a relabeled
trial.

**Chapter 2 contains a cryptographic error.** This is unrelated to the
focus question but was found while surveying, and it outranks everything
else in this plan. See section 1.

Chapter 7 is the only chapter with a genuine trial-content hole.

## 1. Priority zero: a correctness defect in Chapter 2

`02-cryptographic-primitives.qmd` claims three times that a Merkle
commitment hides its leaves, and grounds the claim on the wrong property:

- L830-831: "by preimage resistance a digest does not disclose the record
  that produced it"
- L859-863: "patient confidentiality is preserved, since the published
  root reveals nothing about the data"
- L1512-1513: "the hiding property [rests] on the one-wayness of the
  hash"

Preimage resistance does not give hiding. It says that given a digest of
a *random* input, finding a preimage is hard. It says nothing when the
input space is small enough to enumerate, and trial records are exactly
that case. The chapter's own worked example (L1835-1841) builds leaves as
`paste(subject, arm, outcome, sep = '|')`, giving strings such as
`S0007|A|1` over a space of 16 subjects x 2 arms x 2 outcomes = 64
possibilities.

Verified by direct execution: enumerating that space and matching digests
recovers the exact record in **0.07 ms**. An adversary holding one
sibling digest from an inclusion proof learns a patient's arm assignment
and outcome. This is a re-identification hazard in the section that
promises confidentiality.

The fix is standard: a per-leaf random nonce, so the leaf is
`H(nonce || record)` with the nonce released only alongside the record.
With a 128-bit nonce the enumeration becomes infeasible. The chapter
already introduces hiding commitments at L1501-1521 but never connects
them back to the Merkle construction or the worked example, so the
machinery is present and merely needs wiring.

**Actions.**

1. Correct L830-831 and L859-863 to state that hiding requires either
   high-entropy leaves or explicit blinding, and that the raw
   construction does not provide it.
2. Correct L1512-1513: hiding rests on blinding or input entropy, not on
   one-wayness.
3. Add the salted-leaf variant to the worked example at L1835-1841.
4. Add an exercise: brute-force an unsalted leaf, then repeat with a
   nonce. This turns the defect into the chapter's most memorable lesson.
5. Cite `@rocher2019reidentification` and `@na2018reidentifying` for
   calibrated re-identification risk on the kind of low-dimensional
   records this readership handles.

This is the book's own critical standard applied to its own construction,
and it converts an error into a teaching asset.

## 2. Establish the prospective-study thread

The three actions below are prerequisites; the later cohort-specific
insertions have nothing to attach to without them. Check against ch. 6
(L49, L1296) and ch. 10, which already use a longitudinal cohort, so the
case study is defined once rather than twice.

**2.1 Add a third running case study** (`00-intro.qmd:227-256`). The two
existing cases both terminate: the trial locks its database, the cold
chain completes delivery. A prospective cohort or registry with periodic
data freezes demonstrates what neither can — open-ended accrual with no
lock date, repeated measurement on the same subject, consent withdrawable
mid-followup, and therefore a *sequence* of commitments requiring
consistency proofs rather than a single root.

**2.2 Develop the open disease registry** (`01-consensus-problem.qmd:95-105`).
It currently exists only to motivate the Sybil attack. Developed into a
parallel case, it becomes the book's one honest instance of genuinely
open, unaccountable membership — the condition the chapter says is rare
in health (L891-893) and which the rest of the book presupposes. A
participatory-surveillance or citizen-science registry has genuinely
unenumerable reporters; a trial consortium does not.

**2.3 Motivate consistency proofs**
(`02-cryptographic-primitives.qmd:965-992`). `@rfc6962` is cited for
"proof that the log was only ever appended to" and then dropped. Periodic
cohort freezes supply the motivation: each freeze must be provably an
extension of the last, not a rewrite.

## 3. Chapter 7: the one real hole

Ch. 7's four trial mentions are all boilerplate — three are the running-
example definition (L245-246, L257) and one is a repeated phrase (L884).
The chapter contains no trial content.

The proposal to use participant reimbursement and site payments as an
escrow example is sound and **completes rather than contradicts** the
chapter's existing argument. The chapter's moral (L97-100) is that the
hard part is the trigger and the oracle, not the payment mechanism. A
second escrow with a locally verifiable trigger is a controlled
comparison: vary the trigger, hold the plumbing fixed.

One correction to that proposal, and it is the best material here. For
**site payments** the trigger is *not* cleanly verifiable, because the
attester is the payee. A site attesting its own visit completion in order
to be paid is a principal-agent problem, and it is the documented
mechanism of real trial fraud. The oracle problem is not eliminated; it
changes type.

| Escrow | Trigger failure mode | Remedy |
|---|---|---|
| Epidemic bond (existing, L1146-1238) | Epistemic: quantity genuinely uncertain, under-ascertained | Threshold design; sensitivity/specificity trade-off |
| Site payment | Strategic: quantity knowable, reporter financially interested | Separate attestation from payment; independent monitoring; audit sampling |
| Participant reimbursement | Trigger clean: attester is not the payee | Binding constraint becomes ethical and regulatory |

Present all three as a graded sequence ordered by trigger hardness. Only
participant reimbursement behaves as originally described; site payment
is the richer case.

**Actions.** New subsection at L1238, between the trigger discussion and
the callout at L1239. Two or three sentences of orientation at ~L100 and
one row in `tbl-defi-primitives` (L134-142). Do not disturb L1083-1237.

Citations: `@grady2005payment` (payment-model taxonomy),
`@halpern2021incentives` (two RCTs finding no undue inducement — a
result that corrects the reflexive assumption), `@persad2019differential`
(may a contract pay participants differently within one study — the
question programmability forces), `@gneezy2000payenough` (non-monotonic
crowding-out, which defeats naive token rewards),
`@abdelazeem2022incentives`, `@parkinson2019incentives` (design checklist
= the specification a contract must encode), `@kitterman2011lowenrolling`
(dollar cost of accrual failure). `@till2017cryptocurrencies` is the
named foil the callout at L1240 currently lacks.

## 4. Chapter-by-chapter actions

### Ch. 0 (intro)

- **L138-181**, "Why now": the section argues the technology has arrived
  in health but names no research-integrity driver. Add the measured
  failure rates: `@hartung2014discrepancies`, `@anderson2015compliance`,
  `@kasenda2014discontinued`. This applies the book's own falsifiability
  method to its own motivating case.
- **L92-113**: add a fifth translation — a hash commitment is the
  cryptographic form of a sealed protocol deposit, and HARKing is what it
  forecloses (`@kerr1998harking`, `@chan2013spirit`).

### Ch. 1 (consensus)

- **L1002-1017**: the chapter's central skeptical claim — that "a
  well-governed database with cryptographic audit logging delivers
  tamper-evidence at a fraction of the cost" — never names one. Name
  REDCap (`@harris2009redcap`) and an integrated CTMS (`@park2018ctms`).
  This is the single change that most strengthens the existing argument,
  converting a rhetorical comparator into a falsifiable one. Apply the
  same fix to the table cell at L785-793.
- **L959-1000**: the review numbers quantify health blockchain generally.
  Add the trial-specific counterpart, and develop `@benchoufi2017trials`,
  which is currently a bare citation at L967 despite being the book's
  closest antecedent.

### Ch. 2 (primitives)

Beyond the priority-zero fix:

- **L838-863**: the commitment is justified by assertion. Add the
  measured rates (`@hartung2014discrepancies`, `@anderson2015compliance`)
  and the analytic-flexibility evidence (`@john2012qrp`,
  `@head2015phacking`). State precisely which failure mode a commitment
  forecloses: it stops post-lock alteration, but not fabrication at
  entry, and not HARKing unless the analysis plan is also committed.
- **L1501-1521**: hiding currently does no work anywhere in the chapter.
  The sealed analysis plan — commit the pre-specified endpoint before
  unblinding, reveal after — is the first place it does, and it closes
  the HARKing gap. Cite `@chan2013spirit` for what is committed.

### Ch. 3 (proof-of-work)

**No action.** Near saturation: every section already terminates in a
trial reading, and the NHS negative result at L951-1001 is calibrated.
Adding more risks losing the protocol thread.

### Ch. 4 (mining statistics)

- **L869-950**, fork and orphan rate: a fork is two miners racing to have
  a block accepted — a **competing-risks** problem the chapter never
  names, though L881 asks "how often does such a competing block occur?".
  `P(fork) = 1 - e^{-Delta/mu}` is the cause-specific-hazard calculation.
  "Competing risk" appears zero times in the chapter. Six to ten lines.
- **L240-290**: the Poisson table maps to "surveillance case counts" but
  never to incidence rate per **person-time**, the actual epidemiological
  quantity. One row or clause.
- **Do not extend L621-652.** The adaptive-design analogy is already
  present and already bounded, and the data-generating-process versus
  observation-process distinction is the most honest passage in these
  chapters. Extending it would dilute it.

### Ch. 5 (security economics)

This chapter has the substantive gap in the Bitcoin group.

- **After L962**, the insider threat: the entire attack model is an
  external adversary renting hash power, but the documented trial-
  integrity failure mode is an insider fabricating at the point of entry,
  which no consensus mechanism addresses. L960-962 concedes this in one
  clause. Develop it with `@mccurry2014valsartan` (a named criminal
  case), `@george2015fraud`, `@gupta2013misconduct`. Twelve to fifteen
  lines. Highest-value addition in these three chapters, and it
  strengthens the chapter's own skeptical thesis.
- **After L334**, the cost of the alternative: the chapter prices the
  attack but never the defense it competes with. Add the per-subject
  monitoring cost (`@olsen2016monitoring`, `@funning2009gcpcost`,
  `@mealer2013sdv`), with `@catalini2016economics` supplying the cost-of-
  verification frame that makes it one comparison rather than two
  unrelated numbers.
- **L1187-1240**: add a break-even exercise using the monitoring cost.

### Ch. 6 (Ethereum/EVM)

- **~L1315**: the consent section asserts a contract can hold a
  permission state but never shows the machine-readable object it
  compiles. `@dyke2016consentcodes` and `@woolley2018adam` supply it;
  `@kaye2015dynamic` is the canonical definition and is currently
  uncited anywhere in the book.
- **~L1348**: extend from cohort to trial with `@albanese2020dynamic`
  and `@choudhury2018humansubjects` (IRB rules as contracts);
  `@peyrone2023formal` supplies a formal-verification register.
- **L1165**: `@szabo1997formalizing` belongs here — the book cites
  Buterin and Wood but not the origin of the smart-contract concept.
- **L1516-1529**: the cold-chain paragraph is the chapter's weakest
  public-health passage, asserted and uncited. Multi-site trial data
  quality (`@choudhury2019quality`, `@nugent2016transparency`) carries
  the same architectural point with evidence.

### Ch. 8 (MEV)

**No action.** L889-951 is the strongest public-health section in the
book and should be the template for the others. Optionally add
`@agniel2018ehrbias` at ~L906 to extend the information-leakage point
from trials to observational cohort data.

### Ch. 9 (proof-of-stake)

**No action.** The best-integrated prospective-study material in the
book: correlated slashing as shared frailty (L1175-1239), committee
sortition as PPS sampling (L616-680).

### Ch. 10 (on-chain data)

- **~L604**: re-identification evidence stops at genomics. Add
  `@rocher2019reidentification` (calibrated per-individual
  probabilities), `@na2018reidentifying` (NHANES accelerometry — the
  dataset this readership handles), `@gymrek2013surname`.
- **~L1429**: the "defensible pattern" paragraph asserts off-chain
  storage without naming a working alternative. `@beaulieujones2019synthetic`
  (differentially private synthetic SPRINT data reproducing the original
  analysis), `@weber2009shrine`, `@harris2009redcap`.
- **~L1401**: `@zafar2025reconciling` updates `@finck2018gdpr` by seven
  years; `@minssen2021transparency` is trial-data-specific;
  `@farshid2019forgetting` is a worked redactable-chain attempt.
- **~L351**: `@agniel2018ehrbias` in the measurement bullet.

## 5. Where NOT to add trial material

Stated plainly, because the failure mode of a plan like this is thematic
veneer:

- **Ch. 7 CFMMs, impermanent loss, AMM convexity (L314-671)** — the
  convexity cost of a liquidity position is Jensen's inequality. It has a
  general statistical reading but no *trial* reading.
- **Ch. 7 stablecoins (L900-1047), lending and liquidation (L672-781)**.
- **Ch. 6 gas, EIP-1559, EIP-4844, rollups (L521-1164)** — already well
  motivated as feedback control.
- **Ch. 8 sandwich optimization (L519-626)** — the trial connection is
  correctly made at L889 and does not belong in the optimization math.
- **Ch. 9 Casper, Gasper, Ouroboros finality (L372-491)** — accountable
  safety is a distributed-systems result with no analogue.
- **Ch. 5 selfish mining (L394-900, ~500 lines)** — there is no trial
  analogue of withholding a block to waste a competitor's work.

The structural principle these share: chapters 3 through 9 earn their
public-health relevance in **one designated section each**, not
throughout. That structure works. Ch. 7's fix is to give it the section
it lacks, not to thread trials through its mathematics.

Also note that `@halpern2002underpowered` and `@kitterman2011lowenrolling`
concern trial economics and ethics, not ledger security. Placing them in
ch. 5's cost-of-attack section would conflate two unrelated cost
structures; they belong in ch. 7.

## 6. Sequencing

1. **Ch. 2 correctness fix** (section 1). Independent of everything else
   and should not wait.
2. **Ch. 7 escrow subsection** (section 3). Largest single gain; the only
   chapter with a real hole.
3. **Prospective-study anchors** (section 2), in order 2.1, 2.2, 2.3.
   The cohort-specific insertions elsewhere depend on these.
4. **Ch. 1 named comparator** (L1002-1017). One paragraph, high leverage
   on the book's central argument.
5. **Ch. 5 insider threat and cost-of-alternative.**
6. **Ch. 6 consent ontology; ch. 10 re-identification and alternatives.**
7. **Ch. 4 competing risks and person-time.**

Rough scale: items 1 through 5 are on the order of 150 to 200 lines of
new prose plus two exercises. Items 6 and 7 are mostly citation
placement into existing passages.

## 7. Known gap in the new bibliography

The 93 merged references are trial-heavy because they were mined from the
reference lists of blockchain papers, which cite trial work far more than
cohort work. Prospective epidemiology is thinly covered: there is no
citation for FDA Sentinel-style distributed pharmacovigilance (the
candidate found had no DOI), none for registry-based randomized trials
such as TASTE within SWEDEHEART, none for cohort attrition and loss-to-
followup methods, and none for large prospective cohort governance (UK
Biobank, All of Us).

If section 2 is adopted, that material needs fresh sourcing rather than
further mining of the blockchain literature. Registry-based randomized
trials would be a particularly strong addition, since they sit exactly at
the junction of the two study designs this plan is trying to strengthen.

## 8. Epistemic status

Chapter analyses were performed by reading the full chapter sources; line
numbers were checked at the time of writing. The Chapter 2 defect was
verified by executing the attack, not merely reasoned about. The
citation-to-insertion-point matches are proposals based on abstracts and
titles; the 93 references' full texts have not been read, so each should
be confirmed to say what is claimed before it is cited in the text. No
chapter files have been modified.
