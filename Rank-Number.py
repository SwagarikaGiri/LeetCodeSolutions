def rank_people(Ranked, Unranked):
    ranks = []
    for ele in Unranked:
        unique_n =  list(set(Ranked))
        count = sum(1 for x in unique_n if x > ele)
        ranks.append(count+1)
        Ranked.append(ele)
    return ranks



# Read input from STDIN
N, P = map(int, input().split())
ranked_weights = list(map(int, input().split()))
weights = list(map(int, input().split()))




p_ranks = rank_people(ranked_weights, weights)

for p_rank in p_ranks:
    print(p_rank)


