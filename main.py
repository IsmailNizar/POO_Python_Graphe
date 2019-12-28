# -*-coding:Latin-1 -*
import os
import json
from graph import AgreeablenessGraph
from zone import Zone , Position

class Agent :

    def __init__(self,position,**agents_attributes):
        self.position = position
        for attr_name , attr_val in agents_attributes.items():
            setattr(self, attr_name ,attr_val)
        self.age = []

def main ():
    
    for agents_attributes in json.load(open("agents-100k.json")): #read from json file
        longitude = agents_attributes.pop('longitude')
        latitude = agents_attributes.pop('latitude')
        pos = Position(longitude,latitude) # create a new position for every agent
        agent = Agent(pos,**agents_attributes) # create the agent
        zone = Zone.find_zone_that_contains(pos)# find the zone in which the agent exist
        zone.add_inhabitant(agent) # add the agent in this zone

    agreeableness_graph = AgreeablenessGraph () # initialise the graph
    agreeableness_graph.show(Zone.ZONES)

main()
os.system("pause")