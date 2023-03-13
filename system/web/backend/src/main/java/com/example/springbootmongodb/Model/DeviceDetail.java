package com.example.springbootmongodb.Model;

import lombok.Data;
import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

import java.util.List;
@Data
@Document("Product_Detail")
public class DeviceDetail {
    @Id
    @Field(value = "_id")
    private ObjectId Oid ;
    @Field(value = "name")
    private String name ;
    @Field(value = "Technology")
    private String Technology ;
    @Field(value = "2G bands")
    private String Bands_2G  ;
    @Field(value = "3G bands")
    private String Bands_3G  ;
    @Field(value = "4G bands")
    private String Bands_4G  ;
    @Field(value = "5G bands")
    private String Bands_5G  ;
    @Field(value = "Speed")
    private String Speed ;
    @Field(value = "Announced")
    private String Announced ;
    @Field(value = "Status")
    private String Status ;
    @Field(value = "Dimensions")
    private String Dimensions ;
    @Field(value = "Weight")
    private String Weight ;
    @Field(value = "Build")
    private String Build ;
    @Field(value = "SIM")
    private String SIM ;
    @Field(value = "Type")
    private String Type ;
    @Field(value = "Size")
    private String Size ;
    @Field(value = "Resolution")
    private String Resolution ;
    @Field(value = "Protection")
    private String Protection ;
    @Field(value = "OS")
    private String OS ;
    @Field(value = "Chipset")
    private String Chipset ;
    @Field(value = "CPU")
    private String CPU ;
    @Field(value = "GPU")
    private String GPU ;
    @Field(value = "Card slot")
    private String Card_slot ;
    @Field(value = "Internal")
    private String Internal ;
    @Field(value = "Triple")
    private String Triple ;
    @Field(value = "Features")
    private String Features ;
    @Field(value = "Video")
    private String Video ;
    @Field(value = "Single")
    private String Single ;
    @Field(value = "Loudspeaker")
    private String Loudspeaker ;
    @Field(value = "3.5mm jack")
    private String jack_3_5mm  ;
    @Field(value = "WLAN")
    private String WLAN ;
    @Field(value = "Bluetooth")
    private String Bluetooth ;
    @Field(value = "Positioning")
    private String Positioning ;
    @Field(value = "NFC")
    private String NFC ;
    @Field(value = "Radio")
    private String Radio ;
    @Field(value = "USB")
    private String USB ;
    @Field(value = "Sensors")
    private String Sensors ;
    @Field(value = "Charging")
    private String Charging ;
    @Field(value = "Colors")
    private String Colors ;
    @Field(value = "Models")
    private String Models ;
    @Field(value = "SAR")
    private String SAR ;
    @Field(value = "SAR EU")
    private String SAR_EU ;
    @Field(value = "Price")
    private String Price ;
    @Field(value = "Performance")
    private String Performance ;
    @Field(value = "Display")
    private String Display ;
    @Field(value = "Camera")
    private String Camera ;
    @Field(value = "Battery life")
    private String Battery_life ;

    public DeviceDetail() {
    }

    public DeviceDetail(ObjectId oid, String name, String technology, String bands_2G, String bands_3G, String bands_4G,
                        String bands_5G, String speed, String announced, String status, String dimensions, String weight,
                        String build, String SIM, String type, String size, String resolution, String protection,
                        String OS, String chipset, String CPU, String GPU, String card_slot, String internal,
                        String triple, String features, String video, String single, String loudspeaker,
                        String jack_3_5mm, String WLAN, String bluetooth, String positioning, String NFC, String radio,
                        String USB, String sensors, String charging, String colors, String models, String SAR,
                        String SAR_EU, String price, String performance, String display, String camera,
                        String battery_life) {
        Oid = oid;
        name = name;
        Technology = technology;
        Bands_2G = bands_2G;
        Bands_3G = bands_3G;
        Bands_4G = bands_4G;
        Bands_5G = bands_5G;
        Speed = speed;
        Announced = announced;
        Status = status;
        Dimensions = dimensions;
        Weight = weight;
        Build = build;
        this.SIM = SIM;
        Type = type;
        Size = size;
        Resolution = resolution;
        Protection = protection;
        this.OS = OS;
        Chipset = chipset;
        this.CPU = CPU;
        this.GPU = GPU;
        Card_slot = card_slot;
        Internal = internal;
        Triple = triple;
        Features = features;
        Video = video;
        Single = single;
        Loudspeaker = loudspeaker;
        this.jack_3_5mm = jack_3_5mm;
        this.WLAN = WLAN;
        Bluetooth = bluetooth;
        Positioning = positioning;
        this.NFC = NFC;
        Radio = radio;
        this.USB = USB;
        Sensors = sensors;
        Charging = charging;
        Colors = colors;
        Models = models;
        this.SAR = SAR;
        this.SAR_EU = SAR_EU;
        Price = price;
        Performance = performance;
        Display = display;
        Camera = camera;
        Battery_life = battery_life;
    }

    public ObjectId getOid() {
        return Oid;
    }

    public void setOid(ObjectId oid) {
        Oid = oid;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        name = name;
    }

    public String getTechnology() {
        return Technology;
    }

    public void setTechnology(String technology) {
        Technology = technology;
    }

    public String getBands_2G() {
        return Bands_2G;
    }

    public void setBands_2G(String bands_2G) {
        Bands_2G = bands_2G;
    }

