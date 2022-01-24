# Bug_tool

the application accepts json body for all the post, get, put and delete requests and responses with json.

-----------BUGS-------------------
-to create a bug send post request with required fields to http://127.0.0.1:8000/bug/
-to get all the bugs send get request to --> http://127.0.0.1:8000/bug/
-to get a certain bug send get request with id to --> http://127.0.0.1:8000/bug/id/
-to get a bugs with certain status send get request with query params --> http://127.0.0.1:8000/bug/?status=1
-to update a bug send put request with bug id and fields that need to be updated to http://127.0.0.1:8000/bug/id/
-to delete a bug send delete request with bug id to http://127.0.0.1:8000/bug/id/

------------COMMENTS----------

-to create a comment send post request with required fields to http://127.0.0.1:8000/comment/
-to delete a comment send delete request with bug id to http://127.0.0.1:8000/comment/id/


Tech Stack is Python 3.8.8

asgiref==3.5.0
Django==3.1.3
djangorestframework==3.12.3
pytz==2021.3
sqlparse==0.4.2
