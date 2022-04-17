FROM python:3.9 as base
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements-base.txt

COPY ./resources /code/resources
COPY ./floor_plan_puzzle /code/floor_plan_puzzle

CMD ["python", "code/floor_plan_puzzle/main.py"]