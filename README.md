# File Type Identifier

A Python-based file analysis utility that identifies a file's true type using magic number signatures rather than relying on file extensions.

## Features

- Magic number file type detection
- JSON signature database
- SHA256 hashing
- Human-readable file sizes
- MIME type identification
- Extension mismatch detection
- ZIP container analysis
- Detects:
  - DOCX
  - XLSX
  - PPTX
  - APK
  - JAR

## Example

```text
=== File Information ===

Type      : DOCX
Extension : .zip
Mime      : application/zip
Size      : 11.14 KB

SHA256    : 825e2228...

WARNING:
Extension mismatch detected!
```

## Technologies

- Python
- JSON
- hashlib
- os
- zipfile

## Future Improvements

- Directory scanning
- JSON reports
- CSV reports
