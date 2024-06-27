FROM python:3.12-slim

RUN pip install pipenv

WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --deploy --ignore-pipfile

ENTRYPOINT ["pipenv", "run", "pytest", "--alluredir=./allure-results"]
CMD ["tests"]
