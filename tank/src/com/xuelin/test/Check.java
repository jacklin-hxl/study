package com.xuelin.test;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Vector;

/**
 * @author : xuelin
 * @version V1.0
 * @date 2021/11/3 0:04
 * @Description:
 */


public class Check {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("chinese");
        list.add("math");
        list.add("english");
        Iterator<String> iterator = list.iterator();
        while (iterator.hasNext()) {
            String nextElement = iterator.next();
//            if ("math".equals(nextElement)) {
//                //使用ArrayList的boolean remove(Object o)方法进行删除
//                list.remove("math");
//            }
            iterator.remove();
        }
        System.out.println(list);

    }
}
