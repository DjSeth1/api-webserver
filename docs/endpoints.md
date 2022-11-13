# Barbershop API Endpoint Docs

## Auth Routes:

### /auth/register

- Methods: POST
- Arguments: *None*
- Description: Registers/Create a new user in the database
- Authentication: *None*
- Headers-Authorization: *None*
- Request Body:

```json
{
	"email": "divijseth@gmail.com",
	"password": "Coderacademy1",
	"f_name": "Divij",
	"l_name": "Seth",
	"phone": "021432346"

}

```

• Response Body:

```json
{
	"email": "divijseth@gmail.com",
	"f_name": "Divij",
	"l_name": "Seth",
	"phone": "021432346"

}
```

• Email already exists

```json
{"error": "Email is already in use, please use another email address"}
```

### /auth/login

- Methods: POST
- Arguments: *None*
- Description: Login as a registered user
- Authentication: *None*
- Headers-Authorization: *None*
- Request Body:

```json
{
	"email": "divijseth@gmail.com",
	"password": "Coderacademy1",
}
```

- Response Body:
- Logs in successfully

```json
{
"email": "divijseth@gmail.com",
"token": hexadecimal token value generated
"is_admin": false
}
```

- Login unsucessful

```json
{
    "error": "Invalid email or password"
}
```

## Barber Routes

### /barber/all_barbers/

- Methods: GET
- Arguments: *None*
- Description: Check database for all Barbers
- Authentication: *None*
- Headers-Authorization: *None*
- Request Body:None
- Response Body:

```json
[
    {
        "id": 1,
        "f_name": "Byron",
        "l_name": "Hogan",
        "phone": "0214253543",
        "email": "byronhogan@gmail.com",
        "appointments": [
            {
                "id": 1,
                "time": "10:00",
                "service": {
                    "type": "Hair and Beard",
                    "price": 45
                },
                "user": {
                    "id": 2,
                    "f_name": "Aditya",
                    "l_name": "Arora",
                    "phone": "0245322134",
                    "email": "aditya@gmail.com"
                }
            }
        ],
        "is_admin": true,
        "time_slots": "{10:00,11:00,12:00,13:00,14:00,15:00,16:00,17:00,18:00,19:00}"
    }
]
```

### /barber/<int:id>/

- Methods: GET
- Arguments: id = 1
- Description: Check database for barber by id
- Authentication: *None*
- Headers-Authorization: *None*
- Request Body:None
- Response Body

```json
[
    {
        "id": 1,
        "f_name": "Byron",
        "l_name": "Hogan",
        "phone": "0214253543",
        "email": "byronhogan@gmail.com",
        "appointments": [
            {
                "id": 1,
                "time": "10:00",
                "service": {
                    "type": "Hair and Beard",
                    "price": 45
                },
                "user": {
                    "id": 2,
                    "f_name": "Aditya",
                    "l_name": "Arora",
                    "phone": "0245322134",
                    "email": "aditya@gmail.com"
                }
            }
        ],
        "is_admin": true,
        "time_slots": "{10:00,11:00,12:00,13:00,14:00,15:00,16:00,17:00,18:00,19:00}"
    }
]
```

- No ID Response

```
{
    "error": "Barber with id 2 does not exist"
}
```

## Service Routes

### /service/all_services

- Methods: GET
- Arguments: *None*
- Description: Check database for all services
- Authentication: jwt required.
- Headers-Authorization: Bearer Token
- Request Body:None
- Response Body:

```json
services{
{
	"id" : "1"
	"type": "Hair",
	"price": "30"
},

{ 
	"id" : "2"
	"type": "Hair and Beard",
	"price": 45
}

```

- Token Expired body

```json
{
    "msg": "Token has expired"
}
```

- No authorisation

```json
{
    "msg": "Missing Authorization Header"
}
```

### /service/<int:id>/

- Methods: GET
- Arguments: *None*
- Description: Check database for one service
- Authentication: jwt required.
- Headers-Authorization: Bearer Token
- Request Body:None
- Response Body:

```json
{
	"id" : "1"
	"type": "Hair",
	"price": "30"
},

```

- Error if wrong service id

```json
{
	"error":"Service with id 3 does not exist"
}
```

- Token Expired body

```json
{
    "msg": "Token has expired"
}
```

- No authorisation

```json
{
    "msg": "Missing Authorization Header"
}
```

## User Routes

### /users/all_users

- Methods: GET
- Arguments: *None*
- Description: Check database for all users
- Authentication: jwt required.
- Headers-Authorization: Bearer Token
- Request Body:None
- Response Body:
    
    ```json
    {
    	"id": "1"
    	"email": "divijseth@gmail.com",
    	"f_name": "Divij",
    	"l_name": "Seth",
    	"phone": "021432346",
    	"appointment": None
    }
    ```
    

- Token Expired body

```json
{
    "msg": "Token has expired"
}
```

- No authorisation

```json
{
    "msg": "Missing Authorization Header"
}
```

### /users/<int:id>/

- Methods: GET
- Arguments: int id
- Description: Check database for one user by id.
- Authentication: jwt required.
- Headers-Authorization: Bearer Token
- Request Body:None
- Response Body:
    
    ```json
    {
    	"id": "1"
    	"email": "divijseth@gmail.com",
    	"f_name": "Divij",
    	"l_name": "Seth",
    	"phone": "021432346",
    	"appointment": None
    }
    ```
    
- Response if no such user with that id
    
    ```json
    {"error": "there is no user with id 3."}
    ```
    
- Token Expired body

```json
{
    "msg": "Token has expired"
}
```

- No authorisation

```json
{
    "msg": "Missing Authorization Header"
}
```

