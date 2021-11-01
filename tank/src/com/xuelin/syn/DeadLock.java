package com.xuelin.syn;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/10/31 19:22
 * @Description:
 */


public class DeadLock {
   public static void main(String[] args) {
      Demo demo1 = new Demo(true);
      Demo demo2 = new Demo(true);
      demo1.start();
      demo2.start();
   }

}

class Demo extends Thread {
   static Object o1 = new Object();
   static Object o2 = new Object();
   boolean flag;

   public Demo(boolean flag) {
       this.flag = flag;
   }

   public void run() {
      if (flag) {
         synchronized (o1) {
            System.out.println(1);
            synchronized (o2) {
               System.out.println(2);
            }
         }
      } else {
         synchronized (o2) {
            System.out.println(3);
            synchronized (o1) {
               System.out.println(4);
            }
         }
      }
   }
}