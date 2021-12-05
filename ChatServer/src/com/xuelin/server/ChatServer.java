package com.xuelin.server;

import com.xuelin.common.Message;
import com.xuelin.common.MessageType;
import com.xuelin.common.User;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class ChatServer {
    private ServerSocket serverSocket;
    private int port;

    // TODO: 2021/12/4 后续使用properties配置端口
    public ChatServer(int port) {
        this.port = port;
    }

    public void run() {
        try {
            System.out.println("server listen " + port);
            serverSocket = new ServerSocket(port);

            while (true) {
                // 堵塞，每次有客户端连接返回一个新的socket
                Socket socket = serverSocket.accept();
                ObjectInputStream ois = new ObjectInputStream(socket.getInputStream());
                ObjectOutputStream oos = new ObjectOutputStream(socket.getOutputStream());

                User u = (User) ois.readObject();

                if (UsersMap.checkUser(u)) {
                    Message message = new Message();
                    message.setMesType(MessageType.MESSAGE_LOGIN_SUCCEED);
                    message.setGetter(u.getUserId());
                    oos.writeObject(message);
                    System.out.println("用户 " + u.getUserId() + " 登录成功");


                    CSSThread cssThread = new CSSThread(socket, ois, oos);
                    cssThread.start();
                    ThreadManage.add(u.getUserId(), cssThread);
                } else {
                    Message message = new Message();
                    message.setMesType(MessageType.MESSAGE_LOGIN_FAIL);
                    message.setGetter(u.getUserId());
                    oos.writeObject(message);
                    System.out.println("用户 " + u.getUserId() + " 登录失败");
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
