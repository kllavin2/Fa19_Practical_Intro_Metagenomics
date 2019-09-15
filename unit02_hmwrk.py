#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:36:34 2019

@author: kristi beers
This script will detect if a fasta file is zipped or not then display
the number of sequences found and the total number of residues that make them
up.
"""
# for .gz files
import gzip
import re

# Test file from the Monterey Bay Microbial Study from the iMicrobe repository
file = 'CAM_PROJ_MontereyBay.read_pep.fa.gz'

# Holds the number of sequences found in the file
seq_count = 0

# Holds the number of residues(bases) found in the file
res_count = 0
# Test to see if a file is zipped and is a fasta file
if file.endswith('.fa.gz') or file.endswith('.fasta.gz'):
    with gzip.open(file, 'rt') as f:
        for line in f:
            if line.startswith('>'):
                seq_count += 1
#                length = re.search(r'length=\d*', line)
#                if length:
#                    res_count += int(length.group().split("=")[1])
#                begin = re.search(r'begin=\d*', line)
#                end = re.search(r'end=\d*', line)
#
#                if begin and end:
#                    begin = int(begin.group().split("=")[1])
#                    end = int(end.group().split("=")[1])
#                    res_count = res_count + end - begin
            else:
                line.strip('\n')
                for x in line:
                    if x.isalpha():
                        res_count += 1
    print('Total sequences found: ', seq_count)
    print('Total residues found: ', res_count)

# If the files is a fastq file not zipped
else:
    if file.endswith('.fa') or file.endswith('fasta'):
        with open(file) as filename:
            for line in filename:
                if line.startswith('>'):
                    seq_count += 1
                else:
                    line.strip('\n')

                    for x in line:
                        if x.isalpha():
                            res_count += 1
        print('Total sequences found: ', seq_count)
        print('Total residues found: ', res_count)
