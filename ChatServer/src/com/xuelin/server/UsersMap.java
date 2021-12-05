package com.xuelin.server;

import com.xuelin.common.User;

import java.util.HashMap;

public class UsersMap {
    private static HashMap<String, User> hm = new HashMap();

    static {
        hm.put("100", new User("100", "100"));
        hm.put("200", new User("200", "100"));
        hm.put("300", new User("300", "100"));
        hm.put("学琳", new User("学琳", "100"));
    }

    public static boolean checkUser(User user) {
        return user.equals(hm.get(user.getUserId()));
    }
}
