
import React, { Component } from 'react';
import axios from 'axios';
import { useState, useEffect } from 'react';
import './content.module.css';
export default function TableContent() {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    LoadUser();
  }, []);
  const LoadUser = async () => {
    const result = await axios.get("http://localhost:8080/product");
    setUsers(result.data);
  }
  
  return (
    
    <div className="container">
      <div className="review-header">
        <div className="row header-name">
            <h1 style={{backgroundColor: "lightblue"}}>Iphone 14PRo max</h1>
        </div>
        <div className="row">
          <div class="col">
            1 of 3
          </div>
          <div className="col-6">
            2 of 3 (wider)
          </div>
          <div className="col">
            3 of 3
          </div>
        </div>
      </div>
      <table className="table table-hover table-dark">
        <thead>
          <tr>
            <th scope="col">Id</th>
            <th scope="col">Name</th>
            <th scope="col">Ram</th>
            <th scope="col">Rom</th>
            <th scope="col">Color</th>
            <th scope="col">Price</th>
          </tr>
        </thead>
        <tbody>
          {
            users.map((product, index) => (
              <tr>
                <th scope="row" key={index}>{index + 1}</th>
                <td>{product.name}</td>
                <td>{product.ram}</td>
                <td>{product.rom}</td>
                <td>{product.color}</td>
                <td>{product.price}vnd</td>
              </tr>
            ))
          }


        </tbody>
      </table>
    </div>

  )

}
