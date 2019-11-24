#!/usr/bin/env bash
while true; do
    if docker container ls -a -f status=exited -f name=continues_integration-service | grep continues_integration
    then
        echo "[ERROR] The service is down"
        docker logs --tail 50 continues_integration-service
        exit 1
    else
        curl -XGET -f http://localhost/login/
        if [[ "$?" = 0 ]]
        then
            echo "[INFO] The service is up"
            exit 0
        else
            sleep 15s
        fi
    fi
done
