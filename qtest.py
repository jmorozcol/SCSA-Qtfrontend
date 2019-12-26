from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))

datetime = QDateTime.currentDateTime()

print(datetime.toString())
print('Universal datetime: ' + datetime.toUTC().toString(Qt.ISODate))

print("The offset from UTC is: {0} seconds".format(datetime.offsetFromUtc()))

time = QTime.currentTime()

print(time.toString(Qt.DefaultLocaleLongDate))