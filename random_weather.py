import random

weather = ["Sunny", "Rainy", "Cloudy", "Stormy", "Snowy"]
temperature = random.randint(-10, 40)

print(f"Today's weather: {random.choice(weather)}, {temperature}°C")
