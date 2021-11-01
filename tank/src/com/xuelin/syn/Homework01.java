package com.xuelin.syn;

import java.util.Random;
import java.util.Scanner;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/10/31 22:08
 * @Description:
 */


public class Homework01 {
    public static void main(String[] args) {
        Work01 work01 = new Work01();
        Work02 work02 = new Work02(work01);
        new Thread(work01).start();
        new Thread(work02).start();
    }
}


class Work01 implements Runnable {
    private boolean flag = true;

    @Override
    public void run() {
        while (flag) {
            Random r = new Random();
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName() + "random: " + r.nextInt(100));
        }
    }

    public void setFlag(boolean flag) {
        this.flag = flag;
    }
}

class Work02 implements Runnable {
    private Work01 td;

    public Work02(Work01 td) {
        this.td = td;
    }

    @Override
    public void run() {
        while (true) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Type Please");
//            String s = scanner.nextLine();
            char c = scanner.next().toUpperCase().charAt(0);
            System.out.println("===========" + c);
            if (c == 'Q') {
                td.setFlag(false);
                System.out.println("done");
                break;
            }
        }
    }
}