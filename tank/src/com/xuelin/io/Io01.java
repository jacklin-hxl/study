package com.xuelin.io;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Io01 {
    public static void main(String[] args) {
        String fp = "/Users/xuelin/Desktop/1.txt";
        BufferedReader br = null;
        try {
            br = new BufferedReader(new FileReader(fp));
            String line = null;
            int lineNum = 0;
            while ((line = br.readLine()) != null) {
                System.out.println((++lineNum) + " " + line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
