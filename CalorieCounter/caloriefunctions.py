# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#    This file is part of Calorie Counter.
#
#    Calorie Counter is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Calorie Counter is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Calorie Counter.  If not, see <http://www.gnu.org/licenses/>
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import math

# # # # # # # # # # # # # # # # # # # # # # # #
#
#   conversion/calculation functions
#
# # # # # # # # # # # # # # # # # # # # # # # #


def convertToFloat(x):
    """
    This function checks that the input can be converted to a float, and then
    does so if it can.
    """
    try:
        float(x)
    except Exception:
        return 0

    return float(x)


def convertToCups(calories, calories_per_cup):
    """
    This takes calorie content per cup from a food and breaks it up into cups
    that the animal should be getting per day for ease of use
    """
    cups_per_day = calories / calories_per_cup
    return cups_per_day


def calculateRER(weight):
    """
    Calculates the dogs' RER(resting energy requirement), after converting the
    weight to kilograms.
    """
    #This is another common eqution used - gives high calorie amounts as 
    #the dog weight increases that are much too high. May use as a range in the
    #future.
    #RER = math.ceil(70 * (weight_kilograms ** (3/4)))
    weight_kilograms = weight / 2.2
    RER = math.ceil((weight_kilograms * 30) + 70)
    return RER


# # # # # # # # # # # # # # # # # # # # # # # #
#
#   Different dog 'type' calorie functions
#
# # # # # # # # # # # # # # # # # # # # # # # #


def neuteredAdult(dog_weight):
    RER = calculateRER(dog_weight)
    return math.ceil(1.6 * RER)


def intactAdult(dog_weight):
    RER = calculateRER(dog_weight)
    return math.ceil(1.8 * RER)


def inactiveObeseProneAdult(dog_weight):
    RER = calculateRER(dog_weight)
    return math.ceil(1.3 * RER)


def weightLoss(dog_weight):
    RER = calculateRER(dog_weight)
    return math.ceil(RER)


def weightGainNeutered(dog_weight):
    """
    Range for weight gain for neutered dogs
    """
    RER = calculateRER(dog_weight)
    minimum = math.ceil(1.6 * RER)
    maximum = math.ceil(1.8 * RER)
    return (minimum, maximum)


def weightGainIntact(dog_weight):
    """
    Range for weight gain for intact dogs
    """
    RER = calculateRER(dog_weight)
    minimum = math.ceil(1.8 * RER)
    maximum = math.ceil(2.0 * RER)
    return (minimum, maximum)


def lightWork(dog_weight):
    RER = calculateRER(dog_weight)
    return math.ceil(2.0 * RER)


def mediumWork(dog_weight):
    RER = calculateRER(dog_weight)
    return math.ceil(3.0 * RER)


def heavyWork(dog_weight):
    RER = calculateRER(dog_weight)
    return math.ceil(4.8 * RER)


def pregnantEarly(dog_weight):
    """
    This is for pregnant dogs during the first 42 days of pregnancy
    """
    RER = calculateRER(dog_weight)
    return math.ceil(1.8 * RER)


def pregnantLate(dog_weight):
    """
    This is for pregnant dogs during the last 21 days of pregnancy
    """
    RER = calculateRER(dog_weight)
    return math.ceil(3.0 * RER)


def lactatingFemale(dog_weight):
    RER = calculateRER(dog_weight)
    return math.ceil(4.8 * RER)


def weaningPuppy(dog_weight):
    """
    This is for puppies weaning - 4 months
    """
    RER = calculateRER(dog_weight)
    return math.ceil(3.0 * RER)


def latePuppies(dog_weight):
    """
    This is for puppies from 4 months to adult
    """
    RER = calculateRER(dog_weight)
    return math.ceil(2.0 * RER)
    
