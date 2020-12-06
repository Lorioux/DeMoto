FROM alpine:latest

EXPOSE 80

RUN mkdir demoto demoto/.dbases demoto/.environ

COPY ../ /demoto

WORKDIR /demoto

RUN cp .devcontainer/setup-entry-point.sh /usr/local/bin/

#ENV SETUP_FILE="/demoto/setup-entry-point.sh"

# Change mode to ./setup-entry-point.sh
RUN chmod +x /usr/local/bin/setup-entry-point.sh

ENTRYPOINT ["setup-entry-point.sh"]

# run server at port 80
CMD python3 manage.py runserver 80

