# TASKS API

## Modo desarrollo
Para correr el proyecto en modo desarrollo se debe clonar el repositorio:

```sh
git clone git@github.com/the-vladman/tasks-api.git
```
### Con virtualenv
```sh
cd tasks-api
python3 -m venv myvenv
source venv/bin/activate

python manage.py migrate
python manage.py runserver
```

### Con Docker Compose:
```sh
docker-compose up
```

## TASKS API
```
URL: /api/tasks
```

### ADD TASK
URL: `/api/tasks`

METHOD: `POST`

BODY REQUEST:
```json
{
    "description": "A task",  (String | Required)
    "estimated_duration": 30, (Int | Required)
}
```

RESPONSE:

STATUS_CODE=201 Success
```json
{
    "id": 3,
    "description": "A task",
    "estimated_duration": 30,
    "completed_duration": null,
    "status": 0
}

```

STATUS_CODE=400 Bad Request
```json
{
    "description": [
        "This field may not be blank."
    ],
    "estimated_duration": [
        "This field may not be null."
    ],
    "status": [
        "This field may not be null."
    ]
}
```


### GET TASKS
URL: `/api/tasks`

METHOD: `GET`

RESPONSE:

STATUS_CODE=200 OK
```json
[
    {
        "id": 3,
        "description": "A task",
        "estimated_duration": 30,
        "completed_duration": null,
        "status": 0
    }
]

```

#### Filter & Search
by query params

Filter by status 
```
status:[
    `0`: `PENDING`,
    `1`: `COMPLETED`
]

URL: `/api/tasks/?status=0`
```

Search by description 
```
q: word to search in description

URL: `/api/tasks/?q=un`
```

### GET A TASK
URL: `/api/tasks/:id`

:id = task id

METHOD: `GET`

RESPONSE:

STATUS_CODE=200 OK
```json
{
    "id": 3,
    "description": "A task",
    "estimated_duration": 30,
    "completed_duration": null,
    "status": 0
}
```
STATUS_CODE=404 Not Found
```json
{
    "detail": "Not found."
}
```


### UPDATE A TASK
URL: `/api/tasks/:id`

:id = task id

METHOD: `PUT`

BODY REQUEST:
```json
{
    "description": "Description de carga",
    "estimated_duration": 20,
    "completed_duration": "00:20:00",
    "status": 1
}
```

RESPONSE:

STATUS_CODE=200 OK
```json
{
    "id": 1,
    "description": "Description de carga",
    "estimated_duration": 20,
    "completed_duration": "00:20:00",
    "status": 1
}
```
STATUS_CODE=404 Not Found
```json
{
    "detail": "Not found."
}
```
STATUS_CODE=400 Bad Request
```json
{
    "non_field_errors": [
        "task completed"
    ]
}
```

### DELETE A TASK
URL: `/api/tasks/:id`

:id = task id

METHOD: `DELETE`

RESPONSE:

STATUS_CODE=HTTP 204 No Content

STATUS_CODE=404 Not Found
```json
{
    "detail": "Not found."
}
```

