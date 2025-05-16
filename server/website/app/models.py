import enum

from flask import Markup
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import ImageColumn
from flask_appbuilder.filemanager import ImageManager
from flask_appbuilder.security.sqla.models import User as FABUser
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
    Float,
    Text,
    Table,
    Enum,
    DateTime,
)
from sqlalchemy.orm import relationship
from datetime import datetime

from .utils import gravatar_url


class Base(Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=lambda: datetime.now(), nullable=True)


class User(FABUser):
    __tablename__ = "ab_user"

    avatar = Column(
        String(255),
        default=gravatar_url(email="anonymous@gmail.com"),
    )

    def avatar_image(self):
        return Markup(
            f"<img src='{self.avatar}' alt='{self.username}' class='img-thumbnail img-rounded img-responsive' width='40' height='40' />"
        )

    def __repr__(self):
        return self.username


class Genre(Base):
    name = Column(String(80), unique=True)

    def __repr__(self):
        return self.name


class Tag(Base):
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"#{self.name}"


book_tag = Table(
    "book_tag",
    Model.metadata,
    Column("book_id", Integer, ForeignKey("book.id"), nullable=True),
    Column("tag_id", Integer, ForeignKey(Tag.id), nullable=True),
)


class BookType(enum.Enum):
    HARDCOVER = "Hardcover"
    PAPERBACK = "Paperback"
    EBOOK = "Ebook"


class Book(Base):
    title = Column(String(100), unique=True, nullable=False)
    image = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)), nullable=True)
    description = Column(Text)
    price = Column(Float, default=0.00)
    quantity = Column(Integer, default=1)
    type = Column(
        Enum(BookType),
        default=BookType.EBOOK,
        nullable=False,
        info={"marshmallow_enum": {"by_value": False}},
    )

    genre_id = Column(Integer, ForeignKey(Genre.id), nullable=False)
    genre = relationship("Genre")
    tags = relationship("Tag", secondary=book_tag, backref="book", info={"required": True})

    def thumbnail(self):
        return ImageManager().get_url(self.image) if self.image else "https://placehold.co/300"

    def photo_image(self):
        url = ImageManager().get_url(self.image) if self.image else "https://placehold.co/300"
        return Markup(
            f'<img src="{url}" alt="{self.title}" class="img-thumbnail img-rounded img-responsive" />'
        )

    def photo_image_thumbnail(self):
        url = (
            ImageManager().get_url_thumbnail(self.image)
            if self.image
            else "https://placehold.co/30"
        )
        return Markup(
            f'<img src="{url}" alt="{self.title}" class="img-thumbnail img-rounded img-responsive"/>'
        )

    def __repr__(self):
        return self.title
