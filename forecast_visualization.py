import requests
import matplotlib.pyplot as plt
import seaborn as sns

# OpenWeatherMap API Key
API_KEY = '581127197832298e7fd3857ed6bbfefb'

# City for weather forecast
city = 'Daltonganj'

# API URL
url = 'https://api.openweathermap.org/data/2.5/forecast'
params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'  
}

# Fetch data from API
response = requests.get(url, params=params)
data = response.json()

# Extract dates and temperatures
dates = []
temperatures = []

for item in data['list']:
    dates.append(item['dt_txt'])
    temperatures.append(item['main']['temp'])

# Create visualization
sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temperatures, marker='o', color='teal')

plt.title(f"5-Day Temperature Forecast for {city}", fontsize=16)
plt.xlabel("Date & Time", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Save and display the graph
plt.savefig('weather_forecast_dashboard.png')
plt.show()
