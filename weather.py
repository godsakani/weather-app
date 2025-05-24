import requests
import streamlit as st


    
def get_weather(city, country_code):
    api_key = st.secrets['my_secrets']['API_KEY']
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={api_key}"
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
       
    

# city = input("Enter city name: ")
# weather_data = get_weather(city)
# curr_temp = weather_data['main']['temp']
# condition = weather_data['weather'][0]['description']
# city_humidity = weather_data['main']['humidity']
# print(f"Weather data for {city}:")
# print(f"Current temperature  {curr_temp} Kelvin.")
# print (f"Current weather condition: {condition}.")
# print(f"Humidity: {city_humidity}%.")



st.title("Weather App")
st.write("Enter a city name to get the current weather information.")
city = st.text_input("City Name", "Bamenda")
country_code = st.text_input("Country Code", "CM") 
st.markdown("[Get Country Code](https://www.iban.com/country-codes)")

if st.button("Fetch Data"):
    if city and country_code:
        weather_data = get_weather(city, country_code)
        if "error" in weather_data:
            st.error(f"Error fetching data: {weather_data['error']}")
        else:
            curr_temp = weather_data['main']['temp']
            condition = weather_data['weather'][0]['description']
            city_humidity = weather_data['main']['humidity']
            st.success(f"Weather data for {city}:")
            st.write(f"Current temperature: {curr_temp} Kelvin.")
            st.write(f"Current weather condition: {condition}.")
            st.write(f"Humidity: {city_humidity}%.")
    else:
        st.warning("Please enter both city name and country code.")
    