### /users/<int:user_id>

- Methods: PUT, PATCH
- Arguments: user_id
- Description: update user with user id check.
- Authentication: jwt required.
- Headers-Authorization: Bearer Token
- Request Body:

```json
{
	"phone": "021454563"
}
```

- Response Body:
    
    ```json
    {	
    	"success": "You have updated your profile successfully",
      "user details": {
    		"id": "1",
    		"email": "divijseth@gmail.com",
    		"f_name": "Divij",
    		"l_name": "Seth",
    		"phone": "021454563",
    	}
    }
    ```
    
- error message
    
    ```json
    {"error": "User does not exist"}
    ```
    
- Token Expired body

```json
{
    "msg": "Token has expired"
}
```

- No authorisation

```json
{
    "msg": "Missing Authorization Header"
}
```

### /users/<int:user_id>

- Methods: DELETE
- Arguments: user_id
- Description: update user with user id check.
- Authentication: jwt required.
- Headers-Authorization: Bearer Token
- Request Body: None
- Request Response

```json
{
	"message": " Your records with name Divij Seth were successfully deleted!"
}
```

- No user with Id response

```json
{
	"error": "User not found with id 3"
}
```

## Appointment Routes

### /appointment/all_appointments

- Methods: GET
- Arguments: None
- Description: get all appointments
- Authentication: None
- Headers-Authorization: None
- Request Body: None
- Response body

```json
[
    {
        "id": 1,
        "time": "10:00",
        "barber": {
            "f_name": "Byron",
            "l_name": "Hogan"
        },
        "service": {
            "type": "Hair and Beard",
            "price": 45
        },
        "user": {
            "id": 2,
            "f_name": "Aditya",
            "l_name": "Arora"
        }
    }
]
```

- Error handler done via main and schema validators if anything else occurs.

### /appointment/create/<int:user_id>

- Methods: POST
- Arguments: user_id
- Description: create appointment
- Authentication: @jwt_required()
- Headers-Authorization: Bearer {Token} - get_jwt_identity()
- Request Body:

```json
{
	"user":Getsjwtidentity
	"time": "10:00",
	"barber": {
			"f_name" : "Byron",
			"l_name" : "Hogan"
	},
	"service": {
			"type": "Hair",
			"price": "30"
	}
}
```

- Request Response

```json
{
"success": "You have successfully created an appointment", "appointment": 
[
    {
        "id": 1,
        "time": "10:00",
        "barber": {
            "f_name": "Byron",
            "l_name": "Hogan"
        },
        "service": {
            "type": "Hair and Beard",
            "price": 45
        },
        "user": {
            "id": 2,
            "f_name": "Aditya",
            "l_name": "Arora"
        }
    }
]
}
```

- Error if user cannot be queried

```json
{
	"error": "This user does not exist"
}
```

### /appointment/user_appointment/<int:user_id>

- Methods: GET
- Arguments: user_id
- Description: view appointment by the user.
- Authentication: @jwt_required()
- Headers-Authorization: Bearer {Token} - get_jwt_identity()
- Request Body: None
- Response Body:

```json

[
    {
        "id": 1,
        "time": "10:00",
        "barber": {
            "f_name": "Byron",
            "l_name": "Hogan"
        },
        "service": {
            "type": "Hair and Beard",
            "price": 45
        },
       
    }
]
```

- If no appointment
    
    ```json
    {
    	"error": "This user does not have an appointment with id 3."
    }
    ```
    

### /appointment/<int:id>

- Methods: GET
- Arguments: id
- Description: view appointment by appointment id
- Authentication: @jwt_required()
- Headers-Authorization: Bearer {Token} - get_jwt_identity()
- Request Body: None
- Response Body:

```json
[
    {
        "id": 1,
        "time": "10:00",
        "barber": {
            "f_name": "Byron",
            "l_name": "Hogan"
        },
        "service": {
            "type": "Hair and Beard",
            "price": 45
        },
        "user": {
            "id": 2,
            "f_name": "Aditya",
            "l_name": "Arora"
        }
    }
]
```

- If no appointment with that id
- Response Body:

```json
{
	"error": "No such appointment with this id 4. "
} 
```

### /appointment/user_appointment/<int:user_id>

- Methods: POST, PATCH
- Arguments: user_id
- Description: update appointment
- Authentication: @jwt_required()
- Headers-Authorization: Bearer {Token} - get_jwt_identity()
- Request Body:

```json
{
	"time": "12:00"
	"service": {
		"type": "Hair and Beard",
		"price": "45"
	}
}
```

- Response Body:

```json
[
	{"success" : "You have updated your appointment successfully.", '
	"appointment details" :
    {
        "id": 1,
        "time": "12:00",
        "barber": {
            "f_name": "Byron",
            "l_name": "Hogan"
        },
        "service": {
            "type": "Hair and Beard",
            "price": 45
        }
		}
	}
]
```

- Error Body if no user ID
    
    ```json
    {
    	"error": "Appointment of user with id 5 does not exist"
    }
    ```
    

### /appointment/user_appointment/<int:user_id>

- Methods: DELETE
- Arguments: user_id
- Description: delete appointment of user by user
- Authentication: @jwt_required()
- Headers-Authorization: Bearer {Token} - get_jwt_identity()
- Request Body: None
- Response Body:

```json
{
	"success": "The appointment for user 2 were successfully deleted"
}
```

- Error response if no appointment for that user

```json
{
	"error": "The appointment for user 4 was not found"
}
```

## CLI Commands

- **flask db drop**
    - drop all tables in the database
- **flask db create**
    - create the table structures in the database
- **flask db seed**
    - seed the tables in the database with sample data