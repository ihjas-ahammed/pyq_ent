import os
import subprocess
import time

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

# 1. District-wise LDC Question Papers with Answer Keys (2011 - 2024)
ldc_mains = [
    # 2024
    ("1qndLn1vX4F1zoklX_-SqvHexE-8nmJO5", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2024_Thiruvananthapuram_Question_Paper_with_Answer_Key.pdf"),
    ("1Ms5ERIw_jryeKNKe2kJDyC979qF4bzpr", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2024_Kollam_Kannur_Question_Paper_with_Answer_Key.pdf"),
    ("1r9CciKnI9-0QX8t1Dn_wt1nvxAq0YABq", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2024_Thrissur_Pathanamthitta_Kasargod_Question_Paper_with_Answer_Key.pdf"),
    ("1vNEnMz1r6I422BTfZIirNs8APnTJVNJr", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2024_Kottayam_Kozhikode_Question_Paper_with_Answer_Key.pdf"),
    ("1ay8KZFztZmGo0gmTUOf5clpzaeWOFrLs", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2024_Malappuram_Idukki_Question_Paper_with_Answer_Key.pdf"),
    ("1mNFNLAQB5vQ808olltyIqcBLQFkioekY", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2024_Special_Recruitment_052_2024_Question_Paper_with_Answer_Key.pdf"),
    # 2023
    ("1l5PutMVpV7OP8IgjQR8oYzHuVLpBnShH", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2023_Clerk_Accountant_Cashier_239_2023_Question_Paper_with_Answer_Key.pdf"),
    # 2021
    ("1Fpjuv-PCuYqKr6ZTqTbz_SG8uHrmBB2p", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2021_Clerk_Mains_117_2021_Question_Paper_with_Answer_Key.pdf"),
    ("1cZnlpUyM_24IZLMi-Hm1FVjnhIW-BDZA", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2021_ExServicemen_100_2021_Question_Paper_with_Answer_Key.pdf"),
    # 2017
    ("10XO0gloMOs_tJKHXUAvggIoFub8r0xs0", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2017_Kollam_Thrissur_Kasaragod_077_2017_Question_Paper_with_Answer_Key.pdf"),
    ("10pdD2CmapuUBJ3dfBsBHqpBDnyM_0dnQ", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2017_Pathanamthitta_Palakkad_084_2017_Question_Paper_with_Answer_Key.pdf"),
    ("10XLyDVxxU2VaSZGgzbIt29irD5jeAjsG", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2017_Kottayam_Wayanad_095_2017_Question_Paper_with_Answer_Key.pdf"),
    ("10c8OV2pOzwXGYHfdh0FV9Qi4b1uk2chl", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2017_Ernakulam_Kannur_078_2017_Question_Paper_with_Answer_Key.pdf"),
    ("10oJEs_zWi7QQAgkjxEJSLPjwMlxEynxv", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2017_Idukki_Alappuzha_Kozhikode_079_2017_Question_Paper_with_Answer_Key.pdf"),
    # 2014
    ("1DwusUAcgDLXRfHET3cau7c-QtUJ3HVWM", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2014_Idukki_025_2014_Question_Paper_with_Answer_Key.pdf"),
    ("1DxEoz4qq_2f8x_NQM3BCXct-T7kr5e0N", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2014_Ernakulam_001_2014_Question_Paper_with_Answer_Key.pdf"),
    ("1DywnaDdlxybclJ4_9FflHPliWIsIMhB8", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2014_Malappuram_024_2014_Question_Paper_with_Answer_Key.pdf"),
    ("1E2MxMCnkoe30jih8TM7XkodZvCnQapLo", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2014_Palakkad_017_2014_Question_Paper_with_Answer_Key.pdf"),
    ("1EGbZrqirjDROkgi0EtkAPSJo3tTQenCL", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2014_Kozhikode_007_2014_Question_Paper_with_Answer_Key.pdf"),
    ("1EG3yQvT_Rtm-xWi9Mcs15zvi8qC3DS-q", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2014_Various_002_2014_Question_Paper_with_Answer_Key.pdf"),
    # 2013
    ("1-X4wV-mMb1AziRNpKYR0HKSrK9Cj3ze3", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2013_Various_147_2013_Question_Paper_with_Answer_Key.pdf"),
    ("1-oEfL4Ma7249tReKkh9fTnqVCXCzdt3Z", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2013_Various_154_2013_Question_Paper_with_Answer_Key.pdf"),
    ("1-nv0hIauviyHIvYc_Nmd0GY3X6vX3Fn_", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2013_Pathanamthitta_162_2013_Question_Paper_with_Answer_Key.pdf"),
    ("1-q4LpEmo4kLQdkbagjJlSQikv1voekab", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2013_Kasaragod_148_2013_Question_Paper_with_Answer_Key.pdf"),
    # 2011
    ("1Rl3M3pUFDE58Hq4zqmhkEHz4vY8A9Xpt", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2011_Wayanad_058_2011_Question_Paper_with_Answer_Key.pdf"),
    ("1Rz7xP0e8fuj6Ww3eVE_I0TeN8RAVMyKR", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2011_Kozhikode_064_2011_Question_Paper_with_Answer_Key.pdf"),
    ("1Rwl4lZZZaEv73biZt5_FrYDV_P510LZd", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2011_Kottayam_063_2011_Question_Paper_with_Answer_Key.pdf"),
    ("1S-0LP7jEjIkTkRceb6prrkg_ntBay_YY", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2011_Ernakulam_057_2011_Question_Paper_with_Answer_Key.pdf"),
    ("1S4Uhwt2hNK_ZaPkZUjop5_c8-EtyOcOk", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2011_Alappuzha_069_2011_Question_Paper_with_Answer_Key.pdf"),
    ("1S7fqvfEOb4QwAF05uL8A8k2XUzueO6Gi", "LDC/Kerala_PSC_LDC_District_Mains/LDC_2011_Pathanamthitta_050_2011_Question_Paper_with_Answer_Key.pdf"),
]

# 2. Kerala PSC 10th Level Common Preliminary (LDC Screening Stage) (2021 - 2026)
prelim_drives = [
    # 2024
    ("10RvgSiQUCdYGLL5OO3lsWspp3RAk27cw", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2024_Stage_1_185_2024.pdf"),
    ("1NCNxo3DqK7w5NJWlqTcnKNJMi1SMNqcL", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2024_Stage_5_013_2024.pdf"),
    # 2023
    ("1HZsLgQ7ElS0dK-of4Ybkv4O5jQnCQNH2", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2023_Stage_1_202_2023.pdf"),
    ("1DZUgKh5K0-rizJdZB3COQy4pPYxd9_pa", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2023_Stage_2_224_2023.pdf"),
    ("1ytYRYFDVdEAkxT0t_3mLO_KB27cnAnLN", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2023_Stage_3_233_2023.pdf"),
    ("1rifMyaUjNdp4_u4ThYB0GzpX_Q-dLzKg", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2023_Session_B_141_2023.pdf"),
    ("1orF1U5FSQIXnndAEzMGg-an6aDK8SN9o", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2023_Session_B_154_2023.pdf"),
    ("1AtTk3NvLh9HNxqrmrbB3sBYPBO6STy67", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2023_Session_B_166_2023.pdf"),
    ("1pQwADbpEJj1LoTMEJA0lQrjgPTTEtEx4", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2023_Session_B_184_2023.pdf"),
    # 2022
    ("1jttNvwbdYv1EV3x-5NKHCygG-ao4oh-i", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2022_Stage_1_053_2022.pdf"),
    ("1tSwEfgrTAzhXQmprnFGy6IPanqYaUpAV", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2022_Stage_2_060_2022.pdf"),
    ("1EoOZuRjpcSIWHf0EkLAMx1Ofemd49RgG", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2022_Stage_3_068_2022.pdf"),
    ("1N9kqDWSGc3mbS7x6aoGc6peSH0KqWeQS", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2022_Stage_4_071_2022.pdf"),
    ("1ySQ6RbKenQWrBc2T7HPG9X0ohzUqrxEj", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2022_Stage_5_076_2022.pdf"),
    ("1SkSEiJGfSdel5y738ypqrAEwICNoGoMS", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2022_Stage_6_077_2022.pdf"),
    # 2021
    ("1IWAH74OSGU_3AvvqTC3kJ7pHHizJkTKG", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2021_Stage_1_029_2021.pdf"),
    ("1hDxv0YmkzGZbqlyr6WDTuPBPIU8zzc00", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2021_Stage_2_030_2021.pdf"),
    ("14qmRiX8CaG5PrjmSnEDhoYro_tWM4nql", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2021_Stage_3_031_2021.pdf"),
    ("1tx--G2yRsBdBqLIfTmn6JjBQxgiZPidB", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2021_Stage_4_032_2021.pdf"),
    ("1jVotfJss0JKMWXI04VeHz2p_nLmLtFKu", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2021_Stage_5_084_2021.pdf"),
]

# 3. Direct HTTP downloads (Firebase, Kerala PSC Official, Syllabi)
direct_downloads = [
    # 2026 10th Level Prelims
    ("https://firebasestorage.googleapis.com/v0/b/true-turn-learning.firebasestorage.app/o/mock_tests%2Fpdfs%2F1784367355145_10th%20Prelims%20Stage%201%20-%202026%20_%20Answer%20Key.pdf?alt=media&token=e681b677-47d7-48f9-b8c1-102837327363", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2026_Stage_1_with_Answer_Key.pdf"),
    ("https://firebasestorage.googleapis.com/v0/b/true-turn-learning.firebasestorage.app/o/mock_tests%2Fpdfs%2F1784384681856_10th%20Prelims%202nd%20Stage%20-%202026.pdf?alt=media&token=0e6b6981-8aef-498b-b388-9bb08e0ad91b", "LDC/Kerala_PSC_10th_Level_Preliminary/Kerala_PSC_10th_Level_Prelims_2026_Stage_2_Question_Paper.pdf"),
    # Official KPSC 2026 Clerk & LDC papers
    ("https://www.keralapsc.gov.in/sites/default/files/2026-09/088-2026-M-A.pdf", "LDC/Kerala_PSC_LDC_Official/Kerala_PSC_2026_Clerk_088_2026_Question_Paper_Malayalam.pdf"),
    ("https://www.keralapsc.gov.in/sites/default/files/2026-09/AnswerKeysFromJumpled_1.pdf", "LDC/Kerala_PSC_LDC_Official/Kerala_PSC_2026_Clerk_088_2026_Provisional_Answer_Key.pdf"),
    ("https://www.keralapsc.gov.in/sites/default/files/2026-09/final_answer_key__malayalam.pdf", "LDC/Kerala_PSC_LDC_Official/Kerala_PSC_2026_LDC_080_2026_Stage_II_Final_Answer_Key.pdf"),
    # Official Syllabi
    ("https://drive.google.com/uc?export=download&id=1lcIGxWn8Q7eJYad1g_ZWxe2B0NguLuVa", "syllabus/LDC/Kerala_PSC_LDC_Official_Syllabus_Malayalam_English.pdf"),
]

def download_file(url, dest):
    ensure_dir(dest)
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        with open(dest, 'rb') as f:
            if f.read(5) == b'%PDF-':
                print(f"[EXISTS] {dest} ({os.path.getsize(dest)} bytes)")
                return True
    
    cmd = ['curl', '-s', '-L', '-k', '-A', 'Mozilla/5.0', '--connect-timeout', '15', '-m', '90', '-o', dest, url]
    subprocess.run(cmd)
    
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        with open(dest, 'rb') as f:
            if f.read(5) == b'%PDF-':
                print(f"[OK] {dest} ({os.path.getsize(dest)} bytes)")
                return True
    print(f"[FAIL] {dest}")
    return False

def main():
    print("Starting Kerala PSC LDC and Preliminary exam papers download...")
    
    # 1. Download Mains
    for drive_id, path in ldc_mains:
        url = f"https://drive.google.com/uc?export=download&id={drive_id}"
        download_file(url, path)
        time.sleep(0.3)
        
    # 2. Download Prelims
    for drive_id, path in prelim_drives:
        url = f"https://drive.google.com/uc?export=download&id={drive_id}"
        download_file(url, path)
        time.sleep(0.3)
        
    # 3. Download Direct
    for url, path in direct_downloads:
        download_file(url, path)
        time.sleep(0.3)

if __name__ == '__main__':
    main()
