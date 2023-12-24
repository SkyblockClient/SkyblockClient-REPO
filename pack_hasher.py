# Update the hash to the correct one (use md5)
import ujson
import requests
import hashlib

all_packs = ujson.load(open("files/packs.json"))

for pack in all_packs:
    print(pack["id"])
    if "url" not in pack:
        continue
    resp = requests.get(pack["url"], headers={"User-Agent": "Mozilla/5.0"})
    if resp.status_code != 200:
        print("FIXME: " + pack["id"], resp.status_code)
        continue
    pack["hash"] = hashlib.md5(resp.content).hexdigest()

ujson.dump(all_packs, open("files/packs.json", "w"), indent=4)
