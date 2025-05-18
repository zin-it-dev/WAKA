import cloudinary.uploader, json

from hashlib import sha256
from urllib.parse import urlencode


def gravatar_url(email, size=40, default="identicon"):
    digest = sha256(email.lower().encode("utf-8")).hexdigest()
    params = urlencode({"d": default, "s": str(size)})
    return f"https://www.gravatar.com/avatar/{digest}?{params}"


def upload_image(file_data):
    result = cloudinary.uploader.upload(file_data, folder="media")
    return result.get("secure_url")


def load_data(path_name: str):
    with open(path_name, "r", encoding="utf-8") as file:
        return json.load(file)
