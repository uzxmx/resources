package com.example.demo;

import static org.junit.Assert.assertNotNull;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import com.example.demo.service.AnimalService;

@RunWith(SpringRunner.class)
@SpringBootTest
public class SpringJpaApplicationTest {

    @Autowired
    private AnimalService animalService;

    @Test
    public void contextLoads() {
        assertNotNull(animalService);
    }
}
