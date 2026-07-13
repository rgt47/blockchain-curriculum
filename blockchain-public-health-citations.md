# Blockchain in Public Health: Evaluated Citation List
*2026-07-13 16:45 AEST*

Deep literature search across seven application domains, filtered to
scientifically serious work only. Inclusion bar: the study must rest on
real data or real subjects, state a comparator or baseline, and report
its limitations honestly. Architecture-diagram prototypes evaluated on
synthetic patients are excluded, as are retractions, defunct ventures,
and papers retained only as specimens of poor practice.

Every PMID and DOI below was verified by a search agent against a
PubMed record or a successfully fetched publisher or agency page.
See 'Epistemic status' at the end for what that does and does not
guarantee.

## Summary of the evidence

The blockchain-for-health literature is a literature, not a practice.
Its own systematic reviews converge on this verdict from independent
directions, and they are the most valuable citations available:

- Ng et al. (2021) screened 85,375 articles, included 415 full
  reports, and found 9 (2.2 percent) reached real-world clinical
  application.
- Lacson et al. (2024), restricting to work both implemented and
  quantitatively evaluated, found 11 articles in the entire biomedical
  corpus, of which exactly one demonstrated deployment at a medical
  facility.
- Fang et al. (2021) found all 18 tethered blockchain personal-health-
  record designs, the only architecture that could integrate with a
  real health system, remained conceptual. Zero implementations.
- Chandak et al. (2026), searching through March 2025, located 16
  empirical studies worldwide, 'primarily prototypes and pilots',
  constituting 'non-production analyses'.
- Abd-Alrazaq et al. (2020) found that of 19 COVID-19 blockchain
  studies, zero reported expected latency or scalability.

Against this, two bodies of rigorous work define the honest baseline.
First, the cryptographic literature (secure multiparty computation and
homomorphic encryption) achieves genuine privacy for genomic analysis,
and in the strongest papers the blockchain is either absent or confined
to bookkeeping. Second, the digital public-health intervention that
demonstrably worked during COVID-19, the NHS exposure-notification app,
used Bluetooth and public-key cryptography and no ledger at all, and was
evaluated with two independent estimators that its authors reported
honestly despite a two-fold disagreement.

The pharmaceutical supply chain supplies the field's one natural
experiment, and blockchain lost it. See section 5.

## 1. The maturity evidence: rigorous systematic reviews

These are the load-bearing citations for the book's sceptical thesis.
Each is PRISMA-based or equivalent, and each reports counts that
quantify the gap between proposal and deployment.

| Key | Citation | Finding | PMID |
|---|---|---|---|
| `ng2021blockchain` | Ng et al., *Lancet Digit Health* 3(12):e819-e829 | 415 reports; 9 (2.2%) real-world | 34654686 |
| `lacson2024biomedical` | Lacson et al., *JAMIA* 31(6):1423-1435 | 11 implemented + evaluated; 1 deployed | 38726710 |
| `fang2021phr` | Fang et al., *JMIR* 23(4):e25094 | 18/18 tethered PHR designs conceptual | 33847591 |
| `chandak2026ehr` | Chandak et al., *BMC Med Inform Decis Mak* 26(1) | 16 empirical studies; non-production | 41943148 |
| `abdalrazaq2020covid` | Abd-Alrazaq et al., *Comput Methods Programs Biomed Update* 1:100001 | 0/19 reported latency or scalability | 34337586 |
| `hasselgren2020scoping` | Hasselgren et al., *Int J Med Inform* 134:104040 | Scoping review; establishes proposal-volume baseline | 31865055 |
| `kuo2019platforms` | Kuo et al., *JAMIA* 26(5):462-478 | 10 platforms x 21 features; usable matrix | 30907419 |
| `schmeelk2022interop` | Schmeelk et al., *JAMIA Open* 5(3):ooac068 | 152 screened, 15 relevant (signal-to-noise) | 35911668 |
| `fonseca2024his` | Fonseca et al., *IJERPH* 21(11):1512 | 4,864 to 73; latency/throughput are the top metrics reported | 39595779 |
| `phuyal2026consent` | Phuyal et al., *JMIR Med Inform* 14:e88536 | 55 studies; few real deployments; erasure conflict unresolved | 42332966 |
| `beyene2022genomics` | Beyene et al., *JAMIA* 29(8):1433-1444 | DLT in genomics scoping review, 60 papers | 35595301 |

`lacson2024biomedical` strictly supersedes the existing
`kuo2017blockchain` and `agbo2019systematic` on the question that
matters. Retain the older two as historical markers, but the 11-and-1
figure should carry the argument. Note it comes from the Kuo and
Ohno-Machado group, that is, from inside the field.

`fonseca2024his` supports a sharp observation: the field's most-reported
outcome measures are transaction latency and throughput. It audits its
own plumbing rather than any patient.

## 2. Blockchain systems with real subjects or real data

These are the only blockchain-health studies that clear the bar. There
are not many, and that is the point.

