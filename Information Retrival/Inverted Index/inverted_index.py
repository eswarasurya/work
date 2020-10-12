from copy import deepcopy


class Node:  # a node in a Trie data structure
    def __init__(self):
        self.child = [None] * 52
        self.end_list = None


class Trie:
    def __init__(self):
        self.root = Node()

    def get_index(self, ch):  # returns an index to insert for a given character
        temp = ord(ch) - ord('a')
        if temp < 0:
            temp = ord(ch) - 6  # - 33 + 27
        return temp

    def insert(self, key, doc_id):  # inserts a word in the dict and updates the posting list
        temp = self.root
        for i in range(len(key)):
            index = self.get_index(key[i])
            if not temp.child[index]:
                temp.child[index] = Node()
            temp = temp.child[index]
        if temp.end_list is None:
            temp.end_list = [[doc_id, 1]]
        else:
            pos = find_position(temp.end_list, doc_id)
            if pos != -1:
                temp.end_list[pos][1] += 1
            else:
                pos = get_insert_index(temp.end_list, doc_id)
                temp.end_list.insert(pos, [doc_id, 1])

    def find(self, key):  # finds the given word in the trie and returns its posting list
        temp = self.root
        for i in range(len(key)):
            index = self.get_index(key[i])
            if not temp.child[index]:
                return False
            temp = temp.child[index]
        if temp is not None and temp.end_list:
            return temp.end_list
        return False


def get_insert_index(l, x):  # Gets the insert to insert a new element in a posting list using binary search.
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

    return start


def find_position(l, x):  # Finds the position of a given element in the posting list using binary search.
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


def preprocess(doc_id):  # gets data from a document and returns a list of processed words.

    valid = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u',
             'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    stop_words = {'i': '', 'me': '', 'my': '', 'myself': '', 'we': '', 'our': '', 'ours': '', 'ourselves': '',
                  'you': '', 'your': '', 'yours': '', 'yourself': '', 'yourselves': '', 'he': '', 'him': '', 'his': '',
                  'himself': '', 'she': '', 'her': '', 'hers': '', 'herself': '', 'it': '', 'its': '', 'itself': '',
                  'they': '', 'them': '', 'their': '', 'theirs': '', 'themselves': '', 'what': '', 'which': '',
                  'who': '', 'whom': '', 'this': '', 'that': '', 'these': '', 'those': '', 'am': '', 'is': '',
                  'are': '', 'was': '', 'were': '', 'be': '', 'been': '', 'being': '', 'have': '', 'has': '', 'had': '',
                  'having': '', 'do': '', 'does': '', 'did': '', 'doing': '', 'a': '', 'an': '', 'the': '', 'and': '',
                  'but': '', 'if': '', 'or': '', 'because': '', 'as': '', 'until': '', 'while': '', 'of': '', 'at': '',
                  'by': '', 'for': '', 'with': '', 'about': '', 'against': '', 'between': '', 'into': '', 'through': '',
                  'during': '', 'before': '', 'after': '', 'above': '', 'below': '', 'to': '', 'from': '', 'up': '',
                  'down': '', 'in': '', 'out': '', 'on': '', 'off': '', 'over': '', 'under': '', 'again': '',
                  'further': '', 'then': '', 'once': '', 'here': '', 'there': '', 'when': '', 'where': '', 'why': '',
                  'how': '', 'all': '', 'any': '', 'both': '', 'each': '', 'every': '', 'few': '', 'more': '',
                  'most': '',
                  'other': '', 'some': '', 'such': '', 'no': '', 'nor': '', 'not': '', 'only': '', 'own': '',
                  'same': '', 'so': '', 'than': '', 'too': '', 'very': '', 's': '', 't': '', 'can': '', 'will': '',
                  'just': '', 'don': '', 'should': '', 'now': '', '': ''}  # storing stop words in a dict
    doc_id = str(doc_id)
    file = open('./th-dataset/' + doc_id + '.txt', 'r', encoding='utf8')
    s = file.read()
    s = s.lower()
    temp = ''
    for i in range(len(s)):
        if s[i] in valid:
            temp += s[i]
    s = temp.split(' ')
    temp = []
    for x in s:
        if x in stop_words or x in valid or x == '':
            pass
        else:
            temp.append(x)
    s.sort()
    return temp


def add_to_index(doc_id, index):  # adds words to the dict and updates the posting list accordingly
    words = preprocess(doc_id)
    for w in words:
        if w not in index:
            index[w] = [[doc_id, 1]]
        else:
            temp = find_position(index[w], doc_id)
            if temp != -1:
                index[w][temp][1] += 1
            else:
                temp = get_insert_index(index[w], doc_id)
                index[w].insert(temp, [doc_id, 1])


def write_to_file(index, file_name):  # writes the created dict to the output file
    file = open(file_name, "w", encoding='utf8')
    for i in index.keys():
        temp = sum(x[1] for x in index[i])
        file.write(i + ' (' + str(temp) + ') ==> {')
        for p in range(len(index[i])):
            if p == 0:
                file.write(str(index[i][p][0]) + '=' + str(index[i][p][1]))
            else:
                file.write(', ' + str(index[i][p][0]) + '=' + str(index[i][p][1]))
        file.write('}\n')

    file.close()


def find_in_index(word, index):  # finds a given word in the index
    if word in index:
        return index[word]
    return False


def add_to_index_trie(doc_id, index):  # adds words to the trie by calling insert method
    words = preprocess(doc_id)

    for w in words:
        index.insert(w, doc_id)


def return_trie(index, path, res):  # returns all the words and the posting list in the given trie
    for i in range(52):
        if index.child[i] is not None:
            path.append(i)
            if index.child[i].end_list is not None:
                temp = deepcopy(path)
                res.append([temp, index.child[i].end_list])
            return_trie(index.child[i], path, res)
    try:
        path.pop()
    except:
        return


def write_trie_to_file(index, file_name):  # writes the created trie to the output file
    res = []
    return_trie(index.root, [], res)
    file = open(file_name, "w", encoding='utf8')
    for i in range(len(res)):
        ch = ''
        for y in res[i][0]:
            if y < 27:
                ch += chr(y + ord('a'))
            else:
                ch += chr(y + 6)
        res[i][0] = ch
        temp = sum(x[1] for x in res[i][1])
        file.write(res[i][0] + ' (' + str(temp) + ') ==> {')
        for p in range(len(res[i][1])):
            if p == 0:
                file.write(str(res[i][1][p][0]) + '=' + str(res[i][1][p][1]))
            else:
                file.write(', ' + str(res[i][1][p][0]) + '=' + str(res[i][1][p][1]))
        file.write('}\n')


if __name__ == "__main__":

    # using dict and posting list to build inverted index
    index = {}
    for i in range(101, 282):   
        add_to_index(i, index)

    write_to_file(index, 'output.txt')

    word = 'playoffs'
    temp = find_in_index(word, index)
    print(word, temp)
    #################################################

    # using Trie and posting list to build inverted index
    index_trie = Trie()
    for i in range(101, 282):
        add_to_index_trie(i, index_trie)

    write_trie_to_file(index_trie, 'output.txt')

    word = 'playoffs'
    print(word, index_trie.find(word))
    #########################################################
