docker build -f build.Dockerfile -t res-crow-build .
docker run --rm -v "$PWD:/build" res-crow-build g++ server.cpp -o server -lpthread
docker build --no-cache -f crow.Dockerfile -t res-crow .
