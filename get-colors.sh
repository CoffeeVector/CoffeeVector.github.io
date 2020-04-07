#!/bin/sh
convert $1 -colors 5 -unique-colors txt:- | sed 's/..$/$/'| awk '{print $3}' | tail -n +2
