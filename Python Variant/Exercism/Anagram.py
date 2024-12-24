def find_anagrams(word, candidates):

    return [wurd for wurd in candidates if sorted(word.lower()) == sorted(wurd.lower()) \
        and word.lower() != wurd.lower()]