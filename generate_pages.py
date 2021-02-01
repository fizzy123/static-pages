import requests
import json
import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
templateEnv = jinja2.Environment(loader=templateLoader)

# 1. pull information from sheets
response = requests.get("https://spreadsheets.google.com/feeds/list/1X9FSpCIEoputo7chaNdjzyEcHunghZgOK6h4NtjmUpg/od6/public/values?alt=json")
sheet = json.loads(response.content)
# 2. loop over rows
id = 0
for row in sheet["feed"]["entry"]:
    args = {
        "art": row["gsx$art"],
        "artist": row["gsx$artist"],
        "url": row["gsx$url"]
    }
    template = templateEnv.get_template("art.html")
    outputText = template.render(args)
    text_file = open("output/{}_art.html".format(id), "w")
    text_file.write(outputText)
    text_file.close()
    id = id + 1
# 4. save pages to appropriate location in output/