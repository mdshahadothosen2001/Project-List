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