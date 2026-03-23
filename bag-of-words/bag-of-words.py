import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    indices = {}
    for i in range(len(vocab)):
        indices[vocab[i]] = i
    count_vector = np.zeros(len(vocab), dtype=int)
    for token in tokens:
        if token in indices:
            count_vector[indices[token]] += 1
    return count_vector