package com.example.demo.service;

import java.util.function.Supplier;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.TransactionDefinition;
import org.springframework.transaction.support.DefaultTransactionDefinition;

@Service
public class TransactionService {

    @Autowired
    private PlatformTransactionManager txManager;

    public <T> T execute(Supplier<T> supplier) {
        var definition = new DefaultTransactionDefinition();
        return execute(definition, supplier);
    }

    public <T> T execute(TransactionDefinition definition, Supplier<T> supplier) {
        var txStatus = txManager.getTransaction(definition);
        try {
            var result = supplier.get();
            txManager.commit(txStatus);
            return result;
        } catch (Exception e) {
            txManager.rollback(txStatus);
            throw e;
        }
    }
}
