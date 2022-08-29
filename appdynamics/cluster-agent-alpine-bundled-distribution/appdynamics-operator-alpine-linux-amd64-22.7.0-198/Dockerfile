ARG version=latest
FROM alpine:$version

MAINTAINER AppDynamics

LABEL name="AppDynamics Operator" \
      vendor="AppDynamics" \
      version="22.7.0" \
      release="1" \
      url="https://www.appdynamics.com" \
      summary="AppDynamics monitoring solution for applications deployed to Kubernetes clusters" \
      description="The Appdynamics Operator is used to install Cluster Agent & InfraViz"

RUN apk upgrade --update --no-cache

ENV OPERATOR=appdynamics-operator \
    USER_UID=1001 \
    USER_NAME=appdynamics-operator

COPY bin/appdynamics-operator /usr/local/bin/appdynamics-operator
COPY LICENSE /licenses/
COPY scripts/ /usr/local/bin

RUN  /usr/local/bin/ensure-user.sh

ENTRYPOINT ["/usr/local/bin/start-operator.sh"]

USER ${USER_UID}
