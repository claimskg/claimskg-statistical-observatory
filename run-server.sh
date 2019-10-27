#!/bin/bash
redis-server --daemonize yes & 
gunicorn3 -w 8 --bind 0.0.0.0:8080 wsgi
