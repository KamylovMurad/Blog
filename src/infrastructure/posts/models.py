from datetime import datetime
from sqlalchemy import DateTime, func
from sqlalchemy.orm import mapped_column, Mapped
from src.core.sqlalchemy_database import Model


class Posts(Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    theme: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    body: Mapped[str] = mapped_column(nullable=False)
    likes: Mapped[int] = mapped_column(default=0)
    publication_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
