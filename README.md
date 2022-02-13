# WaterMarker
Water Marking Project

To build using Docker:
  Docker build .
  Docker-compose build


To start:
  Docker-compose up


To run tests:
  docker-compose run watermark sh -c "python manage.py test"


The above build command pull a python3.7 alpine image with PostgresSql,
build and start all services needed for the project.

Alternatively, the project can be built using virtualenv or any enviroment
manager of choice by running:
  pip install -r requirements.txt

you can call the services as follow:
  1. Get Document by ticketid:
      127.0.0.1:8000/api/wm/doc_by_id?ticketid=<ticketid>
      eg:
        127.0.0.1:8000/api/wm/doc_by_id?ticketid=D4QRGtMiJU7j25WSnlg4YCM
      this returns a successful response like below:
      [
          {
              "id": 7,
              "ticket_id": "D4QRGtMiJU7j25WSnlg4YCM",
              "content": "book3",
              "title": "Dark Code",
              "topic": "Science",
              "author": "Wayne",
              "water_mark": true
          }
        ]

  2. Post document for watermarking:
      127.0.0.1:8000/api/wm/watermark:
        sample payload:
          {
            "content": "book3",
            "title": "Dark Code",
            "topic": "Science",
            "author": "Wayne"
          }
        Sample response:
        {
          "id": 7,
          "ticket_id": "D4QRGtMiJU7j25WSnlg4YCM",
          "content": "book3",
          "title": "Dark Code",
          "topic": "Science",
          "author": "Wayne",
          "water_mark": true
        }

  Postman documentation can be found using the following URL:
