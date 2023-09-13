#!/bin/sh

cat ./sql/*.sql | mysql -ptest --verbose
