# Sort the JSON file files/mods.json's keys in a custom order
import ujson

all_mods = ujson.load(open("files/mods.json"))
# orig_mods = ujson.load(open("files/origmods.json"))
# for [mod, orig] in zip(all_mods, orig_mods):
for mod in all_mods:
    new_mod = {}
    for key in [
        "id",
        "nicknames",
        "display",
        "enabled",
        "creator",
        "discordcode",
        "command",
        "description",
        "icon",
        "icon_scaling",
        "actions",
        "categories",
        "hidden",
        "file",
        "files",
        "url",
        "forge_id",
        "packages",
        "hash",
    ]:
        if key in mod:
            new_mod[key] = mod[key]
        # elif key in orig:
        #    new_mod[key] = orig[key]
    if "actions" in new_mod:
        for action in new_mod["actions"]:
            if "creator" in action:
                del action["creator"]
    mod.clear()
    mod.update(new_mod)

# Write the new json file
ujson.dump(all_mods, open("files/mods.json", "w"))
