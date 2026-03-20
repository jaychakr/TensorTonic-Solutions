import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    n = len(rater1)
    p_o = 0
    for i in range(len(rater1)):
        if rater1[i] == rater2[i]:
            p_o += 1
    p_o /= n
    p_e = 0
    num_labels = len(set(rater1) | set(rater2))
    for k in range(num_labels):
        p_e += rater1.count(k) / n * rater2.count(k) / n
    kappa = (p_o - p_e) / (1 - p_e)
    return kappa
    