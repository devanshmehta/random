#knapsack algorithm using psuedo polynomial time solution
__author__ = 'devansh.mht@gmail.com'

w = [5,2,6,7,2,4]
v = [1,2,8,5,4,3]

def knapsack(w, v, max_weight, start_item, memo):
  for i in xrange(start_item, len(w)):
    item_weight = w[i]
    item_value = v[i]
    if item_weight > max_weight:
      memo[(i, max_weight)] = 0
    else:
      if (i - 1, max_weight) not in memo:
        value = knapsack(w, v, max_weight, i - 1, memo)
        memo[(i - 1, max_weight)] = value
      if (i - 1, max_weight - item) not in memo:
        value = knapsack(w, v, max_weight - item_weight, i - 1, memo)
        memo[(i - 1, max_weight - item_weight)] = value
      memo[i, max_weight] = max(memo[(i - 1, max_weight)], 
                                memo[(i - 1, max_weight - item_weight)] + item_value)
  return memo[(len(w) - 1, max_weight)]
  
print knapsack(w, v, 10, 0, {})
