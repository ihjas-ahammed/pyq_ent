import os, subprocess, re

# LBS SET questions base url: https://lbsedp.lbscentre.in/set/
sessions = [
    ('2026_Jan', '261', '2026_January'),
    ('2025_Jul', '257', '2025_July'),
    ('2025_Jan', '251', '2025_January'),
    ('2024_Jul', '247', '2024_July'),
    ('2024_Jan', '241', '2024_January'),
    ('2023_Jul', '237', '2023_July'),
    ('2023_Jan', '231', '2023_January'),
]

lbs_downloads = []

for sess_id, prefix, sess_name in sessions:
    # Physics (Code 24)
    lbs_downloads.append((
        f"https://lbsedp.lbscentre.in/set/questions/{sess_id}/{prefix}24.pdf",
        f"LBS/Kerala_SET_Physics/SET_{sess_name}_Physics_Question_Paper.pdf",
        ['--ciphers', 'DEFAULT:@SECLEVEL=1']
    ))
    # Mathematics (Code 21)
    lbs_downloads.append((
        f"https://lbsedp.lbscentre.in/set/questions/{sess_id}/{prefix}21.pdf",
        f"LBS/Kerala_SET_Mathematics/SET_{sess_name}_Mathematics_Question_Paper.pdf",
        ['--ciphers', 'DEFAULT:@SECLEVEL=1']
    ))
    # Statistics (Code 31)
    lbs_downloads.append((
        f"https://lbsedp.lbscentre.in/set/questions/{sess_id}/{prefix}31.pdf",
        f"LBS/Kerala_SET_Statistics/SET_{sess_name}_Statistics_Question_Paper.pdf",
        ['--ciphers', 'DEFAULT:@SECLEVEL=1']
    ))
    # General Paper Teaching Aptitude (Code 36)
    lbs_downloads.append((
        f"https://lbsedp.lbscentre.in/set/questions/{sess_id}/{prefix}36.pdf",
        f"LBS/Kerala_SET_General_Paper_Teaching_Aptitude/SET_{sess_name}_General_Paper.pdf",
        ['--ciphers', 'DEFAULT:@SECLEVEL=1']
    ))

# LBS MCA Entrance Keys & Papers
lbs_downloads.extend([
    (
        "https://lbsedp.lbscentre.in/keys/2026/26020-revised.pdf",
        "LBS/LBS_MCA_Entrance/LBS_MCA_2026_Entrance_Revised_Answer_Key.pdf",
        ['--ciphers', 'DEFAULT:@SECLEVEL=1']
    ),
    (
        "https://lbsedp.lbscentre.in/keys/2025/25020-revised.pdf",
        "LBS/LBS_MCA_Entrance/LBS_MCA_2025_Entrance_Revised_Answer_Key.pdf",
        ['--ciphers', 'DEFAULT:@SECLEVEL=1']
    ),
    (
        "https://lbsedp.lbscentre.in/keys/2024/24025.pdf",
        "LBS/LBS_MCA_Entrance/LBS_MCA_2024_Entrance_Answer_Key.pdf",
        ['--ciphers', 'DEFAULT:@SECLEVEL=1']
    ),
    (
        "https://lbsedp.lbscentre.in/keys/2023/23013-revised.pdf",
        "LBS/LBS_MCA_Entrance/LBS_MCA_2023_Entrance_Revised_Answer_Key.pdf",
        ['--ciphers', 'DEFAULT:@SECLEVEL=1']
    ),
    (
        "https://lbsedp.lbscentre.in/setjan26/keys/setjan2026_revised_key.pdf",
        "LBS/Kerala_SET_General_Paper_Teaching_Aptitude/SET_2026_Jan_Revised_Answer_Key_All_Subjects.pdf",
        ['--ciphers', 'DEFAULT:@SECLEVEL=1']
    ),
    (
        "https://lbscentre.in/postbbscnursing2024/downloads/previousquestion.pdf",
        "LBS/LBS_Other_Entrance/LBS_Nursing_Entrance_Previous_Question_Paper.pdf",
        None
    )
])

print(f"Total LBS items to download: {len(lbs_downloads)}")
for url, path, extra in lbs_downloads:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path) and os.path.getsize(path) > 500:
        print(f"[EXISTS] {path}")
        continue
    cmd = ['curl', '-s', '-L', '-k', '--connect-timeout', '10', '-m', '60']
    if extra:
        cmd.extend(extra)
    cmd.extend(['-o', path, url])
    subprocess.run(cmd)
    if os.path.exists(path) and os.path.getsize(path) > 500:
        print(f"[OK] {path} ({os.path.getsize(path)} bytes)")
    else:
        print(f"[FAIL] {path}")
