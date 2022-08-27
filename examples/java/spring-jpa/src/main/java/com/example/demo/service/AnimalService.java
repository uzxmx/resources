package com.example.demo.service;

import java.util.List;

import javax.transaction.Transactional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.entity.Animal;
import com.example.demo.repository.AnimalRepository;

@Service
public class AnimalService {

    @Autowired
    private AnimalRepository animalRepository;

    public List<Animal> list() {
        return animalRepository.findAll();
    }

    @Transactional
    public Animal create(Animal animal) {
        return animalRepository.save(animal);
    }
}