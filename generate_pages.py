import requests
import json
import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)

# generate art pages
sheetIndex = 1
response = requests.get("https://spreadsheets.google.com/feeds/list/1X9FSpCIEoputo7chaNdjzyEcHunghZgOK6h4NtjmUpg/{}/public/values?alt=json".format(sheetIndex))
sheet = json.loads(response.content)

id = 0
for row in sheet["feed"]["entry"]:
    args = {
        "art": row["gsx$art"]["$t"],
        "artist": row["gsx$artist"]["$t"],
        "url": row["gsx$url"]["$t"]
    }
    template = templateEnv.get_template("art.html")
    outputText = template.render(args)
    text_file = open("output/{}_art.html".format(id), "w")
    text_file.write(outputText)
    text_file.close()
    id = id + 1

# generate campfire page
sheetIndex = 2
response = requests.get("https://spreadsheets.google.com/feeds/list/1X9FSpCIEoputo7chaNdjzyEcHunghZgOK6h4NtjmUpg/{}/public/values?alt=json".format(sheetIndex))
sheet = json.loads(response.content)
questions = []
for row in sheet["feed"]["entry"]:
  questions.append(row["gsx$question"]["$t"])
questionsString = json.dumps(questions)
template = templateEnv.get_template("campfire.html")
outputText = template.render({"questions": questions})
text_file = open("output/campfire.html", "w")
text_file.write(outputText)
text_file.close()

# generate telephone page
sheetIndex = 3
response = requests.get("https://spreadsheets.google.com/feeds/list/1X9FSpCIEoputo7chaNdjzyEcHunghZgOK6h4NtjmUpg/{}/public/values?alt=json".format(sheetIndex))
sheet = json.loads(response.content)
gifs = []
for row in sheet["feed"]["entry"]:
  gifs.append(row["gsx$gif"]["$t"])
gifsString = json.dumps(gifs)
template = templateEnv.get_template("telephone.html")
outputText = template.render({"gifs": gifs})
text_file = open("output/telephone.html", "w")
text_file.write(outputText)
text_file.close()