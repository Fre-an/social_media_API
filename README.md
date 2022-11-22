# Social Media API
Website link: https://social-media-frensi.herokuapp.com/docs (should work as long as the Heroku Postgres free plan is available).

This social media API incldes the main basic functionalities of a social media app, including creating users, posts, voting, commenting, and authentication.

### The purpose of this project is to learn and practice concepts such as:
> - Building an API
> - FastAPI
> - Python

### Creating this project included:
> - PostgreSQL relational database
> - Database migration (Alembic)
> - Schema validation
> - HTTP (GET, POST, PUSH, DELETE, status codes)
> - Authentication (OAuth2, JWT token, password hashing)
> - SQLAlchemy ORM to access database
> - Testing API endpoints (Postman)
> - Deployment in Heroku

### Website look:
![Screen Shot 2022-11-21 at 12 59 06 PM](https://user-images.githubusercontent.com/67911608/203197035-5860d02f-b99a-4ac1-bb55-88984823bf8a.jpeg)

## Sample endpoints using Postman:
### [HttpGet] Receiving posts from database, returns "200 OK" status code.
![Screen Shot 2022-11-21 at 12 56 57 PM](https://user-images.githubusercontent.com/67911608/203198078-749bb1dd-9245-4e40-92eb-6cc943b420eb.jpg)

### [HttpPost] Creating a new user, returns "201 Created" sttus code.
![Screen Shot 2022-11-21 at 12 56 57 PM](https://user-images.githubusercontent.com/67911608/203198090-5e3f081c-a620-4535-ad49-f5589306b398.jpg)
