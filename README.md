# AccuKnox-Project


> First version Deployment to be done on Shahil Khan 
> jun 3 - 2024


### Activating the virtual environment
The virtual environment in created as .venv
activate that by running the following command :
```
source  venv/bin/activate
```

or delete the .env file and recreate again

```
python3 -m venv .env
```
And then activate it again

### Installing dependencies

The requirements.txt file is added to this repo 
run it by running this :

```
pip install -r requirements.txt
```
### Migrations

```
python manage.py makemigrations 
python manage.py migrate 

```


### Create SuperUser
```
python manage.py createsuperuser 
```

## Adding Sample Data for Test Purposes
Adding  sample users
```
python3 manage.py load_user               
```




## API Reference

#### POST An User

```http
  POST /auth/users/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your username |
| `password` | `string` | **Required**. Your password |
| `email` | `string` | **Required**. Your email |
| `first_name` | `string` | Your first_name |
| `last_name` | `string` |  Your last_name |


![App Screenshot](https://github.com/shahilkk/AccuKnox-Project/blob/main/Scrnshot/Screenshot%202024-06-04%20at%208.28.31%E2%80%AFPM.png?raw=true)
#### Authentication

```http
  POST /token/
```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. Username|
| `password`      | `string` | **Required**. password |

![App Screenshot](https://github.com/shahilkk/AccuKnox-Project/blob/main/Scrnshot/Screenshot%202024-06-04%20at%206.31.38%E2%80%AFPM.png?raw=true)

To authenticate, add the following to the header:

Key: Authorization

Value: JWT {access token obtained from token generation}






#### Search User


```http
  GET /api/v1/user/search/?search={value}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `search` | `string` | **Required**. Can be Name ,Username or Email |

![App Screenshot](https://github.com/shahilkk/AccuKnox-Project/blob/main/Scrnshot/Screenshot%202024-06-04%20at%207.53.28%E2%80%AFPM.png?raw=true)

#### Friend Request

```http
  POST /api/v1/user/friend-request/

```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `to_user`      | `int` | **Required**. UserID |



![App Screenshot](https://github.com/shahilkk/AccuKnox-Project/blob/main/Scrnshot/Screenshot%202024-06-04%20at%208.02.24%E2%80%AFPM.png?raw=true)

#### Friend Request pending

```http
  GET /api/v1/user/friend-requests/pending/

```




![App Screenshot](https://github.com/shahilkk/AccuKnox-Project/blob/main/Scrnshot/Screenshot%202024-06-04%20at%207.53.40%E2%80%AFPM.png?raw=true)

#### Friend Request Action

```http
  PATCH /api/v1/user/friend-request/{id}

```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `status`      | `string` | **Required**. accepted or rejected |



![App Screenshot](https://github.com/shahilkk/AccuKnox-Project/blob/main/Scrnshot/Screenshot%202024-06-04%20at%207.53.48%E2%80%AFPM.png?raw=true)


#### Friend List

```http
  GET /api/v1/user/friends

```


![App Screenshot](https://github.com/shahilkk/AccuKnox-Project/blob/main/Scrnshot/Screenshot%202024-06-04%20at%207.54.46%E2%80%AFPM.png?raw=true)


#### Profile Updation

```http
  GET & POST /api/v1/user/profile/


```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `bio`      | `string` | your bio |
| `location`      | `string` | your location |
| `profile_picture`      | `image` | your image |

Users can update their profile with their location to enable location-based features and services by leveraging the latitude and longitude coordinates obtained through the Location API.


![App Screenshot](https://github.com/shahilkk/AccuKnox-Project/blob/main/Scrnshot/Screenshot%202024-06-04%20at%207.55.14%E2%80%AFPM.png?raw=true)

#### Post Creation

```http
   POST /api/v1/section/posts/

```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user`      | `int` | **Required**. UserID |
| `content`      | `string` | **Required**. content of the post |



![App Screenshot](https://github.com/shahilkk/AccuKnox-Project/blob/main/Scrnshot/Screenshot%202024-06-04%20at%207.55.38%E2%80%AFPM.png?raw=true)

#### Comment Creation

```http
   POST /api/v1/section/comments/

```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user`      | `int` | **Required**. UserID |
| `post`      | `int` | **Required**. POSTID |
| `content`      | `string` | **Required**. content of the post |



![App Screenshot](https://github.com/shahilkk/AccuKnox-Project/blob/main/Scrnshot/Screenshot%202024-06-04%20at%207.55.46%E2%80%AFPM.png?raw=true)



#### Post Like

```http
   POST /api/v1/section/posts/{id}/like/

```

![App Screenshot](https://github.com/shahilkk/AccuKnox-Project/blob/main/Scrnshot/Screenshot%202024-06-04%20at%207.56.37%E2%80%AFPM.png?raw=true)


#### Get Post Detailed

```http
   GET /api/v1/section/posts/

```

![App Screenshot](https://github.com/shahilkk/AccuKnox-Project/blob/main/Scrnshot/Screenshot%202024-06-04%20at%207.56.10%E2%80%AFPM.png?raw=true)

## Database Diagram

![App Screenshot](https://github.com/shahilkk/AccuKnox-Project/blob/main/Scrnshot/AccuKnox%20Project.png?raw=true)



## Authors

- [@shahilkhan](https://github.com/shahilkk)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://shahilkhan.com/)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shahil-khan-192b6a231/)



## Support

For support, email shahilhanarimbra@gmail.com

