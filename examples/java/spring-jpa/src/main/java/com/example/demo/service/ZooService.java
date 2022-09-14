package com.example.demo.service;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.PersistenceContextType;
import javax.transaction.Transactional;
import javax.transaction.Transactional.TxType;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.support.TransactionSynchronizationManager;

import com.example.demo.entity.Zoo;
import com.example.demo.repository.ZooRepository;

@Service
public class ZooService {

    @PersistenceContext
    private EntityManager transactionEntityManager;

    @PersistenceContext(type = PersistenceContextType.EXTENDED)
    private EntityManager extendedEntityManager;

    @Autowired
    private ZooRepository zooRepository;

    @Transactional
    public Zoo save(Zoo zoo) {
        return zooRepository.save(zoo);
    }

    public Zoo saveNoTx(Zoo zoo) {
        return zooRepository.save(zoo);
    }

    // The entity will be saved in the DB.
    @Transactional(TxType.NEVER)
    public Zoo saveWithTxNever(Zoo zoo) {
        assert(!TransactionSynchronizationManager.isActualTransactionActive());
        return zooRepository.save(zoo);
    }

    // The entity will be saved in the DB, and there is no rollback even though an exception happens.
    @Transactional(TxType.NEVER)
    public Zoo saveWithTxNeverThrowException(Zoo zoo) {
        assert(!TransactionSynchronizationManager.isActualTransactionActive());
        zoo.setName(zoo.getName() + " updated");
        zooRepository.save(zoo);
        throw new RuntimeException();
    }

    // With below annotation, `persist` actually runs in a transaction. So the
    // entity will be saved in the DB.
    @Transactional(TxType.NEVER)
    public Zoo saveWithTxNeverByExtendedEntityManager(Zoo zoo) {
        assert(!TransactionSynchronizationManager.isActualTransactionActive());
        zoo.setName(zoo.getName() + " updated");
        extendedEntityManager.persist(zoo);
        return zoo;
    }

    // With below annotation, `persist` actually runs in a transaction. It will
    // rollback the transaction when an exception happens.
    @Transactional(TxType.NEVER)
    public Zoo saveWithTxNeverByExtendedEntityManagerThrowException(Zoo zoo) {
        assert(!TransactionSynchronizationManager.isActualTransactionActive());
        zoo.setName(zoo.getName() + " updated");
        extendedEntityManager.persist(zoo);
        throw new RuntimeException();
    }

    // `persist` doesn't run in a transaction. So the entity won't be saved in the DB.
    public Zoo saveNoTxByExtendedEntityManager(Zoo zoo) {
        assert(!TransactionSynchronizationManager.isActualTransactionActive());
        zoo.setName(zoo.getName() + " updated");
        extendedEntityManager.persist(zoo);
        return zoo;
    }

    @Transactional
    public Zoo saveByTransactionEntityManager(Zoo zoo) {
        assert(TransactionSynchronizationManager.isActualTransactionActive());
        zoo = transactionEntityManager.find(Zoo.class, zoo.getId());
        zoo.setName(zoo.getName() + " updated");
        transactionEntityManager.persist(zoo);
        return zoo;
    }

    // It will throw TransactionRequiredException.
    @Transactional(TxType.NEVER)
    public Zoo saveWithTxNeverByTransactionEntityManager(Zoo zoo) {
        assert(!TransactionSynchronizationManager.isActualTransactionActive());
        zoo.setName(zoo.getName() + " updated");
        transactionEntityManager.persist(zoo);
        return zoo;
    }

    // It will throw TransactionRequiredException.
    public Zoo saveNoTxByTransactionEntityManager(Zoo zoo) {
        assert(TransactionSynchronizationManager.isActualTransactionActive());
        zoo.setName(zoo.getName() + " updated");
        transactionEntityManager.persist(zoo);
        return zoo;
    }

    public Zoo find(Long id) {
        var optional = zooRepository.findById(id);
        if (optional.isPresent()) {
            return optional.get();
        } else {
            return null;
        }
    }

    public Zoo findByExtendedEntityManager(Long id) {
        return extendedEntityManager.find(Zoo.class, id);
    }
}
