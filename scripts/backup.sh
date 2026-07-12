#!/bin/bash
# backup.sh
# Copies all .txt files from app/ into a backup/ folder and reports the count.

# Resolve paths relative to the project root, regardless of where the
# script is called from.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SOURCE_DIR="$PROJECT_ROOT/app"
BACKUP_DIR="$PROJECT_ROOT/backup"

mkdir -p "$BACKUP_DIR"

count=0
for file in "$SOURCE_DIR"/*.txt; do
    if [ -f "$file" ]; then
        cp "$file" "$BACKUP_DIR/"
        count=$((count + 1))
    fi
done

echo "Backup complete. $count file(s) copied."
