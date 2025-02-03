import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
nltk.download('treebank')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""

tokens = nltk.word_tokenize(sentence)

print(tokens)

tagged = nltk.pos_tag(tokens)

# print(tagged[0:6])
print(tagged)

entities = nltk.chunk.ne_chunk(tagged)

print(entities)


from nltk.corpus import treebank

t = treebank.parsed_sents('wsj_0001.mrg')[0]

t.draw()