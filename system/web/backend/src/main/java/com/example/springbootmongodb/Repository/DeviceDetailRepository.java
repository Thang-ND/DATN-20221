package com.example.springbootmongodb.Repository;


import com.example.springbootmongodb.Model.DeviceDetail;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface DeviceDetailRepository extends MongoRepository<DeviceDetail, ObjectId> {
    public List<DeviceDetail> findAllByName(String name);
}
