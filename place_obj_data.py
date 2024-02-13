# Get Metadata from jason file

from json_parser import json_parsing
import random
def config_obj_Matadata():
    objects = json_parsing()
    i = random.randint(0, len(objects))
    key = list(objects.keys())[i]

    print("*************************************************************")
    print(f"category of fourniture is: {objects[key]}, its name is: {key},")
    print("*************************************************************")

    assert key != "bench_kpeeai_0", f"obj cannot be placed on bench_kpeeai_0 because unknown bugs "

    lbia_x = 0.0
    lbia_y = 0.0
    bia_z = 0.0
    rbia_x = 0.0
    rbia_y = 0.0

# tunind of the boundingbox coordinate
    if objects[key] == "sofa":
        if (key == "sofa_ewview_0" or key == "sofa_ewview_1"):
            lbia_x = 1.0
            rbia_x = 0.8
            lbia_y = rbia_y = 1.5
            bia_z = 0.60
        elif (key == "sofa_ksbdlf_0" or key == "sofa_ksbdlf_1"):
            lbia_x = 0.8
            rbia_x = 0.65
            lbia_y = 0.9
            rbia_y = 0.70
            bia_z = 0.45
    if objects[key] == "armchair":
        if (key[9:15] == "hicyww" or key[9:15] == "ukuwuu" or key[9:15] == "jdtdpa"):
            lbia_x = 0.60
            rbia_x = 0.50
            lbia_y = 0.80
            rbia_y = 0.70
            bia_z = 0.60
        elif (key[9:15] == "rtbsof" or key[9:15] == "qyntri" or key[9:15] == "hdibix"):
            lbia_x = 0.60
            rbia_x = 0.60
            lbia_y = 0.70
            rbia_y = 0.70
            bia_z = 0.60
    if (objects[key] == "bench"):
        if (key[6:12] == "ybkjzd"):
            lbia_x = 2.6189
            rbia_x = 3.7
            lbia_y = 7.5519
            rbia_y = 5.85
            bia_z = 0.35
        elif (key[6:12] == "sihckt"):
            lbia_x = 0.71
            rbia_x = 0.54
            lbia_y = 3.10
            rbia_y = 3.192
            bia_z = 0.56
    if (objects[key] == "bar"):
        lbia_x = rbia_x = lbia_y = rbia_y = 0.352
        bia_z = 0.60
    if (objects[key] == "ottoman" or objects[key] == 'breakfast_table'):
        lbia_x = rbia_x = lbia_y = rbia_y = 0.65
        bia_z = 0.33
    if (objects[key] == "console_table"):
        lbia_x = rbia_x = lbia_y = rbia_y = 0.4
        bia_z = 0.30
    if (objects[key] == 'coffee_table'):
        lbia_x = rbia_x = lbia_y = rbia_y = 0.55
        bia_z = 0.1
    return key, lbia_x, lbia_y, bia_z, rbia_x, rbia_y