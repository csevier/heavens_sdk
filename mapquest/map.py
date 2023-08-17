from map_parser import MapParser


mp = MapParser()
# mp.parser_load("test.map")
mp.parser_load("qodot_test.map")
# mp.parser_load("E1M1.MAP")
mp.map_data.load_texture_data()
print("done")
