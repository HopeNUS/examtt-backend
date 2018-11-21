from .examttObject import ExamttObject
import operator


class ExamttCsv(ExamttObject):
    def __init__(self):
        self.csvs = []

    def add_entries(self, entries):
        for entry in entries:
            self.add_entry(entry)

    def add_entry(self, entry):
        slot = entry[self.INDEX_SLOT]
        day = self.format_day(slot.day)
        time = slot.time
        venue = entry[self.INDEX_VENUE]
        module = entry[self.INDEX_MODULE]
        student = entry[self.INDEX_STUDENT]
        self.csvs.append(
            (day, time, venue.name, module.code,
                student.name, student.lifegroup))

    def format_day(self, day):
        day = day[2:] + day[:2]
        day = day.replace("DEC", "12").replace("NOV", "11")
        return int(day)

    def unformat_day(self, day):
        day = str(day)
        date = day[2:]
        month = day[:2]
        month = "DEC" if month == "12" else "NOV"
        return date + month

    def make_row(self, day, time, venue, module, student, lifegroup):
        return '{}, {}, {}, {}, "{}", {}\n'.format(
            self.unformat_day(day), time, venue, module, student, lifegroup)

    def get_csv(self):
        csv = "date, time, venue, module, name, lifegroup\n"
        self.csvs.sort(key=operator.itemgetter(1, 2, 3))
        for row in self.csvs:
            csv = csv + self.make_row(*row)
        return csv
