anagrams = {}
with open('words (1).txt') as f:
    for line in f:
        line = line.strip() #strip whitespace
        sortedline = ''.join(sorted(line)) #split each word into individual letters and sort them in alphabetical order
        anagrams.setdefault(sortedline, []).append(line) #sets a default value for each key if there is not one already and sets the key as the alphabetically sorted word, then appends the unsorted word to the dictionary entry if there is one with the same key
results = [i for i in anagrams.values() if len(i) > 1] #loop through to check to see if the values are the same(if the length of the value is greater than 1, then it has an anagram and is printed)
print results




