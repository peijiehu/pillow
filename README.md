## pillow

Find your dream home

Flask backend, deployed on Heroku.

### Development

    pip install -r requirements.txt

To run locally in debug mode

    python app.py

To run tests

    python tests/test_app.py

To run in production

    gunicorn app:app

### TODO:
1. More unit tests to cover corner cases and negative tests
2. Add quick search links below search bar for recent and frequent searched addresses
3. Logging to a cloud service
4. Integrate with a Continuous Integration tool for testing and building new versions
5. Better frontend - use a framework like React