**`kuo2020explorerchain`** Kuo TT, Gabriel RA, Cidambi KR,
Ohno-Machado L (2020). 'ExplorerChain: expectation propagation logistic
regression on permissioned blockchain.' *JAMIA* 27(5):747-756. PMID
32364235.
The single most scientifically serious paper in the corpus.
Decentralised online logistic regression across institutions, evaluated
on three real healthcare and genomic datasets against a centralised
baseline. The authors report honestly that discrimination was
statistically similar to the central-server counterpart and that
runtime was somewhat worse. The ledger bought removal of a single point
of failure and cost speed; it did not improve the model. **Recommended
as the book's primary worked example**: it poses 'what did
decentralisation cost, and was the trade worth it?' with real numbers.

**`huh2022metory`** Huh KY, Moon SJ, Jeong SU, et al. (2022).
'Evaluation of a blockchain-based dynamic consent platform (METORY) in
a decentralized and multicenter clinical trial using virtual drugs.'
*Clin Transl Sci* 15(5):1257-1268. PMID 35157788.
The only genuine dataset in the trials literature. 60 subjects, two
centres, with protocol amendments deliberately injected. Consent
proportion 95.7 +/- 13.7 percent; median re-consent response 0.2 h;
drug-taking 90.8 +/- 19.2 percent but schedule compliance only 69.1
+/- 27.0 percent, degrading after major amendments. Real n, real SDs,
and a negative finding.

**`kuo2023logging`** Kuo TT, Pham A, Edelson ME, et al. (2023).
'Blockchain-enabled immutable, distributed, and highly available
clinical research activity logging system for federated COVID-19 data
analysis from multiple institutions.' *JAMIA* 30(6):1167-1178. PMID
36916740.
Built on 9,166 real consortium SQL queries with an explicit
head-to-head against a centralised baseline. Log write ~2 s on-chain
versus 5-9 s baseline; query ~0.4 s versus ~2.1 s. A rare case where the
ledger beats the control on a measured task, and rarer still for having
a control at all.

**`wong2019untrustworthy`** Wong DR, Bhattacharya S, Butte AJ (2019).
'Prototype of running clinical trials in an untrustworthy environment
using blockchain.' *Nat Commun* 10(1):917. PMID 30796226.
Replays raw data from a real completed trial onto a blockchain portal
and adversarially tests tamper resilience. Names its own status
honestly.

**`hirano2020sandbox`** Hirano T, Motohashi T, Okumura K, et al. (2020).
'Data validation and verification using blockchain in a clinical trial
for breast cancer: regulatory sandbox.' *JMIR* 22(6):e18938. PMID
32340974.
Real breast-cancer trial under a Japanese Cabinet Office regulatory
sandbox. The strongest regulatory-legitimacy anchor in the literature.

**`motohashi2019mhealth`** Motohashi T, Hirano T, Okumura K, et al.
(2019). 'Secure and scalable mHealth data management using blockchain
combined with client hashchain.' *JMIR* 21(5):e13385. PMID 31099337.
Real insomnia patients in a registered trial (UMIN000032951). The
client-side hashchain is the only serious attempt in the literature to
close the oracle gap at the point of capture.

**`glicksberg2020cgt`** Glicksberg BS, Burns S, Currie R, et al. (2020).
'Blockchain-authenticated sharing of genomic and clinical outcomes data
of patients with cancer: prospective cohort study.' *JMIR* 22(3):e16810.
PMID 32196460.
A real prospective cohort of N=18, with a completeness comparison of two
EHR extraction formats against source documents (n=17, difference not
significant). The tiny n is itself a teachable point about pilots.

**`mamo2020dwarna`** Mamo N, Martin GM, Desira M, et al. (2020).
'Dwarna: a blockchain solution for dynamic consent in biobanking.'
*Eur J Hum Genet* 28:609-626. PMID 31844175.
Deployed as the consent portal for the Malta Biobank. The canonical
resolution of the erasure-versus-immutability conflict, which is: put
nothing personal on the chain. That resolution is also an admission that
the chain is not doing the interesting work.

**`oakley2022scrybe`** Oakley J, Worley C, Yu L, et al. (2022).
'Scrybe: a secure audit trail for clinical trial data fusion.' *Digital
Threats* 4(2):24. PMID 37937206.
The only serious treatment of 21 CFR Part 11 and ISO 27789, walking
control by control and arguing why Ethereum-family chains fail them.
Essential for any audit-trail claim the book makes.

**`teo2024retinal`** Teo ZL, Zhang X, Yang Y, et al. (2024).
'Privacy-preserving technology using federated learning and blockchain
in protecting against adversarial attacks for retinal imaging.'
*Ophthalmology*. PMID 39424148.
27,145 real images across three countries, non-IID, with adversarial
robustness measured against baselines and the blockchain overhead
quantified (~5 s per global epoch). Cite critically: the robustness
gains come from the aggregation method, not the ledger, and the paper
is honest about this.

### The iDASH benchmark set

The field's only rigorous, reproducible, code-available benchmarks, and
they measure the one thing blockchain genuinely does well: tamper-
evident logging of access to controlled-access data. Cite as a set.

- **`kuo2021benchmark`** Kuo TT, Bath T, Ma S, et al. (2021).
  *Int J Med Inform* 154:104559. PMID 34474309. ~60 s to import 4,000
  records from 4 sites; ~0.5 s per retrieval query. Code public.
- **`gursoy2020logging`** Gursoy G, Bjornson R, Green ME, Gerstein M
  (2020). *BMC Med Genomics* 13. PMID 32693796. Competition winner.
  12 s / 120 MB at 100,000 log entries; memory linear to 470 MB at
  600,000. Explicit time-space tradeoff curve.
