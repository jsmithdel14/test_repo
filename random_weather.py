import random

def get_random_weather():
    weather = ["Sunny", "Rainy", "Cloudy", "Stormy", "Snowy"]
    temperature = random.randint(-10, 40)

    return f"Today's weather: {random.choice(weather)}, {temperature}°C"
