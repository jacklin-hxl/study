package com.xuelin.syn;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/10/31 23:52
 * @Description:
 */


public class Homework02 {
    public static void main(String[] args) {
        User01 user01 = new User01();
        new Thread(user01).start();
        new Thread(user01).start();
        new Thread(user01).start();
        new Thread(user01).start();
    }
}

class User01 implements Runnable {
    private int money = 100000;

    @Override
    public void run() {
        while (true) {
            synchronized (this) {
                if (!(money < 500)) {
                    money = money - 500;
                    System.out.println(Thread.currentThread().getName() + " current: " + money);
                } else {
                    System.out.println("余额不足");
                    break;
                }
            }

//            try {
//                Thread.sleep(500);
//            } catch (InterruptedException e) {
//                e.printStackTrace();
//            }
        }
    }
}