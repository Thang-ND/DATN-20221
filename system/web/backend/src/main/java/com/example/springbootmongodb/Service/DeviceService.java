package com.example.springbootmongodb.Service;


import com.example.springbootmongodb.Repository.DeviceRepository;
import com.example.springbootmongodb.Model.Device;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import java.util.List;
@AllArgsConstructor
@Service
public class DeviceService {
    @Autowired
    private  final DeviceRepository deviceRepository;

    @Autowired
    private MongoTemplate mt;
    public List<Device> getAllDevices(){
        return deviceRepository.findAll();
    }
    public List<Device> searchDevice(String name,String color,int ram,double rom){
        Query query = new Query();
        Criteria criteria = new Criteria();
        //query.addCriteria(Criteria.where("name").is(name));
        criteria.and("name").is(name);
        if (!color.equals("unknown")) {
            criteria.and("color").is(color);
        }
        if (ram != 0) {
            criteria.and("ram").is(ram);
        }
        if (rom != 0) {
            criteria.and("rom").is(rom);
        }
        query.addCriteria(criteria);
        //System.out.println(query);
        List<Device> result = mt.find(query, Device.class);
        return result;
    }
    public List<Device> findProductsWithPagination(String name,String color,int ram,double rom,int page,int pageSize){
        Query query = new Query();
        Criteria criteria = new Criteria();
        //query.addCriteria(Criteria.where("name").is(name));
        criteria.and("name").is(name);
        if (!color.equals("unknown")) {
            criteria.and("color").is(color);
        }
        if (ram != 0) {
            criteria.and("ram").is(ram);
        }
        if (rom != 0) {
            criteria.and("rom").is(rom);
        }
        query.addCriteria(criteria);
        query.with(PageRequest.of(page, pageSize));
        List<Device> devices = mt.find(query, Device.class);
        return devices;
    }

}
