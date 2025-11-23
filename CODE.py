print("\n Weekly Carbon Emission Analyzer (Pure Python)\n")

POWER_FACTOR = 0.82    
TRAVEL_FACTOR = 0.15   
LPG_FACTOR = 2.8       

def get_positive_int(prompt: str) -> int:
    """Ensures input is a positive integer."""
    while True:
        try:
            v = int(input(prompt).strip())
            if v <= 0:
                raise ValueError
            return v
        except ValueError:
            print(" Please enter a valid positive number.")


def get_nonnegative_float(prompt: str) -> float:
    """Ensures input is a non-negative number."""
    while True:
        try:
            v = float(input(prompt).strip())
            if v < 0:
                raise ValueError
            return v
        except ValueError:
            print(" Please enter a valid number (0 or above).")


days = get_positive_int(" How many days do you want to track? ")

electricity = []
travel = []
cooking = []

print("\n Enter your daily usage (units / km / kg):\n")

for i in range(days):
    print(f"  Day {i+1}:")
    electricity.append(get_nonnegative_float("   • Electricity used (units): "))
    travel.append(get_nonnegative_float("   • Distance travelled (km): "))
    cooking.append(get_nonnegative_float("   • LPG used (kg): "))
    print()

eco_power = [e * POWER_FACTOR for e in electricity]
eco_travel = [t * TRAVEL_FACTOR for t in travel]
eco_lpg = [c * LPG_FACTOR for c in cooking]

daily_total = [eco_power[i] + eco_travel[i] + eco_lpg[i] for i in range(days)]

overall = sum(daily_total)
avg_daily = overall / days if days > 0 else 0.0

if daily_total:
    max_emission = max(daily_total)
    min_emission = min(daily_total)
    max_day = daily_total.index(max_emission) + 1
    min_day = daily_total.index(min_emission) + 1
else:
    max_day = None
    min_day = None

print("\n================  CARBON EMISSION SUMMARY ================\n")

for i in range(days):
    print(f"Day {i+1}: {daily_total[i]:.2f} kg CO₂")
    print(f"   - From Electricity: {eco_power[i]:.2f} kg")
    print(f"   - From Travel     : {eco_travel[i]:.2f} kg")
    print(f"   - From LPG        : {eco_lpg[i]:.2f} kg\n")

print("-------------------  Total Stats ------------------------")
print(f" Total Emission    : {overall:.2f} kg CO₂")
print(f" Average per Day   : {avg_daily:.2f} kg CO₂")

if max_day is not None:
    print(f" Highest Emission  : Day {max_day}  ({max_emission:.2f} kg CO₂)")
    print(f" Lowest Emission   : Day {min_day}  ({min_emission:.2f} kg CO₂)")

total_power = sum(eco_power)
total_travel = sum(eco_travel)
total_lpg = sum(eco_lpg)

print("\n---------------- Category-wise Breakdown ----------------")
power_perc = (total_power / overall * 100) if overall else 0
travel_perc = (total_travel / overall * 100) if overall else 0
lpg_perc = (total_lpg / overall * 100) if overall else 0

print(f" Electricity : {total_power:.2f} kg CO₂ ({power_perc:.1f}%)")
print(f" Travel      : {total_travel:.2f} kg CO₂ ({travel_perc:.1f}%)")
print(f" LPG Usage   : {total_lpg:.2f} kg CO₂ ({lpg_perc:.1f}%)")

print("\n--------------------  Suggestions ----------------------")
if avg_daily < 5:
    print(" You're maintaining a very low carbon footprint. Keep it up! ")
elif avg_daily < 12:
    print(" You're doing okay! You can still try reducing fuel or electricity a little.")
else:
    print(" Your carbon footprint is high. Try using public transport, cutting down LPG use,")
    print("  or switching to more energy-efficient appliances.")

print("\n Thank you for taking a step toward a greener planet!\n")
