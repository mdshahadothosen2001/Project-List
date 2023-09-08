**Project-List** <br>
pushes some project for learn concept and be friendly with this concepts.
#




#
## login_system:

**FUNCTIONS**
>+ here login page and register page and home page
>+ see login page and register page before login
>+ register completed after login
>+ then display home page otherwise login page
>+ don't see login page and register page after login

**USE**
>+ first register account (http://127.0.0.1:8000/accounts/register/)
>+ then login (http://127.0.0.1:8000/accounts/login/)
>+ can view home page (http://127.0.0.1:8000/accounts/home/)



#
## customer_user_model:

**FUNCTIONS**
>+ custom user model included some specific fields
>+ create user or superuser by phone number
>+ email and phone number are both unique
>+ phone number required exact 11 digit
>+ here login page and register page and home page
>+ see login page and register page before login
>+ register completed after login
>+ then display home page otherwise login page
>+ don't see login page and register page after login

**USE**
>+ first register account with this path (http://127.0.0.1:8000/accounts/register/)
>+ then login (http://127.0.0.1:8000/accounts/login/)
>+ can view (http://127.0.0.1:8000/accounts/home/)



#
## custom_user_views:

**FUNCTIONS**
>+ here login page and register page and home page
>+ including all from login_system
>+ permission roles based views
>+ making groups
>+ views work by checking user group name
>+ checking user group name if matched template statement do
>+ otherwise no result

**USE**
>+ first register (http://127.0.0.1:8000/accounts/register/)
>+ then login (http://127.0.0.1:8000/accounts/login/)
>+ user can view if permitted your group 'customer' (http://127.0.0.1:8000/accounts/home/)



#
## one_time_passwords

**FUNCTION**
>+ make customuser model using abstracbaseuser
>+ derived some from [custom_user_model]
>+ include some specific model fields
>+ using pyotp module
>+ make 60 seconds session
>+ after login , required otp as a input form
>+ display otp at terminal
>+ checking session time and otp
>+ if true render home page otherwise required valid otp
>+ soon wil build logic for one-time-password generator

**USE**
>+ first register account (http://127.0.0.1:8000/accounts/register/)
>+ then login (http://127.0.0.1:8000/accounts/login/)
>+ can view home page (http://127.0.0.1:8000/accounts/home/)



#
## view_versatility

**FUNCTION**
>+ make two app (functionview, classview)
>+ functionview here make views using function based concept
>+ classview here make views using class based concept

**USE**
>+ see 'Hello World with function based (http://127.0.0.1:8000/accounts/functionview/)
>+ see 'Hello World with class based (http://127.0.0.1:8000/accounts/classview/)



#
## model_data_access

**FUNCTION**
>+ make two app (accounts, tasks)
>+ accounts have made two view for display data from model
>+ tasks have 5 view (tasks_view, task_detail, task_update, task_delete)
>+ tasks_view display all tasks name as a list
>+ task_details display all data which want select by task id
>+ task_update modify data any specific task select by task id
>+ task_delete remove any specific task

**USE**
>+ see data from model function based (http://127.0.0.1:8000/accounts/data-view/)
>+ data view from class based (http://127.0.0.1:8000/accounts/data/)
>+ see data (http://127.0.0.1:8000/tasks/)



#
## user_account_activation

**FUNCTION**
>+ make custom user model using abstracbaseuser
>+ derived some from [custom_user_model]
>+ include some specific model fields
>+ make register and login page
>+ view home page required login

**USE**
>+ first register account (http://127.0.0.1:8000/accounts/register/)
>+ then login with phone number (http://127.0.0.1:8000/accounts/login/)
>+ can view home page (http://127.0.0.1:8000/accounts/home/)



#
## form_versatility

**FUNCTION**
>+ make form many way
>+ class based form
>+ function based form
>+ html based form
>+ use django default form

**USE**
>+ create car detail with some path
>for using diffrent way like function, class based and default
>+ create (http://127.0.0.1:8000/accounts/car-form/)
or (http://127.0.0.1:8000/accounts/car-form-feilds/)
or (http://127.0.0.1:8000/accounts/car_form_default/)
>+ see (http://127.0.0.1:8000/accounts/cars/)



#
## jwt_authentication

**FUNCTION**
>+ make custom user model
>+ make api for token
>+ use jwt authentication system
>+ make home view with permission
>+ authorization can by bearer token
>+ send otp to email
>+ set otp validation time
>+ token save in user request session
>+ can access token or payload data from anywhere
>+ change password just give new_password
>+ recover account password by email and first name

**USE**
>+ RESTFull API
>+ user can use postman app for API hit
>+ first register with data request and hit api
(http://127.0.0.1:8000/api/register/) method is POST and data
like
{"email":"test@gmail.com",
  "first_name":"test",
  "last_name":"test",
  "password":"test"
}
>+ then activate account with otp and API
 (http://127.0.0.1:8000/api/activate/) and method is PATCH and data
 like
{"email":"test@gmail.com",
"otp":9070}
>+ token for (http://127.0.0.1:8000/api/token/) method is POST and data
like
{"email":"test@gmail.com",
"password":"test"
}
>+ refresh token for (http://127.0.0.1:8000/api/token/refresh/) method is POST and data like
{"access":"....."}
>+ then need to login with token
(http://127.0.0.1:8000/api/home/) method is GET and give token at postman app auth -> bearer option
>+ for change password (http://127.0.0.1:8000/api/reset/) method is PATCH and with new password
 like
{"new_password":"......"}
>+ forgotten password (http://127.0.0.1:8000/api/recover/) method is PATCH and with data like
{"email":".......",
"first_name":"....."
}


#
## signal_middleware

**FUNCTION**
>+ make app and model
>+ make a user view api for create new user or display user list
>+ used signal
>+ make signal function to send welcome message to user when user do registration
>+ used middleware
>+ print message when hit request api
>+ print message when return response api

**USE**
>+ >+ RESTFull API
>+ user can use postman app for API hit
>+ see result at terminal before login
>+ and after login
>+ see result at terminal when user hit api (http://127.0.0.1:8000/accounts/user/) method is GET



#
## drf_portion

**FUNCTION**
>+ it's a drf concepts learn project
>+ one by one topic learn and implement
>+ push and learn new concepts

**USE**
>+ RESTFull API
>+ first login can use basic auth of postman
>+ see both at terminal or response used patch method and hit data request like {"Name":"Md. Shahadot Hosen"} with (http://127.0.0.1:8000/home/hello/)



#
## orm_portion

**FUNCTION**
>+ used for django orm concepts
>+ created model
>+ just register at admin panel which model created

**USE**
>+ see model field at (http://127.0.0.1:8000/admin/)



#
## production_order

**FUNCTIONS**
>+ django class based display data from model
>+ django templates and views
>+ user can order confirm from product list

**USAGE**
>+ go browser (http://127.0.0.1:8000/)
>+ first login, see product list
>+ have oder option, if need order just click



#
## production_order

**FUNCTIONS**
>+ used DRF and make APIs

**USE:**
>+ RESTFull API
>+ user can use postman app for API hit
>+ login for  (http://127.0.0.1:8000/base/home/) method is GET then select auth option then basic in postman app
>+ see product list (http://127.0.0.1:8000/base/) method is GET
>+ for generate order  (http://127.0.0.1:8000/base/order) method is POST and with request data product id
like
{ "products":[1,3]}



#
## dj_postgresql

**FUNCTION**
>+ used for clear to concept of postgresql database

**USE**
>+ run project use localhost server
>+ for see model go admin panel



#
## day_calculator

**FUNCTION**
>+ used DRF
>+ used for logic day calculation between two dates
>+ make view and APIs

**USE**
>+ RESTFull API
>+ user can use postman for API hit
>+ for calculate hit API (http://127.0.0.1:8000/) method is POST and give data request
like
{"first_date":"2023-08-08",
"last_date":"2023-09-09"
}



#
## name_picker

**FUNCTION**
>+ used for token login authentication with token wich given from another project
>+ used for make API
>+ user give some name list return random choichen name from these

**USE**
>+ user can logig with access token to select auth -> bearer
>+ API for authentication (http://127.0.0.1:8000/) GET
>+ for name pick hit API (http://127.0.0.1:8000/name-picker) method is POST
name list request like
{"names":["apple","banana","orange"]}
