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
    sentence_tfidf_sums_array = np.asarray(sentence_tfidf_sums_matrix).squeeze()

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
    text = """Required Minimum ROUGE-L f-score: 0.6
        Required Maximum Summary Character Count: 3003
        Those Who Are Resilient Stay In The Game Longer
        "On the mountains of truth, you can never climb in vain: either you will reach a point higher up today, or you will be training your powers so that you will be able to climb higher tomorrow." - Friedrich Nietzsche
        Challenges and setbacks are not meant to defeat you, but to promote you. However, I realize that after many years of defeats, it can crush your spirit and it is easier to give up than risk further setbacks and disappointments. Have you experienced this before? To be honest, I don't have the answers. I can't tell you what the right course of action is; only you will know. However, it's important not to be discouraged by failure when pursuing a goal or a dream, since failure itself means different things to different people. To a person with a Fixed Mindset, failure is a blow to their self-esteem, yet to a person with a Growth Mindset, it's an opportunity to improve and find new ways to overcome their obstacles. The same failure, but different reactions. Who is right and who is wrong? Neither, as each person has a different mindset that decides their outcome. Those who are resilient stay in the game longer and draw on their inner resources to succeed.
        I've coached mummy and mom clients who gave up after many years of toiling away at their respective goals or dreams. It was at that point that their biggest breakthrough came. Perhaps all those years of perseverance have finally paid off. It was the 19th century minister Henry Ward Beecher who once said: "One's best success comes after their greatest disappointments." No one knows what the future holds, so your only guide is whether you can endure repeated defeats and disappointments and still pursue your dream. Consider the advice from the American academic and psychologist Angela Duckworth who writes in Grit: "The Power of Passion and Perseverance: Many of us, it seems, quit what we start far too early and far too often." Even more than the effort a gritty person puts in on a single day, what matters is that they wake up the next day, and the next, ready to get on that treadmill and keep going.
        I know one thing for certain: don't settle for less than what you're capable of, but strive for something bigger. Some of you reading this might identify with this message because it resonates with you on a deeper level. For others, at the end of their tether, the message might be nothing more than a trivial pep talk. What I wish to convey, irrespective of where you are in your journey, is: NEVER settle for less. If you settle for less, you will receive less than you deserve and you will convince yourself you are justified in receiving it.
        "Two people on a precipice over Yosemite Valley" by Nathan Shipps on Unsplash
        Develop A Powerful Vision Of What You Want
        "Your problem is to bridge the gap that exists between where you are now and the goal you intend to reach." - Earl Nightingale
        I recall a passage my father often used when I was growing up in the 1990s: "Don't tell me your problems unless you've spent weeks trying to solve them yourself." That advice has echoed in my mind for decades and became my motivator. Don't leave it to other people or outside circumstances to motivate you because you will be let down every time. It must come from within you. Gnaw away at your problems until you solve them or find a solution. Problems are not stop signs; they are advising you that more work is required to overcome them. Most of the time, problems help you gain a skill or develop the resources to succeed later. So embrace your challenges and develop the grit to push past them instead of retreating in resignation. Where are you settling in your life right now? Could you be playing for bigger stakes than you are? Are you willing to take risks even if it means experiencing repeated failures and setbacks? You should ask yourself these questions to decide whether you're willing to put yourself on the line or settle for less. And that's fine if you're content to receive less, as long as you're not regretful later.
        If you have not achieved the success you deserve and are considering giving up, will you regret it in a few years or decades from now? Only you can answer that, but you should carve out time to discover your motivation for pursuing your goals. It's a fact that if you don't know what you want, you'll get what life hands you, and it may not be in your best interest, affirms author Larry Weidel: "Winners know that if you don't figure out what you want, you'll get whatever life hands you." The key is to develop a powerful vision of what you want and hold that image in your mind. Nurture it daily and give it life by taking purposeful action towards it.
        Vision + desire + dedication + patience + daily action leads to astonishing success. Are you willing to commit to this way of life or jump ship at the first sign of failure? I'm amused when I read questions written by millennials on Quora who ask how they can become rich and famous or the next Elon Musk. Success is a fickle and long game with highs and lows. Similarly, there are no assurances, even if you're an overnight sensation, that you'll be able to sustain it for long, particularly if you don't have the mental and emotional means to endure it. This means you must rely on the one true constant in your favor: your personal development. The more you grow, the more you gain in terms of financial resources, status, success - simple. If you leave it to outside conditions to dictate your circumstances, you are rolling the dice on your future.
        So become intentional about what you want out of life. Commit to it. Nurture your dreams. Focus on your development and if you want to give up, know what is involved before you take the plunge. Because I assure you, someone out there right now is working harder than you, reading more books, sleeping less and sacrificing all they have to realize their dreams, and it may compete with yours. Don't leave your dreams to chance.
        Your ROUGE-L f-score: 0.7951807180851923
        Your summary character count: 2809
        Your generated summary: Those Who Are Resilient Stay In The Game Longer
        "On the mountains of truth, you can never climb in vain: either you will reach a point higher up today, or you will be training your powers so that you will be able to climb higher tomorrow."However, I realize that after many years of defeats, it can crush your spirit and it is easier to give up than risk further setbacks and disappointments.However, it's important not to be discouraged by failure when pursuing a goal or a dream, since failure itself means different things to different people.To a person with a Fixed Mindset, failure is a blow to their self-esteem, yet to a person with a Growth Mindset, it's an opportunity to improve and find new ways to overcome their obstacles.I've coached mummy and mom clients who gave up after many years of toiling away at their respective goals or dreams.It was the 19th century minister Henry Ward Beecher who once said: "One's best success comes after their greatest disappointments."No one knows what the future holds, so your only guide is whether you can endure repeated defeats and disappointments and still pursue your dream.Consider the advice from the American academic and psychologist Angela Duckworth who writes in Grit: "The Power of Passion and Perseverance: Many of us, it seems, quit what we start far too early and far too often."Even more than the effort a gritty person puts in on a single day, what matters is that they wake up the next day, and the next, ready to get on that treadmill and keep going.I know one thing for certain: don't settle for less than what you're capable of, but strive for something bigger."Two people on a precipice over Yosemite Valley" by Nathan Shipps on Unsplash
        Develop A Powerful Vision Of What You Want
        "Your problem is to bridge the gap that exists between where you are now and the goal you intend to reach."- Earl Nightingale
        I recall a passage my father often used when I was growing up in the 1990s: "Don't tell me your problems unless you've spent weeks trying to solve them yourself."It's a fact that if you don't know what you want, you'll get what life hands you, and it may not be in your best interest, affirms author Larry Weidel: "Winners know that if you don't figure out what you want, you'll get whatever life hands you."I'm amused when I read questions written by millennials on Quora who ask how they can become rich and famous or the next Elon Musk.Similarly, there are no assurances, even if you're an overnight sensation, that you'll be able to sustain it for long, particularly if you don't have the mental and emotional means to endure it.Because I assure you, someone out there right now is working harder than you, reading more books, sleeping less and sacrificing all they have to realize their dreams, and it may compete with yours.
        """

    # Generate summary
    sol = tldr(text)

    # Print the summary
    print(sol)