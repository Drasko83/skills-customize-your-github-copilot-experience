# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI and Python. In this assignment, you will learn how to create API routes, handle CRUD operations, and return clear HTTP responses for client applications.

## 📝 Tasks

### 🛠️ Create Your First FastAPI App

#### Description
Set up a basic FastAPI project and create a simple route to confirm your API is running.

#### Requirements
Completed program should:

- Create a FastAPI app instance in starter code.
- Add a GET endpoint at / that returns a JSON welcome message.
- Run the API locally with Uvicorn.
- Open the automatic docs page at /docs and confirm it loads.


### 🛠️ Build CRUD Endpoints for Tasks

#### Description
Create endpoints that let users create, read, update, and delete task items. Use in-memory storage so you can focus on API behavior.

#### Requirements
Completed program should:

- Define a Pydantic model for a task with fields such as id, title, and completed.
- Implement POST /tasks to create a task.
- Implement GET /tasks and GET /tasks/{task_id} to read tasks.
- Implement PUT /tasks/{task_id} to update a task.
- Implement DELETE /tasks/{task_id} to remove a task.


### 🛠️ Add Validation and Error Responses

#### Description
Improve API reliability by validating input and returning meaningful errors when requests are invalid.

#### Requirements
Completed program should:

- Return 404 when a task id does not exist.
- Validate that title is not empty.
- Return appropriate status codes for create, update, and delete operations.
- Provide clear JSON error messages for invalid operations.
- Demonstrate at least three endpoint tests using curl, HTTPie, or Postman.
