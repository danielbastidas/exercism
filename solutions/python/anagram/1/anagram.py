def find_anagrams(word, candidates):
    anagrams = []
    word = word.lower()
    for index, candidate in enumerate(candidates):
        candidate = candidate.lower()
        if len(word) == len(candidate) and word != candidate:
            for letter in word:
                candidate = candidate.replace(letter, '', 1)
            if len(candidate) == 0:
                anagrams.append(candidates[index])
    return anagrams
