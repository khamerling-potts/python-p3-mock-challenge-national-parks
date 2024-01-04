# National parks            Visitors
#                   Trips


class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, "name") and isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception("national park name must be a str more than 3 chars long")

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max(set(visitors), key=visitors.count)
        # for trip in self.trips():
        #     if trip.visitor in visitors:
        #         visitors[trip.visitor] += 1
        #     else:
        #         visitors[trip.visitor] = 0
        # return max(visitors, key=lambda visitor: visitors[visitor])
        # # or use key=visitors.get
        # # for each visitor, find the value of visitors[visitor] and use max of that
        # # visitor => visitors.get(visitor)


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
        else:
            raise Exception("start date must be a string at least 7 chars long")

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
        else:
            raise Exception("end date must be a string at least 7 chars long")

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception("visitor must be a Visitor")

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception("national park must be a NationalPark")


class Visitor:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    # getter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("visitor name must be a string between 1-15 chars long")

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})

    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])
