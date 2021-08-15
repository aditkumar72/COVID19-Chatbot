import joblib
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def load_tfidf(filename):
    return joblib.load(f'assets/{filename}')

def load_dataset(filename):
    return pd.read_csv(f'dataset/{filename}')

def load_tfidf_matrix(filename):
    return pd.read_csv(f'assets/{filename}').values

def get_cosine_similarity(X, y):
    return cosine_similarity(X, y)

def get_question_tfidf(question):
    if type(question) != list: question = [question]
    tfidf = load_tfidf('tfidf')
    return tfidf.transform(question).toarray()

def get_max_idx(matrix, axis=0):
    return np.argmax(matrix, axis=axis)

def get_answer_util(question, dataset='covid_faq.csv', col='answers'):
    question_tfidf = get_question_tfidf(question)
    tfidf_matrix = load_tfidf_matrix('tfidf_matrix.csv')
    similarity = get_cosine_similarity(tfidf_matrix, question_tfidf)
    idx = get_max_idx(similarity)
    df = load_dataset(dataset)
    ans = df.iloc[idx][col].values.item()
    return ans

def get_answer(question):
    return get_answer_util(question)
