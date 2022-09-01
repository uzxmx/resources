package com.example.demo;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.orm.ObjectOptimisticLockingFailureException;
import org.springframework.test.context.junit4.SpringRunner;

import com.example.demo.entity.Zoo;
import com.example.demo.service.TransactionService;
import com.example.demo.service.ZooService;

@RunWith(SpringRunner.class)
@SpringBootTest
public class OptimisticLockTest {

    @Autowired
    private TransactionService txService;

    @Autowired
    private ZooService zooService;

    @Test
    public void testVersionIsIncreased() {
        var zoo = new Zoo();
        zoo.setName("foo");
        zoo = zooService.save(zoo);
        assertEquals(Long.valueOf(0), zoo.getVersion());

        zoo.setName("bar");
        zoo = zooService.save(zoo);
        assertEquals(Long.valueOf(1), zoo.getVersion());

        zoo.setName("baz");
        zoo = zooService.save(zoo);
        assertEquals(Long.valueOf(2), zoo.getVersion());
    }

    @Test
    public void testVersionIsNotIncreasedInOneTx() {
        var z = txService.execute(() -> {
            var zoo = new Zoo();
            zoo.setName("foo");
            zoo = zooService.saveNoTx(zoo);
            assertEquals(Long.valueOf(0), zoo.getVersion());

            zoo.setName("bar");
            zoo = zooService.saveNoTx(zoo);
            assertEquals(Long.valueOf(0), zoo.getVersion());

            zoo.setName("baz");
            zoo = zooService.save(zoo);
            assertEquals(Long.valueOf(0), zoo.getVersion());

            return zoo;
        });

        txService.execute(() -> {
            z.setName("baz");
            assertEquals(Long.valueOf(1), zooService.saveNoTx(z).getVersion());

            return true;
        });
    }

    @Test
    public void testExceptionIsThrownWhenVersionIsNotMatched() {
        var zoo = new Zoo();
        zoo.setName("foo");
        zoo = zooService.save(zoo);
        assertEquals(Long.valueOf(0), zoo.getVersion());

        var finalZoo = zoo;
        var result = new Object[]{null};
        var thread = new Thread(() -> {
            finalZoo.setName("bar");
            result[0] = zooService.save(finalZoo).getVersion();
        });
        thread.start();
        try {
            thread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        assertEquals(Long.valueOf(1), result[0]);
        assertEquals(Long.valueOf(0), zoo.getVersion());

        zoo.setName("baz");
        var exceptionIsThrown = false;
        try {
            zooService.save(zoo);
        } catch (ObjectOptimisticLockingFailureException e) {
            exceptionIsThrown = true;
        }
        assertTrue(exceptionIsThrown);
    }
}
