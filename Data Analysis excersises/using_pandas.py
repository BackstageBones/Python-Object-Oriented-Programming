import pandas

df = pandas.read_json("../resources/supermarkets.json")
df = df.set_index("Address")

