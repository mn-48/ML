# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np
# from nltk import sent_tokenize
# from nltk.corpus import stopwords


# def tldr(text_to_summarize):
#     print(text_to_summarize)
#     sentence_tokens = np.array(sent_tokenize(text_to_summarize))

#     # print("sentence_tokens: ", sentence_tokens)

#     stop_word_set = set(stopwords.words("english"))

#     # print("stop_word_set: ", stop_word_set)

#     tf_idf_vectorizer = TfidfVectorizer(stop_words=stop_word_set)
#     tf_idf = tf_idf_vectorizer.fit_transform(sentence_tokens)
#     sentence_tfidf_sums_matrix = tf_idf.sum(axis=1)
#     sentence_tfidf_sums_array = np.asarray(
#         sentence_tfidf_sums_matrix).squeeze()
#     selected_sentence_indicies = np.where(sentence_tfidf_sums_array > 3)
#     summary_sentences = sentence_tokens[selected_sentence_indicies]
#     summary = ''.join(summary_sentences)

#     # print(summary)

#     return summary


from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk import sent_tokenize
from nltk.corpus import stopwords


def tldr(text_to_summarize):
    # Tokenize the text into sentences
    sentence_tokens = np.array(sent_tokenize(text_to_summarize))

    # Get English stopwords and convert to a list
    stop_word_list = list(stopwords.words("english")) 

    # Create TF-IDF Vectorizer with custom stopwords
    tf_idf_vectorizer = TfidfVectorizer(stop_words=stop_word_list)
    tf_idf = tf_idf_vectorizer.fit_transform(sentence_tokens)

    # Sum TF-IDF scores for each sentence
    sentence_tfidf_sums_matrix = tf_idf.sum(axis=1)
    sentence_tfidf_sums_array = np.asarray(
        sentence_tfidf_sums_matrix).squeeze()

    # Select sentences with TF-IDF sums greater than a threshold (e.g., 3)
    selected_sentence_indicies = np.where(sentence_tfidf_sums_array > 3)
    summary_sentences = sentence_tokens[selected_sentence_indicies]

    # Join the selected sentences into a summary
    summary = ' '.join(summary_sentences)

    return summary


if __name__ == "__main__":
    import nltk

    # Download required NLTK data
    nltk.download('punkt')  # For sentence tokenization
    nltk.download('stopwords')  # For stopwords

    # Input text
    # text = """Bangladesh is my homeland. The name of our country is Bangladesh. It became independent in 1971. Dhaka is the capital of Bangladesh. It is a small country. It has a land area of 147570 square kum. There are 17 crore people t in the country. Bangladesh is mainly an agricultural country. Rice, jute, sugar cane and tea are the main crops of Bangladesh. Many kinds of fruits also grown here. Jack fruit, mangoes, bananas, pine apples, guavas and water melons are the most common fruit in Bangladesh. There are also many rivers in Bangladesh. The Padma, the Meghna, the Jamuna, the Karnaphuly are the main rivers in Bangladesh. There are many varities of fishes in these rivers. Bangladesh has many interesting places. The Sundarbans, Rangamati and Cox's Bazar are very attractive. Cox's Bazar is the longest sea beach in the world. It is about 120 k.m long. The Royal Bengal Tiger lives in the Sundarbans. Many people visit these interesting places every year. Bangladesh is a peaceful country. People from different communities live here in peace. I love my country very much.
    # """

    text = """
    My country, Bangladesh, is a land of vibrant culture, rich history, and immense natural beauty. Nestled in South Asia, it is known for its lush green landscapes, meandering rivers, and bustling cities. The country is home to a diverse population with a strong sense of unity and resilience. From the historical landmarks like the ancient city of Mahasthangarh to the modern marvels of Dhaka, Bangladesh presents a blend of the old and the new. The people of Bangladesh are renowned for their hospitality and warmth, embodying a spirit of generosity and friendliness. Our festivals, such as Pohela Boishakh and Durga Puja, are celebrated with great enthusiasm, showcasing our cultural richness. Despite facing challenges, including natural disasters and economic hurdles, Bangladesh continues to strive towards progress and development. The nation's dedication to education, innovation, and social welfare reflects its commitment to building a better future for its people. My country, with its unique blend of tradition and modernity, stands as a testament to resilience, hope, and progress.
    """

    # Generate summary
    sol = tldr(text)

    # Print the summary
    print(sol)
