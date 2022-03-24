# ozon-learning
There are only python tests for Go CRUD microservice here. These tests were implemented during studying on a course in Ozon-learning.
The CRUD service was running locally in Docker container, that's why it is called via localhost

The service consist of 4 endpoints:

1. Group create: "POST" `http://localhost:8080/v1/groups`
    
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
    
2. List of groups: "GET" `http://localhost:8080/v1/groups`
    
    Response:
    
    ```json
    "items":[
    {
    "group_id": int
    "foo": ""
    }
    ]
    ```
    
3. Group's decription: "GET" `http://localhost:8080/v1/groups/{group_id}`
    
    group_id ≠ 0
    
    Response:
    
    ```json
    "group":{
    "group_id": int
    "foo": ""
    }
    ```
    
    group_id not in DB → "not found"
    
4. Delete group: "DELETE" `http://localhost:8080/v1/groups/{group_id}`
    
    group_id ≠ 0
    
    Response:
    
    ```json
    {
    "found": bool
    }
    ```
    
    group_id not in DB → "not found"
