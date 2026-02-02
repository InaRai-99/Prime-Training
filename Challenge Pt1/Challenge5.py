temps = [22.5, 19.0, 25.5, 21.0]
summary = {"min": min(temps), "max": max(temps), "avg": sum(temps) / len(temps)}
if summary["avg"] > 20:
    print("Average temperature is comfortable.")
print("Summary:", summary)