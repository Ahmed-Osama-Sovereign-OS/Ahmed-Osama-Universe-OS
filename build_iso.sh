#!/bin/bash
echo "Building Ahmed Osama Universe ISO..."
mkdir -p build/iso_root
cp main_core.py build/iso_root/
cp installer_logo.png build/iso_root/
# أمر توليد الـ ISO (يتطلب أدوات genisoimage)
genisoimage -o Ahmed_Osama_OS.iso -R -J build/iso_root
echo "The Monster ISO is Ready!"
