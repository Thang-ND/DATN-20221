import React from 'react';
import PropTypes from 'prop-types';
import { useState } from 'react';
import { useRef } from 'react';

PostFilterForm.propTypes = {
    onsubmit:PropTypes.func,
};

PostFilterForm.defaulProps= {
    onsubmit:null,
}

function PostFilterForm(props) {
    const {onsubmit} = props;
    const [searchTerm,setSearchTerm]=useState('');
    const typingTimeoutRef = useRef(null);
//debounce
    function handSearchTermChange(e){
        const value = e.target.value;
        setSearchTerm(value);
        if(!onsubmit) return;
        if(typingTimeoutRef.current){
            clearTimeout(typingTimeoutRef.current);
        };
        typingTimeoutRef.current=setTimeout(()=>{
            const formValues = {
                searchTerm: value,
            };
            onsubmit(formValues);
        },2000);
       
    }
    return (
      <form>
            <input
            type="text" id="name" placeholder="Enter name" 
            value={searchTerm}
            onChange={handSearchTermChange}
            />
            </form>
    );
}

export default PostFilterForm;