FROM python:3-slim

ADD src /src/

RUN pip install tornado
RUN pip install requests

ENV PYTHONPATH "${PYTHONPATH}:src/handlers"
ENV PYTHONPATH "${PYTHONPATH}:src/bootstrap"

CMD [ "python", "src/webserver.py" ]
