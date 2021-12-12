package com.xuelin.client;

import com.xuelin.common.Message;
import com.xuelin.common.MessageType;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;

public class CCSThread implements Runnable{
    private Socket socket;
    private boolean loop = true;
    private ObjectInputStream ois;
    private ObjectOutputStream oos;

    public CCSThread(Socket socket) {
        this.socket = socket;
    }

    public CCSThread(Socket socket, ObjectInputStream ois, ObjectOutputStream oos) {
        this.socket = socket;
        this.ois = ois;
        this.oos = oos;
    }

    // 维持通信
    @Override
    public void run() {
        while (loop) {
            try {
                System.out.println("客户端线程， 等待读取服务端消息");
                Message o = (Message) ois.readObject();

                switch (o.getMesType()) {
                    case MessageType.MESSAGE_RET_FRIEND:
                        String content = o.getContent();
                        String[] array = content.split(",");
                        System.out.println("============在线用户列表============");
                        for (String s : array) {
                            System.out.println(s);
                        }
                        break;
                    case MessageType.MESSAGE_COMM_MES:
                        String s = o.getContent();
                        String sender = o.getSender();
                        System.out.println("用户: " + sender + " 私聊你: " + s);
                        break;
                }
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
