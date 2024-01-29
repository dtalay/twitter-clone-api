# This is the first stage, it is named requirements-stage.
FROM python:3.12 as requirements-stage

# Set /tmp as the current working directory.
# Here's where we will generate the file requirements.txt
WORKDIR /tmp

#
RUN pip install poetry

#
COPY ./pyproject.toml ./poetry.lock* /tmp/

#
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

#
FROM python:3.12

#
WORKDIR /app

#
COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt



#
COPY entrypoint.sh entrypoint.sh
COPY wait-for-it.sh wait-for-it.sh
COPY alembic.ini alembic.ini
COPY ./src src
COPY ./migration migration



EXPOSE 8000

#
ENTRYPOINT ["/app/entrypoint.sh"]