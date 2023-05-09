import pandas

data = pandas.read_csv("cpsc_data.csv")
data["Primary Fur Color"]
squirel_colors = set(data["Primary Fur Color"].to_list())
squirel_colors_count = {}
squirel_count = []
for color in list(squirel_colors)[1::]:
    print(color)
    squirel_count.append(len(data[data["Primary Fur Color"] == color]))
squirel_colors_count["Fur Color"] = list(squirel_colors)[1::]
squirel_colors_count["Count"] = squirel_count
print(squirel_colors_count)
df = pandas.DataFrame(squirel_colors_count)
df.to_csv("squirel_fur_color_count.csv")
