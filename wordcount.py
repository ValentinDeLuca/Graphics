import matplotlib.pyplot as plt
"""VARIABLES"""

""" - Errors"""
OSERROR = "OSError Opening File: "

""" - Graph Tuning"""

"""     - Bars Thickness"""
WIDTH = 0.9

"""     - When the graph limit goes from one number to the same, expand limits in both ways (y-axis) by this much"""
OFFSET = 0.5

"""     - Out of the difference between the higher and lower bar, show this percentage as white above the highest bar 
          and show this much percentage of the lowest bar"""
LIMIT_PERCENTAGE = 5

""" - Messages"""
X_AXIS_LABEL = "Characters Involved"
Y_AXIS_LABEL = 'Number of appearances'

""" - Utilities"""
COLORS_USED = ['r', '#ffa500', '#66bb00', 'g', 'b', '#4b0082', 'm']

"""FUNCTIONS

     - Opens the password file"""
def open_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except OSError as problem:
        print(f"{OSERROR}{problem}")
        exit(1)


"""  - Returns a dictionary with the number of appearances (value) for every character (key) in the password"""
def count_characters(text):
    aux = text
    count = {}
    words = set(aux)
    for word in words:
        count[word] = text.count(word)
    return count


"""  - Plots a bar graph from a dictionary (data_base) and the total number of characters (n) in the password file"""
def make_graph(data_base, n):
    left, height, tick_label = [], [], []
    top = list(data_base.values())[0]
    lower = list(data_base.values())[-1]
    offset = 0
    if top == lower:
        offset = OFFSET
    limit = (top-lower)*LIMIT_PERCENTAGE/100
    for i, key in enumerate(data_base):
        left.append(i)
        height.append(data_base[key])
        tick_label.append(key)

    plt.bar(left, height, tick_label=tick_label, width=WIDTH, color=COLORS_USED)
    plt.xlim([0-WIDTH, len(data_base)])
    plt.ylim([lower-limit-offset, top+limit+offset])
    plt.xlabel(X_AXIS_LABEL)
    plt.ylabel(Y_AXIS_LABEL)
    plt.title(f'Password Graph - {n} characters')
    plt.show()


"""  - Analyzes the password and plots a bar graph"""
def main(filename, n):
    text = open_file(filename)
    dict_characters = dict(sorted(count_characters(text).items(), key=lambda x: x[1], reverse=True))
    make_graph(dict_characters, n)


"""--------------------------------------------END OF THE CODE-------------------------------------------------------"""

"""OBSOLETE FUNCTIONS"""
"""def make_graph(data_base, n): # Receives the number for each character:
    top = list(data_base.values())[0]
    lower = list(data_base.values())[-1]
    asterisc = "■"
    for character in data_base:
        print(f"{character}:{asterisc*(1+((data_base[character] - lower) * 100 // top))} {round((100 * data_base[character]) / n, 2)}%")
"""
