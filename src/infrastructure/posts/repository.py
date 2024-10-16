from typing import List

from pydantic import TypeAdapter

from src.core.sqlalchemy_database import async_session
from src.infrastructure.posts.exceptions import ObjectNotFoundException
from src.infrastructure.posts.models import Posts
from src.infrastructure.posts.schemas import SchemaPost, ShortSchemaPost
from sqlalchemy import update, delete, select


class PostRepository:
    model = Posts
    entity = SchemaPost

    @classmethod
    async def get_posts(cls) -> List[SchemaPost]:
        async with async_session() as session:
            stmt = select(cls.model)
            response = await session.scalars(statement=stmt)
            posts_type_adapter = TypeAdapter(List[SchemaPost])
            return posts_type_adapter.validate_python(
                response,
                from_attributes=True,
            )

    @classmethod
    async def create(cls, post: ShortSchemaPost) -> SchemaPost:
        async with async_session() as session:
            new_post = Posts(**post.model_dump())
            session.add(new_post)
            await session.commit()
            return cls.entity.model_validate(
                obj=new_post,
                from_attributes=True,
            )

    @classmethod
    async def update(cls, post_id: int, post: ShortSchemaPost) -> SchemaPost:
        async with async_session() as session:
            stmt = update(cls.model).where(
                cls.model.id == post_id
            ).values(**post.model_dump()).returning(cls.model)
            updated_post = await session.scalar(stmt)
            if not updated_post:
                raise ObjectNotFoundException
            await session.commit()
            return SchemaPost.model_validate(
                obj=updated_post,
                from_attributes=True,
            )

    @classmethod
    async def delete(cls, post_id: int) -> None:
        async with async_session() as session:
            stmt = delete(cls.model).where(
                cls.model.id == post_id
            ).returning(cls.model.id)
            result = await session.scalar(stmt)
            if not result:
                raise ObjectNotFoundException
            await session.commit()

    @classmethod
    async def increase_likes(cls, post_id: int) -> SchemaPost:
        async with async_session() as session:
            post = await session.get(entity=cls.model, ident=post_id)
            if not post:
                raise ObjectNotFoundException
            post.likes += 1
            await session.commit()
            return SchemaPost.model_validate(
                obj=post,
                from_attributes=True,
            )

    @classmethod
    async def decrease_likes(cls, post_id: int) -> SchemaPost:
        async with async_session() as session:
            post = await session.get(entity=cls.model, ident=post_id)
            if not post:
                raise ObjectNotFoundException
            if post.likes > 0:
                post.likes -= 1
            await session.commit()
            return SchemaPost.model_validate(
                obj=post,
                from_attributes=True,
            )







