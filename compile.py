print("Compiling Advanced Mode Raw Data.")
print("(c) Advanced Mode Foundation 2019")
print("=================================\n")
import json

print("Loading in raw data...")
rulesData = []
with open("./json-data/rules.json") as f:
    rulesData = json.loads(f.read())

styleData = []
with open("./json-data/styles.json") as f:
    styleData = json.loads(f.read())

variationsData = []
with open("./json-data/variations.json") as f:
    variationsData = json.loads(f.read())

print("Compiling...")
# prepare the compiled data structure
compiledData = {
    "rules": {
        "data": {},
        "aliases": {}
    },
    "styles": {
        "data": {},
        "aliases": {},
    },
    "variations": {
        "data": {},
        "aliases": {}
    }
}

def compile(data):
    miniCompiled = {
        "data": {},
        "aliases": {}
    }
    for i in data:
        # find the identifier & aliases
        identifier = i["identifier"]
        aliases = i["aliases"]

        # compile the aliases
        for j in aliases:
            miniCompiled["aliases"][j] = identifier

        # compile the rules
        miniCompiled["data"][identifier] = i
        #del miniCompiled["data"][identifier]["aliases"]
    return miniCompiled

print(" - Rules... ", end="")
compiledData["rules"] = compile(rulesData)
print("Done!")

print(" - Styles... ",end="")
compiledData["styles"] = compile(styleData)
print("Done!")

print(" - Variations...",end="")
compiledData["variations"] = compile(variationsData)
print("Done!")

print("Saving... ",end="")
# save the compiled data
with open("./compiled/advancedModeData.json", 'w') as f:
    f.write(json.dumps(compiledData))
print("Saved.")

input("Press enter to exit.")