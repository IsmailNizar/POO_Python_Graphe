import math

class Position :

    def __init__(self, longitude_degrees ,latitude_degrees):
        self.longitude_degrees = longitude_degrees
        self.latitude_degrees = latitude_degrees
    
    @property
    def longitude (self): # Passage du radians au degrees de la Longitude
        return self.longitude_degrees * math.pi / 180
    
    @property
    def latitude (self): # Passage du radians au degrees de la Latitude
        return self.latitude_degrees * math.pi / 180 

class Zone :

    ZONES = []
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1
    HEIGHT_DEGREES = 1
    EARTH_RADIUS_KILO = 6371

    def __init__(self , corner1 ,corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = []
    
    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)
    
    def contains(self, position):
        return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
            position.longitude < max(self.corner1.longitude, self.corner2.longitude) and \
            position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
            position.latitude < max(self.corner1.latitude, self.corner2.latitude)

    @property
    def width(self): # Passage du radians au kilo de la longitude du zone
        return abs(self.corner1.longitude - self.corner2.longitude) * self.EARTH_RADIUS_KILO 

    @property
    def height(self): # Passage du radians au kilo de la latitude du zone
        return abs(self.corner1.latitude - self.corner2.latitude) * self.EARTH_RADIUS_KILO
    
    @property
    def area(self): # Calcul de la surface d'une zone en kilo
        return self.height * self.width

    @property
    def population(self):
        return len(self.inhabitants)

    @classmethod
    def find_zone_that_contains(cls, position):
        # Compute the index in the ZONES array that contains the given position
        if not cls.ZONES:
            cls._intialize_zones()
        longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES)/ cls.WIDTH_DEGREES)
        latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES)/ cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES) # 180-(-180) / 1
        zone_index = latitude_index * longitude_bins + longitude_index

        # Just checking that the index is correct
        zone = cls.ZONES[zone_index]
        assert zone.contains(position)

        return zone

    def population_density(self):
        return self.population / self.area

    def average_agreeableness(self):
        if not self.inhabitants:
            return 0
        return sum([inhabitant.agreeableness for inhabitant in self.inhabitants]) / self.population

    @classmethod
    def _intialize_zones(cls):
        for latitude in range (cls.MIN_LATITUDE_DEGREES , cls.MAX_LATITUDE_DEGREES , cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES , cls.MAX_LONGITUDE_DEGREES , cls.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude , latitude)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES , latitude + cls.HEIGHT_DEGREES )            
                zone = Zone(bottom_left_corner,top_right_corner)
                cls.ZONES.append(zone)
