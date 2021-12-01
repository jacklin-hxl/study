package com.vertx.websocket.verticle;

import com.vertx.websocket.handler.Consumer;
import com.vertx.websocket.handler.Producer;
import io.vertx.core.AbstractVerticle;
import io.vertx.core.http.HttpServer;
import io.vertx.core.http.ServerWebSocket;
import io.vertx.ext.web.Router;


public class WebsocketVerticle extends AbstractVerticle {

    @Override
    public void start() throws Exception {

        HttpServer httpServer = vertx.createHttpServer();
        Router router = Router.router(vertx);

        router.route("/io/test").handler(rc -> {
            System.out.println(vertx);
            ServerWebSocket ws = rc.request().upgrade();
            String topic = rc.request().getParam("topic");

            Producer producer = new Producer(ws, vertx, topic);
            producer.onProduce().onClose();

            Consumer consumer = new Consumer(ws, vertx, topic);
            consumer.onConsume().onClose();

        });

        httpServer.requestHandler(router::accept).listen(8080);
    }
}
