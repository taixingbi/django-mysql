from .models import Timeslot

import json


class TimeslotSerializer():

    def toList():#list of object
        data = list( Timeslot.objects.filter().values() )
        print(data)

        return data


