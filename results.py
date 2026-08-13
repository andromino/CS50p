results = ["Mario","Luigi"]

results.append("Peach")
results.append(["Bowser","Wario"])

print(results)

results.remove(["Bowser","Wario"])
results.extend(["Bowser","Wario"])

print(results)

results.insert(0, "Toad")

print(results)

results.reverse()

print(results)