from copy import deepcopy
import math
import heapq


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

    doc_id = str(doc_id)
    file = open('pages/' + doc_id + '.txt', 'r')
    s = file.read()
    s = s.lower()
    temp = ''
    for i in range(len(s)):
        if s[i] == '\n':
            temp += ' '
        elif s[i] in valid:
            temp += s[i]
    s = temp.split(' ')
    temp = []
    for x in s:
        if x.find('httpswww') != -1 or x in valid or x == '' or x.isdigit():
            pass
        else:
            try:
                if x[-3:] == 'min':
                    continue
            except:
                pass
            temp.append(x)
    s.sort()
    return temp


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
        temp = sum(x[1] for x in res[i][1])  # term frequency
        temp1 = len(res[i][1])  # document frequency
        file.write(res[i][0] + ' (' + str(temp) + ')')
        file.write('(' + str(temp1) + ') ==> {')
        for p in range(len(res[i][1])):
            if p == 0:
                file.write(str(res[i][1][p][0]) + '=' + str(res[i][1][p][1]))
            else:
                file.write(', ' + str(res[i][1][p][0]) + '=' + str(res[i][1][p][1]))
        file.write('}\n')


def write_to_file_titles(N: int):  # writes titles and the doc id to the file
    titles_dict = {}
    for i in range(1, N):
        file = open('pages/' + str(i) + '.txt', 'r')
        s = file.read().split('\n')[0].lower()
        if not s in titles_dict:
            titles_dict[s] = [i]
        else:  # already present in dict
            titles_dict[s].append(i)

    f = open('titles.txt', 'w')
    for i in sorted(titles_dict.keys()):
        f.write(i + ' {')
        for x in titles_dict[i]:
            f.write(str(x) + ' ')
        f.write('}\n')

    f.close()


def find_in_file(word, file_name):  # finds the given word in the file
    file = open(file_name, 'r')
    lines = file.readlines()
    start = 0
    end = len(lines) - 1
    while start <= end:
        mid = (start + end) // 2
        if lines[mid][:lines[mid].index(' ')] == word:
            return lines[mid]
        elif lines[mid][:lines[mid].index(' ')] < word:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def get_tf_idf_weight(tf, df, N):  # Computes the tf-idf score
    return (1 + math.log(tf)) * math.log(N / df)


def calculate_ranking(docs, line, N):  # Calculates score for the documents based on tf-idf score
    ind2 = line.find(')')
    temp = line[ind2 + 2:]
    ind1 = temp.find('(')
    ind2 = temp.find(')')
    df = int(temp[ind1 + 1:ind2])
    start_ind = line.find('{')
    end_ind = line.find('}')
    i = start_ind + 1

    prev_temp = ''
    temp = ''
    while i < end_ind + 1:
        if line[i].isdigit():
            temp += line[i]
            i += 1
        elif line[i] == '=':
            prev_temp = temp
            i += 1
            temp = ''
        elif line[i] == ',':
            if int(prev_temp) not in docs:
                docs[int(prev_temp)] = get_tf_idf_weight(int(temp), df, N)
            else:
                docs[int(prev_temp)] += get_tf_idf_weight(int(temp), df, N)
            i += 1
            temp = ''

        else:
            i += 1
    if int(prev_temp) not in docs:
        docs[int(prev_temp)] = get_tf_idf_weight(int(temp), df, N)
    else:
        docs[int(prev_temp)] += get_tf_idf_weight(int(temp), df, N)

    return docs


def get_top_results(docs, n):  # Returns top n results
    return heapq.nlargest(n, docs, key=docs.get)


def process_title_list(line: str):
    docs = []
    start = line.find('{')
    end = line.find('}')
    temp = ''
    for i in range(start + 1, end):
        if line[i] == ' ':
            docs.append(int(temp))
            temp = ''
        temp += line[i]
    return docs


def find_ratings(movie_name):  # extracts rating from a file for the given movie name
    temp = find_in_file(movie_name, 'titles.txt')
    if temp != -1:
        print('Movie Name: ' + movie_name)
        print('Ratings: ')
        docs = process_title_list(temp)
        for x in docs:
            f = open('pages/' + str(x) + '.txt', 'r')
            s = f.read().split('\n')
            if s[1].find('imdb') != -1:
                print('IMDB: ', end='')
                for i in range(2, len(s)):
                    if s[i].find('/') != -1 and s[i].find('10') != -1:
                        print(s[i][:3])
            elif s[1].find('metacritic') != -1:
                print('Metacritic: ', end='')
                print(s[4])


if __name__ == "__main__":

    N = 48690  # number of documents in the collection

    ##########################################
    # Uncomment the below code if running for the first time on dataset
    # index_trie = Trie()
    # for i in range(1, N):
    #     add_to_index_trie(i, index_trie)
    #
    # write_trie_to_file(index_trie, 'output.txt')

    # write_to_file_titles(N)

    ######################################

    query = 'Inception'

    # Sample quires: 'Leonardo DiCaprio', 'Avengers'

    docs = {}
    for x in query.split(' '):
        ttemp = find_in_file(x.lower(), 'output.txt')
        if ttemp != -1:
            calculate_ranking(docs, ttemp, N)
    top_results = get_top_results(docs, 10)
    if len(top_results) != 0:
        print('Relevant Documents: ')
        for x in top_results:
            print(x, end=' ')
        print()
    find_ratings(query.lower())
    print('\n')
    for x in top_results:
        f = open('pages/' + str(x) + '.txt', 'r')
        print(f.read().split('\n')[0])
