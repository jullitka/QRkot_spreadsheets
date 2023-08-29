from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import User
from app.services.investing import investing
from app.schemas.donation import DonationDB, DonationCreate

router = APIRouter()

EXCLUDE_FOR_CURRENT_USER = ('user_id',
                            'invested_amount',
                            'fully_invested',
                            'close_date')


@router.post(
    '/',
    response_model=DonationDB,
    response_model_exclude_none=True,
    response_model_exclude={*EXCLUDE_FOR_CURRENT_USER}
)
async def create_new_donation(
    donation: DonationCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    new_donation = await donation_crud.create(donation, session, user)
    await investing(new_donation, session)
    await session.refresh(new_donation)
    return new_donation


@router.get(
    '/',
    response_model=List[DonationDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    all_donations = await donation_crud.get_multi(session)
    return all_donations


@router.get(
    '/my',
    response_model=List[DonationDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_user)],
    response_model_exclude={*EXCLUDE_FOR_CURRENT_USER}
)
async def get_all_donations_by_user(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    all_donations = await donation_crud.get_all_donations_by_user(user, session)
    return all_donations
