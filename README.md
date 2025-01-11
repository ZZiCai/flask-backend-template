# flask-server-template
The template includes best practices for structuring your Flask application, handling API routes, and managing database interactions.


## Getting Started

1. **Configure the Database**:
   - Edit the `configs.py` file to set up your database connection.

2. **Define Data Models**:
   - Create your data models in the `models.py` file.

3. **Initialize the Database**:
   - Run `python init.py` to automatically connect to the database and create the necessary tables.

4. **Develop APIs**:
   - Write your API endpoints in the `app.py` file.

5. **Debugging**:
   - Use `python app.py` to run the application in debug mode.

6. **Production Deployment**:
   - For production, use `gunicorn` with the provided configuration template.
   - Modify the `gunicorn_cf.py` file as needed.
   - Run the application with `gunicorn -c gunicorn_cf.py app:app`.

Alternatively, you can use other WSGI servers like `uWSGI` or `waitress` for deployment.
