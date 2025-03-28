# vibe-coding

 entirely vibecoded and semi-vibecoded little projects... various AI
LLMs and various languagues.  


## background

I give up and carve-in to the idea that I simply don't like the
expression"vibe coding", but that is exactly what I am doing here in
this project.

folder structure will emerge eventually, at this point in time it's
rather random.


sooo... let's dive right in.


## timeline / progress

here i'll add 3rd level headlines that represent my vibe-coding timeline / eprogress / "evolution" 


## boring hardcoded anagram toy
### initial prompt


```
generate an ordered list ("data set") of all "perfect" anagrams
(exclude duplicate anagrams early).  these are your Letters. you HAVE
TO always use all letters, and always all of them, you are restricted
to only and exactly these letters!!!!  Every time you pick a letter
from the set, you can no longer use it.  Example you have exactly one
'L' at your disposal, but two 'A'.  [A, A, I, I, O, T, N, N, S, S, L,
M]

did you understand the task?  first re-formulate  the task in a best possible way for yourself and other AI LLMs that it's VERY  clear instructions that are as brief and short as possible but have zero margin of error or misunderstandings!   in your next reply, in the first step, give me that instruction, I'll need it later! in the second step, give me  BASH script code to generate this  data set (as efficiently as possible) and output the resulting dataset to STDOUT!  afterwards, I want to hard-code this data-set. 

make sure you are 100% accurate in generating this dataset, I WILL test your output an scrutinize.
```

### Step 1: Re-formulated Task Instruction

``` 
Generate every unique permutation (perfect anagram) of the given
multiset of letters—specifically, 2×A, 2×I, 1×O, 1×T, 2×N, 2×S, 1×L,
1×M. Every anagram must use exactly these 12 letters (using each
letter only as many times as available), and duplicate anagrams must
be eliminated. The final output should be an ordered
(e.g. lexicographically sorted) list.
```

#### Step 1b: Bash script

```bash
#!/usr/bin/env bash
python3 << 'EOF'
def next_permutation(seq):
    # Convert sequence to a list (in case it's not already)
    seq = list(seq)
    # Step 1: Find the largest index i such that seq[i] < seq[i+1]
    i = len(seq) - 2
    while i >= 0 and seq[i] >= seq[i+1]:
        i -= 1
    if i < 0:
        return None  # Last permutation reached
    # Step 2: Find the largest index j greater than i such that seq[j] > seq[i]
    j = len(seq) - 1
    while seq[j] <= seq[i]:
        j -= 1
    # Step 3: Swap the value of seq[i] with that of seq[j]
    seq[i], seq[j] = seq[j], seq[i]
    # Step 4: Reverse the subsequence from seq[i+1] to the end
    seq[i+1:] = reversed(seq[i+1:])
    return seq

# Start with the sorted list of letters.
# Sorted order of: [A, A, I, I, O, T, N, N, S, S, L, M] is:
letters = sorted(['A','A','I','I','O','T','N','N','S','S','L','M'])

current = letters
while current is not None:
    # Print the current permutation as a string.
    print("".join(current))
    current = next_permutation(current)
EOF
```
