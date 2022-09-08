FROM osgeo/gdal:ubuntu-full-latest

WORKDIR /home/app/web

RUN apt update \
    && apt install -y gettext python3 python3-pip python3-venv python3-dev libpq-dev curl
RUN mkdir -p /home/app/web/static

# install dependencies
RUN pip3 install --upgrade pip \
    && pip3 install poetry
RUN poetry config virtualenvs.create false
COPY ["poetry.lock", "pyproject.toml", "./"]
RUN poetry install

COPY . .

RUN sed -i 's/\r$//g' /home/app/web/entrypoint.sh
RUN chmod +x /home/app/web/entrypoint.sh

ENTRYPOINT ["sh", "/home/app/web/entrypoint.sh"]