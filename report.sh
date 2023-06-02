#!/usr/bin/env bash

py.test -s -v Login --html=./reports/reports.html --capture sys --show-capture=no --alluredir=allure-report/



