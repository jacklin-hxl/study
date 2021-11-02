package com.xuelin.tankgame;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/11/1 1:08
 * @Description: 坦克子弹对象
 */


public class Shot implements Runnable{
    int x; // 子弹x坐标
    int y; // 子弹y坐标
    int direct = 0; // 子弹方向, 0 1 2 3 上右下左
    int speed = 2; // 子弹速度

    public void setLive(boolean live) {
        isLive = live;
    }

    boolean isLive = true;

    public boolean isLive() {
        return isLive;
    }


    public Shot(int x, int y, int direct) {
        this.x = x;
        this.y = y;
        this.direct = direct;
    }

    @Override
    public void run() {
        while (isLive) {
//            synchronized (this) {
                switch (direct) {
                    case 0:
                        y -= speed;
                        break;
                    case 1:
                        x += speed;
                        break;
                    case 2:
                        y += speed;
                        break;
                    case 3:
                        x -= speed;
                        break;
                }

//                System.out.println(x + ", " + y);

                if ( x <=0 || x >= 1000 || y <=0 || y>= 750 ) { // 有一个满足条件就进入
                    isLive = false;
                    break;
                }
//            }

            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

        }

        System.out.println("子弹线程退出");
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}
