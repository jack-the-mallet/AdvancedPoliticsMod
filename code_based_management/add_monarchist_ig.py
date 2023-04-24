

def is_monarchist(c_dict, country):
    monarchist = False
    monarchist_politics = ["effect_starting_politics_conservative", "effect_starting_politics_reactionary"]
    anti_monarchist_laws = ["law_type:law_chiefdom", "law_type:law_presidential_republic",
                            "law_type:law_parliamentary_republic", "law_type:law_theocracy",
                            "law_type:law_council_republic"]
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
    # print("base monarchism: ", monarchist)
    if 'activate_law' in good_dict:
        for law in good_dict['activate_law']:
            # print(law)
            if law == "law_type:law_monarchy":
                monarchist = True
            if law in anti_monarchist_laws:
                # print("ANTI MONARCHIST!!")
                monarchist = False

    return monarchist

# print(country_dict['c:ABS'])
# for country in country_dict:
#    m = is_monarchist(country_dict,country)
#    if m:
#        print(country)
