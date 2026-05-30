import requests

def get_weather(city):
    response = requests.get(
        f"https://wttr.in/{city}",
        params={"format": "3"},
        timeout=10
    )

    response.raise_for_status()
    return response.text

def main():
    city = input("Enter city name: ")

    try:
        weather = get_weather(city)
        print(weather)
    except Exception as e:
        print(f"Error: {e}")

main()