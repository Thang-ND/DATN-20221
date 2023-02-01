package com.example.springbootmongodb.Model;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;
@Data
@Document("Product_Detail")
public class DeviceDetail {
    @Id
    private String _id ;
    private String $oid ;
    private String name ;
    private String Technology ;
    private String bands_2G  ;
    private String bands_3G  ;
    private String bands_4G  ;
    private String bands_5G  ;
    private String Speed ;
    private String Announced ;
    private String Status ;
    private String Dimensions ;
    private String Weight ;
    private String Build ;
    private String SIM ;
    private String Type ;
    private String Size ;
    private String Resolution ;
    private String Protection ;
    private String OS ;
    private String Chipset ;
    private String CPU ;
    private String GPU ;
    private String Card_slot ;
    private String Internal ;
    private String Triple ;
    private String Features ;
    private String Video ;
    private String Single ;
    private String Loudspeaker ;
    private String jack_3_5mm  ;
    private String WLAN ;
    private String Bluetooth ;
    private String Positioning ;
    private String NFC ;
    private String Radio ;
    private String USB ;
    private String Sensors ;
    private String Charging ;
    private String Colors ;
    private String Models ;
    private String SAR ;
    private String SAR_EU ;
    private String Price ;
    private String Performance ;
    private String Display ;
    private String Camera ;
    private String Battery_life ;

    public DeviceDetail() {
    }

    public DeviceDetail(String _id, String $oid, String name, String technology, String bands_2G, String bands_3G,
                        String bands_4G, String bands_5G, String speed, String announced, String status,
                        String dimensions, String weight, String build, String SIM, String type, String size,
                        String resolution, String protection, String OS, String chipset, String CPU, String GPU,
                        String card_slot, String internal, String triple, String features, String video, String single,
                        String loudspeaker, String jack_3_5mm, String WLAN, String bluetooth, String positioning,
                        String NFC, String radio, String USB, String sensors, String charging, String colors,
                        String models, String SAR, String SAR_EU, String price, String performance, String display,
                        String camera, String battery_life) {
        this._id = _id;
        this.$oid = $oid;
        this.name = name;
        Technology = technology;
        this.bands_2G = bands_2G;
        this.bands_3G = bands_3G;
        this.bands_4G = bands_4G;
        this.bands_5G = bands_5G;
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

    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }

    public String get$oid() {
        return $oid;
    }

    public void set$oid(String $oid) {
        this.$oid = $oid;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getTechnology() {
        return Technology;
    }

    public void setTechnology(String technology) {
        Technology = technology;
    }

    public String getBands_2G() {
        return bands_2G;
    }

    public void setBands_2G(String bands_2G) {
        this.bands_2G = bands_2G;
    }

    public String getBands_3G() {
        return bands_3G;
    }

    public void setBands_3G(String bands_3G) {
        this.bands_3G = bands_3G;
    }

    public String getBands_4G() {
        return bands_4G;
    }

    public void setBands_4G(String bands_4G) {
        this.bands_4G = bands_4G;
    }

    public String getBands_5G() {
        return bands_5G;
    }

    public void setBands_5G(String bands_5G) {
        this.bands_5G = bands_5G;
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
