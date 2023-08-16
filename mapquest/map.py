from map_parser import MapParser


mp = MapParser()
mp.parser_load("E1M1.MAP")
print(mp.map_data)
