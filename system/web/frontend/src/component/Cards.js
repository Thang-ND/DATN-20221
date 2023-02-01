import React from 'react';
import CardItem from './CardItem';
import './Cards.css';
function Card() {
    return (
        <div className='cards'>
            <h1>NEWS</h1>
            <div className='cards__container'>
                <div className='cards__wrapper'>
                    <ul className='cards__items'>
                        <CardItem
                            src='images/img-1.jpeg'
                            text='An exterior shot of the 14th-century Cathedral of Our Lady Antwerp '
                            lable='Adventure'
                            path='/services'
                        />
                        <CardItem
                            src='images/img-2.jpeg'
                            text='The manicured grounds of The Rubens House '
                            lable='Adventures'
                            path='/services'
                        />
                        <CardItem
                            src='images/img-3.jpeg'
                            text='Charlotte’s Uptown offers plentiful dining opportunities '
                            lable='Luxury'
                            path='/services'
                        />
                    </ul>
                    <ul className='cards__items'>
                        <CardItem
                            src='images/img-4.jpeg'
                            text='Why We Need The Fashion Act, According To State Senator Alessandra Biaggi'
                            lable='Fashion'
                            path='/services'
                        />
                        <CardItem
                            src='images/img-5.jpeg'
                            text='The Launch: January’s Hottest Fashion Drops'
                            lable='Fashion'
                            path='/services'
                        />
                    </ul>                    </div>

            </div>
        </div>
    )
}

export default Card
