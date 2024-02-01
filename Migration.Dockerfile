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
WORKDIR /opt/project

#
COPY --from=requirements-stage /tmp/requirements.txt /opt/project/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /opt/project/requirements.txt



#

COPY alembic.ini alembic.ini
COPY ./src src
COPY ./migration migration

# RUN alembic upgrade head




CMD ["alembic", "upgrade", "head"]