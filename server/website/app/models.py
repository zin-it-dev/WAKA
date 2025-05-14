from flask import Markup
from flask_appbuilder import Model
from flask_appbuilder.security.sqla.models import User as FABUser
from flask_appbuilder.models.mixins import ImageColumn
from flask_appbuilder.filemanager import ImageManager
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, Float, Text, Table
from sqlalchemy.orm import relationship
from datetime import date


class Base(Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, default=True)
    date_created = Column(Date, default=date.today)
    date_updated = Column(Date, default=date.today, onupdate=date.today)


class User(FABUser):
    __tablename__ = "ab_user"

    avatar = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

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


class Book(Base):
    title = Column(String(100), unique=True, nullable=False)
    image = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    description = Column(Text)
    price = Column(Float, default=0.00)
    quantity = Column(Integer, default=1)

    genre_id = Column(Integer, ForeignKey(Genre.id), nullable=False)
    genre = relationship("Genre")
    tags = relationship("Tag", secondary=book_tag, backref="book", info={"required": True})

    def photo_image(self):
        im = ImageManager()
        if self.image:
            return Markup(
                f"<img src='{im.get_url(self.image)}' alt='{self.title}' class='img-thumbnail img-rounded img-responsive' />"
            )
        else:
            return Markup(
                f"<img src='//:0' alt='{self.title}'  class='img-thumbnail img-responsive' />"
            )

    def photo_image_thumbnail(self):
        im = ImageManager()
        if self.image:
            return Markup(
                f'<img src="{im.get_url_thumbnail(self.image)}" alt="{self.title}" class="img-thumbnail img-rounded img-responsive" />'
            )
        else:
            return Markup(f'<img src="//:0" alt="{self.title}" class="img-responsive" />')

    def __repr__(self):
        return self.title
