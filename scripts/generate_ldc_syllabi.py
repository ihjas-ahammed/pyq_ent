import os
import subprocess

CSS = """
  @page {
    size: A4;
    margin: 18mm 15mm 18mm 15mm;
    @bottom-center {
      content: "Page " counter(page) " of " counter(pages);
      font-size: 9pt;
      color: #6b7280;
    }
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #1f2937;
    line-height: 1.55;
    font-size: 10.5pt;
    margin: 0;
    padding: 0;
  }
  .header {
    text-align: center;
    border-bottom: 2.5px solid #047857;
    padding-bottom: 14px;
    margin-bottom: 20px;
  }
  .header .inst-logo-sub {
    font-size: 11pt;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #4b5563;
    font-weight: 600;
    margin-bottom: 4px;
  }
  .header h1 {
    font-size: 21pt;
    color: #065f46;
    margin: 0 0 6px 0;
    font-weight: 800;
    letter-spacing: -0.5px;
  }
  .header h2 {
    font-size: 13.5pt;
    color: #059669;
    margin: 0 0 8px 0;
    font-weight: 600;
  }
  .header .badge-bar {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 8px;
  }
  .badge {
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    color: #047857;
    padding: 3px 10px;
    border-radius: 9999px;
    font-size: 8.5pt;
    font-weight: 600;
  }
  .pattern-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 24px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    overflow: hidden;
  }
  .pattern-table th, .pattern-table td {
    padding: 9px 12px;
    border: 1px solid #cbd5e1;
    font-size: 9.5pt;
    text-align: left;
  }
  .pattern-table th {
    background: #065f46;
    color: #ffffff;
    font-weight: 600;
  }
  .unit-card {
    border: 1px solid #e2e8f0;
    border-left: 4px solid #059669;
    border-radius: 0 6px 6px 0;
    padding: 12px 16px;
    margin-bottom: 14px;
    page-break-inside: avoid;
    background: #ffffff;
  }
  .unit-title {
    font-weight: 700;
    font-size: 11.5pt;
    color: #065f46;
    margin-bottom: 6px;
  }
  .unit-topics {
    margin: 0;
    padding-left: 20px;
    color: #374151;
  }
  .unit-topics li {
    margin-bottom: 4px;
  }
  .topic-name {
    font-weight: 600;
    color: #111827;
  }
  .sec-heading {
    font-size: 13.5pt;
    font-weight: 700;
    color: #065f46;
    border-bottom: 1.5px solid #cbd5e1;
    padding-bottom: 4px;
    margin-top: 24px;
    margin-bottom: 12px;
  }
"""

