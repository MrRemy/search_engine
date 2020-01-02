from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def tf_idf(search_keys, documents):
    tfidf_vectorizer = TfidfVectorizer(use_idf=True)

    tfidf_weights_matrix = tfidf_vectorizer.fit_transform(documents)
    search_query_weights = tfidf_vectorizer.transform([search_keys])

    return search_query_weights, tfidf_weights_matrix


def cos_similarity(search_query_weights, tfidf_weights_matrix):
    cosine_distance = cosine_similarity(search_query_weights, tfidf_weights_matrix)
    similarity_list = cosine_distance[0]

    return similarity_list


def find_best_matching(search_keys, documents):
    search_query_weights, tfidf_weights_matrix = tf_idf(search_keys, documents)
    sim_data = cos_similarity(search_query_weights, tfidf_weights_matrix)

    index = 0
    for i in range(1, len(sim_data)):
        if sim_data[i] > sim_data[index]:
            index = i
    return index, sim_data[index]

