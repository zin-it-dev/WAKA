import logging, os

from app import appbuilder, db
from app.models import Genre, Book
from app.utils import load_data
from config import basedir

log = logging.getLogger(__name__)

# Get role Admin
role_admin = appbuilder.sm.find_role(appbuilder.sm.auth_role_admin)
if role_admin is None:
    log.error("Error: please run 'flask fab create-admin' before loading data!")
    exit(1)


# Configuring role Staff
role_staff = appbuilder.sm.find_role("Staff")
if role_staff is None:
    appbuilder.sm.add_role("Staff")
    role_staff = appbuilder.sm.find_role("Staff")


for pv in role_admin.permissions:
    if "GenreRestApi" in pv.__repr__() or "BookRestApi" in pv.__repr__():
        appbuilder.sm.add_permission_role(role_staff, pv)
    if (
        "MyPassword" in pv.__repr__()
        or "mypassword" in pv.__repr__()
        or ("userinfo" in pv.__repr__() and "userinfoedit" not in pv.__repr__())
        or ("UserInfo" in pv.__repr__() and "UserInfoEdit" not in pv.__repr__())
    ):
        appbuilder.sm.add_permission_role(role_staff, pv)


# Configuring role Public
role_public = appbuilder.sm.find_role("Public")
if role_public is None:
    appbuilder.sm.add_role("Public")
    role_public = appbuilder.sm.find_role("Public")

for pv in role_admin.permissions:
    if ("GenreRestApi" in pv.__repr__() or "BookRestApi" in pv.__repr__()) and not (
        "add" in pv.__repr__()
        or "delete" in pv.__repr__()
        or "edit" in pv.__repr__()
        or "post" in pv.__repr__()
        or "show" in pv.__repr__()
        or "put" in pv.__repr__()
    ):
        appbuilder.sm.add_permission_role(role_public, pv)


# Configuring role User
role_user = appbuilder.sm.find_role("User")
if role_user is None:
    appbuilder.sm.add_role("User")
    role_user = appbuilder.sm.find_role("User")

for pv in role_admin.permissions:
    if ("GenreRestApi" in pv.__repr__() or "BookRestApi" in pv.__repr__()) and not (
        "add" in pv.__repr__()
        or "delete" in pv.__repr__()
        or "edit" in pv.__repr__()
        or "post" in pv.__repr__()
        or "show" in pv.__repr__()
        or "put" in pv.__repr__()
    ):
        appbuilder.sm.add_permission_role(role_user, pv)
    if (
        "MyPassword" in pv.__repr__()
        or "mypassword" in pv.__repr__()
        or ("userinfo" in pv.__repr__() and "userinfoedit" not in pv.__repr__())
        or ("UserInfo" in pv.__repr__() and "UserInfoEdit" not in pv.__repr__())
    ):
        appbuilder.sm.add_permission_role(role_user, pv)


staff = appbuilder.sm.add_user(
    username="sj",
    first_name="Steve",
    last_name="Johnson",
    email="steve.johnson@aol.com",
    role=role_staff,
    password="123",
)
user = appbuilder.sm.add_user(
    username="js",
    first_name="Jay",
    last_name="Smith",
    email="jay.smith@aol.com",
    role=role_user,
    password="123",
)


try:
    genres = load_data(os.path.join(basedir, "database", "genres.json"))
    books = load_data(os.path.join(basedir, "database", "books.json"))

    for genre in genres:
        item = Genre(
            name=genre["name"],
            created_by=staff,
            changed_by=staff,
        )
        db.session.add(item)

    for book in books:
        item = Book(
            title=book["title"],
            price=book["price"],
            genre_id=book["genre_id"],
            created_by=staff,
            changed_by=staff,
        )
        db.session.add(item)

    db.session.commit()
    log.info("Seeding successfully !!!")
except Exception as e:
    log.error("Genre creation error: %s", e)
    db.session.rollback()
    exit(1)
