FROM golang:1.23-alpine AS builder
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -o /out/main main.go

FROM alpine:3.20
WORKDIR /action
COPY --from=builder /out/main /action/main
ENTRYPOINT ["/action/main"]
