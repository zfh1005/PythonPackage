import datetime

class IncidentError(Exception):
    pass

class Incident:
    def __init__(self, report_id, date, airport, aircraft_id,
                 aircragt_type, pilot_percent_hours_on_type,
                 pilot_total_hours, midair, narrative = ""):
        assert len(report_id) >= 8 and len(report_id.split()) == 1, "invalid report ID"
        self.__report_id = report_id
        self.date = date
        self.airport = airport
        self.aircraft_id = aircraft_id
        self.aircragt_type = aircragt_type
        self.pilot_percent_hours_on_type = pilot_percent_hours_on_type
        self.pilot_total_hours = pilot_total_hours
        self.midair = midair
        self.narrative = narrative

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date):
        assert isinstance(date, datetime.date), "invalid date"
        self.__date = date

    @property
    def airport(self):
        return self.airport
    @airport.setter
    def airport(self, airport):
        assert airport is not None, "invalid airport"
        self.airport = airport

    @property
    def aircraft_id(self):
        return self.aircraft_id
    @aircraft_id.setter
    def aircraft_id(self, aircraft_id):
        assert aircraft_id is not None, "invalid aircraft_id"
        self.aircraft_id = aircraft_id

    @property
    def aircragt_type(self):
        return self.aircragt_type
    @aircragt_type.setter
    def aircragt_type(self, aircragt_type):
        assert aircragt_type is not None, "invalid aircragt_type"
        self.aircragt_type = aircragt_type

    @property
    def pilot_percent_hours_on_type(self):
        return self.pilot_percent_hours_on_type
    @pilot_percent_hours_on_type.setter
    def pilot_percent_hours_on_type(self, pilot_percent_hours_on_type):
        assert pilot_percent_hours_on_type in range(0, 100), "invalid pilot_percent_hours_on_type"
        self.pilot_percent_hours_on_type = pilot_percent_hours_on_type
  
    @property
    def pilot_total_hours(self):
        return self.pilot_total_hours
    @pilot_total_hours.setter
    def pilot_total_hours(self, pilot_total_hours):
        assert pilot_total_hours > 0, "invalid pilot_total_hours"
        self.pilot_total_hours = pilot_total_hours

    @property
    def midair(self):
        return self.midair
    @midair.setter
    def midair(self, midair):
        assert midair in [False, True], "invalid midair"
        self.midair = midair

    @property
    def narrative(self):
        return self.narrative
    @narrative.setter
    def narrative(self, narrative):
        assert narrative is not None, "invalid narrative"
        self.narrative = narrative

        
