from copy import deepcopy
from datetime import datetime
from typing import List

from aiogoogle import Aiogoogle

from app.core.config import settings


FORMAT = "%Y/%m/%d %H:%M:%S"
ROW_COUNT = 100
COLUMN_COUNT = 11

RANGE = 'R1C1:R{row}C{col}'


def now_date(format=FORMAT):
    return datetime.now().strftime(format)


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


async def spreadsheets_create(
        wrapper_services: Aiogoogle,
        spreadsheet_body=deepcopy(SPREADSHEET_BODY)
) -> str:
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body['properties']['title'] += now_date()
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheet_id = response['spreadsheetId']
    return spreadsheet_id


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = dict(type='user',
                            role='writer',
                            emailAddress=settings.email)
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheet_id: str,
        projects: List[dict],
        wrapper_services: Aiogoogle
) -> None:
    service = await wrapper_services.discover('sheets', 'v4')
    table_values = [
        ['Отчет от', now_date()],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание'],
        *[[str(project['name']), str(project['delta']),
           str(project['description'])] for project in projects]
    ]
    row_count = len(table_values)
    column_count = max(map(len, table_values))
    if row_count > ROW_COUNT or column_count > COLUMN_COUNT:
        raise ValueError('Данные не соответствуют размеру таблицы.'
                         f'Сформировано: {row_count}. Допустимое значение:{ROW_COUNT}'
                         f'Сформировано: {column_count}. Допустимое значение:{COLUMN_COUNT}')
    update_body = dict(majorDimension='ROWS',
                       values=table_values)
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=RANGE.format(row=row_count, col=column_count),
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
