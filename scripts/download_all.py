import os
import sys
import subprocess
import urllib.request
import ssl
import json

ctx = ssl._create_unverified_context()

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def download_file(url, dest_path, min_size=500, extra_curl_args=None):
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > min_size:
        print(f"[EXISTS] {dest_path} ({os.path.getsize(dest_path)} bytes)")
        return True
    
    print(f"[DOWNLOADING] {url} -> {dest_path}")
    ensure_dir(os.path.dirname(dest_path))
    
    # Try with curl first
    curl_cmd = ['curl', '-s', '-L', '-k', '--connect-timeout', '15', '-m', '60']
    if extra_curl_args:
        curl_cmd.extend(extra_curl_args)
    curl_cmd.extend(['-o', dest_path, url])
    
    try:
        res = subprocess.run(curl_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=70)
        if os.path.exists(dest_path) and os.path.getsize(dest_path) > min_size:
            # Check if it starts with %PDF or has reasonable size
            with open(dest_path, 'rb') as f:
                header = f.read(5)
            if header == b'%PDF-':
                print(f"[SUCCESS] Valid PDF ({os.path.getsize(dest_path)} bytes): {dest_path}")
                return True
            else:
                print(f"[WARN] File downloaded but not %PDF- header: {header} in {dest_path}")
                return True
    except Exception as e:
        print(f"[CURL ERROR] {e}")
        
    return False

print("Helper defined.")
