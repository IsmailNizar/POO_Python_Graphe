import matplotlib.pyplot as plt  # library that allow you to trace a graph

class BaseGraph:

    def __init__(self):
        self.title = "graph title"
        self.x_label = "X-axis label"
        self.y_label = "Y-axis label"
        self.show_grid = True

    def xy_values(self,zones):
        raise NotImplementedError # if a childClass do not use this function Raise implemented error

    def show(self, zones):
        x_values , y_values = self.xy_values(zones)
        plt.plot(x_values , y_values ,'.')
        plt.xlabel(self.x_label) # Set the X-axis title
        plt.ylabel(self.y_label) # Set the Y-axis title
        plt.title(self.title) # Set the title for the graph
        plt.grid(self.show_grid)
        plt.show()

class AgreeablenessGraph(BaseGraph):

    def __init__(self):
        super().__init__()
        self.title = "Agreeableness-Graph"
        self.x_label = "Population density"
        self.y_label = "Agreeableness"

    def xy_values(self,zones):
        x_values = [zone.population_density() for zone in zones]
        y_values = [zone.average_agreeableness() for zone in zones]
        return x_values,y_values
