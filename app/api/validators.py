from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.constants import COLUMN_COUNT, ROW_COUNT
from app.crud.charity_project import charity_project_crud
from app.models import CharityProject


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    """Проверка существоания в базе проекта с именем project_name"""
    project_id = await charity_project_crud.get_obj_id_by_name(project_name, session)
    if project_id is not None:
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!'
        )


async def check_full_amount(
        project_id: int,
        new_amount: int,
        session: AsyncSession,
) -> None:
    """Проверка того, что новая сумма проекта не меньше уже установленной"""
    invested_amount = await charity_project_crud.get_project_invested_amount(
        project_id, session
    )
    if invested_amount > new_amount:
        raise HTTPException(
            status_code=422,
            detail='Сумма не может быть меньше уже установленной!'
        )


async def check_charity_project_exists(
        project_id: int,
        session: AsyncSession,
) -> CharityProject:
    """Проверка существования проекта в базе по id"""
    charity_project = await charity_project_crud.get(
        project_id, session
    )
    if charity_project is None:
        raise HTTPException(
            status_code=404,
            detail='Проект не найден!'
        )
    return charity_project


async def check_project_invested(
    project_id: int,
    session: AsyncSession
) -> None:
    """Проверка того, инвестированы ли уже в проект средства.
    Если да, то проект нельзя удалить"""
    invested_amount = await charity_project_crud.get_project_invested_amount(
        project_id, session
    )

    if invested_amount:
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!',
        )


async def check_project_closed(
    project_id: int,
    session: AsyncSession,
) -> None:
    """Проверка, является ли проект закрытым.
    Если да, то его нельзя редактировать"""
    project_closed = await charity_project_crud.get_project_fully_invested(
        project_id, session
    )
    if project_closed:
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!',
        )


async def check_size_table(
    row_count: int,
    column_count: int,
) -> None:
    """Проверка, соответствует ли количество необходимыз строк и столбцов
    установленным в таблице"""
    if row_count > ROW_COUNT or column_count > COLUMN_COUNT:
        raise HTTPException(
            status_code=400,
            detail='Данные не соответствуют размеру таблицы. '
                   f'Сформировано: {row_count} строк(и). Допустимое значение: {ROW_COUNT} строк(и) '
                   f'Сформировано: {column_count} столбца(ов). Допустимое значение: {COLUMN_COUNT} столбца(ов)')
