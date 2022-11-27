#!/bin/zsh

echo "Deleting outdated cache";
rm -rf output.ltx;
echo "Running script";
python3 FormulaeGenerator.py;
echo "Publishin to ~/out.pdf";
pandoc -i output.ltx -o ~/out.pdf;
