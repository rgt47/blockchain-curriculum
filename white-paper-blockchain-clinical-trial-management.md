# Blockchain and the Clinical Trial Management Problem: Fraud Detection, Data Quality, Adherence, and Attrition
*2026-07-06 17:12 PDT*

## Executive summary

Clinical trial management faces four persistent, partially distinct
integrity and operational problems: outright data fraud, general data
quality and provenance failures, patient non-adherence to protocol,
and patient attrition. Blockchain and distributed-ledger technology
has been proposed as a partial remedy for each, but the strength of
the supporting evidence differs sharply by domain.

For fraud detection and data quality/provenance, a body of
peer-reviewed proposals and small proofs-of-concept exists, alongside
a mature, independently validated statistical toolkit that predates
blockchain and remains the more evidence-backed line of defense. For
adherence and attrition, the literature is markedly thinner: a
targeted PubMed search combining blockchain with adherence terms, and
a separate search combining blockchain with retention/dropout terms,
each returned zero direct hits. The strongest single data point
available, a real pilot deployment (Mak et al., Boehringer
Ingelheim/IBM), explicitly reported no measurable improvement in
protocol non-compliance despite large efficiency and trust gains in
consent and monitoring workflows. This paper synthesizes what the
literature actually supports, distinguishes verified findings from
conceptual proposals, and identifies where the evidence is genuinely
absent rather than merely under-searched.

## 1. Framing the problem

Clinical trial data integrity failures fall on a spectrum from
outright fabrication to more mundane forms of quality erosion:
transcription error, protocol deviation, missing data, selective
reporting, and outcome switching. Separately, trial execution depends
on two behavioral factors largely outside a sponsor's direct control:
whether enrolled patients adhere to the assigned protocol (medication
intake, visit schedules, procedures), and whether those patients
remain in the trial through its planned duration. Fraud and general
data quality problems are primarily about the trustworthiness of
recorded data; adherence and attrition are primarily about patient
behavior, which recorded data can only partially observe.

Blockchain's core properties, cryptographic hashing, append-only
ledger structure, and (in permissioned deployments) multi-party
consensus, offer a specific and narrow capability: making a given
record tamper-evident and time-ordered once it has been written. This
capability maps cleanly onto data quality and provenance problems and
onto detecting post-hoc alteration of fraud. It does not, by
construction, verify the truth of data at the point of entry, and it
does not directly change patient behavior. These distinctions
recur throughout the findings below and materially affect which
claims in the literature are well supported and which are aspirational.

## 2. Fraud detection

### 2.1 The scope of the problem

Fraud is a documented but statistically minor contributor to trial
retractions relative to plagiarism and duplicate publication. In a
systematic review of 39 retractions in the medically-assisted-
reproduction literature, fraud/suspected fraud accounted for 9.3
percent of cases (4 of 39), versus 30.2 percent for plagiarism and
25.6 percent for duplicate publication. Overall retraction rates in
that corpus were low: 0.47 percent across 523,067 fertility/
infertility records and 0.20 percent among RCTs specifically
(93/45,616) [1]. These figures are domain-specific to fertility
research and should not be generalized as a base rate across all of
clinical medicine, but they establish that fraud is the less common,
not the dominant, failure mode among retracted trials.

Confirmed fraud cases show the practical cost of slow detection. A
trial report retracted in 2008 for data falsification was still being
cited 11 years later; of 148 direct citations and 2,542 second-
generation citations through 2019, 96 percent of analyzable
post-retraction direct citations never mentioned the retraction [2].
This is a citation-integrity problem downstream of detection, and
blockchain has no bearing on it; it is included here because it
illustrates the cost of delayed or unresolved fraud findings, which
faster detection would mitigate.

### 2.2 The pre-existing statistical toolkit

Before any blockchain proposal, a substantial statistical toolkit for
detecting fabricated or falsified trial data already existed and
remains, on current evidence, the more rigorously validated approach.

Al-Marzouki et al. (BMJ, seminal) used t-tests and F-tests on
baseline means and variances, and chi-squared tests on terminal-digit
distributions, as fraud screens resting on the principle that
randomization should make baseline covariates statistically similar
across arms. Applied to a suspected fraudulent diet trial (831
coronary heart disease patients), 16 of 22 variables showed
significant variance differences (p-values as low as 2e-133), and 14
of 22 variables showed anomalous digit preference [3].

