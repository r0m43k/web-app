FROM golang:1.19-alpine
WORKDIR /app
COPY main.go .
RUN go build -o myapp main.go && rm -rf /var/cache/*
EXPOSE 8080
CMD ["./myapp"]
