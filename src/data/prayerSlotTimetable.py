class PrayerSlotTimetable(object):
    prayerSlots = []
    prayerSlotsWrrior = []

    def addPrayerSlot(self, id, meetingPoint, date, time):
        self.prayerSlots.append({id, meetingPoint, date, time, })

    def prayerSlotsWrrior(self, prayerSlotId, warriorName):
        self.students.append((prayerSlotId, warriorName, ))

    def serialise(self):
        return {self.prayerSlots, self.prayerSlotsWrrior}
