# Python-test
This repository contains source files related to python test

==========================================================================================

*** Login information ***
In order to login to to the following link: http://hassamhassan.pythonanywhere.com/admin/

login user: adam

login password: lawson123

==========================================================================================

*** In order to see API docs go to http://hassamhassan.pythonanywhere.com/docs/ ***

Note:
In the following call: POST => http://hassamhassan.pythonanywhere.com/json_rest_api/service_area/
The polygon must follow the following format: POLYGON ((lat lng, lat/lng, lat/lng, lat/lng, .......))
FOR EXAMPLE: POLYGON ((10.0 20, 10 15.8, 30 40.4, 50.9 60))

In order to get list of all polygons that include the given lat/lng use the following endpoint.
/json_rest_api/service_area/?polygon=lat/lng

FOR EXAMPLE:
http://hassamhassan.pythonanywhere.com/json_rest_api/service_area/?polygon=50.9/60

Keep the value of polygon in following format: lat/lng

==========================================================================================
*** Django Rest FrameWork Urls ***
Apart from API docs some DRF urls are also available from where we can preform CRUD
http://hassamhassan.pythonanywhere.com/json_rest_api/service_area/
http://hassamhassan.pythonanywhere.com/json_rest_api/provider/