This approach has been extended and, in places, corrected. Carlisle's
combined baseline p-value method (2017) was designed for continuous
variables; applied naively to dichotomous variables it produces
p-values wrong by orders of magnitude [4]. A newer L-squared test
statistic explicitly derives its distribution through eigenvalue
decomposition of the covariate covariance matrix, avoiding the naive
assumption of covariate independence that would otherwise distort
conclusions [5].

The strongest real-world validation of this toolkit comes from the
ESPS2 trial (Second European Stroke Prevention Study; 7,040 patients,
60 centers, 13 countries, 1989-1995), in which center #2013 (438
patients) was confirmed to have falsified enrollment. A retrospective
Data Inconsistency Score, an unsupervised multivariate monitoring
score computed as a weighted geometric mean of p-values across 838
tests per center, ranked the confirmed fraudulent center second
highest among five flagged centers (DIS = 4.14, flag threshold DIS >=
1.3 at p < 0.05), and indicated the fraud would have been
statistically detectable at approximately 25 percent of final data
volume, well before its actual discovery [6]. This is, to date, the
best available empirical evidence that a statistical method (not a
blockchain-based one) can catch fraud materially earlier than
standard trial conduct otherwise would.

Standard continuous-variable methods do not transfer well to discrete
or questionnaire-based outcome data. Taylor, McEntegart, and Stillman
(2002, foundational) proposed a graphical technique and a formal
randomization test premised on the observation that fabricated
responses fail to reproduce the natural inter-item correlation
structure of genuine questionnaire data, illustrated on a
schizophrenia trial (BPRS) dataset [7].

### 2.3 Blockchain-based fraud prevention proposals

Blockchain proposals for fraud prevention target a different point in
the pipeline: not detecting fabricated data after the fact, but
making certain forms of post-hoc manipulation (retroactive outcome
switching, silently dropping unfavorable data points, altering
timestamps) infeasible in the first place.

Nugent, Upton, and Cimpoesu (2016) proposed a hierarchical Regulator/
Trial smart-contract architecture on a private, permissioned Ethereum
blockchain, explicitly targeting outcome switching, missing data, and
selective publication through tamper-resistant, immutable timestamped
records [8]. Benchoufi and Ravaud (2019) frame the underlying value
proposition as "proof of trust", time-stamping and time-ordering data
so that the trial no longer depends on reliance on institutional
trust, with smart contracts automating IF/THEN quality checks to
reduce selective reporting and outcome switching. They describe
TrialChain, a prototype using a private blockchain synchronized to
the public Ethereum network for data-integrity verification [9].

Critically, Benchoufi and Ravaud's own review states that blockchain
"does not exhaust all problems" and cannot itself prevent fabricated
data from being entered by a compliant insider before it ever reaches
the chain [9]. This is a structural, not incidental, limitation: a
blockchain proposal secures the chain of custody of a record, not the
truthfulness of the underlying observation. No proposal reviewed here
resolves this gap; the pre-existing statistical toolkit described in
section 2.2 remains the primary available defense against pure
fabrication, and is complementary to, rather than superseded by,
blockchain-based provenance.

All fraud-prevention blockchain architectures identified in this
review remain prototypes or proofs-of-concept. No source located
reports validated, multi-site production deployment of a fraud-
prevention blockchain system, nor real-world adoption, regulatory
acceptance, or scalability data.

## 3. Data quality, monitoring, and provenance

A closely related but broader set of proposals targets general data
quality, capture integrity, consent management, and audit-trail
provenance, independent of whether the underlying failure is
fraudulent or merely careless.

BlockTrial (Maslove et al., 2018) is a proof-of-concept Ethereum
smart-contract system with separate Patient and Researcher contracts.
Clinical data itself is kept off-chain in a conventional database;
only hashed query results and consent/access transactions are written
to the chain, giving patients the ability to grant and revoke
researcher access and producing a durable, transparent audit log of
data-access events [10]. This is explicitly a consent-and-provenance
system, distinct from the outcome-switching focus of Nugent et al.
and Benchoufi and Ravaud.

Scrybe is a proposed permissioned blockchain for storing proof of
clinical trial data provenance, integrating context-aware smart
devices and wearable/IoT sensor data into the trial data stream [11].
A separate Hyperledger Fabric-based framework proposes automating six
distinct clinical trial processes through permissioned channels and
smart contracts, chosen for pluggable consensus, encryption, and
identity-management components [12].

