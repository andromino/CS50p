import random


def main():
    moisture = random.randint(0, 100)
    while moisture >20:
        print(f"Soil moisture: {moisture}%")
        moisture = random.randint(0, 100)    
    print(f"Water the plant! Soil moisture: {moisture}%")


main()