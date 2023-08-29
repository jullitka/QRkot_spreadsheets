from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        """Получить id проекта по его имени"""
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalars().first()
        return db_project_id

    async def get_project_invested_amount(
        self,
        project_id: int,
        session: AsyncSession
    ) -> Optional[int]:
        """Получить сумму, уже инвестированную в проект"""
        invested_amount = await session.execute(
            select(CharityProject.invested_amount).where(
                CharityProject.id == project_id
            )
        )
        return invested_amount.scalars().first()

    async def get_project_fully_invested(
        self,
        project_id: int,
        session: AsyncSession,
    ) -> bool:
        """Определить закрыт проект или нет"""
        fully_invested = await session.execute(
            select(CharityProject.fully_invested).where(
                CharityProject.id == project_id
            )
        )
        return fully_invested.scalars().first()

    async def get_projects_by_completion_rate(
        self,
        session: AsyncSession
    ) -> List[dict]:
        closed_projects = await session.execute(
            select(
                CharityProject.name,
                CharityProject.create_date,
                CharityProject.close_date,
                CharityProject.description
            ).where(CharityProject.fully_invested)
        )
        return closed_projects.scalars().all()

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession
    ) -> list[dict]:
        closed_projects = await session.execute(
            select(
                CharityProject.name, CharityProject.close_date,
                CharityProject.create_date,
                CharityProject.description).where(
                    CharityProject.fully_invested))
        closed_projects_list = []
        for project in closed_projects:
            closed_projects_list.append({
                'name': project.name,
                'description': project.description,
                'delta': project.close_date - project.create_date
            })
        return sorted(closed_projects_list, key=lambda x: x['delta'])


charity_project_crud = CRUDCharityProject(CharityProject)
