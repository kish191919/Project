import forecastio

FORECAST_TOKEN = "b54225b399dd39a1879ccba6ef1bad58"
def forecast(lat = 33.5186, lng = 86.8104):
    forecast = forecastio.load_forecast(FORECAST_TOKEN, lat, lng)
    byHour = forecast.hourly()
    return byHour.summary
