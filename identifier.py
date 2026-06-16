import json
import os
import hashlib
import zipfile



with open("signatures.json") as f :
    signatures = json.load(f)

def identify_file(path):
    with open(path,"rb") as f:
        header = f.read(32)
        header_hex = header.hex().upper()

    for entry in signatures:
        if header_hex.startswith(entry["signature"]):
            return entry
        
    return None

def calculate_sha256(path):
    sha256 = hashlib.sha256()

    with open(path,"rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

def format_size(size):
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def inspect_zip(path):
    with zipfile.ZipFile(path,"r") as z:
        files = z.namelist()

        if "word/document.xml" in files:
            return "DOCX"
        if "xl/workbook.xml" in files:
            return "XLSX"
        if "ppt/presentation.xml" in files:
            return "PPTX"
        if "AndroidManifest.xml" in files:
            return "APK"
        if "META-INF/MANIFEST.MF" in files:
            return "JAR"
        
    return "ZIP"

path = input("Enter File path: ")

result = identify_file(path)

if result and result["name"] == "ZIP":
    actual_type = inspect_zip(path)
else:
    actual_type = result["name"]

if result:
    size = os.path.getsize(path)
    sha256 = calculate_sha256(path)
    filename_extension = os.path.splitext(path)[1].lower()

    print("\n=== File Information ===")
    print(f"type : {actual_type}")
    print(f"Extension : {result["extension"]}")
    print(f"Mime : {result["mime"]}")
    print(f"Size : {format_size(size)}")
    print(f"SHA256  : {sha256}")

    if filename_extension != result["extension"].lower():
        print("\n Warning Extention Missmatch")
        print(f"Filename extention : {filename_extension}")
        print(f"Actual Extention : {result["extension"]}")

else:
    print("Unknown File Type")
# result = identify_file("test.png")
# print(f"Detected : {result}")


# for filetype, signature in signatures.items():
#     if header_hex.startswith(signature):
#         print(f"Detected : {filetype}")
#         found = True
#         break

# if not found:
#     print("Unknown")

# def identify_file(path,signatures):
#     with open(path,"rb") as f:
#         header = f.read(32)

#     header_hex = header.hex().upper()

#     for filetype, sig in signatures.items():
#         if header_hex.startswith(sig):
#             return filetype

    # return "Unknown"



