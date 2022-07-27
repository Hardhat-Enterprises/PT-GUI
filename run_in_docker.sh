#!/bin/bash

export DISPLAY=:0
xhost +local:docker
sudo docker-compose up
