import folium
from constants.webmap_constants import WebMapConstants


class FoliumWebMap():
    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude
        self._map = None

    @classmethod
    def from_tuple(cls, obj_tuple):
        latitude, longitude = obj_tuple[0], obj_tuple[1]
        return cls(latitude, longitude)

    def make_map(self):
        self._map = folium.Map((self._latitude, self._longitude), zoom_start=13)
        return self

    def add_pinpoints(self, markers):
        """
        :param markers: dictionary
        :return: object
        """
        fg = folium.FeatureGroup(name='Fortyfikacje')
        for marker in markers:
            fg.add_child(folium.Marker(location=markers[marker], popup=marker,
                                       icon=folium.Icon(icon_color='green'
                                                        )))
        self._map.add_child(fg)
        return self

    def save_to_file(self, name):
        return self._map.save(name)


my_map = FoliumWebMap.from_tuple(WebMapConstants.localizations.get('Wroclaw'))
my_map.make_map()
my_map.add_pinpoints(WebMapConstants.markers)
my_map.save_to_file('Map_1.html')
