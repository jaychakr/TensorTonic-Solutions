def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = recommended[:k]
    top_k = set(top_k)
    hits = len(top_k.intersection(relevant))
    precision = hits / k
    recall = hits / len(relevant)
    return [precision, recall]
    