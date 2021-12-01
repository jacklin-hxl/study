package com.vertx.websocket.main;


import com.vertx.websocket.verticle.WebsocketVerticle;
import io.vertx.core.DeploymentOptions;
import io.vertx.core.Vertx;

public class Start {
    public static void main(String[] args) {
        Vertx vertx = Vertx.vertx();

        DeploymentOptions deploymentOptions = new DeploymentOptions();
        vertx.deployVerticle(WebsocketVerticle.class.getName());

    }
}
