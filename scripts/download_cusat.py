import os, subprocess, json, urllib.request

# 1. Download SelfStudys CUSAT Solved Papers
papers = [
    ('2023', 'https://www.selfstudys.com/sitepdfs/X9bUfErSoHsKX1B2OTEH'),
    ('2022', 'https://www.selfstudys.com/sitepdfs/7h41rLNtUNi2p7qx5RVN'),
    ('2021', 'https://www.selfstudys.com/sitepdfs/7pW3XW9I1JGRwI83wEqz'),
    ('2019', 'https://www.selfstudys.com/sitepdfs/H0vEU5no2UXgbcbE7j3l'),
    ('2018', 'https://www.selfstudys.com/sitepdfs/mbE65ObIjnCWBCE9CFUg')
]

os.makedirs("CUSAT/PH", exist_ok=True)
os.makedirs("CUSAT/MT", exist_ok=True)

for year, url in papers:
    ph_dest = f"CUSAT/PH/CUSAT_CAT_{year}_Physics_Chemistry_Maths_Solved_Paper.pdf"
    mt_dest = f"CUSAT/MT/CUSAT_CAT_{year}_Physics_Chemistry_Maths_Solved_Paper.pdf"
    
    if not (os.path.exists(ph_dest) and os.path.getsize(ph_dest) > 10000):
        print(f"Downloading CUSAT {year}...")
        cmd = ['curl', '-s', '-L', '-k', '--connect-timeout', '15', '-m', '90', '-o', ph_dest, url]
        subprocess.run(cmd)
    
    if os.path.exists(ph_dest) and os.path.getsize(ph_dest) > 10000:
        print(f"Downloaded CUSAT {year}: {os.path.getsize(ph_dest)} bytes")
        # Hardlink or copy to CUSAT/MT
        if not os.path.exists(mt_dest):
            try:
                os.link(ph_dest, mt_dest)
            except Exception:
                import shutil
                shutil.copy2(ph_dest, mt_dest)
            print(f"Linked to {mt_dest}")
    else:
        print(f"Failed to download CUSAT {year}")

# 2. Fetch 2025s4.json and render HTML -> PDF for Physics and Mathematics
print("Fetching 2025 dataset...")
url_2025 = 'https://raw.githubusercontent.com/ABHINAV-321/Cusat-pyq/master/2025s4.json'
req = urllib.request.Request(url_2025, headers={'User-Agent': 'Mozilla/5.0'})
raw_data = urllib.request.urlopen(req).read().decode('utf-8')
data_2025 = json.loads(raw_data)

def render_subject_pdf(subject_key, subject_title, output_pdf):
    sub_qs = [q for q in data_2025 if q.get('subject') == subject_key]
    print(f"Generating PDF for {subject_title}: {len(sub_qs)} questions...")
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>CUSAT CAT 2025 - {subject_title} Question Paper with Detailed Solutions</title>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
  @page {{
    size: A4;
    margin: 1.5cm;
    @bottom-center {{
      content: counter(page);
    }}
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1f2937;
    line-height: 1.5;
    padding: 0;
    margin: 0;
  }}
  .header {{
    text-align: center;
    border-bottom: 2px solid #2563eb;
    padding-bottom: 15px;
    margin-bottom: 25px;
  }}
  .header h1 {{
    margin: 0 0 6px 0;
    color: #1e3a8a;
    font-size: 22pt;
  }}
  .header h2 {{
    margin: 0 0 6px 0;
    color: #3b82f6;
    font-size: 15pt;
  }}
  .header p {{
    margin: 0;
    color: #4b5563;
    font-size: 10pt;
  }}
  .q-card {{
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 18px;
    page-break-inside: avoid;
    background: #ffffff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }}
  .q-header {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 8px;
  }}
  .q-num {{
    font-weight: 700;
    color: #1e40af;
    font-size: 11pt;
  }}
  .q-diff {{
    font-size: 8pt;
    text-transform: uppercase;
    background: #eff6ff;
    color: #1d4ed8;
    padding: 2px 8px;
    border-radius: 9999px;
    font-weight: 600;
  }}
  .q-text {{
    font-size: 10.5pt;
    margin-bottom: 12px;
    color: #111827;
  }}
  .options-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 12px;
  }}
  .opt-item {{
    padding: 8px 12px;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    font-size: 10pt;
    background: #f9fafb;
  }}
  .opt-item.correct {{
    border-color: #16a34a;
    background: #f0fdf4;
    color: #15803d;
    font-weight: 600;
  }}
  .sol-box {{
    background: #f8fafc;
    border-left: 3px solid #3b82f6;
    padding: 10px 14px;
    border-radius: 0 6px 6px 0;
    font-size: 9.5pt;
    color: #334155;
  }}
  .sol-title {{
    font-weight: 700;
    color: #1e3a8a;
    margin-bottom: 4px;
  }}
</style>
</head>
<body>
  <div class="header">
    <h1>Cochin University of Science and Technology</h1>
    <h2>CUSAT CAT 2025 Entrance Examination</h2>
    <p>Subject: <strong>{subject_title}</strong> | Questions: {len(sub_qs)} | Complete with Official Answers & Detailed Step-by-Step Solutions</p>
  </div>
"""
    for idx, q in enumerate(sub_qs, 1):
        q_text = q.get('question', '').replace('<', '&lt;').replace('>', '&gt;')
        diff = q.get('difficulty', 'standard').capitalize()
        correct_idx = q.get('correct', 0)
        options = q.get('options', [])
        ans_text = q.get('answer', '')
        exp_text = q.get('explanation', '')
        
        opt_html = ""
        for oi, opt in enumerate(options):
            is_c = (oi == correct_idx)
            c_class = " correct" if is_c else ""
            prefix = f"({chr(65+oi)}) "
            opt_html += f'<div class="opt-item{c_class}">{prefix}{opt}</div>'
            
        html += f"""
  <div class="q-card">
    <div class="q-header">
      <span class="q-num">Question {idx}</span>
      <span class="q-diff">{diff}</span>
    </div>
    <div class="q-text">{q_text}</div>
    <div class="options-grid">
      {opt_html}
    </div>
    <div class="sol-box">
      <div class="sol-title">Correct Answer: Option ({chr(65+correct_idx)}) | {ans_text}</div>
      <div><strong>Explanation:</strong> {exp_text}</div>
    </div>
  </div>
"""
    html += """
</body>
</html>
"""
    tmp_html = f"/tmp/cusat_{subject_key}_2025.html"
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"HTML written to {tmp_html}, rendering PDF via chrome...")
    chrome_cmd = [
        'google-chrome-stable',
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={output_pdf}',
        tmp_html
    ]
    subprocess.run(chrome_cmd)
    if os.path.exists(output_pdf):
        print(f"Generated: {output_pdf} ({os.path.getsize(output_pdf)} bytes)")
    else:
        print(f"Failed to render: {output_pdf}")

render_subject_pdf('physics', 'Physics', 'CUSAT/PH/CUSAT_CAT_2025_Physics_PYQ_with_Solutions.pdf')
render_subject_pdf('maths', 'Mathematics', 'CUSAT/MT/CUSAT_CAT_2025_Mathematics_PYQ_with_Solutions.pdf')

