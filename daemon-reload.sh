#!/usr/bin/env bash

sudo systemctl daemon-reload
sudo systemctl restart ertai_kz.service
sudo systemctl status ertai_kz.service