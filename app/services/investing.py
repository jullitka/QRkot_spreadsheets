from datetime import datetime
from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.donation import donation_crud
from app.crud.charity_project import charity_project_crud
from app.models import CharityProject, Donation


async def close_invested_object(
    obj: Union[CharityProject, Donation],
) -> None:
    obj.fully_invested = True
    obj.close_date = datetime.now()


async def investing(
    obj_in: Union[CharityProject, Donation],
    session: AsyncSession
):
    amount = obj_in.full_amount
    if isinstance(obj_in, Donation):
        open_objects = await charity_project_crud.get_open_objects(session)
    else:
        open_objects = await donation_crud.get_open_objects(session)
    if open_objects:
        for open_object in open_objects:
            need_amount = open_object.full_amount - open_object.invested_amount
            if need_amount < amount:
                to_invest = need_amount
            else:
                to_invest = amount
            open_object.invested_amount += to_invest
            obj_in.invested_amount += to_invest
            amount -= to_invest
            if open_object.invested_amount == open_object.full_amount:
                await close_invested_object(open_object)
            if not amount:
                await close_invested_object(obj_in)
                break
        await session.commit()
    return obj_in
