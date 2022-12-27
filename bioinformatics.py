def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    # your code here
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        # add each key to words whose corresponding frequency value is equal to m
        if freq[key] == m:
            words.append(key)
    return words

# Copy your FrequencyMap() function here.
def FrequencyMap(Text, k):
    # your code here.
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    # for each dictionary item, count number of times it occurs in the Text
    
    for a in freq:
        count = 0
        for i in range(len(Text)-k +1):
             if Text[i:i+k] == a:
                count = count+1 
        freq[a] = count
    return freq


def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

    # Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    # your code here
    newPatt = Pattern[::-1]
    return newPatt

# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
def Complement(Pattern):
    complement_base = {"T":"A", "A":"T", "G":"C", "C":"G"}
    newPatt = ""
    for char in Pattern:
        newPatt = newPatt + complement_base[char]
    return newPatt

# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    for i in range(len(Genome)- len(Pattern) +1):
        if Genome[i:i+len(Pattern)] == Pattern:
           positions.append(i)
    return positions

text = "CCAGATC"
print(ReverseComplement(text))