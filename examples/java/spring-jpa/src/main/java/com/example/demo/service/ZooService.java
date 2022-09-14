package com.example.demo.service;

import javax.transaction.Transactional;
import javax.transaction.Transactional.TxType;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.entity.Zoo;
import com.example.demo.repository.ZooRepository;

@Service
public class ZooService {

    @Autowired
    private ZooRepository zooRepository;

    @Transactional
    public Zoo save(Zoo zoo) {
        return zooRepository.save(zoo);
    }

    public Zoo saveNoTx(Zoo zoo) {
        return zooRepository.save(zoo);
    }

    @Transactional(TxType.NEVER)
    public Zoo saveWithTxNever(Zoo zoo) {
        return zooRepository.save(zoo);
    }
}
