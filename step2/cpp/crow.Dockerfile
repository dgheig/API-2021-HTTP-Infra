FROM debian:bullseye-slim
COPY server .
CMD ["./server"]
