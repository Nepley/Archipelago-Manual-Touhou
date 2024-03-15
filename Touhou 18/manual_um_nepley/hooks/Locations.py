import random, re

# called after the locations.json has been imported, but before ids, etc. have been assigned
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def before_location_table_processed(location_table: list) -> list:
    for location in location_table:
        # print(location)
        if 'region' in location:
            match location["region"]:
                case "Shop-Item":
                    price = "("+str(random.randint(1, 40))+"0)"
                    location["name"] = re.sub("\(.*\)", price, location["name"])

    return location_table
