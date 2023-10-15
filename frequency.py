from string import punctuation

def words_count(text: str) -> dict:
    sentence = "This this is simple, simple,,, metohd to do simple things in simple time"
    result =""
    for letter in sentence:
        if letter not in punctuation:
            result += letter
    print(result)
    sentence_split = result.split()

    dicty = {}
    for x in sentence_split:

            if x in dicty:
                dicty[x.lower()] += 1
            else:
                dicty[x.lower()] = 1
    return dicty


print(words_count("simple"))
