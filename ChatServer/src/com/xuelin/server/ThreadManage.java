package com.xuelin.server;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class ThreadManage {
    private static HashMap<String, CSSThread> hm = new HashMap<>();

    public static void add(String uid, CSSThread thread) {
        hm.put(uid, thread);
    }

    public static CSSThread get(String uid) {
        return hm.get(uid);
    }

    public static void remove(String uid) {
        hm.remove(uid);
    }

    public static String getUsers() {
        StringBuilder stringBuilder = new StringBuilder();
        Set<Map.Entry<String, CSSThread>> entrySet = hm.entrySet();
        for (Map.Entry<String, CSSThread> entry: entrySet) {
            stringBuilder.append(",");
            stringBuilder.append(entry.getKey());
        }
        return stringBuilder.toString();
    }
}
