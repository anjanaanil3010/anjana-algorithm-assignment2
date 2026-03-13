airports = ["A", "B", "C", "D", "E"]
routes = [
("A","B",4),
("A","C",3),
("B","C",1),
("B","D",2),
("C","D",4),
("C","E",5),
("D","E",1)
]

print("Airline Flight Scheduling for Minimum Fuel Cost")

print("\nAirports:")
for a in airports:
    print(a)

print("\nRoutes with Fuel Cost:")
for r in routes:
    print(r[0],"-",r[1],":",r[2])



routes.sort(key=lambda x: x[2])

parent = {}
for a in airports:
    parent[a] = a

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(x,y):
    parent[find(x)] = find(y)

selected = []
total_cost = 0

for u,v,c in routes:
    if find(u) != find(v):
        selected.append((u,v,c))
        total_cost += c
        union(u,v)

print("\nSelected Routes (Optimal Schedule):")
for r in selected:
    print(r[0],"-",r[1],":",r[2])

print("\nTotal Minimum Fuel Cost:", total_cost)
print("\nTime Complexity: O(E log E)")



file = open("flight_schedule_output.txt","w")

file.write("Airline Flight Scheduling for Minimum Fuel Cost\n\n")

file.write("Airports:\n")
for a in airports:
    file.write(a+"\n")

file.write("\nRoutes with Fuel Cost:\n")
for r in routes:
    file.write(f"{r[0]} - {r[1]} : {r[2]}\n")

file.write("\nSelected Routes (Optimal Schedule):\n")
for r in selected:
    file.write(f"{r[0]} - {r[1]} : {r[2]}\n")

file.write("\nTotal Minimum Fuel Cost: "+str(total_cost))
file.write("\nTime Complexity: O(E log E)")

file.close()
