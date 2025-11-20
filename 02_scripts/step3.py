titles = data_array[:, 0]     #제목
rates = data_array[:, 2].astype(float)   #평점
years = data_array[:, 3].astype(int)     #연도

max_rate = rates.max()
print("최고 평점:", max_rate)

mask = (rates == max_rate)
print(mask[:10])

top_titles = titles[mask]
top_rates = rates[mask]

print("⭐️최고 평점 영화 목록:\n")

for t, r in zip(top_titles, top_rates):
    print(f"{t} - 평점: {r:.1f}")