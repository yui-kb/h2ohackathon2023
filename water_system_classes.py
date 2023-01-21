
# Standard library imports
import random
from datetime import date, datetime

# Local imports
from temp_change import temp_change

LOWEST_PIPE_DEPTH = 5 # In metres, of the whole system
MAXIMUM_PIPE_AGE = 200 # In years, choice based on introductory talk

class material():
    """ Potential water and sewage pipe materials, and their associated properties. """

    def __init__(self, sewageRate, cleanRate, Strength):
        """ Initial values. """
        self.sewageRate = sewageRate
        self.cleanRate = cleanRate
        self.Strength = Strength
class Monitor:
    """ Monitors measure data and are the joining points of the pipe() object. """

    def __init__(self,longitude,latitude,curFlow,avgFlow):
        """ Initialise each Monitor with location and flow data."""
        self.longitude = float(longitude) # Monitor location
        self.latitude = float(latitude)
        self.curFlow = float(curFlow) # Current flow rate
        self.avgFlow = float(avgFlow) # Average flow rate based on past data

    def update(self):
        """ Allows to update current flow, currently randomised for demonstration purposes. """
        self.curFlow = random.uniform(0,20.5)


class pipe:
    """ pipes() are modelled as edges between the Monitors, which are nodes. """

    def __init__(self,start,end,depth,sewage,material,installDate):
        """ Initial values. """
        self.start = start
        self.end = end
        self.avgFlow = (start.avgFlow + end.avgFlow)/2
        self.depth = depth
        self.sewage = bool(sewage)
        self.curFlow = (start.curFlow + end.curFlow)/2
        self.material = material
        self.installDate = installDate

    def returnPipeAge(self):
        """ Calculate the age in years of the pipe. """

        today = date.today()

        return today.year - self.installDate

    def isLeaking(self):
        if self.curFlow - 10 < self.avgFlow:
            return True
        else:
            return False

    def ErRisk(self):
        """ Calculates the risk of pipe erosion
        based on pipe material and whether the pipe is a sewage or water pipe."""

        if self.sewage:
            erRate = self.material.sewageRate
        else:
            erRate = self.material.cleanRate

        erRisk = (self.returnPipeAge() / MAXIMUM_PIPE_AGE) * erRate

        return erRisk

    def TempRisk(self):
        """ Calculate the risk of pipe weakness due to free-thaw events. """

        chance_of_thaw = temp_change()
        tempRisk = chance_of_thaw * self.material.Strength / (self.depth)
        return tempRisk

    def risk(self):
        """ Calculate an overall risk value, for the
        likelihood a pipe will burst or leak soon. """
        # print(self.TempRisk(), self.ErRisk())
        riskPoint = ((7 * self.TempRisk()) + (3 * self.ErRisk())) / 10
        return riskPoint



