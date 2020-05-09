# By: Gerges Wageh #
# 9 - 5 - 2020 #
def show_segments_table(self, pro_segment):
    values = []
    for value in pro_segment.values():
        values.append(value)
    output = {}
    for i in range(len(values)):
        output.setdefault(values[i][0], []).append(values[i][1])
    processes = []
    segments = []
    for key in output.keys():
        processes.append(key)
    for value in output.values():
        segments.append(value)
    for i in range(len(processes)):
        temp = ''
        self.tableWidget.setRowCount(i)  # take care of the table name you are dealing with
        self.tableWidget.insertRow(i)
        self.tableWidget.setItem(i, 0, QTableWidgetItem(processes[i]))
        self.tableWidget.setItem(i, 1, QTableWidgetItem(str(len(segments[i]))))
        for segment in segments[i]:
            temp += segment + '\n'
        self.tableWidget.setItem(i, 2, QTableWidgetItem(temp))
        self.tableWidget.resizeRowsToContents()