import json


class PrayerSlotTimetable(object):
    prayerSlots = []
    prayerSlotsWrriors = []

    def addPrayerSlot(self, id, location, meetingPoint, date, time):
        self.prayerSlots.append({
            'id': id,
            'location': location,
            'meetingPoint': meetingPoint,
            'date': date,
            'time': time,
        })

    def prayerSlotsWrrior(self, prayerSlotId, warriorName):
        self.prayerSlotsWrriors.append((prayerSlotId, warriorName, ))

    def serialise(self):
        return json.dumps(
            {"prayerSlots": self.prayerSlots,
                "prayerSlotsWarriors": self.prayerSlotsWrriors},
            sort_keys=True, indent=4)
