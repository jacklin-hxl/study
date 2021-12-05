package com.xuelin.server;

import com.xuelin.common.Message;
import com.xuelin.common.MessageType;


import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;

public class CSSThread extends Thread{
    private Socket socket;
    private boolean loop = true;
    private ObjectOutputStream oos;
    private ObjectInputStream ois;
    private Message message = new Message(); // 复用一个对象

    public CSSThread(Socket s) {
        this.socket = s;
    }

    public CSSThread(Socket s, ObjectInputStream ois, ObjectOutputStream oos) {
        this.socket = s;
        this.oos = oos;
        this.ois = ois;
    }


    @Override
    public void run() {

        while (loop) {
            try {
                System.out.println("服务端正在监听");
                Message msg = (Message) ois.readObject();
                System.out.println(msg.hashCode());
                switch (msg.getMesType()) {
                    case MessageType.MESSAGE_GET_FRIEND:
                        String users = ThreadManage.getUsers();
                        message.setAll(null, msg.getSender(), users, null, MessageType.MESSAGE_RET_FRIEND);
                        oos.writeObject(message);
                        System.out.println("获取在线用户列表");
                        break;
                    case MessageType.MESSAGE_CLIENT_EXIT:
                        socket.close();
                        ThreadManage.remove(msg.getSender());
                        loop = false;
                        System.out.println("用户: " + msg.getSender() + " 下线");
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