- **`ozdayi2020immutable`** Ozdayi MS, Kantarcioglu M, Malin B (2020).
  *BMC Med Genomics* 13. PMID 32693807. Blockchain versus SQLite
  head-to-head: 0.2 s to 6 s difference by query type.
- **`ma2020audit`** Ma S, Cao Y, Xiong L (2020). *BMC Med Genomics* 13.
  PMID 32693835. Hierarchical timestamps: at least an order of
  magnitude speedup on range queries; 25 percent storage reduction.

### Real DSCSA pilots (use with a stated conflict caveat)

- **`chien2020bruinchain`** Chien W, de Jesus J, Taylor B, et al.
  (2020). *Blockchain Healthc Today* 3. PMID 36777051. An official FDA
  DSCSA pilot at UCLA Health with real patients and real drugs.
  Caveat required: the 100 percent success rates come from a small
  curated single site, the vendor co-authored, and the per-unit cost
  figures ($0.17 falling to $0.13) are projections, not measurements.
  The absence of any confidence interval on the derived '$183 million
  annual saving' is itself an exercise.
- **`ashkar2021xatp`** Ashkar GL, Patel KS, de Jesus J, et al. (2021).
  *Blockchain Healthc Today* 4. PMID 36777488. Cite chiefly for the
  finding that undercuts the thesis: 86 percent accuracy on
  serialisation matching, with the 14 percent error rate attributed to
  human factors. The ledger was not the failure mode. The humans were.

## 3. The honest baseline: rigorous non-blockchain science

The book's thesis is that the ideas that succeeded in health shed the
word 'blockchain' and won as cryptographic-signature infrastructure.
These citations are what that claim rests on.

### Digital public health that actually worked

- **`wymant2021nhsapp`** Wymant C, Ferretti L, Tsallis D, et al. (2021).
  'The epidemiological impact of the NHS COVID-19 app.' *Nature*
  594(7863):408-412. PMID 33979832.
- **`kendall2023nhsapp`** Kendall M, Tsallis D, Wymant C, et al. (2023).
  'Epidemiological impacts of the NHS COVID-19 app in England and Wales
  throughout its first year.' *Nat Commun* 14(1):858. PMID 36813770.

16.5M users; roughly 1M cases, 44,000 hospitalisations and 9,600 deaths
averted in year one. **The pedagogical core**: cases averted were
estimated two independent ways, by modelling (284,000; range
108,000-450,000) and by matched-neighbour statistical comparison
(594,000; 95% CI 317,000-914,000). The estimators disagree roughly
two-fold on the same quantity and the authors report the discrepancy
honestly. This is a ready-made worked example in model-based versus
design-based inference. Bluetooth and public-key cryptography. No
ledger.

- **`ramos2022events`** Ramos R, et al. (2022). 'SARS-CoV-2
  transmission risk screening for safer social events: a non-randomised
  controlled study.' *Sci Rep* 12:12794. PMID 35896583. 1,351 attendees
  versus 4,050 matched controls; **null result** (difference -1.8 per
  100,000 person-days, 95% CI -22.8 to 19.3). The only controlled study
  with any plausible blockchain involvement, and it found nothing.
- **`muwonge2025haulage`** Muwonge A, Bessell PR, Bronsvoort MB, et al.
  (2025). 'Assessing the impact of haulage drivers in Uganda's COVID-19
  Delta wave.' *J Epidemiol Glob Health* 15(1):54. PMID 40178677.
  625,422 national surveillance records with a fitted SIR model and a
  counterintuitive iatrogenic finding: mandatory border testing-and-
  waiting *increased* risk in Tororo by up to 6 percent. Excellent
  exercise material. Note the blockchain framing prominent in the 2022
  protocol has evaporated from the 2025 results paper.

### Cryptography that delivers what blockchain promises

- **`cho2018secure`** Cho H, Wu DJ, Berger B (2018). 'Secure
  genome-wide association analysis using multiparty computation.'
  *Nat Biotechnol* 36:547-551. PMID 29734293.
- **`blatt2020secure`** Blatt M, Gusev A, Polyakov Y, Goldwasser S
  (2020). 'Secure large-scale genome-wide association studies using
  homomorphic encryption.' *PNAS* 117(21):11608-11613. PMID 32398369.
  100,000 individuals x 500,000 SNPs in 5.6 h on one node, 11 min on 31.
  The crispest cost-of-privacy numbers available.
- **`froelicher2021famhe`** Froelicher D, Troncoso-Pastoriza JR,
  Raisaro JL, et al. (2021). 'Truly privacy-preserving federated
  analytics for precision medicine with multiparty homomorphic
  encryption.' *Nat Commun* 12:5910. PMID 34635645. Reproduces two
  published centralised studies (Kaplan-Meier survival; a GWAS) in a
  federated encrypted setting with no intermediate leakage. The word
  'truly' is a deliberate shot at federated-learning papers that leak
  via gradients.
- **`hie2018pharmacological`** Hie B, Cho H, Berger B (2018). 'Realizing
  private and practical pharmacological collaboration.' *Science*
  362(6412):347-350. PMID 30337410. SMPC over >1M interactions,
  more accurate than the non-private state of the art, and the
  discovered interactions were experimentally validated by assay. Uses
  no blockchain, which is the argument.
