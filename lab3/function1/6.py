def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])


sentence = input("Введите предложение: ")
print(reverse_sentence(sentence))