import os


def repeatedly_index_set(key_list, dictionary, value):
    current = dictionary

    for index in range(len(key_list) - 1):
        current = current[key_list[index]]
    # if type(value) == dict:
    #    current[key_list[-1]] = value
    #    return
    if key_list[-1] in current:
        current[key_list[-1]].append(value)

    else:
        current[key_list[-1]] = [value]
        # key_list.append(0)
    if type(value) == dict:
        key_list.append(len(current[key_list[-1]]) - 1)


game_history_location = "C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game\common\history"
game_location = "C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game"
laws_location = game_location+"\common\laws"
country_loc = game_history_location + "\countries"

mod_laws_location = r"C:\Users\clone\Documents\Paradox Interactive\Victoria 3\mod\Advanced Politics Mod\common\laws"
country_dict = {}

def update_pdxinfo(old, new):
    for key in new:
        if key in old:
            old[key] += new[key]
        else:
            old[key] = new[key]

def convert_directory_to_dict(directory, final_dict):
    lst = os.listdir(directory)

    for path in lst:
        if not path[-4:] == ".txt":
            continue
        print(path)
        with open(directory + "\\" + path) as file:
            text = file.read()[3:]
            new_str = ""
            for line in text.split('\n'):
                try:
                    k = line.index('#')
                    line = line[0:k]
                except:
                    pass
                new_str += line + "\n"
            text = new_str
            text = text.replace("\t", "")
            text = text.replace(" ", "")
            text = text.replace("}", "\n}")
            text = text.replace("{", "{\n")
            #text = text.replace("#", "\n#")
            text = text.split("\n")
            temp_dict = {}
            keys = []
            thebigkey = ""
            iterations = 0
            for line in text:
                #print()

                if line == "":
                    continue
                if line[0] == '#':
                    continue
                if line == "}":
                    if (type(keys[-1] == int)):
                        keys.pop()
                    keys.pop()
                    continue
                asdf = line.split("=")
                size = len(asdf)
                #print(line)
                #print(keys)
                #print(temp_dict)
                if size <= 1:
                    index = keys + [asdf[0]]
                    value = None
                    repeatedly_index_set(index,temp_dict, value)
                    #keys.pop()
                    #if type(keys[-1]) == dict:
                    #    keys.pop()
                    #repeatedly_index_set(keys, temp_dict, asdf[0])
                    continue

                key = asdf[0]
                value = asdf[1]
                if iterations == 0:
                    thebigkey = key
                iterations += 1
                if value == "{":
                    keys.append(key)
                    repeatedly_index_set(keys, temp_dict, dict())
                else:
                    index = keys+[key]
                    #print(index)
                    #print(value)
                    repeatedly_index_set(index, temp_dict, value)
        #final_dict.update(temp_dict)
        update_pdxinfo(final_dict, temp_dict)

laws_dict = {}
convert_directory_to_dict(laws_location, laws_dict)
convert_directory_to_dict(mod_laws_location, laws_dict)
print(laws_dict)
# convert_directory_to_dict(country_loc,country_dict)

#character_loc = game_history_location + "\characters"
#character_dict = {}
#convert_directory_to_dict(character_loc, character_dict)
#print(character_dict)





class GameManager:
    game_loc = "C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game"
    laws = []
    techs = []
    country_modifiers = []
    state_modifiers = []
    def __init__(self):
        laws = []

