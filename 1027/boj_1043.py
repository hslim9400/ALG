
N, M = map(int, input().split())
detectors = list(map(int, input().split()))
detectors = set(detectors[1:])

ans = 0
parties = []
for _ in range(M):
    participants = list(map(int, input().split()))
    participants = set(participants[1:])
    parties.append(participants)

while True:
    temp = len(detectors)
    for party in parties:
        if party & detectors:
            detectors = detectors.union(party)
    if temp == len(detectors):
        break

for party in parties:
    if not party & detectors:
        ans += 1
print(ans)
