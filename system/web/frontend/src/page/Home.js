import React from 'react';
import '../App.css';
import HeroSection from '../component/HeroSection';
import Cards from '../component/Cards';
import Footer from '../component/Footer';
import Products from '../../src/page/search/ProductSearch'

function Home(){
    return(
        <>
            <HeroSection/>
            <Cards/>
            <Footer/>
        </>
    );
}
export default Home;