- **`yang2022trustgwas`** Yang M, Zhang C, Wang X, et al. (2022).
  'TrustGWAS.' *Cell Syst* 13(9):752-767. PMID 36041458. Full encrypted
  PLINK-equivalent pipeline naming the specific statistical tests (QC,
  LD pruning, PCA, chi-square, Cochran-Armitage, covariate regression).
  100,000 individuals x 1M variants in under 50 h.
- **`li2023collagene`** Li W, Kim M, Zhang K, et al. (2023).
  'COLLAGENE enables privacy-aware federated and collaborative genomic
  data analysis.' *Genome Biol* 24:204. PMID 37697426. Includes a secure
  meta-analysis protocol.
- **`grishin2021citizen`** Grishin D, Raisaro JL, Troncoso-Pastoriza JR,
  et al. (2021). 'Citizen-centered, auditable and privacy-preserving
  population genomics.' *Nat Comput Sci* 1:192-198. PMID 38183193. The
  honest architecture: HE and SMPC do the privacy, the blockchain does
  the audit log, and the two are not conflated.
- **`warnat2021swarm`** Warnat-Herresthal S, Schultze H, Shastry KL, et
  al. (2021). 'Swarm learning for decentralized and confidential
  clinical machine learning.' *Nature* 594:265-270. PMID 34040261.
  >16,400 blood transcriptomes, >95,000 chest X-rays. Cite critically:
  the claim that it 'completely fulfils local confidentiality
  regulations by design' is an assertion, not a proof, and parameter
  sharing is exactly the channel gradient-inversion attacks exploit.
  Contrast directly with `froelicher2021famhe`.

### Re-identification and privacy statistics (the real mathematics)

- **`homer2008resolving`** Homer N, Szelinger S, Redman M, et al.
  (2008). *PLoS Genet* 4(8):e1000167. PMID 18769715. Detects an
  individual contributing under 0.1 percent of a mixture. The direct
  cause of NIH withdrawing aggregate GWAS summary statistics from open
  access. An explicit likelihood test statistic with derived limits.
- **`raisaro2017beacon`** Raisaro JL, Tramer F, Ji Z, et al. (2017).
  'Addressing Beacon re-identification attacks.' *JAMIA* 24(4):799-805.
  PMID 28339683. **The best statistics-ready example in the set**: a
  likelihood-ratio membership-inference test with a power curve, and a
  query-budget mitigation structurally identical to a privacy budget.
- **`johnson2013gwas`** Johnson A, Shmatikov V (2013).
  'Privacy-preserving data exploration in genome-wide association
  studies.' *KDD* 2013:1079-1087. PMID 26691928. Differential privacy
  for the actual GWAS workflow, with explicit epsilon and utility-versus-
  epsilon curves. Remarkably little has improved on it.
- **`elhussein2024sharing`** Elhussein A, et al. (2024). 'A framework
  for sharing of clinical and genetic data for precision medicine
  applications.' *Nat Med* 30:3155-3163. PMID 39227443. Demonstrates
  increased statistical power for rare-disease analysis from pooling.
  The power-versus-privacy tradeoff is exactly the book's subject.
- **`aherrahrou2024privacy`** Aherrahrou N, Tairi H, Aherrahrou Z
  (2024). *Brief Bioinform* 25(5):bbae356. PMID 39073827. The best
  recent taxonomy (HE / SMPC / DP / FL) for GWAS privacy.

### Standards that solve the problem without a chain

- **`rfc3161`** Adams C, Cain P, Pinkas D, Zuccherato R (2001). RFC
  3161, *Internet X.509 PKI Time-Stamp Protocol*. IETF.
  A Time Stamping Authority accepts a hash, never the raw data, and
  returns a signed token proving the datum existed before a given time.
  This is the entire integrity value proposition of most health-
  blockchain papers, standardised in 2001, at negligible cost.
- **`rfc6962`** Laurie B, Langley A, Kasper E (2013). RFC 6962,
  *Certificate Transparency*. IETF. Append-only Merkle tree with
  O(log n) inclusion and consistency proofs. Tamper-evidence without
  consensus, mining, or tokens, running at internet scale for a decade.
- **`trillian`** Google Trillian, *Transparent Logging: A Guide*.
  Generalises Certificate Transparency to arbitrary data. The
  production-grade answer to 'we need a tamper-evident health audit
  log'.
- **`rehm2021ga4gh`** Rehm HL, Page AJH, Smith L, et al. (2021).
  'GA4GH: international policies and standards for data sharing across
  genomic research and healthcare.' *Cell Genomics* 1(2):100029. PMID
  35072136. The institutional competitor to blockchain (Beacon,
  Passports, DUO, htsget), and the one that actually got adopted.
- **`ncsc2021dlt`** UK National Cyber Security Centre (2021).
  *Distributed Ledger Technology* white paper.
  A government security authority stating the three-condition test
  (multiple writers, mutual distrust, no trusted central authority) and
  the oracle problem outright: 'the correctness of data in the ledger is
  not guaranteed.' Regulator-grade weight to complement `wust2018need`.

