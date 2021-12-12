package com.xuelin.view;


import com.xuelin.client.ChatClient;
import com.xuelin.common.MessageType;
import com.xuelin.common.User;
import com.xuelin.utils.Utility;

public class View {
    private boolean loop = true;
    private String key = "";

    public static void main(String[] args) {
        new View().mainMenu();
        System.exit(0);
    }

    public void mainMenu() {
        while (loop) {
            System.out.println("============欢迎登录网络通信系统=============");
            System.out.println("\t\t 1 登录系统");
            System.out.println("\t\t 9 退出系统");

            key = Utility.readString(1);

            switch (key) {
                case "1":
                    System.out.println("请输入用户号：");
                    String userId = Utility.readString(50);
                    System.out.println("请输入密  码：");
                    String pwd = Utility.readString(50);

                    User user = new User(userId, pwd);
                    ChatClient chatClient = new ChatClient(user);
                    boolean flag = chatClient.checkUser();

                    if (flag) {
                        System.out.println("欢迎用户登录");
                        // 进入二级菜单
                        while (loop) {
                            System.out.println("\n===============网络通信二级菜单(用户 " + userId + ")===============");
                            System.out.println("\t\t 1 显示在线用户列表");
                            System.out.println("\t\t 2 群发消息");
                            System.out.println("\t\t 3 私聊消息");
                            System.out.println("\t\t 4 发送文件");
                            System.out.println("\t\t 9 退出系统");
                            System.out.println("请输入你的选择: ");

                            key = Utility.readString(1);
                            switch (key) {
                                case "1":
                                    chatClient.sendByType(null, null,  null, MessageType.MESSAGE_GET_FRIEND);
                                    break;
                                case "2":
                                    System.out.println("群发消息");
                                    break;
                                case "3":
                                    System.out.println("输入私聊者：");
                                    String s = Utility.readString(50);
                                    System.out.println("输入消息：");
                                    String content = Utility.readString(200);
                                    chatClient.sendByType(s, content, null, MessageType.MESSAGE_COMM_MES);
                                    break;
                                case "4":
                                    System.out.println("发送文件");
                                    break;
                                case "9":
                                    chatClient.onClose();
                                    loop = false;
                                    break;
                            }

                        }
                    } else {
                        System.out.println("登录服务器失败");
                    }

                    break;
                case "9":
                    loop = false;
                    break;
            }
        }
        System.out.println("客户端退出系统");
    }

}
