import requests
import datetime


def get_location_iss():
    """
    Fetch and display the current location of the International Space Station (ISS).
    The function retrieves latitude, longitude, and a timestamp of the current position.
    """
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        position = data["iss_position"]
        timestamp = data["timestamp"]
        date_time = datetime.datetime.fromtimestamp(timestamp)
        print(f"Current ISS Location:")
        print(f"  Latitude: {position['latitude']}")
        print(f"  Longitude: {position['longitude']}")
        print(f"  Date and Time: {date_time}")
    else:
        print("Error retrieving ISS location.")


def get_astronauts():
    """
    Fetch and display the number of astronauts currently in space and their names.
    The function also identifies which astronauts are aboard the ISS.
    """
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        people = data["people"]
        print(f"\nTotal number of astronauts in space: {data['number']}")
        print("Current occupants of the ISS:")
        for person in people:
            if person["craft"] == "ISS":
                print(f"  - {person['name']}")
    else:
        print("Error retrieving astronaut data.")


def main():
    """
    Main program function. Displays information about the ISS location and the astronauts aboard.
    """
    print("=== ISS Information ===\n")
    get_location_iss()
    get_astronauts()


if __name__ == "__main__":
    main()
