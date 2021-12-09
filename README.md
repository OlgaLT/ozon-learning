# ozon-learning
Тесты на python для CRUD микросервиса, написанного на go. Сервис запускался локально в Docker контейнере, поэтому обращение через localhost
Сервис состоит из 4 ручек:

1. Создание группы: "POST" `http://localhost:8080/v1/groups`
    
    Body:
    
    ```json
    {
      "foo": "group name 10 - 1000 runes"
    }
    
    ```
    
    Response:
    
    ```json
    {
    "group_id": int
    }
    
    ```
    
2. Список групп: "GET" `http://localhost:8080/v1/groups`
    
    Response:
    
    ```json
    "items":[
    {
    "group_id": int
    "foo": ""
    }
    ]
    ```
    
3. Описание группы: "GET" `http://localhost:8080/v1/groups/{group_id}`
    
    group_id ≠ 0
    
    Response:
    
    ```json
    "group":{
    "group_id": int
    "foo": ""
    }
    ```
    
    group_id not in DB → "not found"
    
4. Удаление группы: "DELETE" `http://localhost:8080/v1/groups/{group_id}`
    
    group_id ≠ 0
    
    Response:
    
    ```json
    {
    "found": bool
    }
    ```
    
    group_id not in DB → "not found"
