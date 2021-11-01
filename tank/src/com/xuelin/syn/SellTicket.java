package com.xuelin.syn;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/10/30 19:31
 * @Description:
 */


public class SellTicket {
    public static void main(String[] args) {
        Sell sell = new Sell();
        Sell sell1 = new Sell();
        Sell sell2 = new Sell();
        sell1.start();
        sell.start();
        sell2.start();
//        Sell sell = new Sell();
//        new Thread(sell).start();
//        new Thread(sell).start();
//        new Thread(sell).start();
    }
}


class Sell extends  Thread {
    private static int ticketNum = 100;
    private  static boolean loop = true;

    public void m() {
        synchronized (Sell.class){
            if (ticketNum <= 0) {
                System.out.println("done");
                loop = false;
                return;
            }

            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            System.out.println(Thread.currentThread().getName() + "current ticketNum: " + (--ticketNum));
        }


    }


    @Override
    public void run() {
        while (loop) {
            m();
        }
    }

}