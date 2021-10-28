package com.xuelin.tankgame;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/10/28 0:39
 * @Description:
 */


public class Tank {
    private int x; // 横坐标
    private int y; // 纵坐标
    private int direct; // 坦克方向

    private int speed = 1; // 坦克速度

    public Tank(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void moveUp(){ y -= speed; }

    public void moveDown(){ y += speed; }

    public void moveLeft(){ x -= speed; }

    public void moveRight(){ x += speed; }

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
