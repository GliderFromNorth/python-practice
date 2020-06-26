product = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
lett_d ={}
for x in product:
    if x not in lett_d:
        lett_d[x] = 0
    lett_d[x] = lett_d[x] +1

max_=([x for x in lett_d.values()])

for k in lett_d:
    if lett_d[k] == min(max_):
        max_value = lett_d[k]
        print(max)