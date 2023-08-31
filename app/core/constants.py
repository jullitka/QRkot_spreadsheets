FORMAT = "%Y/%m/%d %H:%M:%S"
ROW_COUNT = 100
COLUMN_COUNT = 11

RANGE = 'R1C1:R{row}C{col}'

SPREADSHEET_BODY = dict(
    properties=dict(
        title='Отчет на',
        locale='ru_RU'
    ),
    sheets=[dict(properties=dict(
        sheetType='GRID',
        sheetId=0,
        title='Лист1',
        gridProperties=dict(rowCount=ROW_COUNT,
                            columnCount=COLUMN_COUNT)))]
)