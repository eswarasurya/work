def read_from_file(file_name):
    valid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    file = open('./' + file_name, 'r', encoding='utf8')
    s = file.read()
    s = s.lower()
    start = 0
    words = {}
    for i in range(len(s)):
        if s[i] not in valid:
            temp = s[start:i]
            if temp not in words:
                words[temp] = 1
            else:
                words[temp] += 1
            start = i + 1
    return words


def get_bigrams(file_name):
    file = open('./' + file_name, 'r', encoding='utf8')
    s = file.read()
    s = s.lower()
    s = s.split('\n')
    bigrams = {}
    for x in s:
        temp = x.replace('\t', ' ').split(' ')
        if temp[0] not in bigrams:
            bigrams[temp[0]] = [[temp[1], temp[2]]]
        else:
            bigrams[temp[0]].append([temp[1], temp[2]])
    return bigrams


def get_probability_of_word(word: str, words: dict):    # returns p(w) of a given word
    if word not in words:
        return 0
    total = sum(words.values())
    probability = words[word] / total
    return probability


def find_position(l, x):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (start + end) // 2
        if l[mid][0] == x:
            return mid
        elif l[mid][0] < x:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def get_bigram_probability(prev_word, word, bigrams):   # returns the occurrence of the word after the prev_word
    temp = bigrams[prev_word]
    start = 0       # finding word by binary search
    end = len(temp) - 1
    while start <= end:
        mid = (start + end) // 2
        if temp[mid][0] == word:
            return int(temp[mid][1])
        elif temp[mid][0] < word:
            start = mid + 1
        else:
            end = mid - 1
    return 1


def insert_word(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    inserts = []
    for x in letters:
        for i in range(len(word) + 1):
            inserts.append(word[:i] + x + word[i:])
    return inserts


def delete_word(word):
    deletes = []
    for i in range(len(word)):
        deletes.append(word[:i] + word[i + 1:])
    return deletes


def transpose_word(word):
    transpose = []
    for i in range(len(word) - 1):
        transpose.append(word[:i] + word[i + 1] + word[i] + word[i + 2:])
    return transpose


def replace_word(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    replace = []
    for x in letters:
        for i in range(len(word)):
            replace.append(word[:i] + x + word[i + 1:])
    return replace


def generate_edit1(word):   # generates all words within edit distance one
    return set(insert_word(word) + delete_word(word) + transpose_word(word) + replace_word(word))


def generate_edit(word, n):     # generates all words within edit distance n
    temp = [word]
    for i in range(n):
        temp2 = []
        for x in temp:
            temp2 += generate_edit1(x)
        temp = set(temp2)
    return temp2


def present_in_words(words, words_list):    # checks of the given word is present in the vocabulary
    temp = []
    for x in words:
        if x in words_list:
            temp.append(x)
    return set(temp)


def generate_candidate_set(word, word_list):    # Generates the candidate set for the given word
    if len(present_in_words([word], word_list)) != 0:
        return [word]
    if len(present_in_words(generate_edit(word, 1), word_list)) != 0:
        return present_in_words(generate_edit(word, 1), word_list)
    if len(present_in_words(generate_edit(word, 2), word_list)) != 0:
        return present_in_words(generate_edit(word, 2), word_list)
    return [word]


def correction(word, word_list):    # gets the correction of the given word
    max_list = []
    max = -1
    candidate_set = generate_candidate_set(word, word_list)
    for x in candidate_set:
        temp = get_probability_of_word(x, word_list)
        if temp == max:
            max_list.append(x)
        elif temp > max:
            max_list = [x]
            max = temp
    return max_list


def get_correction(word, prev_word, word_list, bigrams):    # gets the correction of a word considering the previous word
    max_value = 0
    max_item = ''
    candidate_set = generate_candidate_set(word, word_list)
    if prev_word == '':
        for x in candidate_set:
            temp = get_probability_of_word(x, word_list)
            if temp > max_value:
                max_item = x
                max_value = temp
    else:
        for x in candidate_set:
            temp = get_probability_of_word(x, word_list) * get_bigram_probability(prev_word, x, bigrams)
            if temp > max_value:
                max_item = x
                max_value = temp
    return max_item


def test(word_list, file_name):  # Tests against the given file and returns the accuracy
    file = open('./' + file_name, 'r', encoding='utf8')
    s = file.read()
    s = s.lower()
    s = s.split('\n')
    accuracy = 0
    count = 0
    for x in s:
        temp = x.split(' ')
        target = temp[0].replace(':', '')
        for i in range(1, len(temp)):
            count += 1
            correct = correction(temp[i], word_list)[0]
            print('word: ', temp[i], ' correction: ', correct, ' Acutal: ',  target)
            if target == correct:
                accuracy += 1
    return (accuracy / count) * 100


if __name__ == '__main__':
    word_list = read_from_file('big.txt')
    accuracy = test(word_list, 'spell-testset1.txt')
    print('Accuracy: ', accuracy)
    print()
    bigrams = get_bigrams('bigrams.txt')
    sentence = 'this is a veryy good moive'
    print('The given sentence: ', sentence)
    words = sentence.split(' ')
    res = ''
    prev = ''
    for i in range(len(words)):
        temp = get_correction(words[i], prev, word_list, bigrams)
        res += temp + ' '
        prev = temp
    print('After correction: ', res)
