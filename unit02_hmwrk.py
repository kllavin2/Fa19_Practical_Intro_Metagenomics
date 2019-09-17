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

# Test file from the Monterey Bay Microbial Study from the iMicrobe repository
file = '/home/kristi/Documents/F19/CAM_PROJ_SargassoSea.read_pep.fa'

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
            else:
                line = line.rstrip()
                for x in line:
                    res_count += len(x)

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
                    line = line.rstrip()

                    for x in line:
                        res_count += len(x)
        print('Total sequences found: ', seq_count)
        print('Total residues found: ', res_count)

