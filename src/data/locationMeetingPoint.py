class LocationMeetingPoint(object):
    locations = []
    meetingPoints = []

    def addMeetingPoint(self, meetingPoint):
        self.prayerSlots.append(meetingPoint)

    def prayerSlotsWrrior(self, location, meetingPoint=None):
        self.students.append({location, meetingPoint, })

    def serialise(self):
        return {self.locations, self.meetingPoints}
