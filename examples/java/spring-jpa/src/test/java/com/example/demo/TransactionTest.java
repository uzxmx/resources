package com.example.demo;

import static org.junit.Assert.assertEquals;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.transaction.IllegalTransactionStateException;

import com.example.demo.entity.Zoo;
import com.example.demo.service.TransactionService;
import com.example.demo.service.ZooService;

@RunWith(SpringRunner.class)
@SpringBootTest
public class TransactionTest {

    @Autowired
    private TransactionService txService;

    @Autowired
    private ZooService zooService;

    @Test
    public void testThatZooIsSaved() {
        var zoo = new Zoo();
        zoo.setName("foo");
        zoo = zooService.save(zoo);
        assertEquals(Long.valueOf(0), zoo.getVersion());

        zoo = new Zoo();
        zoo.setName("bar");
        zoo = zooService.saveNoTx(zoo);
        assertEquals(Long.valueOf(0), zoo.getVersion());

        zoo = new Zoo();
        zoo.setName("baz");
        zoo = zooService.saveWithTxNever(zoo);
        assertEquals(Long.valueOf(0), zoo.getVersion());
    }

    @Test(expected = IllegalTransactionStateException.class)
    public void testThatZooSaveWithTxNeverThrowException() {
        txService.execute(() -> {
            var zoo = new Zoo();
            zoo.setName("foo");
            zooService.saveWithTxNever(zoo);
            return true;
        });
    }
}