def generate_pdf(html_content, output_pdf):
    os.makedirs(os.path.dirname(output_pdf), exist_ok=True)
    tmp_html = f"/tmp/ldc_syll_{os.path.basename(output_pdf)}.html"
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    cmd = [
        'google-chrome-stable',
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={output_pdf}',
        tmp_html
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(output_pdf) and os.path.getsize(output_pdf) > 1000:
        print(f"[GENERATED] {output_pdf} ({os.path.getsize(output_pdf)} bytes)")
    else:
        print(f"[FAILED] {output_pdf}")

# 1. Kerala PSC LDC Mains Blueprint
def get_kpsc_ldc_mains_html():
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Kerala PSC LDC Mains - Official Detailed Syllabus & Blueprint</title>
<style>{CSS}</style>
</head>
<body>
  <div class="header">
    <div class="inst-logo-sub">Kerala Public Service Commission (KPSC)</div>
    <h1>Lower Division Clerk (LDC) - Main Examination</h1>
    <h2>Official Detailed Examination Blueprint & Subject-Wise Syllabus</h2>
    <div class="badge-bar">
      <span class="badge">Recruitment: Direct & By-Transfer (Part I & II)</span>
      <span class="badge">Qualification: SSLC / 10th Standard</span>
      <span class="badge">Total Marks: 100</span>
    </div>
  </div>

  <table class="pattern-table">
    <tr>
      <th>Section</th>
      <th>Subject Area</th>
      <th>Marks Weightage</th>
    </tr>
    <tr>
      <td><strong>Part I</strong></td>
      <td>General Knowledge & Current Affairs (History, Geography, Economics, Civics, Science)</td>
      <td>50 Marks</td>
    </tr>
    <tr>
      <td><strong>Part II</strong></td>
      <td>General English (Grammar, Vocabulary, Sentence Correction)</td>
      <td>20 Marks</td>
    </tr>
    <tr>
      <td><strong>Part III</strong></td>
      <td>Regional Language (Malayalam / Tamil / Kannada)</td>
      <td>20 Marks</td>
    </tr>
    <tr>
      <td><strong>Part IV</strong></td>
      <td>Simple Arithmetic & Mental Ability (Reasoning)</td>
      <td>10 Marks</td>
    </tr>
    <tr>
      <td><strong>Exam Timing</strong></td>
      <td>1 Hour 15 Minutes (75 Minutes) - OMR / CBT Objective Multiple Choice</td>
      <td><strong>Total: 100 Marks</strong></td>
    </tr>
  </table>

  <div class="sec-heading">Part I: General Knowledge & Science (50 Marks)</div>

  <div class="unit-card">
    <div class="unit-title">1. History (5 Marks)</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Kerala History:</span> Arrival of Europeans, contribution of Portuguese, Dutch, French, and British; Travancore, Cochin, and Malabar administrative history; Social reform movements in Kerala (Sree Narayana Guru, Chattampi Swamikal, Ayyankali, Vaikunda Swamikal, Poykayil Yohannan, K. Kelappan); Temple entry agitations (Vaikom and Guruvayur Satyagraha); Formation of Kerala state.</li>
      <li><span class="topic-name">Indian History:</span> Ancient and medieval India overviews, First War of Indian Independence (1857), Indian National Congress, Gandhian era, Partition, and Independence.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">2. Geography (5 Marks)</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Physical & Political Geography:</span> Earth structure, atmosphere, climate, seasons; Physiography of India: Himalayas, Northern plains, Peninsular plateau, Coastal plains; Rivers and river systems in India and Kerala; Soils, forests, national parks, wild life sanctuaries; Minerals and agriculture.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">3. Indian Constitution & Civics (5 Marks)</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Polity:</span> Constituent Assembly, Preamble, Fundamental Rights, Fundamental Duties, Directive Principles of State Policy; Union Executive (President, Vice-President, Prime Minister, Council of Ministers); Union Legislature (Lok Sabha, Rajya Sabha); Judiciary (Supreme Court, High Courts); Constitutional bodies (Election Commission, CAG, UPSC, State PSCs); Important Constitutional amendments.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">4. Kerala Governance & Administrative Systems (5 Marks)</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Administration:</span> Local Self Government Institutions (Panchayati Raj and Municipalities), Right to Information Act (RTI 2005), Right to Public Service Act, State Human Rights Commission, Lokayukta, Child Rights Commission, Women's Commission.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">5. General Science (10 Marks)</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Biology & Public Health:</span> Human physiology, diseases and prevention, vitamins and deficiency, health programmes in India and Kerala, environment and biodiversity.</li>
      <li><span class="topic-name">Physics & Chemistry:</span> Work, energy, power, light, sound, heat, electricity, atom structure, periodic table, acids, bases, chemical reactions in daily life.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">6. Current Affairs (20 Marks)</div>
    <ul class="unit-topics">
      <li>National and international events, awards and honours, sports, science and technology achievements, Kerala government development schemes.</li>
    </ul>
  </div>

  <div class="sec-heading">Part II: General English (20 Marks)</div>
  <div class="unit-card">
    <div class="unit-title">English Grammar & Vocabulary</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Grammar:</span> Types of sentences, Interchange of sentences, Parts of Speech, Agreement of Subject and Verb, Articles, Prepositions, Tenses, Active and Passive Voice, Direct and Indirect Speech, Degrees of Comparison, Question Tags.</li>
      <li><span class="topic-name">Vocabulary:</span> Synonyms, Antonyms, Idioms and Phrases, One-word substitutions, Phrasal Verbs, Common Spelling Errors, Homonyms.</li>
    </ul>
  </div>

  <div class="sec-heading">Part III: Regional Language - Malayalam (20 Marks)</div>
  <div class="unit-card">
    <div class="unit-title">Malayalam Grammar & Usage</div>
    <ul class="unit-topics">
      <li>പദശുദ്ധി (Correction of words), വാക്യശുദ്ധി (Correction of sentences), പരിഭാഷ (Translation).</li>
      <li>ഒറ്റപ്പദം (One-word substitute), പര്യായപദം (Synonyms), വിപരീതപദം (Antonyms), ശൈലികൾ / പഴഞ്ചൊല്ലുകൾ (Idioms & Proverbs).</li>
      <li>സമാനപദം (Words with similar meaning), സ്ത്രീലിംഗം - പുല്ലിംഗം (Gender forms), പിരിച്ചെഴുതുക (Splitting words), ചേർത്തെയെഴുതുക (Joining words).</li>
    </ul>
  </div>

  <div class="sec-heading">Part IV: Simple Arithmetic & Mental Ability (10 Marks)</div>
  <div class="unit-card">
    <div class="unit-title">Quantitative Aptitude & Reasoning</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Arithmetic:</span> Numbers and basic operations, Fractions and Decimals, Percentages, Profit and Loss, Simple and Compound Interest, Ratio and Proportion, Time and Work, Time and Distance, Averages.</li>
      <li><span class="topic-name">Mental Ability:</span> Series (Number, Alphabet), Coding and Decoding, Blood Relations, Direction Sense, Analogy, Odd one out, Clock and Calendar problems.</li>
    </ul>
  </div>
</body>
</html>
"""

# 2. Kerala PSC 10th Level Common Preliminary Syllabus
def get_kpsc_prelim_html():
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Kerala PSC 10th Level Common Preliminary Examination - Official Syllabus</title>
<style>{CSS}</style>
</head>
<body>
  <div class="header">
    <div class="inst-logo-sub">Kerala Public Service Commission (KPSC)</div>
    <h1>Common Preliminary Examination (SSLC / 10th Level)</h1>
    <h2>Official Screening Examination Syllabus for Lower Division Clerk (LDC) & Equivalent Posts</h2>
    <div class="badge-bar">
      <span class="badge">Screening Stage: Common Preliminary</span>
      <span class="badge">Standard: 10th Standard / Matriculation</span>
      <span class="badge">Duration: 75 Minutes</span>
    </div>
  </div>

  <table class="pattern-table">
    <tr>
      <th>Subject Category</th>
      <th>Marks Weightage</th>
      <th>Language Medium</th>
    </tr>
    <tr>
      <td>General Knowledge & Current Affairs (History, Geography, Economics, Civics, Kerala Affairs)</td>
      <td>50 Marks</td>
      <td>Malayalam / Tamil / Kannada</td>
    </tr>
    <tr>
      <td>General Science (Natural Science, Physical Science, Public Health)</td>
      <td>20 Marks</td>
      <td>Malayalam / Tamil / Kannada</td>
    </tr>
    <tr>
      <td>Simple Arithmetic & Mental Ability</td>
      <td>20 Marks</td>
      <td>Malayalam / Tamil / Kannada</td>
    </tr>
    <tr>
      <td>General English & Regional Language Basics</td>
      <td>10 Marks</td>
      <td>English / Malayalam</td>
    </tr>
  </table>

  <div class="unit-card">
    <div class="unit-title">Section 1: General Knowledge, Indian & Kerala History</div>
    <ul class="unit-topics">
      <li>Salient features of Indian independence movement, landmark struggles in Kerala history, renaissance leaders of Kerala.</li>
      <li>Basic features of Indian Constitution, fundamental rights, directive principles, governance machinery.</li>
      <li>Geography of India and Kerala: physical features, climate, soil, major rivers, mineral wealth, transport systems.</li>
      <li>Flagship development and welfare schemes implemented by the Government of Kerala.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Section 2: General Science & Health</div>
    <ul class="unit-topics">
      <li>Human organ systems, nutrition and balanced diet, communicable and non-communicable diseases, public health hygiene.</li>
      <li>Basic physics concepts: force, pressure, motion, energy, optics, acoustics, heat and electricity.</li>
      <li>Basic chemistry concepts: elements, compounds, mixtures, acids and bases, metals and non-metals.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">Section 3: Simple Arithmetic & Mental Ability</div>
    <ul class="unit-topics">
      <li>Fundamental arithmetic operations, LCM & HCF, fractions and decimals, percentages, profit & loss, ratio & proportion.</li>
      <li>Simple interest, compound interest, time & work, work & wages, speed, distance & time.</li>
      <li>Alphabetical & numerical series, coding-decoding, mathematical operational replacements, blood relations, spatial awareness.</li>
    </ul>
  </div>
</body>
</html>
"""

# 3. SSC CHSL (LDC / JSA) Official Syllabus
def get_ssc_chsl_ldc_html():
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Staff Selection Commission - SSC CHSL (LDC / JSA) Official Syllabus</title>
<style>{CSS}</style>
</head>
<body>
  <div class="header">
    <div class="inst-logo-sub">Staff Selection Commission (SSC)</div>
    <h1>Combined Higher Secondary Level (CHSL) Examination</h1>
    <h2>Official Syllabus for Lower Division Clerk (LDC) / Junior Secretariat Assistant (JSA)</h2>
    <div class="badge-bar">
      <span class="badge">Tier 1: Computer Based Examination</span>
      <span class="badge">Tier 2: Objective & Skill/Typing Test</span>
      <span class="badge">Cadre: Central LDC / JSA</span>
    </div>
  </div>

  <table class="pattern-table">
    <tr>
      <th>Tier</th>
      <th>Section / Module</th>
      <th>Questions</th>
      <th>Max Marks</th>
    </tr>
    <tr>
      <td rowspan="4"><strong>Tier 1 (60 Mins)</strong></td>
      <td>English Language (Basic Knowledge)</td>
      <td>25</td>
      <td>50</td>
    </tr>
    <tr>
      <td>General Intelligence & Reasoning</td>
      <td>25</td>
      <td>50</td>
    </tr>
    <tr>
      <td>Quantitative Aptitude (Basic Arithmetic Skills)</td>
      <td>25</td>
      <td>50</td>
    </tr>
    <tr>
      <td>General Awareness</td>
      <td>25</td>
      <td>50</td>
    </tr>
    <tr>
      <td rowspan="3"><strong>Tier 2 (Session I & II)</strong></td>
      <td>Module I: Mathematical Abilities + Module II: Reasoning</td>
      <td>60</td>
      <td>180</td>
    </tr>
    <tr>
      <td>Module I: English Language + Module II: General Awareness</td>
      <td>60</td>
      <td>180</td>
    </tr>
    <tr>
      <td>Computer Knowledge Module + Typing Test for LDC/JSA</td>
      <td>15 Qs + Typing</td>
      <td>45 (Qualifying)</td>
    </tr>
  </table>

  <div class="sec-heading">Tier 1 Detailed Modules</div>

  <div class="unit-card">
    <div class="unit-title">1. English Language</div>
    <ul class="unit-topics">
      <li>Spot the Error, Fill in the Blanks, Synonyms/Homonyms, Antonyms, Spellings/Detecting mis-spelt words, Idioms & Phrases, One word substitution, Improvement of Sentences, Active/Passive Voice, Direct/Indirect narration, Shuffling of Sentence parts, Cloze Passage, Comprehension Passage.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">2. General Intelligence</div>
    <ul class="unit-topics">
      <li>Semantic Analogy, Symbolic/Number Analogy, Figural Analogy, Semantic Classification, Symbolic/Number Classification, Space Orientation, Venn Diagrams, Drawing inferences, Figural Classification, Punched hole/pattern-folding & unfolding, Semantic Series, Figural Pattern-folding and completion, Number Series, Embedded figures, Critical Thinking, Problem Solving.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">3. Quantitative Aptitude</div>
    <ul class="unit-topics">
      <li><span class="topic-name">Number Systems:</span> Computation of Whole Numbers, Decimals and Fractions, Relationship between numbers.</li>
      <li><span class="topic-name">Fundamental Arithmetical Operations:</span> Percentages, Ratio and Proportion, Square roots, Averages, Interest (Simple and Compound), Profit and Loss, Discount, Partnership Business, Mixture and Alligation, Time and distance, Time and work.</li>
      <li><span class="topic-name">Algebra & Geometry:</span> Basic algebraic identities, linear equations, triangles, circles, tangents, quadrilaterals, regular polygons.</li>
      <li><span class="topic-name">Mensuration & Trigonometry:</span> Sphere, hemisphere, cylinders, cones, trigonometric ratios, heights and distances.</li>
    </ul>
  </div>

  <div class="unit-card">
    <div class="unit-title">4. General Awareness</div>
    <ul class="unit-topics">
      <li>Questions designed to test knowledge of current events and matters of everyday observation; History, Culture, Geography, Economic Scene, General Policy, and Scientific Research relating to India and neighboring countries.</li>
    </ul>
  </div>

  <div class="sec-heading">Tier 2 Skill Test: Typing Test for LDC / JSA</div>
  <div class="unit-card">
    <div class="unit-title">Typing Speed Standards</div>
    <ul class="unit-topics">
      <li>English Medium: 35 words per minute (w.p.m.) corresponding to ~10,500 key depressions per hour.</li>
      <li>Hindi Medium: 30 words per minute (w.p.m.) corresponding to ~9,000 key depressions per hour.</li>
      <li>Test Duration: 10 minutes on computerized passage entry.</li>
    </ul>
  </div>
</body>
</html>
"""

def main():
    generate_pdf(get_kpsc_ldc_mains_html(), "syllabus/LDC/Kerala_PSC_LDC_Mains_Official_Syllabus_and_Exam_Pattern.pdf")
    generate_pdf(get_kpsc_prelim_html(), "syllabus/LDC/Kerala_PSC_10th_Level_Preliminary_Official_Syllabus.pdf")
    generate_pdf(get_ssc_chsl_ldc_html(), "syllabus/LDC/SSC_CHSL_LDC_Tier1_and_Tier2_Official_Syllabus.pdf")

if __name__ == '__main__':
    main()
