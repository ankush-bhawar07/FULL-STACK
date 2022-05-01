#  Reverse each word of a string

def reverse_words(sentence):
    # Split string on whitespace ( generates list of words)
    words = sentence.split(" ")

    # iterate list and reverse each word using ::-1
    reversed_words = [word[::-1] for word in words]

    # Joining the new list of words
    result = " ".join(reversed_words)

    return result

given_sentence = "Welcome To CodeCompete"
print(reverse_words(given_sentence))
