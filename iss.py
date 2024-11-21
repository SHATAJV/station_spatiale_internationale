import requests
import datetime

def get_location_iss():
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

        
def main():
    print("=== ISS Information ===\n")
    get_location_iss()


if __name__ == "__main__":
    main()
