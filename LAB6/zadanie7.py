# Testing shutil.copy
import os
import shutil


src = "source.txt"
dst_dir = "dest/"
dst_file = os.path.join(dst_dir, "source.txt")

# Ensure dest dir exists
os.makedirs(dst_dir, exist_ok=True)

# Create source file
with open(src, "w") as f:
  f.write("Test content")

# 1. File does not exist in dest
try:
  shutil.copy(src, dst_file)
  print("Copy 1: success")
except Exception as e:
  print(f"Copy 1 error: {e}")

# 2. File exists in dest
try:
  shutil.copy(src, dst_file)
  print("Copy 2: success")
except Exception as e:
  print(f"Copy 2 error: {e}")

# 3. Dest dir does not exist
try:
  shutil.copy(src, "nonexistent/source.txt")
  print("Copy 3: success")
except Exception as e:
  print(f"Copy 3 error: {e}")
