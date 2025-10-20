import pandas as pd, numpy as np, random

names = ["Alice", "Bob", "Carlos", "Dani", "Eve"]
cities = ["Lisbon", "Porto", "Faro", "Coimbra", None]
ages = [random.choice([25, 30, 35, None]) for _ in range(20)]
incomes = [random.choice(["35000", "42000", "not_available", None]) for _ in range(20)]

df = pd.DataFrame({
    "name": [random.choice(names) for _ in range(20)],
    " age ": ages,
    " city ": cities * 4,
    " income": incomes
})
df.to_csv("messy_generated.csv", index=False)
