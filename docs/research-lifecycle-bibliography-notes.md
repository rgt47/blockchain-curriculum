# Extended Bibliography: Blockchain in the Research Lifecycle
*2026-08-03 17:49 PDT*

Companion notes to `analysis/book/references-research-lifecycle.bib` (93
entries). This document records how the bibliography was assembled, what
each cluster is for, and where the textbook could be strengthened using
it.

## 1. Provenance and method

The JMIR theme *Blockchain, Distributed Ledger Apps for Health and
Medicine* contains 98 articles. Of these, 15 were identified as directly
concerning the research lifecycle: clinical trial conduct, informed
consent, biospecimen management, participant and site payment, and
quality control. Their reference lists were retrieved from PubMed Central
and pooled, yielding 796 citations and 680 unique references after
deduplication.

Those 680 were then deduplicated against the book's existing
`references.bib` and `references-health.bib`, removing 24 already-cited
works and leaving 656 candidates. Four independent curation passes, one
per domain, selected 93 for inclusion. Bibliographic metadata was
retrieved from the DOI registry by content negotiation rather than
transcribed, so author lists, volumes, and pagination are authoritative.

**Epistemic status.** Selection was made from titles, venues, years, and
cross-citation counts, together with the abstracts of the 15 source
papers. Full texts of the 93 selected works were not read. A handful of
uncertain items were verified against the publisher record. The tier A
and tier B labels therefore express expected value to the book, not a
verified assessment of each paper's quality.

Two caveats on the selection itself. First, mining reference lists
inherits the source papers' citation bias: this pool over-represents work
that blockchain researchers already cite and under-represents the
non-blockchain trial-operations literature, which is why several
deliberate counterfactual citations (REDCap, Sentinel-style distributed
networks, BBMRI-ERIC Negotiator) were included. Second, all 15 source
papers are from a single publisher's theme collection, so the pool
reflects JMIR's editorial scope.

## 2. What the bibliography contains

The `.bib` file is organized into four sections, each entry marked tier A
or tier B.

**Trial conduct, data quality, and research integrity (27 entries).**
The research-integrity measurement literature (Hartung, Anderson, Head,
John, Kerr) supplies quantified evidence that selective reporting and
analytic flexibility are real and measurable, which is what makes a
cryptographic pre-commitment worth teaching. The monitoring-economics
literature (Olsen, Funning, Mealer) supplies the cost baseline. REDCap
and a conventional integrated CTMS are included as the honest
non-blockchain comparators.

**Informed consent, governance, and data sovereignty (22 entries).**
Kaye's dynamic-consent paper and the machine-readable permission
artifacts (GA4GH consent codes, ADA-M) are the load-bearing additions:
they turn "encode consent in a smart contract" from a slogan into an
engineering claim with a concrete ontology behind it. The GDPR and
European Health Data Space material covers the immutability-versus-
erasure collision. The Indigenous data sovereignty cluster (Mackey's
*Cell* framework, CARE principles, Kukutai, Fox) supports the UC San
Diego thread that the 2026 JMIR paper continues.

**Biospecimens, participant payment, and research economics (20
entries).** This is the largest gap the exercise closed. The participant-
payment literature is mature and quantitative: Halpern's two randomized
trials on whether incentives are coercive, a meta-analysis of incentive
effects, Grady's taxonomy of payment models, and the FDA guidance that
constrains any automated payment scheme. Gneezy and Rustichini's
non-monotonic incentive result is the mechanism by which naive token
rewards fail. Moore v. Regents is the legal fact that determines whether
a specimen token can convey ownership at all.

**Cryptographic and systems substrate (24 entries).** Szabo's 1997 paper
(the origin of the smart-contract concept, currently absent from the
book), the IPFS paper behind every off-chain-storage design, measured
permissioned-ledger benchmarks, and the re-identification literature
(Gymrek, Rocher, Na) that quantifies why "de-identified, therefore
consent-exempt" is unsound.

## 3. Suggested enhancements to the textbook

Ordered by expected improvement per unit of work.

### 3.1 The research-lifecycle thread is the book's strongest unclaimed asset

The book currently cites `benchoufi2017trials` and little else on trial
conduct, yet every chapter already has a public-health connection section
and the white paper `white-paper-blockchain-clinical-trial-management.md`
contains a fully developed critical analysis of exactly this material.
The clearest structural improvement would be to run one worked example,
a multi-site randomized trial, as a spine across the existing chapters
rather than adding a new chapter:

