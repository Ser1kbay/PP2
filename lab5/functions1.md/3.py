def solve(numheads, numlegs):
    
    if numheads < 0 or numlegs < 0 or numheads > numlegs:
        return "error"
    num_rabbits = (numlegs - 2 * numheads) / 2
    num_chickens = numheads - num_rabbits
    if num_rabbits.is_integer() and num_chickens.is_integer():
        return int(num_chickens), int(num_rabbits)
    else:
        return "error"
numheads = int(input())
numlegs = int(input())
result = solve(numheads, numlegs)
if result == "error":
    print("-")
else:
    chickens, rabbits = result
    print(f"There are {chickens} chickens and {rabbits} rabbits.")
