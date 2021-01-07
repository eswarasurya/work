The code returns the correct sentence for a given sentence which has spell errors.

For a given sentence, it breaks the sentence into words.
for each word:
	generating the candidate set.
	if it is not the first word:
		return the word with max(p(wi|wi-1) * p(wi))
	else:
		return the word with max(p(wi))

For generating the candidate set for a given word, we perform the following operations
1) insertion
2) deletion
3) transposition
4) replace

First, we check if the word is present in the vocabulary or not. If present, we will not perform any corrections.
If the word is not present in the vocabulary, then we generate a set of words which are within edit distance one.
We remove the words that are not in the vocabulary. if the set is empty then we go for edit distance two. 
If that set is also empty then we return the same word (we were unable to correct it).

For computing p(w) we are using big.txt file.
we iterate through the file and compute the occurrences of all the words. 
we can get probability of a word by (occurrences of word)/(total number of words).

For getting the probability p(wi|wi-1) we are using the file bigrams.txt which has the probability for all words in the vocabulary.