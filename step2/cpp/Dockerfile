FROM debian AS builder
RUN mkdir -p /build && \
    apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends tzdata && \
    apt install -y g++ libboost-all-dev
WORKDIR /build

FROM builder AS building
COPY . /src
WORKDIR /src
RUN g++ server.cpp -o server -lpthread

FROM debian:bullseye-slim
COPY --from=building /src/server .
CMD ["./server"]
