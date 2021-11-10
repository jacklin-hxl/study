package com.xuelin.tankgame;

import java.util.Vector;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/11/1 0:54
 * @Description:
 */


public class Enemy extends Tank implements Runnable{

    public Enemy(int x, int y) {
        super(x, y);
        super.setDirect(2);
    }

    @Override
    public void run() {
        while (isLive()) {
            shot(1);
            switch (getDirect()) { //随机取0-3
                case 0:
                    moveUp();
                    break;
                case 1:
                    moveRight();
                    break;
                case 2:
                    moveDown();
                    break;
                case 3:
                    moveLeft();
                    break;
            }

            int random = (int) (Math.random() * 4);
            setDirect(random);

        }
    }

    @Override
    public void moveUp() {
        for (int i = 0; i < 30; i++) {
            super.moveUp();
            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }

    @Override
    public void moveDown() {
        for (int i = 0; i < 30; i++) {
            super.moveDown();
            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }

    @Override
    public void moveLeft() {
        for (int i = 0; i <30; i++) {
            super.moveLeft();
            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    @Override
    public void moveRight() {
        for (int i = 0; i < 30; i++) {
            super.moveRight();
            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
