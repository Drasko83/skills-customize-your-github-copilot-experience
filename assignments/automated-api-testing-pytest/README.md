# 📘 Assignment: Automated API Testing with pytest

## 🎯 Objective

Learn how to write automated tests for Python code and FastAPI endpoints using pytest. In this assignment, you will validate core behavior, check API responses, and catch bugs before they reach users.

## 📝 Tasks

### 🛠️	Write Unit Tests for Task Logic

#### Description
Use pytest to test helper functions that manage task data. Focus on correct behavior for normal cases and invalid input.

#### Requirements
Completed program should:

- Write tests for creating a task and marking it complete.
- Write a test that rejects empty task titles.
- Write a test for deleting an existing task.
- Use clear test names that describe expected behavior.
- Run tests with pytest and confirm all unit tests pass.


### 🛠️	Test FastAPI Endpoints

#### Description
Add integration-style tests for API routes using FastAPI TestClient. Verify returned status codes and response JSON.

#### Requirements
Completed program should:

- Test GET /tasks returns a list response.
- Test POST /tasks creates a task and returns success.
- Test GET /tasks/{task_id} returns the correct task for a valid id.
- Test GET /tasks/{task_id} returns 404 for an invalid id.
- Test DELETE /tasks/{task_id} removes the task and returns success.


### 🛠️	Find and Fix a Failing Test

#### Description
Intentionally run the full suite, identify at least one failing test, and fix the implementation code so tests pass again.

#### Requirements
Completed program should:

- Run pytest and identify a failing test from output.
- Fix the implementation bug causing the failure.
- Re-run pytest and confirm all tests pass.
- Add a short code comment near the fix explaining what was corrected.
- Share a brief note describing the bug and how the test caught it.
