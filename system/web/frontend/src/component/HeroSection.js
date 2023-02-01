import React, { useEffect, useState } from 'react';
import axios from "axios";
import '../App.css';
import queryString from "query-string";
import './HeroSection.css';
import './Button.css'
import Pagination from '../component/Pagination/index'
import PostForm from './PostForm';
import DeviceList from './Device';


function HeroSection() {
  const [filters, setFilters] = useState({
    name: '',
    color: '',
    ram: '',
    rom: '',
    offset: 0,
    pageSize: 9,
  });
  const [urlStore,setUrlStore]=useState('');
  const [submit, setSubmit] = useState(false);
  
  const [device, setDevice] = useState({});
  const [pagination, setPagination] = useState({
    _page: 0,
    _limit: 9,
    _totalPost: 9,
  });

  function handlePageChange(newOffset) {
    setFilters({
      ...filters,
      offset: newOffset,
    })
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
        const requestUrl = `http://localhost:8080/api/devices/pagination?${paramsString}`;
        const response = await fetch(requestUrl);
        const responseJSON = await response.json();

        const { content, pageable } = responseJSON;
        
        //console.log(responseJSON);
        // setPagination({
        //   _page: pageable.pageNumber,
        //   _limit: pageable.offset,
        //   _totalPost: pagination._totalPost,
        // });
        setDevice(responseJSON);

      } catch (err) {
        console.log(err);
      }
    };
    fetchPostList();
  }, [filters]);




  const AddPost = (post) => {
    setDevice({});
    setPagination({});
    setSubmit(false);
    
    axios.
      all([axios.get(`http://localhost:8080/api/devices/pagination?name=${post.name}&color=${post.color}&ram=${post.ram}&rom=${post.rom}&offset=0&pageSize=9`), 
      axios.get(`http://localhost:8080/api/devices/phone/search?name=${post.name}&color=${post.color}&ram=${post.ram}&rom=${post.rom}`)])
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
            offset: 0,
            pageSize: 9,
          })

          setSubmit(true);
        })
      );

  };
  async function SpecificDeviceAdd(list_id,url) {
   
    if(typeof(list_id)=='undefined'){
      window.location.href=urlStore;
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
      const response = await fetch(`http://localhost:8080/api/devices/specificDevice`, requestOptions);
      const responJSON = await response.json();
      setUrlStore(url);
    
      setDevice(responJSON);
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
        offset: 0,
        pageSize: responJSON.length,
      })
    
  }

  return (
    <div className='hero-container'>
      <h1>SEARCHING PRODUCTS</h1>
      <div class="typed-animation">
        <h1 class="typed-out">What are you waiting for?</h1>
      </div>

      <PostForm OnAdd={AddPost} />

      {submit && <DeviceList devices={device} productList={SpecificDeviceAdd} />}

      {submit && <Pagination pagination={pagination}
        onPageChange={handlePageChange}
      />}
    </div>
  );
}

export default HeroSection;