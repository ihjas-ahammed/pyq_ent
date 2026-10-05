# PYQ Entrance (`pyq_ent`)

Comprehensive repository of Previous Year Question (PYQ) papers, official answer keys, detailed solutions, and **year-wise official syllabi** for premier competitive and university entrance examinations in India.

---

## Repository Structure

```
pyq_ent/
├── GATE/
│   └── DA/                                # GATE Data Science & Artificial Intelligence (DA) PYQs
│       ├── Official/                      # Official IISc Bangalore & IIT Roorkee Question Papers & Keys
│       ├── Books_and_Compilations/        # Gate Overflow DA PYQ Book & Engineering Mathematics
│       └── Similar_Exams/                 # CMI MSc Data Science (2018-2025), GATE CS & ST 2025
├── CUSAT/
│   ├── PH/                                # CUSAT CAT Physics Papers & Solved Solutions (2018-2025)
│   └── MT/                                # CUSAT CAT Mathematics Papers & Solved Solutions (2018-2025)
├── JAM/
│   ├── PH/                                # IIT JAM Physics (2012-2025) + CMI PG Physics
│   └── MT/                                # IIT JAM Mathematics (2012-2025) & Statistics (MS) + CMI PG Maths
├── LBS/
│   ├── Kerala_SET_Physics/                # Kerala State Eligibility Test (SET) Physics (2023-2026)
│   ├── Kerala_SET_Mathematics/            # Kerala SET Mathematics (2023-2026)
│   ├── Kerala_SET_Statistics/             # Kerala SET Statistics (2023-2026)
│   ├── Kerala_SET_General_Paper_Teaching_Aptitude/ # Kerala SET Paper I General / Teaching Aptitude
│   ├── LBS_MCA_Entrance/                  # Kerala MCA Entrance Examination Answer Keys (2023-2026)
│   └── LBS_Other_Entrance/                # LBS Nursing & Paramedical Previous Year Papers
├── LDC/                                   # Lower Division Clerk (LDC / Clerk) Examination Archive
│   ├── Kerala_PSC_LDC_District_Mains/     # District-wise LDC Papers with Answer Keys (2011-2024)
│   ├── Kerala_PSC_10th_Level_Preliminary/ # 10th Level Screening Exams for LDC (2021-2026)
│   └── Kerala_PSC_LDC_Official/           # Latest 2026 Official KPSC Clerk Papers & Final Answer Keys
├── syllabus/                              # Year-wise Official Syllabi & Curriculum Blueprints
│   ├── GATE/DA/                           # GATE DA 2024, 2025, 2026 + Overlap (CS, ST, MA, GA) + CMI
│   ├── CUSAT/PH/                          # CUSAT CAT UG (2024-2026) & PG M.Sc Physics Syllabi
│   ├── CUSAT/MT/                          # CUSAT CAT UG (2024-2026) & PG M.Sc Mathematics Syllabi
│   ├── JAM/PH/                            # IIT JAM Physics (2025, 2026) + Brochures + CMI PG Physics
│   ├── JAM/MT/                            # IIT JAM Mathematics & Statistics (2025, 2026) + CMI PG Math
│   ├── LBS/                               # Kerala SET (Paper I, Physics, Maths, Stats) + Prospectuses + MCA
│   └── LDC/                               # Kerala PSC LDC, 10th Prelims & SSC CHSL LDC Syllabi
├── extracted/                             # Topic-wise extracted PYQs in Markdown with detailed solutions
│   └── probability/                       # Probability & Statistics PYQs (Year-wise)
│       ├── 2024.md                        # GATE DA 2024 Official Paper + Sample Paper (Sorted by Difficulty)
│       ├── 2025.md                        # GATE DA 2025 Official Paper + GATE CS 2025 S1 (Sorted by Difficulty)
│       └── year_source.md                 # Academic Source & Origin Attribution (Book, Person, GATE Exclusive)
├── year_source.md                         # Root copy of academic source attribution
└── scripts/                               # Reproducible download and generator scripts
```

---

## Syllabi (`syllabus/<exam>`)

Official curriculum documents, topic breakdowns, and examination pattern blueprints for each exam:

