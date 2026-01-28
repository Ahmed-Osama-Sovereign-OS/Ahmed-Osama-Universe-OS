#!/bin/bash
echo "Building Ahmed Osama Universe OS ISO..."
# كود تحويل الملفات إلى ISO
genisoimage -o Ahmed_Osama_OS.iso -R -J .
echo "The Monster is Ready for Action!"
