package com.example.springbootmongodb.Repository;


import com.example.springbootmongodb.Model.SpecificDevice;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface SpecificDeviceRepository extends MongoRepository<SpecificDevice,String> {
    public List<SpecificDevice> getAllByIdIn(List<String> list_id);
}
