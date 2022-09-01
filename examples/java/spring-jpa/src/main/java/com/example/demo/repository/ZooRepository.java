package com.example.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demo.entity.Zoo;

public interface ZooRepository extends JpaRepository<Zoo, Long> {
}
