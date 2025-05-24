# Weather App

A simple Streamlit web application to fetch and display current weather information for any city using the OpenWeatherMap API.

## Features

- Enter a city name and country code to get real-time weather data.
- Displays temperature, weather condition, and humidity.
- User-friendly interface built with Streamlit.

## Setup

1. **Clone the repository**
2. **Install dependencies**
3. **Set up API Key**  
- Add your OpenWeatherMap API key in `.streamlit/secrets.toml`:
  ```
  [my_secrets]
  API_KEY="your_api_key_here"
  ```

## Usage

Run the app with:

```bash
streamlit run app.py
```

## Notes

- Get your country code from [IBAN Country Codes](https://www.iban.com/country-codes).
- Requires an internet connection to fetch weather data.