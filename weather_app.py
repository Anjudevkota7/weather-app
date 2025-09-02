import requests
import tkinter as tk
from tkinter import messagebox

# Replace with your OpenWeatherMap API key
API_KEY = "e901f3666e55c3dbdc18558ea4eb4f85"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result = (
            f"Weather in {city_name}, {country}:\n"
            f"Temperature: {temp}°C\n"
            f"Condition: {weather}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} m/s"
        )
        result_label.config(text=result)

    except Exception as e:
        messagebox.showerror("Error", f"Could not retrieve weather data.\n{e}")

# Tkinter setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Simple Weather App", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# City input
city_entry = tk.Entry(root, width=25, font=("Arial", 12))
city_entry.pack(pady=5)

# Search button
search_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12))
search_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the application
root.mainloop()
