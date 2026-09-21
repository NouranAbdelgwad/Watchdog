stream = ["100 km/h", "N/A", "999 km/h","50", "Error"]

def clean_data(value):
  try:
    clean = value.replace("km/h", "")
    clean = clean.strip()
    return int(clean)
  except:
    return None


def analyze_risk(value):
    if value > 500:
      return "critical 🚨"
    elif value > 120:
      return "Warning ⚠️"
    else:
      return "OK ✅"


results = []

for value in stream:
  speed = clean_data(value)
  if speed is None:
    print(f"Skip bad data: {value}")
    continue
  status = analyze_risk(speed)
  entry = {"speed": speed, "status": status}
  results.append(entry)

print("\n--- MISSION REPORT ---")
for r in results:
  print(f"Speed: {r['speed']} -> {r['status']}")