The one deployment in this review with real, quantitative outcome
data is a Hyperledger Fabric pilot (Mak et al., Blockchain in
Healthcare Today, 2021) run within an active phase II trial across
five sites and twelve participants (2019), covering consent and
reconsent tracking. It reduced mean monitoring-visit time from 475 to
7 minutes and mean per-visit monitoring cost from EUR 722 to EUR 10,
and 91, 82, and 63 percent of patients reported increased trust,
transparency, and empowerment respectively [13]. This is a genuine,
measured operational improvement, and it is the strongest evidence in
this entire review of a real efficiency gain from blockchain
deployment in an active trial. It is important to note precisely what
it measured: consent-monitoring efficiency and patient-reported
trust, not data fraud detection, not adherence, and, as discussed in
section 4, explicitly not a reduction in protocol non-compliance.

A 2026 JMIR Medical Informatics systematic review of blockchain smart
contracts for clinical trial automation concludes that the field
remains "dominated by simulation-based prototypes, primarily
Ethereum-dependent," and lacks cost-effectiveness, governance, or
real-deployment evidence at scale [14]. This is the most direct
critique available in the literature of the field's overall maturity,
and it applies across the fraud-prevention and data-quality
proposals alike.

## 4. Adherence monitoring

This is where the evidentiary base becomes markedly thinner. A PubMed
query combining blockchain, clinical trial, and adherence-related
terms returned essentially no direct hits during this research pass;
what exists is either conceptual architecture, vendor gray
literature, or a real pilot that measured an adjacent outcome and
found no adherence effect.

The Mak et al. pilot described in section 3 is the one real
deployment with quantitative data touching on this question, and its
finding cuts against the optimistic case: the study explicitly
reported no measurable difference in protocol non-compliance between
the blockchain-supported arm and standard monitoring, despite large
gains in monitoring efficiency and patient-reported trust [13]. This
should be read as direct, if limited (single small trial), evidence
that blockchain-based consent/monitoring infrastructure does not, by
itself, change adherence behavior.

Conceptual proposals go further than deployed systems have yet
demonstrated. An AMIA 2018 proceedings paper proposes a smart-contract
framework for real-time, tiered-access trial data sharing among
sponsors, sites, and regulators, framed as enabling "persistent
monitoring," but this is a design/simulation study, not a deployment
with adherence-specific outcome measurement [15]. A 2024 Drug
Discovery Today article discusses blockchain as a conceptual "forcing
function" for adherence reporting and automatic smart-contract
verification of protocol compliance, built on Ethereum-plus-IPFS
architectures, but remains narrative and non-empirical [16]. A vendor
case study (not peer-reviewed) describes an IoT pill-dispensing device
that logs every dispensing event to a blockchain ledger, explicitly
pitched against the commonly cited figure that up to half of trial
medication non-compliance goes undetected; no named trial, no
independent verification, and no published outcome data support this
claim [17].

No dedicated, peer-reviewed study describing patient-facing token or
incentive mechanisms tied to measured adherence outcomes was located.
General review and proposal papers mention token-based incentive
concepts abstractly, for example rewarding data contribution or site
participation, but none operationalizes a patient-facing adherence
incentive with reported results. This is best characterized as a
genuine gap in the literature rather than a search failure, given that
a direct PubMed query for the combination returned zero hits.

## 5. Attrition and retention

The evidentiary base here is similarly thin, and for the same
structural reason: a PubMed query combining blockchain with retention
and dropout/attrition terms returned zero hits.

The mechanisms proposed in the literature to address attrition through
blockchain fall into three categories, none with reported retention
outcome data. First, transparent consent and data-ownership models,
intended to build patient trust and thereby reduce dropout, as in
BlockTrial [10] and the Mak et al. pilot's patient-reported trust and
empowerment findings [13], though again, that pilot did not measure
retention as an endpoint. Second, decentralized or direct-to-patient
trial architectures enabled by blockchain-based smart contracts, aimed
at reducing the participation burden thought to drive dropout, as
proposed in a pair of AMIA proceedings papers (2019, 2020) describing
smart-contract modules for patient recruitment, engagement, and
persistent monitoring in home-based virtual trials [18, 19]. Third,
non-monetary incentive mechanisms, including a 2026 JMIR proposal to
use blockchain-minted digital collectibles as engagement incentives
through trial completion, explicitly motivated by the recruitment and
retention problem but entirely conceptual, with no trial data [20].

