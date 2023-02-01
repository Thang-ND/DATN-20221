import React from 'react';
import PropTypes from 'prop-types';
import "../../page/search/Product.css";


DeviceList.propTypes = {
    devices: PropTypes.array,
    productList:PropTypes.func
};

DeviceList.defaultProps = {
    devices: [],
    productList:null
};

function DeviceList(props) {
    const { devices,productList } = props;
    
    const hanldeClickOnDevice =(e,product,url)=>{
        //alert("hoang");
        e.preventDefault();
        if(productList){
            productList(product,url);
            //console.log(product);
        }
       
        
        //console.log(product);
    }
    return (
        <div className='container'>
            <div className='row'>
                {devices.map(device => (
                    
                        <div className='col-4 card_device 'data-category={device.status==0?'New':'Old'}>
                            <div key={device.id} style={{ textDecoration: 'none' }} onClick={(e)=>hanldeClickOnDevice(e,device.list_id,device.url)} >
                                <div className="product row justify-content-md-center">
                                    <div className="productItem col col-lg-4">
                                        <div className="img-container">
                                            <img className="imgUNcover" src='/images/iphone-14-pro-pro-max.jpeg' />
                                        </div>

                                        <div className="description col col-lg-6">
                                            <h3 >{device.name.toLowerCase()}</h3><br />
                                            <span><b>Ram: </b>{device.ram}</span><br />
                                            <span><b>Rom: </b>{device.rom}</span><br />
                                            <span><b>Color: </b>{device.color.toLowerCase()}</span><br />
                                            <p><b>Price: </b>{parseFloat(device.price).toLocaleString('vi', { style: 'currency', currency: 'VND' })}</p><br />
                                        </div>
                                        <div className="description col col-lg-2">
                                            {device.list_id && <span> Stores: {device.list_id.length}</span>}
                                            {device.store && <span > Stores: {device.store}</span>}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                ))};
            </div>
        </div>
    );
}

export default DeviceList;