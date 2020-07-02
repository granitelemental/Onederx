### Usage

1) `docker-compose up --build`
2) Requests to api:

- `POST /alarm` - posts alarm date and description into the database. Request body format: 
```
{
	"date": 1593638798, # UTC timestamp
	"description": "Description"
}
```

- `GET /alarm` - gets list of active alarms. Response example:
```
{
  "data": [
    {
      "date": 1693631678.0,
      "description": "call "
    },
    {
      "date": 1694631678.0,
      "description": "call "
    }
  ],
  "status": "Ok"
}
```

4) Websocket server. Sends messages to a client connected to `SOCKET_HOST` and `SOCKET_PORT` from `docker-compose.yml` (default `SOCKET_HOST=0.0.0.0, SOCKET_PORT=3000`) each 1 second.

Default message example:
```
{
    "Now": "1593692914.0",
    "alarm": null
}
```
Alarm message example:
```
{
    "Now": "1593692986.0",
    "alarm": {
        "description": "call ",
        "date": 1593692986.0
    }
}
```
