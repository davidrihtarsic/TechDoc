cells = ["A", "B", "C", "D", "E"]
widths = [70, 270, 145, 150, 62]
names = ["POZ.", "NAZIV KOSA", "MERE", "MATERIAL", "ŠT. KOSOV" ]
for i in range(len(cells)):
    App.ActiveDocument.Spreadsheet.setColumnWidth(cells[i], widths[i])
    App.ActiveDocument.Spreadsheet.set(cells[i]+"1", names[i])
    App.ActiveDocument.Spreadsheet.setAlignment(cells[i]+"1", 'center', 'keep')

App.ActiveDocument.recompute()


