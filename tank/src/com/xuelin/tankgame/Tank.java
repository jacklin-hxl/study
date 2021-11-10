package com.xuelin.tankgame;

import java.util.List;
import java.util.Vector;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/10/28 0:39
 * @Description:
 */


public class Tank {
    int x; // 横坐标
    int y; // 纵坐标
    int direct; // 坦克方向
    boolean isLive = true;
    int speed = 2; // 坦克速度
    int size = 1; // 子弹数量

    public List<Shot> getShots() {
        return shots;
    }

    List<Shot> shots = new Vector();

    Shot st = null;

    public boolean isLive() {
        return isLive;
    }

    public void setLive(boolean live) {
        isLive = live;
    }

    public Tank(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void moveUp(){
        if (getY() > 0) {
            y -= speed;
        }
    }

    public void moveDown(){

        if (getY() + 60 < 750) {
            y += speed;
        }
    }

    public void moveLeft(){
        if (getX() > 0) {
            x -= speed;
        }
    }

    public void moveRight(){
        if (getX() + 60 < 1000) {
            x += speed;
        }
    }

    public int getX(){
        return this.x;
    }

    public int getY(){
        return this.y;
    }

    public int getDirect() {
        return direct;
    }

    public void setDirect(int direct) {
        this.direct = direct;
    }

    public int getSpeed() {
        return speed;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }

    public Shot getShot() {
        return st;
    }

    public void shot(int size) {
        if (shots.size() < size) {
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
            shots.add(st);
            new Thread(st).start();
        }
    }
}
