def tokenization(corpus,plagiarized_corpus):
#      word_tokens = word_tokenize(corpus)
#      plagiarized_text_tokens = word_tokenize(plagiarized_corpus)
#      token_list = [word_tokens, plagiarized_text_tokens ]
#      return token_list


# def remove_punctuation(corpus, plagiarized_corpus):
#      corpus = corpus.translate(corpus.maketrans('' , '', string.punctuation))
#      plagiarized_corpus = plagiarized_corpus.translate(plagiarized_corpus.maketrans('' , '', string.punctuation))


# def Pre_process(corpus, plagiarized_corpus):
#     filtered_sentence = []
#     plagiarized_filtered_sentence = []
#     token_list = tokenization(corpus, plagiarized_corpus)
#     for word in token_list[0]:
#         if word.lower() not in  stopwords.words('english'):
#             filtered_sentence.append(word)

#     for word in token_list[1]:
#         if word.lower() not in stopwords.words('english'):
#           plagiarized_filtered_sentence.append(word) 

#     stopword_removed_list = [filtered_sentence, plagiarized_filtered_sentence]
#     return stopword_removed_list
