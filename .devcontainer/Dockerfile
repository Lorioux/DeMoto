FROM alpine:latest

EXPOSE 80 8080 8000

RUN mkdir demoto demoto/.dbases demoto/.environ

COPY ../ /demoto

WORKDIR /demoto

COPY .devcontainer/setup-entry-point.sh .environ/setup-entry-point.sh

RUN export SETUP_FILE=/demoto/.environ/setup-entry-point.sh

# Change mode to ./setup-entry-point.sh
RUN chmod +x .environ/setup-entry-point.sh

ENTRYPOINT [".environ/setup-entry-point.sh"]

# run server at port 80
CMD python3 manage.py runserver 80

