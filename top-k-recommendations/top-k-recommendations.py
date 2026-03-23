def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here
    not_seen = [(scores[i], i) for i in range(len(scores)) if i not in rated_indices]
    not_seen.sort(key=lambda x: -x[0])
    indices = [pair[1] for pair in not_seen[:k]]
    return indices