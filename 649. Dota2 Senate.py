from collections import deque

senate = "RDD"
radiant = deque()
dire = deque()
n = len(senate)

for i in range(len(senate)):
    if senate[i] == "R":
        radiant.append(i)
    elif senate[i] == "D":
        dire.append(i)

while len(radiant) > 0 and len(dire) > 0:
    if radiant[0] < dire[0]:
        dire.popleft()
        radiant.append(radiant[0] + n)
        radiant.popleft()

    else:
        radiant.popleft()
        dire.append(dire[0] + n)
        dire.popleft()

if len(radiant) > 0:
    print ("Radiant")
else:
    print("Dire")