import pandas as pd
import time
import re
import gas
import data
import router
import metro

def find_id(name):
    for i in range(len(data.STATIONS)):
        if data.STATIONS[i+1]["name"] == name:
            return i+1

par = pd.read_csv("parameters.csv")

ans = ""
mn = 1e9
for st in range(len(data.STATIONS)):
    start = metro.Station(st+1)
    all_d = []
    r = router.Router()
    dist = r.make_route(start)
    #print(*dist)
    for cur in par["Station"]:
        all_d.append(dist[find_id(cur)])
    if max(all_d) - min(all_d) <= mn:
        ans = data.STATIONS[st+1]["name"]
        mn = max(all_d) - min(all_d)
        #print(*all_d)
print(ans)
