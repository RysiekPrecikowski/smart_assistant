import pyowm
from datetime import datetime
from speaking import read_text
from pytz import timezone

def utc_to_local(d):
    return d.astimezone(timezone('Europe/Warsaw'))

def weather(args):
    owm = pyowm.OWM("a308178fe2a66350898902079b913971")
    mgr = owm.weather_manager()

    text = args.split("in ")[1]
    print("text", text, "\n")


    #TODO rozpoznawanie miasta z mowy

    # city = "Kraków"
    city = text

    observation = mgr.weather_at_place(city)
    weather = observation.weather

    print("location:", observation.location.name)



    # print(weather.status)
    print("status", weather.detailed_status)
    print("temperature", weather.temperature('celsius'))
    print("wind", weather.wind())
    print("rain", weather.rain)
    print("pressure", weather.pressure)

    print("\nsun")
    print("sunrise", utc_to_local(weather.sunrise_time(timeformat='date')))
    print("sunset", utc_to_local(weather.sunset_time(timeformat='date')))

    print("\n\nForecast")
    one_call = mgr.one_call(lat = observation.location.lat, lon =observation.location.lon)

    day = 1 # 0 -today, max 5 days
    forecast = one_call.forecast_daily[day]
    print("forecast for", utc_to_local(forecast.reference_time(timeformat='date')))
    print("temperature", forecast.temperature('celsius'))
    print("wind", forecast.wind())



if __name__ == '__main__':
    weather("What's the weather like in Kraków")