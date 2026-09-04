import sys

def main():
    # Tuples are immutable sequences of objects
    coords = (42.35, -71.05)
    print(f"Latitude: {coords[0]:.2f}, Longitude: {coords[1]:.2f}")

    # Tuple unpacking
    latitude, longitude = coords
    print(f"Latitude: {latitude:.2f}, Longitude: {longitude:.2f}")

    coords_list = [42.35, -71.05]

    # They have greater efficiency than lists for accessing data
    print(f"Storage size of coords: {sys.getsizeof(coords)} bytes")
    print(f"Storage size of coords_list: {sys.getsizeof(coords_list)} bytes")
    
main()