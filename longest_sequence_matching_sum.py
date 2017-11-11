## Given an array A and integer k, find the length of the longest sub-array (consecutive) whose sum is k.
## Example: given A = [100,1,2,3,-1,0,0,5,6,7], k = 5, return 6 (which is the length of [1,2,3,-1,0,0])

from collections import defaultdict

def max_seq_length(arr, k):
    
    left_sum = 0
    left_sums = [0]
    
    for n in arr:
        left_sum += n
        left_sums.append(left_sum)
    
    left_sums_plus_k = [i + k for i in left_sums]
    
    left_sums_index = defaultdict(list)
    for i, s in enumerate(left_sums):
        left_sums_index[s].append(i)
    
    max_length = 0
    for i, s in enumerate(left_sums_plus_k):
        positions = left_sums_index[s]
        if len(positions) == 0:
            continue
        seq_length = max(positions) - i
        if seq_length > max_length:
            max_length = seq_length
    return max_length


k = 5
arr = [100,1,2,3,-1,0,0,5,6,7]

print(max_seq_length(arr, k))
