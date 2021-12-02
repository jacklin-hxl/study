package com.xuelin.client;

import java.util.HashMap;

public class ThreadManage {
    private static HashMap<String, Thread> hashMap = new HashMap<>();

    public static void addThread(String uid, Thread thread){
        hashMap.put(uid, thread);
    }

    public static Thread getThread(String uid) {
        return hashMap.get(uid);
    }
}
