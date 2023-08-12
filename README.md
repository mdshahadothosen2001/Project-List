**Project-List** <br>
pushes some project for learn concept and be friendly with this concepts.

#
 

## login_system:
>+ here login page and register page and home page
>+ see login page and register page before login
>+ register completed after login 
>+ then display home page otherwise login page
>+ don't see login page and register page after login

## customer_user_model:
>+ custom user model included some specific fields
>+ create user or superuser by phone number
>+ email and phone number are both unique
>+ phone number required exact 11 digit
>+ here login page and register page and home page
>+ see login page and register page before login
>+ register completed after login 
>+ then display home page otherwise login page
>+ don't see login page and register page after login


## custom_user_views:
>+ here login page and register page and home page
>+ including all from login_system
>+ permission roles based views
>+ making groups
>+ views work by checking user group name
>+ checking user group name if matched template statement do
>+ otherwise no result 


## one_time_passwords
>+ make customuser model using abstracbaseuser
>+ derived some from [custom_user_model]
>+ include some specific model fields
>+ using pyotp module
>+ make 60 seconds session
>+ after login , required otp as a input form
>+ display otp at terminal
>+ checking session time and otp
>+ if true render home page otherwise required valid otp



## view_versatility
>+ make two app (functionview, classview)
>+ functionview here make views using function based concept
>+ classview here make views using class based concept

## model_data_access
>+ make two app (accounts, tasks)
>+ accounts have made two view for display data from model
>+ tasks have 5 view (tasks_view, task_detail, task_update, task_delete)
>+ tasks_view display all tasks name as a list
>+ task_details display all data which want select by task id
>+ task_update modify data any specific task select by task id
>+ task_delete remove any specific task

## user_account_activation
>+ make custom user model using abstracbaseuser
>+ derived some from [custom_user_model]
>+ include some specific model fields
>+ make register and login page
>+ view home page required login

## form_versatility
>+ make form many way
>+ class based form
>+ function based form
>+ html based form
>+ use django default form

## jwt_authentication
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

## signal_middleware
>+ make app and model
>+ make a user view api for create new user or display user list
>+ used signal
>+ make signal function to send welcome message to user when user do registration
>+ used middleware
>+ print message when hit request api
>+ print message when return response api 