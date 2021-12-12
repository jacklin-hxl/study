package com.xuelin.client;

import com.xuelin.common.Message;
import com.xuelin.common.MessageType;
import com.xuelin.common.User;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.InetAddress;
import java.net.Socket;


public class ChatClient {
    private Socket socket;
    private User u;
    private ObjectOutputStream oos;
    private ObjectInputStream ois;
    private Message message = new Message(); // 复用一个对象

    public ChatClient() {
    }

    public ChatClient(User u) {
        this.u = u;
    }

    public boolean checkUser() {
        String uid = u.getUserId();

        try {
            socket = new Socket(InetAddress.getByName("127.0.0.1"), 9999);
            oos = new ObjectOutputStream(socket.getOutputStream());
            oos.writeObject(u);

            ois = new ObjectInputStream(socket.getInputStream());
            Message msg = (Message) ois.readObject();

            if (msg.getMesType().equals(MessageType.MESSAGE_LOGIN_SUCCEED)) {
                Thread thread = new Thread(new CCSThread(socket, ois, oos));
                thread.start();
                ThreadManage.addThread(uid, thread);
                return true;
            }else {
                socket.close();
                return false;
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public void sendByType(String getter, String content, String sendTime,String messageType) {
        if (oos != null && u != null) {
            message.setAll(u.getUserId(), getter, content, sendTime, messageType);
            send(message);
        } else {
            System.out.println("连接出错");
        }
    }

    public void onClose() {
        if (oos != null && u != null) {
            message.setAll(u.getUserId(), null, null, null, MessageType.MESSAGE_CLIENT_EXIT);
            send(message);
//            try {
//                socket.close();
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
        } else {
            System.out.println("连接出错");
        }
    }

    public void send(Message message){
        try {
//            ObjectOutputStream stream = new ObjectOutputStream(socket.getOutputStream());
//            stream.writeObject(message);
            oos.writeUnshared(message);
//            oos.writeObject(message);
//            oos.reset();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
