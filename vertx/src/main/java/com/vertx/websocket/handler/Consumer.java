package com.vertx.websocket.handler;


import io.vertx.core.MultiMap;
import io.vertx.core.Vertx;
import io.vertx.core.buffer.Buffer;
import io.vertx.core.http.ServerWebSocket;
import io.vertx.core.http.WebSocketFrame;

public class Consumer {

    private ServerWebSocket ws;
    private Vertx vertx;
    private String topic;

    public Consumer(ServerWebSocket ws, Vertx vertx, String topic) {
        this.ws = ws;
        this.vertx = vertx;
        this.topic = topic;
    }

    public Consumer onConsume() {

        System.out.println("Consumer online "+ ws.binaryHandlerID());
        vertx.eventBus().consumer(topic, message -> {
            MultiMap headers = message.headers();
            if (ws.binaryHandlerID() != headers.get("id")) {
                Object body = message.body();
                if (body instanceof Buffer) {
                    Buffer buffer = (Buffer) body;
                    byte[] bytes = buffer.getBytes();
                    String s = new String(buffer.getBytes());
                    ws.writeTextMessage(s);
//                    System.out.println(buffer.toString("UTF-16"));
                }

            }

        });

        return this;
    }

    public Consumer onClose() {
        ws.closeHandler(close -> {
            System.out.println("Consumer offline "+ ws.binaryHandlerID());
        });

        return this;
    }
}
