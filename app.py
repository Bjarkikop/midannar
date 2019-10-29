from flask import Flask, render_template, url_for, request, json
import urllib.request, json 

with urllib.request.urlopen("https://apis.is/petrol") as url:
    data = json.loads(url.read().decode())
myndir = [
    ["Atlantsolía", "Atlantsolía.jpg"],
    ["Costco Iceland", "Costco-Iceland.jpg"],
    ["Dælan", "Dælan.jpg"],
    ["N1", "N1.jpg"],
    ["ÓB", "ÓB.jpg"],
    ["Olís", "Olís.jpg"],
    ["Orkan", "Orkan.jpg"],
    ["Orkan X", "Orkan-X.jpg"]
    ]

app = Flask(__name__)

def companiesOnce():
    companies = []
    for i in data["results"]:
        if i["company"] not in companies:
            companies.append(i["company"])
    return companies
def minnsta_verd_bensin():
    verd = []
    for x in data["results"]:
        verd.append(x["bensin95"])
    return min(verd)

def minnsta_verd_diesel():
    verd = []
    for x in data["results"]:
        verd.append(x["diesel"])
    return min(verd)

@app.route('/')
def index():
    return render_template('index.html', companies=companiesOnce(), data=data, min_verd_bensin=minnsta_verd_bensin(), min_diesel=minnsta_verd_diesel(), myndir=myndir)

@app.route('/company/<id>')
def company(id):
	return render_template('company.html', id=id, data=data)

@app.route('/moreInfo/<id>')
def info(id):
    return render_template("info.html", id=id, data=data, companies=companiesOnce())

 
@app.errorhandler(404)
def error404(error):
	return '<h1>Þessi síða er ekki til</h1> <a href="/">Heim</a>', 404


if __name__ == "__main__":
	app.run(debug=True)
	