### 1. `syllabus/GATE/DA/`
* **GATE DA (Data Science & AI):**
  * `GATE_2024_DA_Data_Science_and_AI_Official_Syllabus.pdf` (IISc Bangalore — Inaugural Session)
  * `GATE_2025_DA_Data_Science_and_AI_Official_Syllabus.pdf` (IIT Roorkee)
  * `GATE_2026_DA_Data_Science_and_AI_Official_Syllabus.pdf` (IIT Guwahati)
* **General Aptitude (GA):**
  * `GATE_2024_GA_General_Aptitude_Official_Syllabus.pdf`
  * `GATE_2025_GA_General_Aptitude_Official_Syllabus.pdf`
  * `GATE_2026_GA_General_Aptitude_Official_Syllabus.pdf`
* **Overlapping / Similar Disciplines:**
  * `GATE_2025_CS_Computer_Science_Official_Syllabus.pdf`
  * `GATE_2026_CS_Computer_Science_Official_Syllabus.pdf`
  * `GATE_2025_ST_Statistics_Official_Syllabus.pdf`
  * `GATE_2026_ST_Statistics_Official_Syllabus.pdf`
  * `GATE_2025_MA_Mathematics_Official_Syllabus.pdf`
  * `GATE_2026_MA_Mathematics_Official_Syllabus.pdf`
  * `CMI_MSc_Data_Science_Official_Syllabus.pdf`

### 2. `syllabus/CUSAT/PH/` (Physics)
* **Undergraduate & 5-Year Integrated M.Sc (NCERT Class XI & XII Standard, Test Code 101):**
  * `CUSAT_CAT_2026_Physics_Syllabus_and_Exam_Pattern.pdf`
  * `CUSAT_CAT_2025_Physics_Syllabus_and_Exam_Pattern.pdf`
  * `CUSAT_CAT_2024_Physics_Syllabus_and_Exam_Pattern.pdf`
  * `CUSAT_CAT_UG_Physics_Official_Syllabus.pdf`
* **Post-Graduate M.Sc Physics (B.Sc Standard, Test Code 612):**
  * `CUSAT_CAT_PG_MSc_Physics_Official_Syllabus.pdf` (Mathematical Physics, Classical Mechanics, EMT, Quantum Mechanics, Thermodynamics & Statistical Mechanics, Solid State, Electronics & Nuclear Physics)

### 3. `syllabus/CUSAT/MT/` (Mathematics)
* **Undergraduate & 5-Year Integrated M.Sc (NCERT Class XI & XII Standard, Test Code 101):**
  * `CUSAT_CAT_2026_Mathematics_Syllabus_and_Exam_Pattern.pdf`
  * `CUSAT_CAT_2025_Mathematics_Syllabus_and_Exam_Pattern.pdf`
  * `CUSAT_CAT_2024_Mathematics_Syllabus_and_Exam_Pattern.pdf`
  * `CUSAT_CAT_UG_Mathematics_Official_Syllabus.pdf`
* **Post-Graduate M.Sc Mathematics (B.Sc Standard, Test Code 611):**
  * `CUSAT_CAT_PG_MSc_Mathematics_Official_Syllabus.pdf` (Real Analysis, Linear Algebra, Abstract Algebra, Complex Analysis, Differential Equations, Topology, Numerical Analysis & Probability)

### 4. `syllabus/JAM/PH/` (Physics)
* `JAM_2026_Physics_Official_Syllabus.pdf` (IIT Bombay)
* `JAM_2025_Physics_Official_Syllabus.pdf` (IIT Delhi)
* `JAM_2026_Official_Admission_Brochure_with_Syllabus.pdf`
* `JAM_2025_Official_Information_Brochure_with_Syllabus.pdf`
* `CMI_PG_Physics_Official_Syllabus.pdf`

### 5. `syllabus/JAM/MT/` (Mathematics & Statistics)
* `JAM_2026_Mathematics_Official_Syllabus.pdf` (IIT Bombay)
* `JAM_2026_Mathematical_Statistics_Official_Syllabus.pdf` (IIT Bombay)
* `JAM_2025_Mathematics_Official_Syllabus.pdf` (IIT Delhi)
* `JAM_2025_Mathematical_Statistics_Official_Syllabus.pdf` (IIT Delhi)
* `JAM_2026_Official_Admission_Brochure_with_Syllabus.pdf`
* `JAM_2025_Official_Information_Brochure_with_Syllabus.pdf`
* `CMI_PG_Mathematics_Official_Syllabus.pdf`

