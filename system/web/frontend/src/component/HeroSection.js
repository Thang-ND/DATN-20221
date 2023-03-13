import React, { useEffect, useState } from 'react';
import axios from "axios";
import '../App.css';
import queryString from "query-string";
import './HeroSection.css';
import './Button.css'
import Pagination from '../component/Pagination/index'
import PostForm from './PostForm';
import DeviceList from './Device';
import { PaginationSpecific } from './PaginationSpecific';
import { Button } from 'bootstrap';
import Services from '../page/Services';


function HeroSection() {
  const[checkViewDetail,setCheckViewDetail]=useState({
    check:false,
    nameProduct:''
  });
  const [currentPage,setCurrentPage] = useState(1);
  const [postsPerPage,setPostsPerPage] = useState(9);
  const [filters, setFilters] = useState({
    name: '',
    color: '',
    ram: '',
    rom: '',
    page: 0,
    pageSize: 9,
  });
  const [urlStore,setUrlStore]=useState('');
  const [checkPagination,setCheckPagination]=useState(true);
  const [submit, setSubmit] = useState(false);
  const [loading, setLoading] = useState(true);
  const [device, setDevice] = useState({});
  const [currentDevice, setcurrentDevice] = useState({});
  const [pagination, setPagination] = useState({
    _page: 0,
    _limit: 9,
    _totalPost: 9,
  });
  const[titleButtonDetail,setTitleButtonDetail] = useState('View More');
  const [openViewMore,setOpenViewMore]=useState(false);

  const [totalPostSPecific,setTotalPostSpecific]=useState(9);

  function handlePageChange(newPage) {
    setFilters({
      ...filters,
      page: newPage,
    })
  };
  //change page
const paginate = (pageNumber) =>{ 
  setcurrentDevice(device.slice(pageNumber*9-9,pageNumber*9));
  console.log(pageNumber);
};
  useEffect(() => {
    async function fetchPostList() {
      try {
        const asArray = Object.entries(filters);
        const filtered = asArray.filter(([key, value]) => value !== '');
        const new_params = Object.fromEntries(filtered);
        
        const paramsString = queryString.stringify(new_params);
        if(!paramsString.includes('name')){
          return;
        }

        const requestUrl = `https://thangnd-hust.fly.dev/api/devices/pagination?${paramsString}`;
        const response = await fetch(requestUrl);
        const responseJSON = await response.json();

        //const { content, pageable } = responseJSON;
        setCheckPagination(true);
        //console.log(responseJSON);
        setPagination(
       {   ...pagination,
          _page: filters.page,
          _limit: filters.pageSize,
        });
        setDevice(responseJSON);

      } catch (err) {
        console.log(err);
      }
    };
    fetchPostList();
  }, [filters]);



// s://white-leaf-1299.fly.dev
  const AddPost = (post) => {
    setDevice({});
    setPagination({});
    setOpenViewMore(false);
    setSubmit(false);
    setCheckViewDetail({nameProduct:filters.name,check:false});
    axios.
      all([axios.get(`https://thangnd-hust.fly.dev/api/devices/pagination?name=${post.name}&color=${post.color}&ram=${post.ram}&rom=${post.rom}&page=0&pageSize=9`), 
      axios.get(`https://thangnd-hust.fly.dev/api/devices/phone/search?name=${post.name}&color=${post.color}&ram=${post.ram}&rom=${post.rom}`)])
      .then(
        axios.spread((searchData, all) => {

          setPagination({
            _page: 0,
            _limit: 9,
            _totalPost: all.data.length,
          });
            
          setDevice(searchData.data);
          setFilters({
            name: post.name,
            color: post.color,
            ram: post.ram,
            rom: post.rom,
            page: 0,
            pageSize: 9,
          })

          setSubmit(true);
          setLoading(true);
        })
      );

  };
  
  async function SpecificDeviceAdd(list_id,url) {
    setCheckViewDetail({nameProduct:filters.name,check:true});
    if(typeof(list_id)=='undefined'){
      //window.location.href=urlStore;
      window.open(url, '_blank');
      return;
    }
      var myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");

      var raw = JSON.stringify(list_id);
    
      var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
      };
      const response = await fetch(`https://thangnd-hust.fly.dev/api/devices/specificDevice`, requestOptions);
      const responJSON = await response.json();
      setUrlStore(url);
    
      setDevice(responJSON);
      setcurrentDevice(responJSON.slice(0,9));
      setTotalPostSpecific(responJSON.length);
      setPagination({
        _page: 0,
        _limit: responJSON.length,
        _totalPost: responJSON.length,
      });
      setFilters({
        name: responJSON.name,
        color: responJSON.color,
        ram: responJSON.ram,
        rom: responJSON.rom,
        page: 0,
        pageSize: responJSON.length,
      })
      setCheckPagination(false);
    setLoading(false);
    setTitleButtonDetail('View More');
  }
  
  const [ok,setOK]=useState();
  async function ViewDetail(e,nameProduct){
    e.preventDefault();
    
    if(titleButtonDetail == "View More"){
      setTitleButtonDetail('Close Detail Device');
      setOpenViewMore(true);
      axios.get(`https://thangnd-hust.fly.dev/api/devices/detailDevice?name=${nameProduct}`)
      .then(res => {
        const product = res.data;
        //console.log(product);
        setOK(product[0]);
     
      })
      .catch(error => console.log(error));
    }else{
      setTitleButtonDetail('View More');
      setOpenViewMore(false);
    }
  
  }

  return (
    <div className='hero-container'>
      
      <h1>SEARCHING PRODUCTS</h1>
      <div class="typed-animation">
        <h1 class="typed-out">What are you waiting for?</h1>
      </div>

      <PostForm OnAdd={AddPost} />

      {checkPagination && submit && <DeviceList devices={device} productList={SpecificDeviceAdd} />}
      {!checkPagination && submit && <DeviceList devices={currentDevice} productList={SpecificDeviceAdd} />}
      {loading && submit && <Pagination pagination={pagination}
        onPageChange={handlePageChange}
      />}
      
      {!loading && <PaginationSpecific postPerPage={postsPerPage} totalPost={totalPostSPecific} paginate={paginate}></PaginationSpecific>}
      { checkViewDetail.check && <button class="view_detail"onClick={(e)=>ViewDetail(e,checkViewDetail.nameProduct)}>{titleButtonDetail}</button>}
      {openViewMore && <Services detailDevice={ok}/>}
    </div>
  );
  }

export default HeroSection;