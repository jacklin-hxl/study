package com.xuelin.tankgame;

import java.util.List;
import java.util.Vector;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/10/28 0:43
 * @Description:
 */


public class Hero extends Tank{

    public List<Shot> getShots() {
        return shots;
    }

    private List<Shot> shots = new Vector();

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
        shots.add(st);
        new Thread(st).start();
    }

    public Shot getShot() {
        return st;
    }

}
