import numpy as np

titles = data_array[:, 0]
genres = data_array[:, 1]
rates = data_array[:, 2].astype(float)

#set 컴프리헨션으로 중복 제거 후, sorted로 정렬
unique_genres = sorted({g.strip() 
                        for s in genres
                        for g in s.split(",")})
print("장르 개수:", len(unique_genres))
print("장르 목록 예시:", unique_genres[:10])

#"각 장르에 대해" 평균 평점 계산하기

genre_stats = []

for g in unique_genres:
  #1) 이 장르 g가 포함된 영화만 고르는 마스크
  mask = np.array([g in s for s in genres])

  #2) 그 영화들의 평점만 모으기
  g_rates = rates[mask]

  #혹시라도 0개면 건너뛰기
  if g_rates.size == 0:
    continue

  #3)평균과 개수 계산  
  mean_g = g_rates.mean()
  n_g = g_rates.size

  #4) 리스트에 저장
  genre_stats.append((g, mean_g, n_g))

  #평균 평점 기준 내림차순 정렬
  genre_stats_sorted = sorted(genre_stats, key=lambda x: x[1], reverse=True)

  #출력
  print("장르별 평균 평점 (내림차순):\n")
  for g, mean_g, n_g in genre_stats_sorted:
    print(f"{g}: {mean_g:.3f} (영화 수: {n_g})")

#각 장르별로 평균 평점 계산하기

#"그 장르가 포함된 영화만" 고르는 마스크 만들기
mask = np.array([g in s for s in genres])

genre_stats = []

for genre_name in unique_genres:
    mask = np.array([genre_name in cell for cell in genres])
    g_rates = rates[mask]

    if g_rates.size == 0:
        continue

    mean_g = g_rates.mean()
    n_g = g_rates.size

    genre_stats.append((genre_name, mean_g, n_g))

#출력

print("장르별 평균 평점 (내림차순):\n")

for g, mean_g, count_g in genre_stats_sorted:
  print(f"{g}: {mean_g:.1f}   (영화 수: {count_g})")
