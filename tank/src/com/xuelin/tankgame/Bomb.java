package com.xuelin.tankgame;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/11/3 1:09
 * @Description:
 */


public class Bomb {
    int x, y;
    int life = 9;
    boolean isLive = true;

    public Bomb(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void lifeDown() {
        if (life > 0) {
            life--;
        } else {
            isLive = false;
        }
    }
}
