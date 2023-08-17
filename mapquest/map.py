from map_parser import MapParser
from geo_generator import GeoGenerator


mp = MapParser()
# mp.parser_load("test.map")
mp.parser_load("test_maps/qodot_test.map")
# mp.parser_load("E1M1.MAP")
mp.map_data.load_texture_data()
geo_gen = GeoGenerator(mp.map_data)
geo_gen.run()
print("done")
