package com.xuelin.test;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/10/29 23:41
 * @Description:
 */


public class ThreadState {
    public static void main(String[] args) throws InterruptedException {
        T t = new T();
        System.out.println(t.getName() + " 状态 " + t.getState());
        t.start();

        while (t.getState() != Thread.State.TERMINATED) {
            System.out.println(t.getName() + " 状态 " + t.getState());
            Thread.sleep(500);
        }

        System.out.println(t.getName() + " 状态 " + t.getState());
    }
}

class T extends Thread {
    @Override
    public void run() {
        while (true) {
            for (int i = 0; i < 10; i++) {
                System.out.println("hi " + i);
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            break;
        }
    }
}