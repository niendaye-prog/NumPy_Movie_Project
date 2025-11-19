#연도와 평점

import numpy as np

years = data_array[:, 3].astype(int)
rates = data_array[:, 2].astype(float)

#등장하는 연도들(오름차순으로 정렬된 상태)
unique_years = np.unique(years)

year_stats = []

for y in unique_years:
  mask = (years == y)
  year_rates = rates[mask]

  mean_y = year_rates.mean()
  count_y = year_rates.size

  year_stats.append((y, mean_y, count_y))

#정렬, 출력

year_stats_sorted = sorted(year_stats, key=lambda x: x[0])

print("연도별 평균 평점(연도 오름차순):\n")
for y, mean_y, count_y in year_stats_sorted:
  print(f"{y} - {mean_y:.1f}")
