#!/usr/bin/env bash

project_name=${1}

if [ -z ${project_name} ];then
  echo "Nome requerido"
  exit 1
fi

docker build -t registry.pe.hmg.asgard.b2w.io/${project_name} . \
&& docker push registry.pe.hmg.asgard.b2w.io/${project_name}