The existing `narayanan2017pedigree` is load-bearing here and should be
promoted: the hash-linked append-only log traces to Haber and Stornetta
circa 1991 and is separable from consensus. A health consortium has a
trusted operator by definition, so it fails the third prong of the NCSC
test; drop the consensus layer that the trusted operator makes
unnecessary and what remains is a Merkle log available since 2001.

## 3a. The Estonia correction (act on this first)

`guardtime2016estonia` is cited in both the preface and 00-intro as
deployment evidence. It is a vendor source, and the scholarly literature
contradicts the reading it invites.

**`semenzin2022estonia`** Semenzin S, Rozas D, Hassan S (2022).
'Blockchain-based application at a governmental level: disruption or
illusion? The case of Estonia.' *Policy and Society* 41(3):386-401.
DOI 10.1093/polsoc/puac014.

What Estonia actually deployed is KSI, a hash-linked timestamping and
tamper-evident logging service, not a decentralised ledger. X-Road, the
actual interoperability backbone carrying the health data, uses no
distributed ledger technology at all, per the Nordic Institute for
Interoperability Solutions. An Estonian health official quoted in the
study puts it plainly: 'We are just using the blockchain data structures
to inform, to make the existing institutions stronger.' The system
reinforces centralisation rather than dispersing it.

This is not a footnote. It is the book's thesis, confirmed in the one
deployment everyone cites as the counterexample: Estonia deployed
integrity verification for audit logs and called it blockchain. Cite
`semenzin2022estonia` wherever `guardtime2016estonia` appears, and
consider making the correction itself a worked example.

Two further quantitative additions from the same search:

- **`fang2021commercial`** Fang HSA (2021). *Blockchain in Healthcare
  Today* 4. PMID 36777489. Screened 4,087 actively tracked crypto
  projects: 10 were health projects with nonzero market cap and at least
  two years' existence. Health is **0.24 percent of projects and under
  0.01 percent of total market capitalisation**, with zero health
  projects in the top 100. Note the inclusion criterion (nonzero market
  cap, two years old) already selects on survival, which makes the paper
  a clean survivorship-bias lesson in its own right.
- **`margheri2020provenance`** Margheri A, Masi M, Miladi A, et al.
  (2020). *Int J Med Inform* 141:104197. PMID 32540775. IHE, HL7, FHIR
  and W3C PROV on Hyperledger Fabric, integrated with a commercial EHR
  engine, no PHI on chain by design, overhead in milliseconds. The best
  engineering paper in the FHIR sub-area and a better citation than most
  FHIRChain successors.
- **`hylock2019healthchain`** Hylock RH, Zeng X (2019). *JMIR*
  21(8):e13592. PMID 31471959. The redactable-block design is one of the
  few honest engineering answers to the erasure problem in
  `finck2018gdpr`.
- **`soohoo2026iagree`** Soohoo SL, et al. (2026). *JAMIA Open*
  9(3):ooag111. PMID 42344107. The state of the art for FHIR plus
  blockchain plus consent, installed at three health systems, and the
  authors are explicit that it runs on **test patients**. Even the best
  2026 work is pre-deployment.
- **`odonoghue2019tradeoffs`** O'Donoghue O, Vazirani AA, Brindley D,
  Meinert E (2019). *JMIR* 21(5):e12426. PMID 31094344. Frames the design
  space as explicit trade-offs between desirable but incompatible
  features. Complements `wust2018need`.

## 4. Health credentials: the cleanest teaching claim

The two credential systems that reached planetary scale used no
blockchain. The two that put a ledger in the stack used it only as a
key and schema registry, and both are dead.

- **EU Digital COVID Certificate**: two-tier X.509 PKI. CBOR payload,
  COSE-signed, base45-encoded QR. The gateway is a *centralised* hub
  distributing signer public keys. **2.3 billion certificates, 78
  countries.** No ledger, no consensus, no chain. Primary source:
  Commission Implementing Decision (EU) 2021/1073.
  `stanimirovic2022dcc` (Stanimirovic D, Tepej Jocic L, *IJERPH*
  19(21):14322, PMID 36361204) is the deployment case study, and none of
  the frictions it documents would have been addressed by a blockchain.
- **SMART Health Cards** (existing `vci2024smart`): W3C Verifiable
  Credential as a JWS, ES256 over P-256, issuer keys at the issuer's own
  domain. Trust root is DNS plus TLS. No ledger.
- **WHO GDHCN** (existing `who2023gdhcn`): PKI trust network derived
  from the EU DCC model. No ledger.

- **`toubiana2022cons`** Toubiana R, Macdonald M, Rajananda S, et al.
  (2022). 'Blockchain for electronic vaccine certificates: more cons
  than pros?' *Front Big Data* 5:833196. PMID 35875593. Harvard Chan and
  Mayo authors reaching the correct conclusion: the useful ingredient is
  cryptography, not the ledger, and since a central authority must
  attest vaccination status anyway (it administered the vaccine),
  distributing the ledger *degrades* the trust model. **The anchor
  critique for this section.**
- **`lin2022iata`** Lin P (2022). 'Privacy and security analysis of the
  IATA Travel Pass Android app.' The Citizen Lab, University of Toronto.
  An empirical security audit finding that the one large blockchain
  credential deployment had its decentralisation nullified in practice:
  a third party, Evernym, held the laboratories' private keys. The
  ledger was in the architecture diagram and absent from the threat
  model. Grey literature, but empirical and rigorous. Label as such.

