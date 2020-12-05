FROM alpine:latest

EXPOSE 80:80 8080:8080 8000:8000

RUN mkdir demoto demoto/.dbases

WORKDIR /demoto

COPY ../ /demoto

# Change mode to ./setup-entry-point.sh
RUN chmod +x setup-entry-point

ENTRYPOINT ["./setup-entry-point.sh"]

# run server at port 80
CMD python3 manage.py runserver 80

