def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    weighted_ratings = []
    for avg_rating, num_votes in items:
        weighted_rating = (num_votes / (num_votes + min_votes)) * avg_rating + (min_votes / (num_votes + min_votes)) * global_mean;
        weighted_ratings.append(weighted_rating);
    return weighted_ratings
        