## 5. The pharmaceutical supply chain: the natural experiment

Blockchain got a fair test against a statutory mandate with a hard
deadline, a technology-neutral regulator, a 20-project federal pilot
programme, and unlimited industry motive. It lost. The primary sources
establish this without needing any journal article.

- **`fda2024edds`** FDA (2024). *Enhanced Drug Distribution Security at
  the Package Level Under the DSCSA: Guidance for Industry.* Rev. 1,
  January 2024. Recommends 'a distributed or semi-distributed data
  architecture model' and the **EPCIS** standard. **Blockchain is not
  named, not required, and not recommended anywhere in the document.**
  Note the distinction the book must draw: *distributed* is not
  *decentralised or trustless*. The recommended model is a federated
  database with point-to-point document exchange.
- **`fda2023pilot`** FDA (2023). *DSCSA Pilot Project Program: Final
  Program Report.* May 2023. **Blockchain appeared in 8 of 19 pilots.**
  In the entire 'Lessons Learned' section it is mentioned exactly once,
  as a parenthetical alongside RFID. The pilot-technology cross-tab is a
  genuinely good contingency-table exercise.
- **`fda2023stabilization`** FDA (2023). *Enhanced Drug Distribution
  Security Requirements Under Section 582(g)(1): Compliance Policies.*
  August 2023.
- **`coustasse2016rfid`** Coustasse A, Kimble CA, Stanton RB, Naylor M
  (2016). 'Could the pharmaceutical industry benefit from full-scale
  adoption of RFID technology with new regulations?' *Perspect Health
  Inf Manag* 13(Fall):1b. PMID 27843419. **Cite deliberately.** This is
  the *previous* hype cycle for the identical problem: RFID was going to
  solve DSCSA and lost to 2D barcodes on cost. The structural parallel is
  exact and deserves to be a named theme.

The residue is instructive and should be stated: where blockchain
survived in pharma, it survived for financial reasons, not safety ones.
Chargebacks and contract alignment involve mutually distrusting
counterparties disputing money. Drug traceability involves a regulator
that can simply compel a data format. That asymmetry, not any property
of hashes, explains the outcome.

## 6. Substandard and falsified medicines: the statistics goldmine

This is where a *statistics* textbook earns its keep, and none of it is
blockchain research. It is the measurement problem that blockchain
claims to solve and does not.

- **`ozawa2018prevalence`** Ozawa S, Evans DR, Bessias S, et al. (2018).
  'Prevalence and estimated economic burden of substandard and falsified
  medicines in low- and middle-income countries: systematic review and
  meta-analysis.' *JAMA Netw Open* 1(4):e181662. PMID 30646106.
  96 studies, 67,839 samples. Pooled prevalence **13.6% (95% CI
  11.0-16.3)**; Africa 18.7%; antimalarials 19.1%. A ready-made
  random-effects meta-analysis exercise, with the authors explicitly
  damning the $10bn-$200bn economic estimates as method-free.
- **`ozawa2022api`** Ozawa S, Chen HH, Lee YA, et al. (2022).
  'Characterizing medicine quality by active pharmaceutical ingredient
  levels.' *Am J Trop Med Hyg* 106(6):1778-1790. PMID 35895431.
  **Load-bearing.** 95,520 samples, 130 studies. Of failed samples,
  only about 13.8 percent were likely falsified; roughly six-sevenths
  were merely substandard, that is, manufacturing-quality failures.
  **Traceability addresses falsification. It does essentially nothing
  about substandard manufacturing, which is the bulk of the problem.**
  This is the sharpest empirical rebuttal available to the
  blockchain-solves-drug-quality narrative.
- **`hauk2021tolerance`** Hauk C, Hagen N, Heide L (2021).
  'Identification of substandard and falsified medicines: influence of
  different tolerance limits and use of authenticity inquiries.'
  *Am J Trop Med Hyg* 104(5):1936-1945. PMID 33788775.
  601 samples. The out-of-specification rate was **9.3 percent under USP
  limits but ranged from 3.3 percent to 35.0 percent depending on which
  pharmacopoeia's tolerance limits were applied.** A ten-fold swing
  driven purely by the choice of measurement threshold. You cannot
  detect what you have not defined. **An outstanding worked example on
  measurement definitions and estimator sensitivity.**
- **`who2017sf`** WHO (2017). *Global Surveillance and Monitoring System
  for substandard and falsified medical products* and the accompanying
  public health and socioeconomic impact study. 10.5 percent estimated
  failure rate in LMICs, from >48,000 samples across 88 countries. The
  regional report distribution (Africa 42%, Americas 21%, Europe 21%,
  W. Pacific 8%, E. Mediterranean 6%, SE Asia 2%) is a textbook
  illustration of **reporting bias**: it reflects where surveillance
  capacity exists, not where falsification occurs.
- **`pisani2021surveillance`** Pisani E, Hasnida A, Rahmi M, et al.
  (2021). 'Substandard and falsified medicines: proposed methods for
  case finding and sentinel surveillance.' *JMIR Public Health Surveill*
  7(8):e29309. PMID 34181563. Argues **no country has ever measured
  market-wide prevalence**, and proposes risk-based sentinel
  surveillance. The natural home for a chapter on sampling design and
  why simple random sampling of a drug market is infeasible.
