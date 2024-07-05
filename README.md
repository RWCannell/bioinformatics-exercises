## Introduction
This repository contains scripts and code for solving problems within the field of bioinformatics.

### GC Content Percentage
A nucleotide sequence consists of the nucleotides adenine (A), cytosine (C), guanine (G), and thymine (T). The GC content percentage (also called the GC ratio) is calculated as follows:
```bash
((number_of_G + number_of_C) / (number_of_A + number_of_C + number_of_G + number_of_T)) * 100
```
A python script for calculating this value can be found over [here](python/calculate_gc_content_percentage.py).