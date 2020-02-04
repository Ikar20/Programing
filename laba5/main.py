import math

def read_file(file):
    with open(file, "r") as file:
        width = int(file.readline())
        line = file.readline().split()
        heights = []
        for x in line:
            heights.append(int(x))
    return width, heights

def optimiser(heights):
    heights = sorted(heights, reverse=True)
    new_heights = []
    for x in range(0, math.ceil(len(heights) / 2)):
        new_heights.append(heights[x])
        new_heights.append(1)
    if len(heights) % 2:
        new_heights.pop()
    return new_heights
    
def get_max_cable_width(width, heights):
    result = 0
    previous_length = math.sqrt(abs(heights[0] - 1) ** 2 + width ** 2)
    print(width)
    if heights[-1] == 1:
        a = abs(heights[len(heights) - 2] - 1)
        b = math.sqrt(a ** 2 + width ** 2)
        result = previous_length + 2 * b
    else:
        c = abs(heights[len(heights) - 1] - 1)
        d = math.sqrt(c ** 2 + width ** 2)
        result = previous_length + d
    for x in range(2, len(heights) - 2, 2):
        e = abs(heights[x] - 1)
        result = result + 2 * math.sqrt(e ** 2 + width ** 2)
    return result

def main():
    width, heights = read_file("file4.in")
    new_heights = optimiser(heights)
    result = get_max_cable_width(width, new_heights)
    print("%.2f" % result)

main()
