import React from "react";
import Search from "../../page/search/Search";
import Dashboard from "../mongodbChart/Dashboard";
import Home from "../../page/Home"
import Products from "../../page/search/ProductSearch";
import Footer from "../Footer";
import Flactuations from "../../page/Flactuations";
import Services from "../../page/Services";
import Card from "../Cards";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import SpecificDevice from "../../page/SpecificDevice";


export default function Navigation() {
    return (
        <Router>
        
            <Route exact path="/SpecificDevive/:list_id">
                <SpecificDevice/>  
                <Footer/>             
            </Route> 

            <Route exact path="/" component={Home}>
                <Search/>                 
            </Route>

            <Route exact path="/searchProduct">
                <Products/>  
                <Footer/>             
            </Route>  

            <Route exact path="/services">
                <Services/>   
                <Card/>
                <Footer/>            
            </Route>  

            <Route exact path="/fluctuations">  
                <Dashboard/>
            </Route>        

        </Router>
    );
}
