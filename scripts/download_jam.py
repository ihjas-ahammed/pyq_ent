import os, subprocess

base = "https://jam2026.iitb.ac.in/files"
jam_ph_urls = [
    (f"{base}/PH{y}.pdf", f"JAM/PH/JAM_{y}_Physics_Question_Paper.pdf") for y in range(2012, 2026)
]
jam_ph_urls.extend([
    (f"{base}/PH_QP.pdf", "JAM/PH/JAM_Physics_Question_Paper_Master.pdf"),
    (f"{base}/PH_AK.pdf", "JAM/PH/JAM_Physics_Final_Answer_Key.pdf")
])

# Also add CMI PG Physics papers (2011 to 2016)
for y in range(2011, 2017):
    jam_ph_urls.append((f"https://www.cmi.ac.in/admissions/sample-qp/pgphysics{y}.pdf", f"JAM/PH/Similar_CMI_PG_Physics_{y}_Question_Paper.pdf"))
    if y >= 2013:
        jam_ph_urls.append((f"https://www.cmi.ac.in/admissions/sample-qp/pgphysics{y}-solutions.pdf", f"JAM/PH/Similar_CMI_PG_Physics_{y}_Solutions.pdf"))

jam_mt_urls = [
    (f"{base}/MA{y}.pdf", f"JAM/MT/JAM_{y}_Mathematics_Question_Paper.pdf") for y in range(2012, 2026)
]
jam_mt_urls.extend([
    (f"{base}/MA_QP.pdf", "JAM/MT/JAM_Mathematics_Question_Paper_Master.pdf"),
    (f"{base}/MA_AK.pdf", "JAM/MT/JAM_Mathematics_Final_Answer_Key.pdf")
])

# Mathematical Statistics papers (2012 to 2026)
for y in range(2012, 2026):
    jam_mt_urls.append((f"{base}/MS{y}.pdf", f"JAM/MT/JAM_{y}_Mathematical_Statistics_Question_Paper.pdf"))
jam_mt_urls.extend([
    (f"{base}/MS_QP.pdf", "JAM/MT/JAM_Mathematical_Statistics_Question_Paper_Master.pdf"),
    (f"{base}/MS_AK.pdf", "JAM/MT/JAM_Mathematical_Statistics_Final_Answer_Key.pdf")
])

# Also CMI PG Math papers (2018 to 2025)
for y in range(2018, 2026):
    jam_mt_urls.append((f"https://www.cmi.ac.in/admissions/sample-qp/pgmath{y}.pdf", f"JAM/MT/Similar_CMI_PG_Mathematics_{y}_Question_Paper.pdf"))
    jam_mt_urls.append((f"https://www.cmi.ac.in/admissions/sample-qp/pgmath{y}-solutions.pdf", f"JAM/MT/Similar_CMI_PG_Mathematics_{y}_Solutions.pdf"))

all_urls = jam_ph_urls + jam_mt_urls

for u, p in all_urls:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if os.path.exists(p) and os.path.getsize(p) > 500:
        continue
    cmd = ['curl', '-s', '-L', '-k', '--connect-timeout', '10', '-m', '60', '-o', p, u]
    res = subprocess.run(cmd)
    if os.path.exists(p) and os.path.getsize(p) > 500:
        print(f"Downloaded: {p} ({os.path.getsize(p)} bytes)")
    else:
        print(f"Failed: {p}")