The one large-scale, non-trial-specific initiative identified is
PharmaLedger, an EU Innovative Health Initiative consortium project
building blockchain-based e-consent and e-enrollment infrastructure
for patient-centric decentralized trials across multiple pharmaceutical
sponsors. Available reporting on this initiative is program-level
gray literature (CORDIS and IHI factsheets) rather than peer-reviewed
outcome data, and does not report retention metrics [21].

The most directly relevant peer-reviewed synthesis, the same 2026
JMIR systematic review cited in sections 3 and 4, explicitly
characterizes the broader field as dominated by simulation-based
prototypes lacking real-deployment evidence [14], a critique that
applies with particular force to attrition, where no deployment
evidence of any kind was located.

## 6. Cross-cutting adoption barriers

Several barriers recur across all four problem domains and are
independent of which specific blockchain application is being
considered. Blockchain immutability is in tension with data-subject
erasure rights under GDPR-type frameworks, since personal data or
even hashes tied to individuals may need to be removable in ways an
append-only ledger resists by design. No source reviewed here
documents a clear regulatory pathway or acceptance decision from FDA,
EMA, or MHRA treating blockchain audit trails as equivalent to
existing 21 CFR Part 11 or Good Clinical Practice electronic-record
requirements; this remains an open question in the literature rather
than a resolved one. Scalability, interoperability with existing
electronic data capture (EDC) systems, and organizational/governance
resistance to permissioned-node control are cited repeatedly as
barriers, generally as narrative critique embedded in review papers
rather than as the subject of dedicated empirical study.

## 7. Synthesis and research gaps

Ranking the four problem areas by strength of supporting evidence,
from strongest to weakest:

1. **Data quality and provenance monitoring efficiency.** One real
   pilot with quantitative operational outcomes (Mak et al.) plus
   several credible architectural proposals. This is where blockchain
   has the clearest, if narrow, demonstrated value: reducing the cost
   and time of consent and monitoring workflows and increasing
   patient-reported trust in data handling.

2. **Fraud detection.** A rigorous, independently validated
   statistical toolkit exists and is the stronger current line of
   defense; blockchain proposals target a genuinely different failure
   mode (post-hoc tampering with already-entered records) but remain
   prototype-stage, and the literature itself concedes blockchain
   cannot prevent insider fabrication at the point of entry.

3. **Adherence.** Conceptual and prototype proposals only, with the
   single relevant real-world data point (Mak et al.) finding no
   measurable adherence improvement. Wearable/IoT-verified compliance
   and token-incentive adherence mechanisms appear in the literature
   as ideas, not as tested interventions.

4. **Attrition/retention.** The thinnest evidence base of the four.
   No study located directly measures a blockchain intervention's
   effect on trial dropout or retention. Proposed mechanisms (trust-
   building consent transparency, decentralized trial architectures,
   non-monetary incentives) are plausible on their face but entirely
   untested against retention as an outcome.

The overall pattern across all four domains is consistent: blockchain
proposals are conceptually well-matched to the tamper-evidence and
provenance problems inherent in trial data management, have produced
one credible real-world efficiency result, but have not yet produced
peer-reviewed evidence of improved fraud detection, improved
adherence, or reduced attrition as measured trial outcomes. Claims to
the contrary found during this research (for example, vendor case
studies of blockchain pill dispensers) are gray literature, self-
reported, and lack independent verification or named trial results.

Open questions meriting further investigation: whether any blockchain
trial system has progressed from prototype to a real multi-site
deployment with reported adherence or retention outcomes; what FDA,
EMA, and MHRA guidance says, if anything, about blockchain audit
trails relative to existing electronic-record requirements; how CRO
and sponsor central statistical monitoring systems combine the
various fraud-detection methods in practice and what their real-world
false-positive and false-negative rates are across many trials rather
than single case studies; and whether any study has directly compared
blockchain architectures to non-blockchain alternatives, such as
cryptographic timestamping or conventional centralized audit trails,
on a cost-effectiveness basis.

## References

1. Systematic review of retractions in medically-assisted-reproduction
   literature. PMC10427242.
   https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10427242/

2. Citation persistence of a retracted, falsified clinical trial
   report. Scientometrics.
   https://link.springer.com/article/10.1007/s11192-020-03631-1

3. Al-Marzouki S, et al. Are these data real? Statistical methods for
   the detection of data fabrication in clinical trials. BMJ. PMC1181267.
   https://pmc.ncbi.nlm.nih.gov/articles/PMC1181267/

