import cloudinary.uploader


def upload_image(file_data):
    result = cloudinary.uploader.upload(file_data)
    return result.get("secure_url")
