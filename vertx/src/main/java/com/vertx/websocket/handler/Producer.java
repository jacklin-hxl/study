package com.vertx.websocket.handler;

import io.vertx.core.Vertx;
import io.vertx.core.eventbus.DeliveryOptions;
import io.vertx.core.http.ServerWebSocket;

public class Producer {
    private ServerWebSocket ws;
    private Vertx vertx;
    private String topic;

    public Producer(ServerWebSocket ws, Vertx vertx, String topic) {
        this.ws = ws;
        this.vertx = vertx;
        this.topic = topic;
    }

    public Producer onProduce() {
        System.out.println("Producer online "+ ws.binaryHandlerID());
        ws.handler(buffer -> {
//            byte[] bytes = buffer.getBytes();
            DeliveryOptions dop = new DeliveryOptions();
            dop.addHeader("id", ws.binaryHandlerID());
            vertx.eventBus().publish(topic, buffer, dop);

        });

        return this;
    }

    public Producer onClose() {
        ws.closeHandler(close -> {
            System.out.println("Producer offline "+ ws.binaryHandlerID());
        });

        return this;
    }
}
