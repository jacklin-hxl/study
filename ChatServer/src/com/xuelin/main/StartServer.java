package com.xuelin.main;

import com.xuelin.server.ChatServer;

public class StartServer {
    public static void main(String[] args) {
        new ChatServer(9999).run();
    }
}