- Ch. 2 already commits a locked trial dataset. Hartung and Anderson
  supply the measured reporting-discrepancy rates that justify the
  commitment; Chan's SPIRIT statement specifies exactly which protocol
  items the hash would cover.
- Ch. 5 already threat-models the trial ledger. McCurry's account of the
  valsartan data falsification gives that threat model a named adversary,
  and Olsen and Funning price the monitoring activity the ledger claims
  to displace.
- Ch. 6 already covers programmable consent. Dyke's consent codes and
  ADA-M give the section a machine-readable object to compile against.
- Ch. 7 already covers parametric escrow. Site payments and participant
  reimbursement are a better-motivated escrow example than epidemic
  bonds, because the trigger (a completed visit, a monitored eCRF entry)
  is genuinely verifiable, and the FDA guidance plus Halpern's trials
  supply the constraints that make it non-trivial.

### 3.2 Participant payment is a stronger Ch. 7 example than DeFi

The chapter's existing verdict is that most DeFi-for-health-financing
pitches fail because the oracle problem is relocated rather than solved.
Participant payment inverts this: the trigger is locally verifiable, so
the contract's mechanics genuinely work, and the binding constraints are
regulatory and ethical instead. Grady's payment taxonomy, the FDA
reimbursement guidance, Persad on differential payment within a study,
and Gneezy's crowding-out result together make a section where the
technology succeeds on its own terms and still must answer to an IRB.
That is a more instructive lesson than another failure case, and it uses
the reader's existing training in study design.

### 3.3 Add the non-blockchain counterfactual explicitly

The book's critical register is its distinguishing feature, but a
skeptical reading is only as strong as the alternative it names. Four
additions make the comparison concrete: REDCap for electronic data
capture, a conventional integrated CTMS, Sentinel-style distributed
networks for federated analysis, and BBMRI-ERIC Negotiator for specimen
access brokering. Each is deployed at scale without a ledger. Li's 2024
tertiary review applies the do-you-need-a-blockchain test within health
specifically, complementing the already-cited `wust2018need`.

### 3.4 Two specific gaps worth closing

*Szabo 1997.* The book cites Buterin and Wood but not the paper that
introduced the smart contract seventeen years before Ethereum. This is a
one-line fix with real pedagogical value: it separates the idea from the
platform.

*Re-identification.* The book cites `homer2008resolving` alone. Gymrek's
surname-inference attack completes the canonical pair, and Rocher's
generative model produces calibrated per-individual re-identification
probabilities, which is directly assignable to a biostatistics audience.
Na's re-identification of NHANES accelerometry data is the closest to
what these readers actually handle.

### 3.5 Reconcile the white paper's findings with the book

The white paper concludes that no blockchain trial system has
demonstrated improved fraud detection, adherence, or retention as a
measured outcome, and that the one credible real-world result concerns
consent and monitoring workflow efficiency. That conclusion is sharper
than anything currently in the book's chapters. Whichever chapter carries
the trial material should state it plainly, with the newly available
citations behind it, rather than leaving the book's strongest empirical
claim confined to a separate document.

## 4. Integration

**This file is not yet active in the book build.** `_quarto.yml` sets
`bibliography: references.bib` (a single file, not a list), so Quarto
does not load it, and no chapter cites any of its keys.

Note the existing convention before wiring it in: all 81 entries of
`references-health.bib` are also present in `references.bib`, which
holds 189 unique entries and is the single file the build actually
reads. `references-health.bib` is therefore a thematic source file whose
contents are merged into the authoritative bibliography, not a second
bibliography loaded in parallel. The existing bibliography is 189
entries, not 270.

Two ways to proceed:

1. *Follow the existing convention.* Append the 93 entries to
   `references.bib`, keeping `references-research-lifecycle.bib` as the
   thematic source file. This matches how the health references are
   handled and requires no change to `_quarto.yml`.

2. *Change the convention.* Make `bibliography` a list of the source
   files and stop merging. This removes the duplication between
   `references.bib` and `references-health.bib`, but it is a change to
   how the book is built and should be a deliberate decision.

Option 1 is the smaller change and is recommended unless the duplication
is already considered a problem.

No citation keys or DOIs collide with the existing entries; this was
checked programmatically against the union of both existing files. The
file parses cleanly under pandoc's biblatex reader, and every entry has a
title and, apart from the court case, an author.
