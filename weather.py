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
# country_code = input("Enter country code: ")
# weather_data = get_weather(city, country_code)
# curr_temp = weather_data['main']['temp']
# curr_temp_celsius  = round(curr_temp - 273.15 , 2)
# condition = weather_data['weather'][0]['description']
# city_humidity = weather_data['main']['humidity']
# wind_speed = weather_data['wind']['speed']
                    
# print(f"Weather data for {city}:")
# print(f"Current temperature  {curr_temp_celsius} °C.")
# print (f"Current weather condition: {condition}.")
# print(f"Humidity: {city_humidity}%.")
# print(f"Wind Speed: {wind_speed} m/s.")

# if curr_temp_celsius > 25 and city_humidity > 70:
#     print(f"It's a hot and dry day in the city of {city}!")
# elif curr_temp_celsius >= 15 and curr_temp_celsius <= 25 and city_humidity <= 70:
#      print(f"The weather in {city} is pleasant today.") 
# elif curr_temp_celsius < 15 and city_humidity > 70:
#      print(f"The weather in {city} is chilly today.")             
# else:
#     print(f"The weather in {city} is cold and humid today and we might experience {condition}.") 



col1, col2 = st.columns(2)

with col1:
    st.title("Weather App")
    st.write("Enter a city name to get the current weather information.")
    city = st.text_input("City Name", "Bamenda")
    country_code = st.text_input("Country Code", "CM") 
    st.markdown("[Get Country Code](https://www.iban.com/country-codes)")
    fetch = st.button("Fetch Data")

with col2:
    if 'fetch' not in st.session_state:
        st.session_state.fetch = False
    if fetch:
        st.session_state.fetch = True
    if st.session_state.fetch:
        if city and country_code:
            weather_data = get_weather(city, country_code)
            if "error" in weather_data:
                st.error(f"Error fetching data: {weather_data['error']}")
            else:
                curr_temp = weather_data['main']['temp']
                curr_temp_celsius  = round(curr_temp - 273.15 , 2)
                condition = weather_data['weather'][0]['description']
                city_humidity = weather_data['main']['humidity']
                wind_speed = weather_data['wind']['speed']
                st.success(f"Weather data for {city}:")
                container = st.container(border=True)
                container.markdown(f"<span style='font-size:32px;'>Temperature: {curr_temp_celsius} °C.</span>", unsafe_allow_html=True)
                container.markdown(f"<span style='font-size:24px;'>Humidity: {city_humidity}%.</span>", unsafe_allow_html=True)
                container.markdown(f"<span style='font-size:18px;'>Wind Speed: {wind_speed} m/s.</span>", unsafe_allow_html=True)
                container.write(f"Weather Condition: {condition}.")
                if curr_temp_celsius > 25 and city_humidity > 70:
                    st.balloons()
                    st.success(f"It's a hot and dry day in the city of {city}!")
                elif curr_temp_celsius >= 15 and curr_temp_celsius <= 25 and city_humidity <= 70:
                    st.balloons()   
                    st.success(f"The weather in {city} is pleasant today.")
                elif curr_temp_celsius < 15 and city_humidity > 70:
                    st.balloons()
                    st.warning(f"The weather in {city} is chilly today.")
                else:
                    st.balloons()
                    st.warning(f"The weather in {city} is cold and humid today and we might experience {condition}.")
        else:
            st.warning("Please enter both city name and country code.")
    