### 6. `syllabus/LBS/` (Kerala SET & LBS Entrances)
* **Kerala State Eligibility Test (SET):**
  * `Kerala_SET_All_Subjects_Official_Syllabus.pdf` (Comprehensive master syllabus for all 31 subjects)
  * `Kerala_SET_Paper_I_General_Knowledge_and_Teaching_Aptitude_Official_Syllabus.pdf`
  * `Kerala_SET_Paper_II_Physics_Official_Syllabus.pdf` (Subject Code 24)
  * `Kerala_SET_Paper_II_Mathematics_Official_Syllabus.pdf` (Subject Code 21)
  * `Kerala_SET_Paper_II_Statistics_Official_Syllabus.pdf` (Subject Code 31)
  * `Kerala_SET_2026_July_Official_Prospectus.pdf`
  * `Kerala_SET_2026_January_Official_Prospectus.pdf`
* **LBS MCA Entrance:**
  * `LBS_MCA_Entrance_Official_Prospectus_and_Syllabus.pdf`

### 7. `syllabus/LDC/` (Lower Division Clerk)
* `Kerala_PSC_LDC_Official_Syllabus_Malayalam_English.pdf`: Official Detailed Syllabus for Clerk (Cat. No: 503/2023, 504/2023) across History, Geography, Economics, Constitution, Science, Malayalam, English, and Mental Ability.
* `Kerala_PSC_10th_Level_Preliminary_Official_Syllabus.pdf`: Official blueprint and mark distribution for 10th Level Common Preliminary Screening Examination.
* `Kerala_PSC_LDC_Mains_Official_Syllabus_and_Exam_Pattern.pdf`: Complete mark-wise syllabus breakdown for LDC Main Exam (100 Marks).
* `SSC_CHSL_LDC_Tier1_and_Tier2_Official_Syllabus.pdf`: Official syllabus and exam pattern for Central Government LDC / JSA recruitment.

---

## PYQ Papers & Answer Keys

### 1. GATE / DA (Data Science & Artificial Intelligence)
* **Official GATE DA:**
  * `GATE_2024_DA_Question_Paper_Official.pdf`: Official Master Question Paper (IISc Bangalore).
  * `GATE_2024_DA_Final_Answer_Key_Official.pdf`: Official Final Answer Key (IISc Bangalore).
  * `GATE_2024_DA_Sample_Paper_IISc.pdf`: Official IISc DA Sample Question Paper.
  * `GATE_2025_DA_Question_Paper_Official.pdf`: Official Master Question Paper (IIT Roorkee).
  * `GATE_2025_DA_Final_Answer_Key_Official.pdf`: Official Final Answer Key (IIT Roorkee).
* **Books & Compilations:**
  * `GATEOverflow_DA_Complete_PYQ_Book.pdf`: Full GATE Overflow question compilation for Data Science & AI.
  * `GATE_Engineering_Mathematics_PYQs.pdf`: Complete Engineering Mathematics compilation.
* **Similar Exams:**
  * **CMI MSc Data Science (2018–2025):** Complete past question papers, official answer keys, and step-by-step solutions.
  * **GATE CS 2025 (Sessions 1 & 2):** Master Question Papers & Answer Keys for overlapping CS/DS topics.
  * **GATE Statistics (ST) 2025:** Master Question Paper & Answer Key for mathematical statistics and probability.

### 2. CUSAT (Cochin University of Science and Technology)
* **`CUSAT/PH` (Physics):**
  * `CUSAT_CAT_2025_Physics_PYQ_with_Solutions.pdf`: Complete 75 Physics questions from CUSAT CAT 2025 with options, official keys, and step-by-step explanations.
  * Solved test papers with answers and solutions for 2023, 2022, 2021, 2019, and 2018.
* **`CUSAT/MT` (Mathematics):**
  * `CUSAT_CAT_2025_Mathematics_PYQ_with_Solutions.pdf`: Complete 90 Mathematics questions from CUSAT CAT 2025 with options, official keys, and step-by-step explanations.
  * Solved test papers with answers and solutions for 2023, 2022, 2021, 2019, and 2018.

