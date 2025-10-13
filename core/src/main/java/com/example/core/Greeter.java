package com.example.core;

public class Greeter {
    public String greet(String name) {
        if (name == null || name.isBlank()) return "Merhaba!";
        return "Merhaba, " + name + "!";
    }
}