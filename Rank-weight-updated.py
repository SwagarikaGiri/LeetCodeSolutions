def rank_people(N, P, ranked_weights, weights):
    ranks = {}

    # Assigning ranks to people in array N
    current_rank = 1
    prev_weight = None

    for weight in ranked_weights:
        if weight != prev_weight:
            rank = current_rank
        ranks[weight] = rank
        current_rank += 1
        prev_weight = weight

    # Assigning ranks to people in array P
    p_ranks = []
    for weight in weights:
        if weight in ranks:
            p_rank = ranks[weight]
        else:
            ranked_weights.append(weight)
            ranked_weights.sort(reverse=True)

            current_rank = 1
            prev_weight = None
            for w in ranked_weights:
                if w != prev_weight:
                    rank = current_rank
                ranks[w] = rank
                current_rank += 1
                prev_weight = w

            p_rank = ranks[weight]

        p_ranks.append(p_rank)

    return p_ranks

# Example usage:
N = 5
P = 3
ranked_weights = [120, 100, 100, 90, 60]
weights = [40, 40, 80]

p_ranks = rank_people(N, P, ranked_weights, weights)

for p_rank in p_ranks:
    print(p_rank)
