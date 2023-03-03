import React from 'react';
import PropTypes from 'prop-types';


Pagination.propTypes = {
    pagination:PropTypes.object.isRequired,
    onPageChange:PropTypes.func,
};

Pagination.defaultProps={
    onPageChange:null,
};

function Pagination(props) {
    const {pagination,onPageChange} = props;
    const {_page,_limit,_totalPost}= pagination;
    const totalPages = Math.ceil(_totalPost/_limit);

    function handlePageChange(newPage){
        if(onPageChange){
            onPageChange(newPage)
        }
    }
    return (
        <div>
            <button className='btn btn-block ' 
            style={{backgroundColor:"white"}}
            disabled={_page<=0}
            onClick={()=>handlePageChange(_page - 1)}
            >
                Prev
            </button>

            <button className='btn btn-block '
            style={{backgroundColor:"white"}}
            disabled={_page >= totalPages}
            onClick={()=>handlePageChange(_page + 1)}
            >
                Next
            </button>
        </div>
    );
}

export default Pagination;