def solve(num_heads, num_legs):
    for chickens in range(num_heads + 1):
        rabbits = num_heads - chickens
        if chickens * 2 + rabbits * 4 == num_legs:
            return chickens, rabbits
    return None, None

heads = 35
legs = 94
chickens, rabbits = solve(heads, legs)
print(f"Курицы: {chickens}, Кролики: {rabbits}")