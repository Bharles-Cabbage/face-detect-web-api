## Face Detect API

This project uses [Face_Recognition](https://github.com/ageitgey/face_recognition) API for all the image processing.

- - -

#### Start server
`python manage.py runserver`
OR
`gunicorn ProcessImage.wsgi`

*Note: This app requires you to store a secret key in `PI_SECRET` environmental variable.*
- - -
#### Endpoints
|   Path    |   Method  |   Parameters  |              Purpose                  |                             Values                                  |
|   ----    |   ------  |   ---------   |              -------                  |                             ------                                  |
| /imageurl |   POST    |   image       |   Use image from a remote location    |   URL (eg. https://www.dmarge.com/wp-content/uploads/2019/05/keanu-ysl-suit.jpg)    |
| /image    |   POST    |   image       |   Upload image from local storage     |   image (i.e \*.jpg, \*.png, \*.jpeg, etc.)                         |

Requests can be sent in either JSON or form formats.

#### Return Values
|      **Key**    |     **Type**      |    **Explanation/Solution** |
|-----------------|-------------------|-----------------------------|
|   face_location | Nested Int Array  |  Box in which the face(s) |
|        err       |      String       |  Error if HTTP Method POST not used. Use POST to resolve this error. |
| Bad Request(400) |      String       | Check the URL and keys being sent in the POST request (eg.`image_url`) |
| Server Error(500)| HTTP Response/String | Check if image URL being sent is valid. Try using other images' URL to test. Contact if still not resolved. |
 

- - -
###### Todo:
* [x] Detect face via image's url
* [x] Detect face from uploded image
* [ ] Live video stream face detection
