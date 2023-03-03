package com.example.springbootmongodb.Controller;

import com.example.springbootmongodb.Model.DeviceDetail;
import com.example.springbootmongodb.Model.SpecificDevice;
import com.example.springbootmongodb.Service.DeviceDetailService;
import com.example.springbootmongodb.Service.DeviceService;
import com.example.springbootmongodb.Model.Device;
import com.example.springbootmongodb.Service.SpecificDeviceService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController // mark as request handler
@RequestMapping("/api/devices")
@AllArgsConstructor

public class DeviceController {
    private final DeviceDetailService deviceDetailService;
    private  final DeviceService deviceService;
    private  final SpecificDeviceService specificDeviceService;
    //@GetMapping("/phone")
    //public List<Device> fetchAllDevice(){
        //return deviceService.getAllDevices();
    //}
    @CrossOrigin("http://localhost:3000")
    @GetMapping("/phone/search")
    public List<Device> searchDevice(@RequestParam String name,
                                     @RequestParam(required = false, defaultValue = "unknown") String color,
                                     @RequestParam(required = false, defaultValue = "0") String ram,
                                     @RequestParam(required = false, defaultValue = "0") String rom){
        int new_ram = Integer.parseInt(ram);
        double new_rom = Double.parseDouble(rom);
        return deviceService.searchDevice(name,color,new_ram,new_rom);
    }
    @CrossOrigin("http://localhost:3000")
    @GetMapping("/pagination")
    public List<Device> getDevicesWithSort(@RequestParam String name,
                                           @RequestParam(required = false, defaultValue = "unknown") String color,
                                           @RequestParam(required = false, defaultValue = "0") String ram,
                                           @RequestParam(required = false, defaultValue = "0") String rom,
                                           @RequestParam(required = false, defaultValue = "0") int page,
                                           @RequestParam(required = false, defaultValue = "9") int pageSize){
        int new_ram = Integer.parseInt(ram);
        double new_rom = Double.parseDouble(rom);
        int new_page = Integer.parseInt(String.valueOf(page));
        int new_pageSize = Integer.parseInt(String.valueOf(pageSize));
        return  deviceService.findProductsWithPagination(name,color,new_ram,new_rom,new_page,new_pageSize);
    }
    @CrossOrigin("http://localhost:3000")
    @PostMapping ("/specificDevice")
    public List<SpecificDevice> getSpecificDevice(@RequestBody List<String> list_id){
        return  specificDeviceService.getAllSpecificDevice(list_id);
    }
    @CrossOrigin("http://localhost:3000")
    @GetMapping ("/detailDevice")
    public List<DeviceDetail> getDetailDevice(@RequestParam(required = false) String name){
        return  deviceDetailService.getAllDeviceDetail(name);
    }
}
