package com.xuelin.tankgame;

import javax.swing.*;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/10/28 0:53
 * @Description:
 */


public class Game extends JFrame {

    MyPanel mp = null;

    public static void main(String[] args) {
        Game game = new Game();
    }

    public Game() {
        mp = new MyPanel();
        new Thread(mp).start();
        this.add(mp);
        this.setSize(1000, 750);
        this.addKeyListener(mp);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setVisible(true);
    }

}
