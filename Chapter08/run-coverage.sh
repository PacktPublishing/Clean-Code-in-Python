#!/bin/bash

N=$1
if [[ "$N" == "" ]]; then
    N=1;
fi

pytest \
    --cov-report term-missing \
    --cov=coverage_$N \
    test_coverage_$N.py
