#!/bin/bash

# Redirect stdout and stderr to a log file
exec > >(tee -a /logs/ip_tracker.log)
exec 2>&1

# cron
while true; do
  python ./ip_service.py
  sleep "$CRON_INTERVAL"
done
