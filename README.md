## Face Detect API

This project uses [Face_Recognition](https://github.com/ageitgey/face_recognition) API for all the image processing.

- - -
#### Start server
_Generate a `secret` and store it in an environment variable `PI_SECRECT`._

`python manage.py runserver`
OR
`gunicorn ProcessImage.wsgi`

- - -
#### Endpoints
`http://your_domain/processimage`

Send JSON with the format `{'image_url': 'https://example.foo/image.jpg'}` as a `POST` request on `/processimage`.

#### Return Values
|      **Key**    |     **Type**      |    **Explanation/Solution** |
|-----------------|-------------------|-----------------------------|
|   face_location | Nested Int Array  |  Box in which the face(s) |
|        err       |      String       |  Error if HTTP Method POST not used. Use POST to resolve this error. |
| Bad Request(400) |      String       | Check the URL and keys being sent in the POST request (eg.`image_url`) |
| Server Error(500)| HTTP Response/String | Check if image URL being sent is valid. Try using other images' URL to test. Contact if still not resolved. |
 


