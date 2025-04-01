#!/usr/bin/env python3
import itertools

# Define the multiset of letters
letters = ['A', 'A', 'I', 'I', 'O', 'T', 'N', 'N', 'S', 'S', 'L', 'M']

# Generate unique permutations and sort them lexicographically
perms = sorted(set(itertools.permutations(letters)))

# To demonstrate, print the first 100 permutations:
for p in perms[:100]:
    print(''.join(p))
