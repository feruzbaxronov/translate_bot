import requests

app_id = "935e8929"
app_key = " 11563ff41877e43d53a43bdc79faaab5"
language = "en-gb"


def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id , "app_key": app_key })
    res=r.json()
    if "error" in res.key():
        return False

    output={}
    senses=res["results"][0]["lexicalEntries"][0]["entries"][0]["senses"]
    definitions=[]
    for sense in senses:
        definitions.append(f"👉{sense['definitions'][0]}")
    output["definitions"]="\n".join(definitions)

    if res["results"][0]["lexicalEntries"][0]["pronunciations"][0].get("audioFile"):
        output["audio"]=res["results"][0]["lexicalEntries"][0]["pronunciations"][0]["audioFile"]
    return output

if __name__=="_main__":
    from pprint import pprint as print
    print(getDefinitions('apple'))
    print(getDefinitiond('meet'))