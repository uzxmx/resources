package com.example.demo;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import javax.persistence.TransactionRequiredException;

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

    @Test
    public void testThatZooSaveWithTxNeverThrowExceptionSavedInDB() {
        var zoo = new Zoo();
        zoo.setName("foo");
        zoo = zooService.save(zoo);
        assertEquals(Long.valueOf(0), zoo.getVersion());

        boolean thrown = false;
        try {
            zooService.saveWithTxNeverThrowException(zoo);
        } catch (Exception e) {
            thrown = true;
        }
        assertTrue(thrown);

        zoo = zooService.find(zoo.getId());
        assertEquals(zoo.getName(), "foo updated");
    }

    @Test
    public void testThatZooSaveWithTxNeverByExtendedEntityManagerThrowExceptionNotSavedInDB() {
        var zoo = new Zoo();
        zoo.setName("foo");
        zoo = zooService.save(zoo);
        assertEquals(Long.valueOf(0), zoo.getVersion());

        boolean thrown = false;
        try {
            zooService.saveWithTxNeverByExtendedEntityManagerThrowException(zoo);
        } catch (Exception e) {
            thrown = true;
        }
        assertTrue(thrown);
        assertEquals(zoo.getName(), "foo updated");

        zoo = zooService.find(zoo.getId());
        assertEquals(zoo.getName(), "foo");
    }

    @Test
    public void testThatZooSaveWithTxNeverByExtendedEntityManagerSavedInDB() {
        var zoo = new Zoo();
        zoo.setName("foo");
        zoo = zooService.save(zoo);
        assertEquals(Long.valueOf(0), zoo.getVersion());

        zoo = zooService.findByExtendedEntityManager(zoo.getId());
        zoo = zooService.saveWithTxNeverByExtendedEntityManager(zoo);
        assertEquals(zoo.getName(), "foo updated");

        zoo = zooService.find(zoo.getId());
        assertEquals(zoo.getName(), "foo updated");
    }

    @Test
    public void testThatZooSaveWithoutTransactionByExtendedEntityManagerNotSavedInDB() {
        var zoo = new Zoo();
        zoo.setName("foo");
        zoo = zooService.save(zoo);
        assertEquals(Long.valueOf(0), zoo.getVersion());

        zoo = zooService.findByExtendedEntityManager(zoo.getId());
        zoo = zooService.saveNoTxByExtendedEntityManager(zoo);
        assertEquals(zoo.getName(), "foo updated");

        zoo = zooService.find(zoo.getId());
        assertEquals(zoo.getName(), "foo");
    }

    @Test
    public void testThatZooSaveByTransactionEntityManagerSavedInDB() {
        var zoo = new Zoo();
        zoo.setName("foo");
        zoo = zooService.save(zoo);
        assertEquals(Long.valueOf(0), zoo.getVersion());

        zoo = zooService.saveByTransactionEntityManager(zoo);
        assertEquals(Long.valueOf(1), zoo.getVersion());

        zoo = zooService.findByExtendedEntityManager(zoo.getId());
        assertEquals(Long.valueOf(1), zoo.getVersion());
    }

    @Test(expected = TransactionRequiredException.class)
    public void testThatZooSaveWithTxNeverByTransactionEntityManagerThrowException() {
        var zoo = new Zoo();
        zoo.setName("foo");
        zoo = zooService.save(zoo);
        assertEquals(Long.valueOf(0), zoo.getVersion());

        zooService.saveWithTxNeverByTransactionEntityManager(zoo);
    }

    @Test(expected = TransactionRequiredException.class)
    public void testThatZooSaveWithoutTransactionByTransactionEntityManagerThrowException() {
        var zoo = new Zoo();
        zoo.setName("foo");
        zoo = zooService.save(zoo);
        assertEquals(Long.valueOf(0), zoo.getVersion());

        zooService.saveNoTxByTransactionEntityManager(zoo);
    }
}
