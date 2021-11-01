package com.xuelin.tankgame;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/11/1 0:54
 * @Description:
 */


public class Enemy extends Tank{


    public Enemy(int x, int y) {
        super(x, y);
        super.setDirect(2);
    }
}
