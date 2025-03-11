import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Step 1: Fetch data from OpenWeatherMap API
def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

# Step 2: Process the data
def process_data(data):
    # Extract the time and temperature
    times = []
    temperatures = []

    for entry in data['list']:
        times.append(entry['dt_txt'])
        temperatures.append(entry['main']['temp'])
    
    # Create a DataFrame for easy manipulation
    df = pd.DataFrame({
        'Time': pd.to_datetime(times),
        'Temperature (°C)': temperatures
    })
    
    return df

# Step 3: Visualize the data
def plot_data(df):
    # Set the style for seaborn
    sns.set(style="darkgrid")
    
    plt.figure(figsize=(10,6))
    
    # Create a line plot for the temperature over time
    sns.lineplot(data=df, x='Time', y='Temperature (°C)', marker='o')
    
    # Customize the plot
    plt.title('Weather Forecast - Temperature Over Time', fontsize=16)
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()

# Main execution
def main():
    city = "ida bollaram"  
    api_key = "06d4435fa262f616c6a4ea70d42eb809"  
    
    # Get weather data
    data = get_weather_data(city, api_key)
    
    # Process the data
    df = process_data(data)
    
    # Visualize the data
    plot_data(df)

if __name__ == "__main__":
    main()