4. Application and limitations of Carlisle's combined baseline
   p-value screening method. arXiv:2209.00131.
   https://arxiv.org/pdf/2209.00131

5. A covariance-aware L-squared test statistic for baseline
   comparison fraud screening. PLOS ONE.
   https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0239121

6. Retrospective validation of a multivariate Data Inconsistency Score
   against the ESPS2 confirmed fraud case. Therapeutic Innovation and
   Regulatory Science.
   https://link.springer.com/article/10.1007/s43441-021-00341-5

7. Taylor RN, McEntegart DJ, Stillman EC. Statistical techniques to
   detect fraud and other data irregularities in clinical
   questionnaire data. Drug Information Journal, 2002.
   https://link.springer.com/article/10.1177/009286150203600115

8. Nugent T, Upton D, Cimpoesu M. Improving data transparency in
   clinical trials using blockchain smart contracts. PMC5357027.
   https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5357027/

9. Benchoufi M, Ravaud P. Blockchain technology for improving clinical
   research quality. Frontiers in Blockchain, 2019.
   https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2019.00023/full

10. Maslove DM, et al. Using blockchain technology to manage clinical
    trials data: a proof-of-concept study (BlockTrial). PMC6320404.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC6320404/

11. Scrybe: a permissioned blockchain for clinical trial data
    provenance. arXiv:2109.05649.
    https://arxiv.org/pdf/2109.05649

12. Hyperledger Fabric framework for clinical trial process
    automation. arXiv:1902.03975.
    https://arxiv.org/pdf/1902.03975

13. Mak KK, et al. Blockchain-enforced informed consent and
    monitoring pilot in an active phase II trial. Blockchain in
    Healthcare Today, 2021. PMC9907430.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC9907430/

14. Blockchain smart contracts for automating clinical trials:
    systematic review and proposed system architecture. JMIR Medical
    Informatics, 2026.
    https://medinform.jmir.org/2026/1/e76980

15. Applying blockchain technology for health information exchange and
    persistent monitoring for clinical trials. AMIA Annual Symposium
    Proceedings, 2018. PMC6371378.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC6371378/

16. Enhancing clinical drug trial monitoring with blockchain
    technology. Drug Discovery Today, 2024.
    https://www.sciencedirect.com/science/article/abs/pii/S1551714424002672

17. IoT-based pill dispensing devices case study (vendor gray
    literature, not peer-reviewed).
    https://www.softlabsgroup.com/case-studies/iot-based-pill-dispensing-devices

18. Zhuang Y, et al. Blockchain framework for clinical trial
    recruitment. AMIA Annual Symposium Proceedings, 2019. PMC7153067.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC7153067/

19. Zhuang Y, et al. Blockchain framework for virtual clinical trials.
    AMIA Annual Symposium Proceedings, 2020. PMC8075489.
    https://pmc.ncbi.nlm.nih.gov/articles/PMC8075489/

20. Unique digital images as engagement incentives in clinical
    trials. JMIR, 2026.
    https://doi.org/10.2196/88022

21. PharmaLedger decentralized trials project. European Commission
    CORDIS and Innovative Health Initiative factsheets.
    https://cordis.europa.eu/article/id/444094-demonstrating-blockchain-s-transformative-potential-for-healthcare
    https://www.ihi.europa.eu/projects-results/project-factsheets/pharmaledger

## Methodology note

This paper synthesizes two research passes: (a) a multi-agent deep-
research workflow (5 search angles, 22 sources fetched, 25 claims
under 3-vote adversarial verification, 23 confirmed) covering fraud
detection and general data quality/provenance, documented in a
companion file (clinical-trial-fraud-blockchain-references.md in this
repository), and (b) two targeted follow-up research passes on
adherence and on attrition/retention specifically, conducted to fill
gaps not covered by the original workflow. Findings from pass (a)
carry adversarial verification; findings from pass (b) reflect a
single research agent's search and synthesis without independent
verification, and are labeled with confidence levels drawn from
source venue and directness of support. Readers should treat sections
4 and 5 as reporting the state of a thin and largely unverified
literature, not as evidence that blockchain-based adherence or
retention interventions have been shown to work.

---
*Rendered on 2026-07-06 at 17:12 PDT.*<br>
*Source: ~/prj/tch/11-blockchain-curriculum/white-paper-blockchain-clinical-trial-management.md*
