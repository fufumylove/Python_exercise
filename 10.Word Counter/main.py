# Find the number of words in a sentence

# USE:
# 1. User_Input
# 2. Functions
# 3. f-string
import string

def count_word(sentence):
    # 创建一个删除标点符号的翻译表
    translator = str.maketrans('', '', string.punctuation)
    # 使用translate方法去除标点符号
    sentence = sentence.translate(translator)
    word_list = sentence.split()
    print(word_list)
    return len(word_list)

user_input = input("Please enter your sentence here: ")

num_words = count_word(user_input)
print(f"The number of words in your sentences is: {num_words}")