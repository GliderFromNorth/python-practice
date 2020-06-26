placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d ={}
for x in placement:
    if x not in d:
        d[x] = 0
    d[x] = d[x] +1
min_ = ([x for x in d.values()])

for k in d:
    if (d[k]) == min(min_):
        min_value = k 
        print(min_value, d[k] )

