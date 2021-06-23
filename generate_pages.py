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


###### GLITCH #######
# generate email pages
sheetIndex = 4
response = requests.get("https://spreadsheets.google.com/feeds/list/1X9FSpCIEoputo7chaNdjzyEcHunghZgOK6h4NtjmUpg/{}/public/values?alt=json".format(sheetIndex))
sheet = json.loads(response.content)

id = 0
for row in sheet["feed"]["entry"]:
    args = {
        "to": row["gsx$to"]["$t"],
        "from": row["gsx$from"]["$t"],
        "subject": row["gsx$subject"]["$t"],
        "body": row["gsx$body"]["$t"].replace("\n","<br>"),
    }
    template = templateEnv.get_template("glitch_email.html")
    outputText = template.render(args)
    text_file = open("output/{}_email.html".format(id), "w")
    text_file.write(outputText)
    text_file.close()
    id = id + 1


# generate modal pages
sheetIndex = 5
response = requests.get("https://spreadsheets.google.com/feeds/list/1X9FSpCIEoputo7chaNdjzyEcHunghZgOK6h4NtjmUpg/{}/public/values?alt=json".format(sheetIndex))
sheet = json.loads(response.content)

id = 0
for row in sheet["feed"]["entry"]:
    args = {
        "type": row["gsx$type"]["$t"],
        "header": row["gsx$header"]["$t"],
        "body": row["gsx$body"]["$t"],
        "cta1": row["gsx$cta1"]["$t"],
        "cta2": row["gsx$cta2"]["$t"],
    }
    template = templateEnv.get_template("glitch_modal.html")
    outputText = template.render(args)
    text_file = open("output/{}_modal.html".format(id), "w")
    text_file.write(outputText)
    text_file.close()
    id = id + 1


# generate chat pages
sheetIndex = 6
response = requests.get("https://spreadsheets.google.com/feeds/list/1X9FSpCIEoputo7chaNdjzyEcHunghZgOK6h4NtjmUpg/{}/public/values?alt=json".format(sheetIndex))
sheet = json.loads(response.content)

id = 0
for row in sheet["feed"]["entry"]:
    print(row.keys())
    args = {
        "person1": row["gsx$person1"]["$t"],
        "person2": row["gsx$person2"]["$t"],
        "messages": [
            row["gsx$message1"]["$t"].split("/"),
            row["gsx$message2"]["$t"].split("/"),
            row["gsx$message3"]["$t"].split("/"),
            row["gsx$message4"]["$t"].split("/"),
            row["gsx$message5"]["$t"].split("/"),
            row["gsx$message6"]["$t"].split("/"),
            row["gsx$message7"]["$t"].split("/"),
            row["gsx$message8"]["$t"].split("/"),
            row["gsx$message9"]["$t"].split("/"),
            row["gsx$message10"]["$t"].split("/"),
            row["gsx$message11"]["$t"].split("/"),
        ]
    }
    template = templateEnv.get_template("glitch_chat.html")
    outputText = template.render(args)
    text_file = open("output/{}_chat.html".format(id), "w")
    text_file.write(outputText)
    text_file.close()
    id = id + 1

