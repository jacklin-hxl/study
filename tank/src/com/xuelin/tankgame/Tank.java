package com.xuelin.tankgame;

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
    int speed = 5; // 坦克速度

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

}
