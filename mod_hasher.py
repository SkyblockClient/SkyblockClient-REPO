# Update the hash to the correct one (use md5)
import ujson
import requests
import hashlib

all_mods = ujson.load(open("files/mods.json"))

for mod in all_mods:
    print(mod["id"])
    if "url" not in mod:
        continue
    resp = requests.get(mod["url"], headers={"User-Agent": "Mozilla/5.0"})
    if resp.status_code != 200:
        print("FIXME: " + mod["id"], resp.status_code)
        continue
    mod["hash"] = hashlib.md5(resp.content).hexdigest()

ujson.dump(all_mods, open("files/mods.json", "w"), indent=4)