- **`gnegel2022minilab`** Gnegel G, Hafele-Abah C, Neci R, Heide L
  (2022). *Sci Rep* 12:13095. PMID 35908047. 1,919 samples across 13
  countries at **EUR 25.85 per sample**. A cost-per-test figure, ideal
  for a cost-effectiveness-of-detection exercise contrasted against the
  cost of ledger infrastructure.
- **`salami2023methods`** Salami RK, Valente de Almeida S, Gheorghe A,
  et al. (2023). *Am J Trop Med Hyg* 109(2):228-240. PMID 37339762.
  Only 11 studies survived screening from 1,078. States plainly that the
  evidence base is limited and social-outcome evidence nonexistent.
- **`beargie2019nigeria`** Beargie SM, Higgins CR, Evans DR, et al.
  (2019). *PLoS ONE* 14(8):e0217910. PMID 31415560. SAFARI agent-based
  model: 12,300 deaths and $892 million per year in Nigeria from
  poor-quality antimalarials. Directly teachable simulation structure.
- **`jackson2020zambia`** Jackson KD, Higgins CR, Laing SK, et al.
  (2020). *BMC Public Health* 20:1083. PMID 32646393. Eliminating
  substandard and falsified antimalarials would avert 8.1 percent
  (n=213) of under-five deaths in Zambia.
- **`ozawa2022models`** Ozawa S, Higgins CR, Nwokike JI, Phanouvong S
  (2022). *Am J Trop Med Hyg* 107(1):14-20. PMID 35895357. Catalogues
  only 7 such models worldwide. A candid statement of how thin the
  quantitative base is.
- **`khurelbat2020mongolia`** Khurelbat D, et al. (2020). *BMC Public
  Health* 20:743. PMID 32434489. 1,770 samples; a clean two-proportion
  comparison (locally produced 5.9% vs imported 4.17%, p=0.0001).
- **`kovacs2014detection`** Kovacs S, Hawes SE, Maley SN, et al. (2014).
  *PLoS ONE* 9(3):e90601. PMID 24671033. 42 detection technologies scored
  on LMIC feasibility with cost tiers. Useful foil: the bottleneck is
  chemistry and field logistics, not ledger architecture.

## 7. Rigorous critiques and legal analysis

- **`elgazzar2020hype`** El-Gazzar R, Stendal K (2020). 'Blockchain in
  health care: hope or hype?' *JMIR* 22(7):e17199. PMID 32673219.
  Concludes that blockchain 'will not solve the issues encountered by
  the health care sector; in fact, it may raise more issues than it will
  solve.' Published at the peak, in a mainstream venue, and correct.
- **`mackey2019fitforpurpose`** Mackey TK, Kuo TT, Gummadi B, et al.
  (2019). '"Fit-for-purpose?" Challenges and opportunities for
  applications of blockchain technology in the future of healthcare.'
  *BMC Med* 17(1):68. PMID 30914045. Insider scepticism, including
  George Church. More persuasive to students than outsider scepticism.
- **`shabani2019governance`** Shabani M (2019). 'Blockchain-based
  platforms for genomic data sharing.' *JAMIA* 26(1):76-80. PMID
  30496430. Early and correct scepticism about whether smart-contract
  'participatory access control' can substitute for a Data Access
  Committee. It cannot.
- **`abuhalimeh2023quality`** AbuHalimeh A, Ali O (2023).
  'Comprehensive review for healthcare data quality challenges in
  blockchain technology.' *Front Big Data* 6:1173620. PMID 37252129. The
  closest thing in the health literature to a dedicated treatment of the
  garbage-in problem. Pair with `ncsc2021dlt`.
- **`scheibner2021pets`** Scheibner J, Raisaro JL,
  Troncoso-Pastoriza JR, et al. (2021). *JMIR* 23(2):e25120. PMID
  33629963. Argues multiparty-HE output qualifies as anonymised data
  under GDPR, thereby escaping the erasure conflict entirely. A stronger
  and more defensible position than anything blockchain-native. Note the
  argument is legally contested and untested by a DPA or court.
- **`phuyal2026law`** Phuyal S, Bhandari M, Correia Bezerra R, et al.
  (2026). 'Dynamic consent for secondary use of health data: challenges
  and opportunities under European law.' *JMIR Med Inform* 14:e93348.
  PMID 42304949. States directly that blockchain immutability conflicts
  with the right to erasure, and notes that the European Health Data
  Space (phasing in from 2029) routes governance through Health Data
  Access Bodies and secure processing environments, **an architecture
  that bypasses blockchain entirely.** The regulator is building the
  non-blockchain alternative.
- **`gonzales2021opioids`** Gonzales A, Smith SR, Dullabh P, et al.
  (2021). *JMIR Med Inform* 9(8):e16293. PMID 34448721. Notable because
  the authors are US HHS/ASPE: a federal health agency documenting that
  the published evidence base was too thin to work from and that they
  had to fall back on grey literature and an expert panel.

## Recommended placement against the current manuscript

The textbook map showed six chapters with a fully-written public-health
section and zero health citations. Concrete assignments:

