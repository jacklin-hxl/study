package com.xuelin.tankgame;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/10/28 0:43
 * @Description:
 */


public class Hero extends Tank{

    private Shot st = null;

    public Hero(int x, int y){
        super(x, y);
    }

    public void shot() {
        switch (getDirect()) {
            case 0:
                st = new Shot(getX() + 20, getY(), getDirect());
                break;
            case 1:
                st = new Shot(getX() + 60, getY() + 20, getDirect());
                break;
            case 2:
                st = new Shot(getX() + 20, getY() + 60, getDirect());
                break;
            case 3:
                st = new Shot(getX(), getY() + 20, getDirect());
                break;
        }

        new Thread(st).start();
    }

    public Shot getShot() {
        if (!(st == null)) {
            return st;
        } else {
            return null;
        }
    }

}
