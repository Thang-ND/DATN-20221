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
import PropTypes from 'prop-types';
Services.propTypes = {
  detailDevice: PropTypes.array,
};

Services.defaultProps = {
  detailDevice: [],
};
export default function Services(props) {
  const {detailDevice} = props;
  return (
    <div className='container'>
   
      
  <div className="main main-review right l-box col ">
   
    <div className="review-header">
      <div className="article-info">
        <div className="article-info-line page-specs light border-bottom">
          <div className="blur review-background"></div>
          <h1 style={{color:'white'}}className="specs-phone-name-title" data-spec="modelname">{detailDevice.name}</h1>
        </div>
        <div className="center-stage container row">
          <div className="specs-photo-main col-md-3">
            <a ><img class="img-fluid" alt="Apple iPad mini 3
              MORE PICTURES" src='/images/iphone-14-pro-pro-max.jpeg' /></a>
          </div>
          <div className='product-container col-md-9'>
            <div className='product-detail row' style={{color:'white'}}>
              <span  style={{color:'white'}}><RiCalendarEventLine/> {detailDevice.status}</span><br></br>
              <span style={{color:'white'}}><MdPhoneIphone/>331g (Wi-Fi) / 341g (3G/LTE), 7.5mm thickness</span><br></br>
              <span style={{color:'white'}}><TbLayersDifference/>iOS 8.1, up to iPadOS 12.5.6</span><br></br>
              <span style={{color:'white'}}><BiMicrochip/>16GB/64GB/128GB storage, no card slot</span>
            </div>
            <div className='row' style={{color:'white'}}>
              <div className='col-md' >
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
          <td scope='col' ><a >Technology</a></td>
          <td scope='col' >{detailDevice.technology}</td>
        </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr scope='row'>
          <th rowspan='2'>Launch</th>
          <td scope='col'><a >Announced</a></td>
          <td scope='col'>{detailDevice.announced}</td>
        </tr>
          <tr scope='row'>
            <td scope='col'><a >Status</a></td>
            <td scope='col'>{detailDevice.status}</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="6" scope="row">Body</th>
          <td className="col"><a >Dimensions</a></td>
          <td className="col" data-spec="dimensions">{detailDevice.dimemsions}</td>
        </tr><tr>
          <td className="col"><a >Weight</a></td>
            <td className="col" data-spec="weight">{detailDevice.weight}</td>
          </tr>
          <tr>
            <td className="col"><a >SIM</a></td>
            <td className="col" data-spec="sim">{detailDevice.sim}</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="5" scope="row">Display</th>
          <td className="col"><a >Type</a></td>
          <td className="col" data-spec="displaytype">{detailDevice.type}</td>
        </tr>
          <tr>
          <td className="col"><a >Size</a></td>
            <td className="col" data-spec="displaysize">{detailDevice.size}</td>
          </tr>
          <tr>
            <td className="col"><a >Resolution</a></td>
            <td className="col" data-spec="displayresolution">{detailDevice.resolution}</td>
          </tr>
          <tr>
            <td className="col"><a >Protection</a></td>
            <td className="col" data-spec="displayprotection">{detailDevice.protection}</td>
          </tr>

        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="4" scope="row">Platform</th>
          <td className="col"><a >OS</a></td>
          <td className="col" data-spec="os">{detailDevice.os}</td>
        </tr>
          <tr><td className="col"><a >Chipset</a></td>
            <td className="col" data-spec="chipset">{detailDevice.chipset}</td>
          </tr>
          <tr><td className="col"><a >CPU</a></td>
            <td className="col" data-spec="cpu">{detailDevice.cpu}</td>
          </tr>
          <tr><td className="col"><a >GPU</a></td>
            <td className="col" data-spec="gpu">{detailDevice.gpu}</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="5" scope="row">Memory</th>
          <td className="col"><a >Card slot</a></td>
          <td className="col" data-spec="memoryslot">{detailDevice.card_slot}</td></tr>
          <tr>
            <td className="col"><a >Internal</a></td>
            <td className="col" data-spec="internalmemory">{detailDevice.internal}</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="4" scope="row" className="small-line-height">Main Camera</th>
          <td className="col"><a >Single</a></td>
          <td className="col" data-spec="cam1modules">{detailDevice.single}</td>
        </tr>
          <tr>
            <td className="col"><a >Features</a></td>
            <td className="col" data-spec="cam1features">{detailDevice.features}</td>
          </tr>
          <tr>
            <td className="col"><a >Video</a></td>
            <td className="col" data-spec="cam1video">{detailDevice.video}</td>
          </tr>
        </tbody></table>
      
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="3" scope="row">Sound</th>
          <td className="col"><a >Loudspeaker</a> </td>
          <td className="col">{detailDevice.loudspeaker}</td>
        </tr>
          <tr>
            <td className="col"><a >3.5mm jack</a> </td>
            <td className="col">{detailDevice.jack_3_5mm}</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="9" scope="row">Comms</th>
          <td className="col"><a >WLAN</a></td>
          <td className="col" data-spec="wlan">{detailDevice.wlan}</td>
        </tr>
          <tr>
            <td className="col"><a >Bluetooth</a></td>
            <td className="col" data-spec="bluetooth">{detailDevice.bluetooth}</td>
          </tr>
          <tr>
            <td className="col"><a >Positioning</a></td>
            <td className="col" data-spec="gps">{detailDevice.positioning}</td>
          </tr>
          <tr>
            <td className="col"><a >NFC</a></td>
            <td className="col" data-spec="nfc">{detailDevice.nfc}</td>
          </tr>
          <tr>
            <td className="col"><a >Radio</a></td>
            <td className="col" data-spec="radio">{detailDevice.radio}</td>
          </tr>
          <tr>
            <td className="col"><a >USB</a></td>
            <td className="col" data-spec="usb">{detailDevice.usb}</td>
          </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="9" scope="row">Features</th>
          <td className="col"><a >Sensors</a></td>
          <td className="col" data-spec="sensors">{detailDevice.sensors}</td>
        </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="7" scope="row">Battery</th>
          <td className="col"><a >Type</a></td>
          <td className="col" data-spec="batdescription1">{detailDevice.type}</td>
        </tr>
        </tbody></table>
      <table className='table table-dark'>
        <tbody><tr>
          <th rowspan="6" scope="row">Misc</th>
          <td className="col"><a >Colors</a></td>
          <td className="col" data-spec="colors">{detailDevice.colors}</td>
        </tr>
          <tr>
            <td className="col"><a >Models</a></td>
            <td className="col" data-spec="models">{detailDevice.models}</td>
          </tr>
          
        </tbody></table>
      
    </div>
  </div>;
  </div>
  )
}