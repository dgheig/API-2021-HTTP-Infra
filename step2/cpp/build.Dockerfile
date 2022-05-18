FROM debian
RUN mkdir -p /build && \
    apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends tzdata && \
    apt install -y g++ libboost-all-dev
WORKDIR /build
