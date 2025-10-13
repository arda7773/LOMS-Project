package com.example.loms;

import com.example.core.Greeter;

public class Main {
    public static void main(String[] args) {
        Greeter g = new Greeter();
        System.out.println(g.greet(args.length > 0 ? args[0] : "Dünya"));
    }
}