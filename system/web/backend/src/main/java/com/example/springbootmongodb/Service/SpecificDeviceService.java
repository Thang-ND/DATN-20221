package com.example.springbootmongodb.Service;

import com.example.springbootmongodb.Model.SpecificDevice;
import com.example.springbootmongodb.Repository.DeviceRepository;
import com.example.springbootmongodb.Repository.SpecificDeviceRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
@AllArgsConstructor
@Service // mark as service provider

public class SpecificDeviceService {
    private  final SpecificDeviceRepository deviceRepository;
    public List<SpecificDevice> getAllSpecificDevice(List<String> list_id){
        return  deviceRepository.getAllByIdIn(list_id);
    }
}
