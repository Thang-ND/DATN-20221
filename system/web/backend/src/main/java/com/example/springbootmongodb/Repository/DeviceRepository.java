package com.example.springbootmongodb.Repository;

import com.example.springbootmongodb.Model.Device;
import com.example.springbootmongodb.Model.SpecificDevice;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import java.util.List;

public interface DeviceRepository  extends MongoRepository<Device,String> {
    public List<Device> findAllByNameContainingIgnoreCaseAndColorIgnoreCaseAndRamIgnoreCaseAndRomIgnoreCase
            (String name, String color, String ram, String rom);
    public Page<Device> findAllByNameContainingIgnoreCaseAndColorIgnoreCaseAndRamIgnoreCaseAndRomIgnoreCase
            (String name,String color,int ram,double rom, Pageable pageable);

    @Query("{$and:[{name: ?0}, {color: ?1}, {ram: ?2}, {rom: ?3}]}")
    List<Device> getDevices(String name, String color, int ram, double rom);
    @Query("[{name: ?0}")
    List<Device> getDevices(String name);

    //Query query = new Query();
    /*
    Query query= new Query();
    query.addCriteria(Criteria.where("id").is(501));
    * */
}

