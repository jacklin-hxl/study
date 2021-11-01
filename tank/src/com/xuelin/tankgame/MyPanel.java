package com.xuelin.tankgame;

import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Vector;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/10/28 0:49
 * @Description:
 */


public class MyPanel extends JPanel implements KeyListener, Runnable {
    Hero hero = null;
    Vector<Enemy> enemys = new Vector<>();
    int enemySize = 3;

    public MyPanel(){
        hero = new Hero(100,100); // 初始化自己的坦克

        // 初始化敌人坦克，使用vector集合保存，每个坦克都生成一个shot线程
        for (int i = 0; i < enemySize; i++) {
            // 每个坦克相距100像素
            Enemy enemy = new Enemy((100 * (i + 1)), 0);
            Shot shot = new Shot(enemy.getX() + 20, enemy.getY() + 60, enemy.getDirect());
            enemy.shots.add(shot);
            new Thread(shot).start();

            enemys.add(enemy);
        }
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        g.fillRect(0, 0 , 1000, 700);

        // 画出坦克-封装方法
        drawTank(hero.getX(), hero.getY(), g, hero.getDirect(), 0); // 自己的坦克

        // 获取自己坦克的shot对象，如果 存在，则绘画shot
        Shot st = hero.getShot();
        if (st != null && st.isLive()) {
            drawShot(st.getX(), st.getY(), g);
//            System.out.println("在发射");
        }

        // 遍历Vector 集合的Enemy 对象，获取每个Enemy对象中的shot集合并遍历绘画出来
        for (Enemy e : enemys) {
            drawTank(e.getX(), e.getY(), g, e.getDirect(), 1);
            for (int i = 0; i < e.shots.size(); i++) {
                Shot shot = e.shots.get(i);
                if (shot.isLive()) {
                    drawShot(shot.getX(), shot.getY(),g);
                }else {
                    // 子弹不存在，从集合中去除
                    e.shots.remove(shot);
                }
            }
        }


    }

    // 编写方法，画出坦克

    /**
     *
     * @param x 坦克的左上角x坐标
     * @param y 坦克的左上角y坐标
     * @param g 画笔
     * @param direct 坦克方向
     * @param type 坦克类型
     */
    public void drawTank(int x, int y, Graphics g, int direct, int type) {

        // 根据坦克类型设置颜色
        switch (type) {
            case 0: // 我的坦克
                g.setColor(Color.PINK);
                break;
            case 1: // 敌人的坦克
                g.setColor(Color.RED);
                break;
        }

        // 根据方向绘图
        switch (direct) {
            case 0: // 向上
                g.fill3DRect(x, y, 10, 60 , false); // 左轮
                g.fill3DRect(x + 30, y, 10, 60, false); // 右轮
                g.fill3DRect(x + 10, y + 10, 20, 40, false); // 盖子
                g.fillOval(x + 10, y + 20, 20, 20); // 圆形盖子
                g.drawLine(x + 20, y + 30, x + 20, y); // 画出炮筒
                break;
            case 1: // 向右
                g.fill3DRect(x, y, 60, 10 , false); // 左轮
                g.fill3DRect(x, y + 30, 60, 10, false); // 右轮
                g.fill3DRect(x + 10, y + 10, 40, 20, false); // 盖子
                g.fillOval(x + 20, y + 10, 20, 20); // 圆形盖子
                g.drawLine(x + 30, y + 20, x + 60, y + 20); // 画出炮筒
                break;
            case 2: // 向下
                g.fill3DRect(x, y, 10, 60 , false); // 左轮
                g.fill3DRect(x + 30, y, 10, 60, false); // 右轮
                g.fill3DRect(x + 10, y + 10, 20, 40, false); // 盖子
                g.fillOval(x + 10, y + 20, 20, 20); // 圆形盖子
                g.drawLine(x + 20, y + 30, x + 20, y + 60); // 画出炮筒
                break;
            case 3: // 向左
                g.fill3DRect(x, y, 60, 10 , false); // 左轮
                g.fill3DRect(x, y + 30, 60, 10, false); // 右轮
                g.fill3DRect(x + 10, y + 10, 40, 20, false); // 盖子
                g.fillOval(x + 20, y + 10, 20, 20); // 圆形盖子
                g.drawLine(x + 30, y + 20, x, y + 20); // 画出炮筒
                break;
            default:
                System.out.println("暂时没有处理");
        }
    }

    public void drawShot(int x, int y, Graphics g) {
        g.setColor(Color.PINK);
        g.draw3DRect(x, y, 1, 1 , false); // 子弹
    }

    // 判断我方的子弹是否击中敌人坦克
    public static void hitTank(Shot s, Enemy enemy) {
        // 判断s 击中坦克
        switch (enemy.getDirect()) {
            case 0:
            case 2:
                if (s.getX() > enemy.getX() && s.getX() < enemy.getX() + 40 &&
                        s.getY() > enemy.getY() && s.getY() < enemy.getY() + 60) {
                    s.setLive(false);
                    enemy.isLive = false;
                }
                break;
            case 1:
            case 3:
                if (s.getX() > enemy.getX() && s.getX() < enemy.getX() + 60 &&
                        s.getY() > enemy.getY() && s.getY() < enemy.getY() + 40) {
                    s.setLive(false);
                    enemy.isLive = false;
                }
                break;
        }
    }

    @Override
    public void keyTyped(KeyEvent e) {

    }

    // 处理键按下的事件
    @Override
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_W) {
            hero.setDirect(0);
            hero.moveUp();
        }else if (e.getKeyCode() == KeyEvent.VK_D) {
            hero.setDirect(1);
            hero.moveRight();
        }else if (e.getKeyCode() == KeyEvent.VK_S) {
            hero.setDirect(2);
            hero.moveDown();
        }else if (e.getKeyCode() == KeyEvent.VK_A) {
            hero.setDirect(3);
            hero.moveLeft();
        }

        if (e.getKeyCode() == KeyEvent.VK_J) {
            System.out.println("shot");
            hero.shot();
        }
        this.repaint();
    }

    @Override
    public void keyReleased(KeyEvent e) {

    }

    @Override
    public void run() {
        while (true) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            this.repaint();
        }
    }
}
