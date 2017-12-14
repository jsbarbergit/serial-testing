#!/bin/bash
socat tcp-l:54321,reuseaddr,fork file:/dev/ttyS0,nonblock,waitlock=/var/run/ttyS0.lock