| Chapter | Current gap | Citations to add |
|---|---|---|
| Preface / 00-intro | 'systematic reviews through the middle of the decade' cited to nothing | `lacson2024biomedical`, `ng2021blockchain`, `fang2021phr`, `chandak2026ehr` |
| 01 consensus | Health corpus discharged in one list-cite | `ncsc2021dlt` (the three-condition test), `elgazzar2020hype`, `mackey2019fitforpurpose` |
| 02 crypto primitives | Merkle-proof trial-lock example, zero citations | `rfc3161`, `rfc6962`, `trillian`, `narayanan2017pedigree` (promote), `oakley2022scrybe` (21 CFR Part 11) |
| 03 proof-of-work | Confirmation depth as critical value; no health cite | `wymant2021nhsapp` (two estimators, honest discrepancy) |
| 04 mining statistics | Outbreak-detection section, no epidemiology cite | `muwonge2025haulage`, `pisani2021surveillance` (sentinel design) |
| 05 security economics | Full threat-model section, zero citations | `lin2022iata` (the ledger absent from the threat model), `abuhalimeh2023quality` |
| 06 Ethereum / consent | Consent section, no consent literature | `huh2022metory`, `mamo2020dwarna`, `phuyal2026consent`, `phuyal2026law` |
| 07 DeFi / parametric | Pandemic-bond argument, zero citations | `beargie2019nigeria`, `jackson2020zambia` (parametric triggers on modelled burden) |
| 08 MEV / ordering | Front-running mapped to allocation concealment, no cite | (gap: see below) |
| 09 proof-of-stake | Correlated dropout / shared frailty, no methods cite | (gap: see below) |
| 10 on-chain data | Re-identification section cites no re-identification lit | `homer2008resolving`, `raisaro2017beacon`, `johnson2013gwas`, `elhussein2024sharing` |
| New: supply chain | Cold-chain case study is thin | `fda2024edds`, `fda2023pilot`, `ozawa2018prevalence`, `ozawa2022api`, `hauk2021tolerance`, `coustasse2016rfid` |

## Gaps this search could not close

Stated plainly, because a completion claim covers only the work done:

1. **No blockchain intervention has been shown to improve a health
   outcome in a controlled evaluation.** A PubMed search restricted to
   `Clinical Trial[Publication Type]` returns 7 records, none of which
   trials a blockchain intervention; five are false positives from
   author affiliations. The single controlled study with plausible
   involvement (`ramos2022events`) was null. **Scope caveat**: this is a
   PubMed-indexed claim only. IEEE Xplore, ACM DL and trial registries
   were not searched. State the claim at that scope and it holds.
2. **No literature on token-economic incentives for health data donation
   with real willingness-to-accept estimates exists.** If the book wants
   that worked example, it must be constructed.
3. **Chapters 08 and 09 have no supporting literature yet.** The
   allocation-concealment / randomisation-blinding mapping and the
   correlated-dropout / shared-frailty mapping are the author's own; the
   trial-methodology and survival-analysis citations to support them were
   outside this search's scope and need a separate pass.
4. **No blockchain AMR-surveillance literature exists** (5 PubMed
   records, none substantive). Civil registration is similarly empty.
   Medical-device UDI is empty. If the book covers these, it argues from
   first principles.
5. **IEEE Xplore, ACM DL and SSRN were not searched.** Much of the CS
   critique of permissioned ledgers, and the membership-inference and
   gradient-inversion attack literature that undercuts federated-learning
   privacy claims, lives there.

## Epistemic status

All PMIDs and DOIs above were verified by search agents against PubMed
records or successfully fetched publisher and agency pages. I re-checked
five of the load-bearing entries directly against PubMed, and that spot
check found three metadata errors in my own transcription, which is
strong evidence that a full pass is necessary rather than optional:

- `lacson2024biomedical`: first author is Roger Lacson, not Ronilda
  (corrected). The two search agents also disagreed on the volume and
  page range; PubMed confirms *JAMIA* 31(6):1423-1435.
- `kuo2020explorerchain`: the title I first recorded was a plausible
  paraphrase rather than the actual title (corrected).
- `huh2022metory`: third author is Jeong Sang-Un, not Sae-Ung
  (corrected).

**The remaining entries have not had this treatment.** Before any of this
reaches print, resolve every DOI and PMID and confirm author lists,
titles and page numbers mechanically. The error rate in my spot check
was three of five.

Specific items carrying residual uncertainty, flagged by the agents:

- `ncsc2021dlt`, `trillian`, `lin2022iata` are grey literature, not
  peer-reviewed. They are rigorous, but label them accordingly.
- `rfc6962` author list was not separately re-verified name by name.
- The FDA guidance claim that blockchain is never mentioned rests on
  inspection of the downloaded PDF by the agent; the pilot-report counts
  (8 of 19) come from its Table 5. Both are high-confidence but worth one
  direct confirmation before print.
- The standalone MediLedger and IBM/KPMG/Merck/Walmart pilot reports were
  not retrieved (FDA media URLs 404'd). Do not attribute specific
  performance numbers to those two pilots without downloading them.
- `who2017sf` figures were verified from the WHO news release and study
  page, not from the full report PDF.

---
*Rendered on 2026-07-13 at 17:04 AEST.*<br>
*Source: ~/prj/tch/11-blockchain-curriculum/blockchain-public-health-citations.md*