### 3. JAM (Joint Admission Test for Masters)
* **`JAM/PH` (Physics):**
  * Consecutive year-wise papers from **2012 to 2025** (`JAM_2012_Physics_Question_Paper.pdf` to `JAM_2025_Physics_Question_Paper.pdf`).
  * Master Question Paper and Official Final Answer Key.
  * CMI PG Physics papers and solutions (2011 to 2016).
* **`JAM/MT` (Mathematics & Mathematical Statistics):**
  * IIT JAM Mathematics (MA) consecutive papers from **2012 to 2025** + Master Paper and Answer Key.
  * IIT JAM Mathematical Statistics (MS) consecutive papers from **2012 to 2025** + Master Paper and Answer Key.
  * CMI PG Mathematics papers and solutions (2018 to 2025).

### 4. LBS (LBS Centre for Science & Technology, Kerala)
* **Kerala SET Physics:** Consecutive papers from 2023 January to 2026 January.
* **Kerala SET Mathematics:** Consecutive papers from 2023 January to 2026 January.
* **Kerala SET Statistics:** Consecutive papers from 2023 January to 2026 January.
* **Kerala SET General Paper:** Consecutive papers from 2023 January to 2026 January.
* **Kerala SET Answer Key:** Revised answer key for all subjects.
* **LBS MCA Entrance:** Official revised answer keys for 2023, 2024, 2025, and 2026.
* **LBS Other Entrances:** Previous question paper for Post Basic B.Sc Nursing.

### 5. LDC (Lower Division Clerk / Kerala Public Service Commission)

#### `LDC/Kerala_PSC_LDC_District_Mains` (30 Papers with Official Keys)
* **2024 District Papers:**
  * `LDC_2024_Thiruvananthapuram_Question_Paper_with_Answer_Key.pdf`
  * `LDC_2024_Kollam_Kannur_Question_Paper_with_Answer_Key.pdf`
  * `LDC_2024_Thrissur_Pathanamthitta_Kasargod_Question_Paper_with_Answer_Key.pdf`
  * `LDC_2024_Kottayam_Kozhikode_Question_Paper_with_Answer_Key.pdf`
  * `LDC_2024_Malappuram_Idukki_Question_Paper_with_Answer_Key.pdf`
  * `LDC_2024_Special_Recruitment_052_2024_Question_Paper_with_Answer_Key.pdf`
* **2023 & 2021 Papers:**
  * `LDC_2023_Clerk_Accountant_Cashier_239_2023_Question_Paper_with_Answer_Key.pdf`
  * `LDC_2021_Clerk_Mains_117_2021_Question_Paper_with_Answer_Key.pdf`
  * `LDC_2021_ExServicemen_100_2021_Question_Paper_with_Answer_Key.pdf`
* **2017 District Papers:**
  * Kollam, Thrissur, Kasaragod (`077/2017`), Pathanamthitta, Palakkad (`084/2017`), Kottayam, Wayanad (`095/2017`), Ernakulam, Kannur (`078/2017`), Idukki, Alappuzha, Kozhikode (`079/2017`).
* **2014 District Papers:**
  * Idukki (`025/2014`), Ernakulam (`001/2014`), Malappuram (`024/2014`), Palakkad (`017/2014`), Kozhikode (`007/2014`), Various (`002/2014`).
* **2013 District Papers:**
  * Various (`147/2013`, `154/2013`), Pathanamthitta (`162/2013`), Kasaragod (`148/2013`).
* **2011 District Papers:**
  * Wayanad (`058/2011`), Kozhikode (`064/2011`), Kottayam (`063/2011`), Ernakulam (`057/2011`), Alappuzha (`069/2011`), Pathanamthitta (`050/2011`).

