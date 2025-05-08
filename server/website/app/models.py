from flask import Markup, url_for
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import ImageColumn
from flask_appbuilder.filemanager import ImageManager
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, Float, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from . import db


class Base(Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    is_active = Column(Boolean, default=True)
    date_created = Column(Date, default=datetime.today().strftime("%Y-%m-%d"))
    date_updated = Column(
        Date,
        default=datetime.today().strftime("%Y-%m-%d"),
        onupdate=datetime.today().strftime("%Y-%m-%d"),
    )

    def save(self):
        db.session.add(self)
        db.session.commit()


class Genre(Base):
    name = Column(String(80), unique=True)

    books = relationship("Book", backref="genre", lazy="selectin")

    def __repr__(self):
        return self.name


class Book(Base):
    title = Column(String(100), unique=True, nullable=False)
    image = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    description = Column(Text)
    price = Column(Float, default=0.00)
    quantity = Column(Integer, default=1)

    genre_id = Column(Integer, ForeignKey(Genre.id), nullable=False, index=True)

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
