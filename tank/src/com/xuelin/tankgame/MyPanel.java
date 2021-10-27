package com.xuelin.tankgame;

import javax.swing.*;
import java.awt.*;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/10/28 0:49
 * @Description:
 */


public class MyPanel extends JPanel {
    Hero hero = null;

    public MyPanel(){
        hero = new Hero(100,100); // 初始化自己的坦克

    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        g.fillRect(0, 0 , 1000, 700);
    }
}
