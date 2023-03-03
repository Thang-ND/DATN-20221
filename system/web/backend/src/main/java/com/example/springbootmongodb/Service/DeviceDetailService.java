package com.example.springbootmongodb.Service;
import com.example.springbootmongodb.Model.DeviceDetail;
import com.example.springbootmongodb.Repository.DeviceDetailRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@AllArgsConstructor
@Service
public class DeviceDetailService {
    private final DeviceDetailRepository deviceDetailRepository;
    public List<DeviceDetail> getAllDeviceDetail(String name)
    {
        return deviceDetailRepository.findAllByName(name);
    }
}
