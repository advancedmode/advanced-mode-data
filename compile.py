import json

# load in the raw data
rulesData = []
with open("./json-data/rules.json") as f:
    rulesData = json.loads(f.read())

# prepare the compiled data
rulesCompiled = {
    "rules": {},
    "aliases": {}
}

for i in rulesData:
    # find the identifier & aliases
    identifier = i["identifier"]
    aliases = i["aliases"]

    # compile the aliases
    for j in aliases:
        rulesCompiled["aliases"][j] = identifier

    # compile the rules
    rulesCompiled["rules"][identifier] = i
    del rulesCompiled["rules"][identifier]["aliases"]

# save the compiled data
with open("./compiled/rules.json", 'w') as f:
    f.write(json.dumps(rulesCompiled))