    public String getBands_3G() {
        return Bands_3G;
    }

    public void setBands_3G(String bands_3G) {
        Bands_3G = bands_3G;
    }

    public String getBands_4G() {
        return Bands_4G;
    }

    public void setBands_4G(String bands_4G) {
        Bands_4G = bands_4G;
    }

    public String getBands_5G() {
        return Bands_5G;
    }

    public void setBands_5G(String bands_5G) {
        Bands_5G = bands_5G;
    }

    public String getSpeed() {
        return Speed;
    }

    public void setSpeed(String speed) {
        Speed = speed;
    }

    public String getAnnounced() {
        return Announced;
    }

    public void setAnnounced(String announced) {
        Announced = announced;
    }

    public String getStatus() {
        return Status;
    }

    public void setStatus(String status) {
        Status = status;
    }

    public String getDimensions() {
        return Dimensions;
    }

    public void setDimensions(String dimensions) {
        Dimensions = dimensions;
    }

    public String getWeight() {
        return Weight;
    }

    public void setWeight(String weight) {
        Weight = weight;
    }

    public String getBuild() {
        return Build;
    }

    public void setBuild(String build) {
        Build = build;
    }

    public String getSIM() {
        return SIM;
    }

    public void setSIM(String SIM) {
        this.SIM = SIM;
    }

    public String getType() {
        return Type;
    }

    public void setType(String type) {
        Type = type;
    }

    public String getSize() {
        return Size;
    }

    public void setSize(String size) {
        Size = size;
    }

    public String getResolution() {
        return Resolution;
    }

    public void setResolution(String resolution) {
        Resolution = resolution;
    }

    public String getProtection() {
        return Protection;
    }

    public void setProtection(String protection) {
        Protection = protection;
    }

    public String getOS() {
        return OS;
    }

    public void setOS(String OS) {
        this.OS = OS;
    }

    public String getChipset() {
        return Chipset;
    }

    public void setChipset(String chipset) {
        Chipset = chipset;
    }

    public String getCPU() {
        return CPU;
    }

    public void setCPU(String CPU) {
        this.CPU = CPU;
    }

    public String getGPU() {
        return GPU;
    }

    public void setGPU(String GPU) {
        this.GPU = GPU;
    }

    public String getCard_slot() {
        return Card_slot;
    }

    public void setCard_slot(String card_slot) {
        Card_slot = card_slot;
    }

    public String getInternal() {
        return Internal;
    }

    public void setInternal(String internal) {
        Internal = internal;
    }

    public String getTriple() {
        return Triple;
    }

    public void setTriple(String triple) {
        Triple = triple;
    }

    public String getFeatures() {
        return Features;
    }

    public void setFeatures(String features) {
        Features = features;
    }

    public String getVideo() {
        return Video;
    }

    public void setVideo(String video) {
        Video = video;
    }

    public String getSingle() {
        return Single;
    }

    public void setSingle(String single) {
        Single = single;
    }

    public String getLoudspeaker() {
        return Loudspeaker;
    }

    public void setLoudspeaker(String loudspeaker) {
        Loudspeaker = loudspeaker;
    }

    public String getJack_3_5mm() {
        return jack_3_5mm;
    }

    public void setJack_3_5mm(String jack_3_5mm) {
        this.jack_3_5mm = jack_3_5mm;
    }

    public String getWLAN() {
        return WLAN;
    }

    public void setWLAN(String WLAN) {
        this.WLAN = WLAN;
    }

    public String getBluetooth() {
        return Bluetooth;
    }

    public void setBluetooth(String bluetooth) {
        Bluetooth = bluetooth;
    }

    public String getPositioning() {
        return Positioning;
    }

    public void setPositioning(String positioning) {
        Positioning = positioning;
    }

    public String getNFC() {
        return NFC;
    }

    public void setNFC(String NFC) {
        this.NFC = NFC;
    }

    public String getRadio() {
        return Radio;
    }

    public void setRadio(String radio) {
        Radio = radio;
    }

    public String getUSB() {
        return USB;
    }

    public void setUSB(String USB) {
        this.USB = USB;
    }

    public String getSensors() {
        return Sensors;
    }

    public void setSensors(String sensors) {
        Sensors = sensors;
    }

    public String getCharging() {
        return Charging;
    }

    public void setCharging(String charging) {
        Charging = charging;
    }

    public String getColors() {
        return Colors;
    }

    public void setColors(String colors) {
        Colors = colors;
    }

    public String getModels() {
        return Models;
    }

    public void setModels(String models) {
        Models = models;
    }

    public String getSAR() {
        return SAR;
    }

    public void setSAR(String SAR) {
        this.SAR = SAR;
    }

    public String getSAR_EU() {
        return SAR_EU;
    }

    public void setSAR_EU(String SAR_EU) {
        this.SAR_EU = SAR_EU;
    }

    public String getPrice() {
        return Price;
    }

    public void setPrice(String price) {
        Price = price;
    }

    public String getPerformance() {
        return Performance;
    }

    public void setPerformance(String performance) {
        Performance = performance;
    }

    public String getDisplay() {
        return Display;
    }

    public void setDisplay(String display) {
        Display = display;
    }

    public String getCamera() {
        return Camera;
    }

    public void setCamera(String camera) {
        Camera = camera;
    }

    public String getBattery_life() {
        return Battery_life;
    }

    public void setBattery_life(String battery_life) {
        Battery_life = battery_life;
    }
}