#### `LDC/Kerala_PSC_10th_Level_Preliminary` (22 Papers across All Stages)
* **2026:** Stage 1 (`66/2026` with Answer Key) and Stage 2 (`67/2026`).
* **2024:** Stage 1 (`185/2024`) and Stage 5 (`013/2024`).
* **2023:** Stages 1, 2, 3, 4 (`202/2023`, `224/2023`, `233/2023`, `239/2023`) & Session B Stages 1, 2, 3, 4 (`141/2023`, `154/2023`, `166/2023`, `184/2023`).
* **2022:** Stages 1, 2, 3, 4, 5, 6 (`053/2022`, `060/2022`, `068/2022`, `071/2022`, `076/2022`, `077/2022`).
* **2021:** Stages 1, 2, 3, 4, 5 (`029/2021`, `030/2021`, `031/2021`, `032/2021`, `084/2021`).

#### `LDC/Kerala_PSC_LDC_Official` (Latest 2026 Papers & Final Keys)
* `Kerala_PSC_2026_Clerk_088_2026_Question_Paper_Malayalam.pdf`
* `Kerala_PSC_2026_Clerk_088_2026_Question_Paper_Tamil.pdf`
* `Kerala_PSC_2026_Clerk_088_2026_Question_Paper_Kannada.pdf`
* `Kerala_PSC_2026_Clerk_088_2026_Provisional_Answer_Key.pdf`
* `Kerala_PSC_2026_Clerk_088_2026_Answer_Key_Tamil.pdf`
* `Kerala_PSC_2026_Clerk_088_2026_Answer_Key_Kannada.pdf`
* `Kerala_PSC_2026_LDC_080_2026_Stage_II_Final_Answer_Key.pdf`

---

## Extracted Questions: Probability & Statistics (`extracted/probability/`)

Topic-wise extracted questions transcribed with exact LaTeX mathematical notation, question types, marks, official answer keys, and step-by-step solutions:

* **[`extracted/probability/2024.md`](extracted/probability/2024.md):**
  * **GATE DA 2024 Official Paper:** 16 Probability & Statistics questions (Q.3, Q.7, Q.11, Q.12, Q.20, Q.24, Q.27, Q.34, Q.36, Q.56, Q.57, Q.58, Q.59, Q.62, Q.64, Q.65) covering Counting, Poisson & Normal distributions, Independence, Naïve Bayes, Bayesian Networks, Descriptive Statistics, Exponential distribution, Bayes' theorem, Joint PDFs, and Covariance.
  * **GATE DA 2024 Official Sample Paper (IISc):** 13 Probability & Statistics questions (Q.4, Q.7, Q.8, Q.9, Q.10, Q.20, Q.28, Q.32, Q.33, Q.36, Q.45, Q.47, Q.53) covering Combinatorics, Conditional Probability, Pearson Correlation, Likelihood Weighting, Uniform RVs, and Statistical Estimation.

* **[`extracted/probability/2025.md`](extracted/probability/2025.md):**
  * **GATE DA 2025 Official Paper:** 16 Probability & Statistics questions (Q.10, Q.11, Q.19, Q.20, Q.21, Q.26, Q.31, Q.35, Q.36, Q.39, Q.40, Q.41, Q.45, Q.54, Q.60, Q.61) covering Expectation of discrete distributions, Law of Total Expectation, CDF & Quantiles, Normal RV transformations, Exponential memoryless property, Bayesian network inference algorithms, Bayes' theorem ball urn models, Naïve Bayes misclassification, Chi-squared distribution, Central Limit Theorem Bernoulli approximation, Exponential floor transformations, Estimator variance, Covariance matrix maximum variance direction, and Binomial expectation.
* **[`year_source.md`](year_source.md) / [`extracted/probability/year_source.md`](extracted/probability/year_source.md):**
  * **Comprehensive Academic Source Attribution:** Maps every single question across all papers to its foundational textbook (Sheldon Ross, Bertsekas & Tsitsiklis, Russell & Norvig, Bishop, Mitchell, Hogg & Craig), historic mathematicians/theorists (Kolmogorov, Bayes, Markov, Pearson, Fisher, Pearl, Shannon), and GATE-exclusive custom design contexts.

---

## Verification & Statistics

* **Total PDF Documents:** 257 (210 Question Papers, Answer Keys & Solutions + 47 Official Syllabi)
* **Total Storage:** ~271 MB
* **Integrity:** Every single PDF verified with standard `%PDF-` header magic bytes.
* **Formats:** Official examination authority PDFs + high-fidelity headless Chrome rendered compilations.
