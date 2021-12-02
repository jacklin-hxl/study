package com.xuelin.client;

import com.xuelin.common.Message;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.Socket;

public class CCSThread implements Runnable{
    private Socket socket;
    private boolean loop;

    public CCSThread(Socket socket) {
        this.socket = socket;
    }

    // 维持通信
    @Override
    public void run() {
        while (loop) {
            try {
                System.out.println("客户端线程， 等待读取服务端消息");
                ObjectInputStream ois = new ObjectInputStream(socket.getInputStream());
                Message o = (Message) ois.readObject();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    public Socket getSocket() {
        return socket;
    }

    public void setSocket(Socket socket) {
        this.socket = socket;
    }
}
