import os
def repeatedly_index_set(key_list, dictionary, value):
    current = dictionary
    
    for index in range(len(key_list)-1):
        current = current[key_list[index]]
    #if type(value) == dict:
    #    current[key_list[-1]] = value
    #    return
    if key_list[-1] in current:
        current[key_list[-1]].append(value)
    else:
        current[key_list[-1]] = [value]
        #key_list.append(0)
    if type(value) == dict:
        key_list.append(len(current[key_list[-1]]) -1 )


game_history_location = "C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game\common\history"
country_loc = game_history_location + "\countries"
country_dict = {}

def convert_directory_to_dict(directory, final_dict):
    lst = os.listdir(directory)

    for path in lst:
        if not path[-4:] == ".txt":
            continue
        print(path)
        with open(directory + "\\" + path) as file:
            text = file.read()[3:]
            text = text.replace("\t","")
            text = text.replace(" ","")
            text = text.replace("}","\n}")
            text = text.replace("{","{\n")
            text = text.replace("#","\n#")



            text = text.split("\n")
            #print(text)
            #print()
            temp_dict = {}
            indentation = 0
            keys = []
            thebigkey = ""
            iterations = 0

            in_stupid_list = False
            for line in text:
                if line == "":
                    continue
                if line[0] == '#':
                    continue
                if line == "}":
                    if(type(keys[-1] == int)):
                        keys.pop()
                    keys.pop()
                    continue
                asdf = line.split("=")
                print(line)
                print(keys)
                print(temp_dict)
                print()
                if len(asdf) <= 1:
                    #in_stupid_list = True
                    saved = keys.pop()
                    repeatedly_index_set(keys,temp_dict,value[0])
                    continue
                
                key = asdf[0]
                value = asdf[1]
                if iterations == 0:
                    thebigkey = key
                iterations += 1
                if value == "{":
                    keys.append(key)
                    repeatedly_index_set(keys,temp_dict,dict())
                else:
                    repeatedly_index_set(keys + [key],temp_dict,value)
        final_dict.update(temp_dict[thebigkey][0])

#convert_directory_to_dict(country_loc,country_dict)

character_loc = game_history_location + "\characters"
character_dict = {}
convert_directory_to_dict(character_loc,character_dict)
print(character_dict)

def is_monarchist(c_dict,country):
    monarchist = False
    monarchist_politics = ["effect_starting_politics_conservative", "effect_starting_politics_reactionary"]
    anti_monarchist_laws = ["law_type:law_chiefdom", "law_type:law_presidential_republic", "law_type:law_parliamentary_republic", "law_type:law_theocracy", "law_type:law_council_republic"]
    decentralized_techs = ["effect_starting_technology_tier_6_tech", "effect_starting_technology_tier_7_tech"]
    native_conscriptions = [
        "effect_native_conscription_1",
        "effect_native_conscription_2",
        "effect_native_conscription_3",
        "effect_native_conscription_4",
        "effect_native_conscription_5",
        "effect_native_conscription_6",
        "effect_native_conscription_7",
        "effect_native_conscription_8",
        "effect_native_conscription_9",
        "effect_native_conscription_10",
        "effect_native_conscription_11",
        "effect_native_conscription_12"
    ]
    monarchist_law = ""
    good_dict = c_dict[country][0]
    for starting in monarchist_politics:
        if starting in good_dict and good_dict[starting] == ['yes']:
            monarchist = True
    
    starting = "effect_starting_politics_traditional"
    if starting in good_dict and good_dict[starting] == ['yes']:
        monarchist = True
        for asdf in native_conscriptions:
            if asdf in c_dict[country]:
                monarchist = False
    #print("base monarchism: ", monarchist)
    if 'activate_law' in good_dict:
        for law in good_dict['activate_law']:
            #print(law)
            if law == "law_type:law_monarchy":
                monarchist = True
            if law in anti_monarchist_laws:
                #print("ANTI MONARCHIST!!")
                monarchist = False
    
    return monarchist

#print(country_dict['c:ABS'])
#for country in country_dict:
#    m = is_monarchist(country_dict,country)
#    if m:
#        print(country)
    