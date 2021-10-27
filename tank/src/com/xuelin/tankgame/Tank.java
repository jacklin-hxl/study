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

    public Tank(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX(){
        return this.x;
    }

    public int getY(){
        return this.y;
    }
}
