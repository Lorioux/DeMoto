FROM alpine:latest

EXPOSE 80 8080 8000

RUN mkdir demoto demoto/.dbases

WORKDIR /demoto

COPY ../ .

RUN mkdir .environ

COPY .devcontainer/setup-entry-point.sh .environ/setup-entry-point.sh

ENV SETUP_FILE=/demoto/.environ/setup-entry-point.sh

# Change mode to ./setup-entry-point.sh
RUN chmod +x $SETUP_FILE

ENTRYPOINT [$SETUP_FILE]

# run server at port 80
CMD python3 manage.py runserver 80

