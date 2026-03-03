def priority_replay_sample(priorities, alpha, beta):
    """
    Compute sampling probabilities and importance sampling weights for PER.
    """
    # Write code here
    powered = [p ** alpha for p in priorities]
    total = sum(powered)
    probs = [x / total for x in powered]
    n = len(priorities)
    raw_weights = [(n * pr) ** (-beta) for pr in probs] 
    normalized_weights = [w / max(raw_weights) for w in raw_weights]
    return [probs, normalized_weights]
    