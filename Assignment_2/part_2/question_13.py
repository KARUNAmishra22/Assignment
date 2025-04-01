def word_intersection():
    word1 = input("Enter the first word: ").lower()
    word2 = input("Enter the second word: ").lower()
    common_letters = set(word1) & set(word2)
    if common_letters:
        print(f"The common letters are: {', '.join(common_letters)}")
    else:
        print("There are no common letters.")

word_intersection()
