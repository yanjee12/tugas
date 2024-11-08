import pandas as pd
data = {
    'A': [3, 2, 40],
    'B': [1, 2, 3]
}
df = pd.DataFrame(data)


df['Penjumlahan'] = df['A'] + df['B']
df['Pengurangan'] = df['A'] - df['B']
df['Perkalian'] = df['A'] * df['B']
df['Pembagian'] = df['A'] / df['B']

print("Hasil aritmatika pada DataFrame:\n", df)
