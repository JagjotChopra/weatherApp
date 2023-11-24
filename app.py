from flask import Flask, render_template, request, redirect,url_for
import requests

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/weatherapp", methods=["POST", "GET"])
def get_weatherdata():
    url="https://api.openweathermap.org/data/2.5/weather"

    params ={
        'q':request.form.get("city"),
        'appid':'f3889be5337dbd054700341de9fbf34a',
        'units':'metrics'
    }
    response=requests.get(url, params=params)
    data = response.json()
    city=data['name']
    weather=data['weather'][0]['main']
    temperature=data['main']['temp']
    humdity=data['main']['humidity']
    feelslike=data['main']['feels_like']
    speed=data['wind']['speed']
    country = data['sys']['country']
    cloudy=data['clouds']['all']
    #return f"data : {data}, city:{city}"
    #return  render_template("index.html",data=data)
    return redirect(url_for("run",cityName=city,temp=temperature,fl=feelslike,weather=weather,humdity=humdity,speed=speed,country=country,cloudy=cloudy))

@app.route('/wt/<string:cityName>/<int:temp>/<int:fl>/<string:weather>/<int:humdity>/<int:speed>/<string:country>/<int:cloudy>')
def run(cityName,temp,fl,weather,humdity,speed,country,cloudy):
    return render_template('index2.html',city=cityName,temp=temp,fl=fl,weather=weather,humdity=humdity,speed=speed,country=country,cloudy=cloudy)

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)