#!/bin/bash

N=$!
if [[ "$N" == "" ]]; then
    N=1;
fi


mut.py \
    --target mutation_testing_$N \
    --unit-test test_mutation_testing_$N \
    --operator AOD  `# delete arithmetic operator` \
    --operator AOR  `# replace arithmetic operator` \
    --operator COD  `# delete conditional operator` \
    --operator COI  `# insert conditional operator` \
    --operator CRP  `# replace constant` \
    --operator ROR  `# replace relational operator` \
    --show-mutants
