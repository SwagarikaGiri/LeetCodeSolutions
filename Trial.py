def rank_people(Ranked, Unranked):
    rank_dict = {rank: i+1 for i, rank in enumerate(Ranked)}
    ranks = [rank_dict[ele] for ele in Unranked]
    
    return ranks





# Read input from STDIN
# Example usage:
N = 5
P = 3
ranked_weights = [120, 100, 100, 90, 60]
weights = [40, 40, 80]



p_ranks = rank_people(ranked_weights, weights)

for p_rank in p_ranks:
    print(p_rank)