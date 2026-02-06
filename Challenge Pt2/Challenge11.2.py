# Analyze mixed sensor data
sensor_data = [
    ("temp", 34.9), 
    ("pressure", 1020), 
    ("temp", 33.7), 
    ("humidity", 55.9),
    ("pressure", 1043)
]

readings = {"temp": [], "pressure": [], "humidity": []}
for data_type, value in sensor_data:
    if data_type in readings:
        readings[data_type].append(value)

results = {}
for data_type, values in readings.items():
    if values:
        results[data_type] = {
            "min": min(values),
            "max": max(values),
            "avg": sum(values)/len(values)
        }

print("Sensor Summary:")
for data_type, stats in results.items():
    print(f"{data_type.capitalize()}:")
    print(f"  Min: {stats['min']}, Max: {stats['max']}, Avg: {stats['avg']:.1f}")