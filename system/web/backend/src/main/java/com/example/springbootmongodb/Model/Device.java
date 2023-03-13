package com.example.springbootmongodb.Model;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;
@Data
@Document("Product_Search") // specify a collection name of the database
public class Device {
    @Id
    private String id;
    private String name;
    private String url;
    private String ram;
    private String rom;
    private String price;
    private String createDate;
    private String color;
    private int status;
    private String url_img;
    private List<String> list_id;

    public Device() {
    }

    public Device(String id, String name, String url, String ram, String rom, String price, String createDate,
                  String color, int status, String url_img, List<String> list_id) {
        this.id = id;
        this.name = name;
        this.url = url;
        this.ram = ram;
        this.rom = rom;
        this.price = price;
        this.createDate = createDate;
        this.color = color;
        this.status = status;
        this.url_img = url_img;
        this.list_id = list_id;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getRam() {
        return ram;
    }

    public void setRam(String ram) {
        this.ram = ram;
    }

    public String getRom() {
        return rom;
    }

    public void setRom(String rom) {
        this.rom = rom;
    }

    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }

    public String getCreateDate() {
        return createDate;
    }

    public void setCreateDate(String createDate) {
        this.createDate = createDate;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public String getUrl_img() {
        return url_img;
    }

    public void setUrl_img(String url_img) {
        this.url_img = url_img;
    }

    public List<String> getList_id() {
        return list_id;
    }

    public void setList_id(List<String> list_id) {
        this.list_id = list_id;
    }
}
