def isValidSubsequence(array, sequence):
    # Write your code here.
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
# True
print(isValidSubsequence(array, sequence))

