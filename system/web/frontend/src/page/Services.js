import React from 'react';
import "../../node_modules/bootstrap/dist/css/bootstrap.min.css";
import { MdPhoneIphone } from "react-icons/md";
import {RiCalendarEventLine} from "react-icons/ri";
import {TbLayersDifference} from "react-icons/tb"; 
import  {BiMicrochip} from "react-icons/bi";  
import {SiPixabay} from "react-icons/si"; 
import {BsCameraFill} from "react-icons/bs"; 
import {GiCpu} from "react-icons/gi"; 
import {BsBatteryCharging} from "react-icons/bs"; 
export default function Services() {
  return (<div className="main main-review right l-box col ">
    <div className="review-header">
      <div className="article-info">
        <div className="article-info-line page-specs light border-bottom">
          <div className="blur review-background"></div>
          <h1 className="specs-phone-name-title" data-spec="modelname">Apple iPad mini 3</h1>
        </div>
        <div className="center-stage container row">
          <div className="specs-photo-main col-md-3">
            <a href=""><img class="img-fluid" alt="Apple iPad mini 3
              MORE PICTURES" src='/images/iphone-14-pro-pro-max.jpeg' /></a>
          </div>
          <div className='product-container col-md-9'>
            <div className='product-detail row'>
              <span><RiCalendarEventLine/> Released 2014, October</span><br></br>
              <span><MdPhoneIphone/>331g (Wi-Fi) / 341g (3G/LTE), 7.5mm thickness</span><br></br>
              <span><TbLayersDifference/>iOS 8.1, up to iPadOS 12.5.6</span><br></br>
              <span><BiMicrochip/>16GB/64GB/128GB storage, no card slot</span>
            </div>
            <div className='row'>
              <div className='col-md'>
                <span><SiPixabay/><br/>7.9" 1536x2048 pixels</span>
              </div>
              <div className='col-md'>
                <span><BsCameraFill/><br/>5MP 1080p</span>
              </div>
              <div className='col-md'>
                <span><GiCpu/><br/>1GB RAM Apple A7</span>
              </div>
              <div className='col-md'>
                <span><BsBatteryCharging/><br/>6470mAh Li-Po</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div id="specs-list">
    <table className='table table-dark '>
        <tbody><tr scope='row' >
          <th scope='col'>NetWork</th>
          <td scope='col' ><a href="">Technology</a></td>
          <td scope='col' >GSM / CDMA / HSPA / EVDO / LTE</td>
        </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr scope='row'>
          <th rowspan='2'>Launch</th>
          <td scope='col'><a href="">Announced</a></td>
          <td scope='col'>2014, October. Released 2014, October</td>
        </tr>
          <tr scope='row'>
            <td scope='col'><a href="">Status</a></td>
            <td scope='col'>Discontinued</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="6" scope="row">Body</th>
          <td className="col"><a href="">Dimensions</a></td>
          <td className="col" data-spec="dimensions">200 x 134.7 x 7.5 mm (7.87 x 5.30 x 0.30 in)</td>
        </tr><tr>
          <td className="col"><a href="">Weight</a></td>
            <td className="col" data-spec="weight">331 g (Wi-Fi) / 341 g (3G/LTE) (11.68 oz)</td>
          </tr>
          <tr>
            <td className="col"><a href="">SIM</a></td>
            <td className="col" data-spec="sim">Nano-SIM and eSIM</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="5" scope="row">Display</th>
          <td className="col"><a href="">Type</a></td>
          <td className="col" data-spec="displaytype">IPS LCD</td>
        </tr>
          <tr>
          <td className="col"><a href="">Size</a></td>
            <td className="col" data-spec="displaysize">7.9 inches, 193.3 cm<sup>2</sup> (~71.7% screen-to-body ratio)</td>
          </tr>
          <tr>
            <td className="col"><a href="">Resolution</a></td>
            <td className="col" data-spec="displayresolution">1536 x 2048 pixels, 4:3 ratio (~324 ppi density)</td>
          </tr>
          <tr>
            <td className="col"><a href="">Protection</a></td>
            <td className="col" data-spec="displayprotection">Oleophobic coating</td>
          </tr>

        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="4" scope="row">Platform</th>
          <td className="col"><a href="">OS</a></td>
          <td className="col" data-spec="os">iOS 8.1, upgradable to iPadOS 12.5.6</td>
        </tr>
          <tr><td className="col"><a href="">Chipset</a></td>
            <td className="col" data-spec="chipset">Apple A7 (28 nm)</td>
          </tr>
          <tr><td className="col"><a href="">CPU</a></td>
            <td className="col" data-spec="cpu">Dual-core 1.3 GHz Cyclone (ARM v8-based)</td>
          </tr>
          <tr><td className="col"><a href="">GPU</a></td>
            <td className="col" data-spec="gpu">PowerVR G6430 (quad-core graphics)</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="5" scope="row">Memory</th>
          <td className="col"><a href="">Card slot</a></td>
          <td className="col" data-spec="memoryslot">No</td></tr>
          <tr>
            <td className="col"><a href="">Internal</a></td>
            <td className="col" data-spec="internalmemory">16GB 1GB RAM, 64GB 1GB RAM, 128GB 1GB RAM</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="4" scope="row" className="small-line-height">Main Camera</th>
          <td className="col"><a href="">Single</a></td>
          <td className="col" data-spec="cam1modules">5 MP, f/2.4, 32mm (standard), AF</td>
        </tr>
          <tr>
            <td className="col"><a href="">Features</a></td>
            <td className="col" data-spec="cam1features">HDR</td>
          </tr>
          <tr>
            <td className="col"><a href="">Video</a></td>
            <td className="col" data-spec="cam1video">1080p@30fps</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="4" scope="row" className="small-line-height">Selfie camera</th>
          <td className="col"><a href="">Single</a></td>
          <td className="col" data-spec="cam2modules">1.2 MP</td>
        </tr>
          <tr>
            <td className="col"><a href="">Features</a></td>
            <td className="col" data-spec="cam2features">face detection, FaceTime over Wi-Fi or Cellular</td>
          </tr>
          <tr>
            <td className="col"><a href="">Video</a></td>
            <td className="col" data-spec="cam2video">720p@30fps</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="3" scope="row">Sound</th>
          <td className="col"><a href="">Loudspeaker</a> </td>
          <td className="col">Yes, with stereo speakers</td>
        </tr>
          <tr>
            <td className="col"><a href="">3.5mm jack</a> </td>
            <td className="col">Yes</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="9" scope="row">Comms</th>
          <td className="col"><a href="">WLAN</a></td>
          <td className="col" data-spec="wlan">Wi-Fi 802.11 a/b/g/n, dual-band</td>
        </tr>
          <tr>
            <td className="col"><a href="">Bluetooth</a></td>
            <td className="col" data-spec="bluetooth">4.0, A2DP, EDR</td>
          </tr>
          <tr>
            <td className="col"><a href="">Positioning</a></td>
            <td className="col" data-spec="gps">GPS, GLONASS</td>
          </tr>
          <tr>
            <td className="col"><a href="">NFC</a></td>
            <td className="col" data-spec="nfc">No</td>
          </tr>
          <tr>
            <td className="col"><a href="">Radio</a></td>
            <td className="col" data-spec="radio">No</td>
          </tr>
          <tr>
            <td className="col"><a href="">USB</a></td>
            <td className="col" data-spec="usb">Lightning, USB 2.0</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="9" scope="row">Features</th>
          <td className="col"><a href="">Sensors</a></td>
          <td className="col" data-spec="sensors">Fingerprint (front-mounted), accelerometer, gyro, compass</td>
        </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="7" scope="row">Battery</th>
          <td className="col"><a href="">Type</a></td>
          <td className="col" data-spec="batdescription1">Li-Po 6470 mAh, non-removable (24.3 Wh)</td>
        </tr>
          <tr>
            <td className="col"><a href="">Talk time</a></td>
            <td className="col" data-spec="battalktime1">Up to 10 h (multimedia)</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="6" scope="row">Misc</th>
          <td className="col"><a href="">Colors</a></td>
          <td className="col" data-spec="colors">Space Gray/Black, Silver/White, Gold</td>
        </tr>
          <tr>
            <td className="col"><a href="">Models</a></td>
            <td className="col" data-spec="models">A1599, A1600, iPad4,7, iPad4,8, iPad4,9</td>
          </tr>
          <tr>
            <td className="col"><a href="">Price</a></td>
            <td className="col" data-spec="price">About 400 EUR</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="5" scope="row">Tests</th>
          <td className="col"><a href="">Performance</a></td>
          <td className="col" data-spec="tbench">
            Basemark X: 14781</td>
        </tr><tr>
            <td className="col"><a href="">Display</a></td>
            <td className="col">
              <a className="noUnd" href="">Contrast ratio: 812 (nominal)</a></td>
          </tr><tr>
            <td className="col"><a href="">Camera</a></td>
            <td className="col">
              <a className="noUnd" href="">Photo</a> / <a className="noUnd" href="">Video</a></td>
          </tr><tr>
            <td className="col"><a href="">Loudspeaker</a></td>
            <td className="col">
              <a className="noUnd" href="">Voice 65dB / Noise 63dB / Ring 70dB</a>
            </td>
          </tr><tr>
            <td className="col"><a href="">Audio quality</a></td>
            <td className="col">
              <a className="noUnd" href="">Noise -93.7dB / Crosstalk -85.2dB</a></td>
          </tr><tr>
          </tr></tbody></table>
    </div>
  </div>
  )
}