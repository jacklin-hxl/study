package com.xuelin.client;

import com.xuelin.common.Message;
import com.xuelin.common.MessageType;
import com.xuelin.common.User;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.InetAddress;
import java.net.Socket;


public class ChatClient {
    private User u;

    public ChatClient() {
    }

    public boolean checkUser(User u) {
        String uid = u.getUserId();
        String pwd = u.getPassword();

        try {
            Socket socket = new Socket(InetAddress.getByName("127.0.0.1"), 9999);
            ObjectOutputStream oos = new ObjectOutputStream(socket.getOutputStream());
            oos.writeObject(u);
//            oos.close();

            ObjectInputStream ois = new ObjectInputStream(socket.getInputStream());
            Message msg = (Message) ois.readObject();
//            ois.close();
            if (msg.getMesType().equals(MessageType.MESSAGE_LOGIN_SUCCEED)) {
                Thread thread = new Thread(new CCSThread(socket));
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
}
