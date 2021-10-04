#!/bin/sh -xe

npm audit --registry=https://registry.npmjs.org --parseable | grep -V \
 https://nodesecurity.io/advisories/786
