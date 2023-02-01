import './Dashboard.css';
import React, { Component }  from 'react';
import Chart from "./Chart";

const Dashboard = () => {
  
  return <div className="App">
    <h1 className="title">Charts</h1>
    <h2 className="title">Devices Dashboard with Filters</h2>
    
    <div className="charts">
      <Chart height={'600px'} width={'800px'}  chartId={'63abfd80-4545-4a82-888c-848d95c24d55'}/>
      <Chart height={'600px'} width={'800px'}  chartId={'63abfef1-2404-4b50-8714-c77500a27885'}/>
    </div>
  </div>
};

export default Dashboard;
 