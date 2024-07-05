## Introduction
This repository contains scripts and code for solving problems within the field of bioinformatics.

### GC Content Percentage
A nucleotide sequence consists of the nucleotides adenine (A), cytosine (C), guanine (G), and thymine (T). The GC content percentage (also called the GC ratio) is calculated as follows:
```bash
((number_of_G + number_of_C) / (number_of_A + number_of_C + number_of_G + number_of_T)) * 100
```
A python script for calculating this value can be found over [here](python/calculate_gc_content_percentage.py).   

### Boyer-Moore Algorithm
The [Boyer-Moore string search algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm) is an algorithm for finding a substring within a string. It is more efficient than using a brute-force method.   

The substring and string have their characters compared, starting from the right-most character of the substring. If the values match, then we shift the substring one index to the _left_ and compare again. If they do not match, then we shift the substring a certain number of indices to the _right_. By how many spaces or indices do we need to shift the substring to the right? A matching table (or dictionary) is constructed from the characters in the substring. This table (or dictionary) has the character as a key and the corresponding value which comes from the formula:
```bash
shift_value = max(1, length_of_substring - index_of_current_character - 1)
```   

This value, which we'll call the `shift_value`, is the amount by which we need to shift the substring to the right as we continue to compare the string to the substring during the iteration. The [boyerMooreAlgorithm.py](python/boyerMooreAlgorithm.py) file contains an implementation of this algorithm.