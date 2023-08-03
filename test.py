from urllib.request import urlopen
import json

def fetch_weather_data():
    url = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22'
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

def get_weather_data(option, data, date):
    filtered_data = [entry for entry in data["list"] if date in entry["dt_txt"]]
    if not filtered_data:
        return None

    if option == 1:
        return filtered_data[0]["main"]["temp"]
    elif option == 2:
        return filtered_data[0]["wind"]["speed"]
    elif option == 3:
        return filtered_data[0]["main"]["pressure"]
    else:
        return None

def main():
    data = fetch_weather_data()

    while True:
        print("Choose an option:")
        print("1. Get temperature")
        print("2. Get wind speed")
        print("3. Get pressure")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                print("Exiting...")
                break
            elif choice >= 1 and choice <= 3:
                date_input = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
                result = get_weather_data(choice, data, date_input)
                if result is not None:
                    if choice == 1:
                        print(f"Temperature on {date_input}: {result} K")
                    elif choice == 2:
                        print(f"Wind Speed on {date_input}: {result} m/s")
                    elif choice == 3:
                        print(f"Pressure on {date_input}: {result} hPa")
                else:
                    print("Invalid date or no data found for the given date.")
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid option (0, 1, 2, or 3).")

if __name__ == "__main__":
    main()
