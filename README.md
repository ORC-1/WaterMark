# WaterMarker
Water Marking Project
 <br />
To build using Docker:<br />
  Docker build .<br />
  Docker-compose build

 <br />
To start:<br />
  Docker-compose up

 <br />
To run tests:<br />
  docker-compose run watermark sh -c "python manage.py test"


The above build command pull a python3.7 alpine image with PostgresSql,
build and start all services needed for the project.

Alternatively, the project can be built using virtualenv or any enviroment
manager of choice by running:<br />
  pip install -r requirements.txt

you can call the services as follow:
 <br />
  1. Get Document by ticketid:<br />
      127.0.0.1:8000/api/wm/doc_by_id?ticketid=<ticketid>
      eg:
        127.0.0.1:8000/api/wm/doc_by_id?ticketid=D4QRGtMiJU7j25WSnlg4YCM
  <br />
      this returns a successful response like below:
  <br />
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
 <br />
  2. Post document for watermarking:
      127.0.0.1:8000/api/wm/watermark:
  <br />
        sample payload:<br />
          {
            "content": "book3",
            "title": "Dark Code",
            "topic": "Science",
            "author": "Wayne"
          }
  <br />
        Sample response:<br />
        {
          "id": 7,
          "ticket_id": "D4QRGtMiJU7j25WSnlg4YCM",
          "content": "book3",
          "title": "Dark Code",
          "topic": "Science",
          "author": "Wayne",
          "water_mark": true
        }
  <br />
  Postman documentation can be found using the following URL:
  https://documenter.getpostman.com/view/5673795/UVeNm2dN
