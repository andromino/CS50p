def main():
    spacecraft = {
        "name": "Voyeger 1",
        "speed": 40000,
    }
    spacecraft.update({
        "distance": 36000000,
        "time": 90,
        "departure": "2026-07-06",
    })
    
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========= REPORT =========
    Name: {spacecraft["name"]}
    Speed: {spacecraft["speed"]}
    Distance: {spacecraft["distance"]}
    Time: {spacecraft["time"]}
    Departure: {spacecraft.get("departure", "Unknown")}
    """





main()    

