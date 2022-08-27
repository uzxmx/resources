package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.example.demo.entity.Animal;
import com.example.demo.entity.Animal.Gender;
import com.example.demo.service.AnimalService;

import lombok.extern.slf4j.Slf4j;

@SpringBootApplication
@Slf4j
public class SpringJpaApplication implements CommandLineRunner {

    @Autowired
    private AnimalService animalService;

    public static void main(String[] args) {
        SpringApplication.run(SpringJpaApplication.class, args);
    }

    @Override
    public void run(String... args) throws Exception {
        var animal = Animal.builder().name("cat foo")
            .gender(Gender.Male)
            .numberOfLegs(4)
            .build();
        animal = animalService.create(animal);
        log.info(animal.toString());

        var list = animalService.list();
        list.forEach(e -> {
            log.info(e.toString());
        });
    }
}
