from map_parser import MapParser


mp = MapParser()
mp.parser_load("test.map")
print(len(mp.map_data.entities))
