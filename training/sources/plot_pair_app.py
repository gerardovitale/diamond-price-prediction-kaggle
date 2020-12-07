import plotting_pair as pair

file_name_csv = 'train.csv'
df = pair.open_csv(file_name_csv)

file_name = 'diamond_per_cut'
hue = 'cut'
hue_order = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
markers = ['s', 'p', 'h', '*', 'o']

# file_name = 'diamond_per_color'
# hue = 'color'
# hue_order = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
# markers = ['s', 'p', 'h', '*', 'o', 'X', 'D']

# file_name = 'diamond_per_clarity'
# hue = 'clarity'
# hue_order = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
# markers = ['s', 'p', 'h', '*', 'o', 'X', 'D', '^']

pair.plotting_pair(
    df,
    file_name=file_name,
    hue=hue,
    hue_order=hue_order,
    markers=markers
    )
