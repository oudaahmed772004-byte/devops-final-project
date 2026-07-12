#!/bin/bash
# info.sh
# Prints basic system information in a readable format.

echo "=========================================="
echo "           SYSTEM INFORMATION"
echo "=========================================="

echo ""
echo "--- OS Name and Version ---"
if [ -f /etc/os-release ]; then
    grep -E "^(NAME|VERSION)=" /etc/os-release
else
    uname -a
fi

echo ""
echo "--- Current Logged-in User ---"
whoami

echo ""
echo "--- Current Date and Time ---"
date

echo ""
echo "--- Disk Usage Summary ---"
df -h

echo ""
echo "=========================================="
echo "              END OF REPORT"
echo "=========================================="
