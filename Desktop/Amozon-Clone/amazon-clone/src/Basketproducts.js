// Basketproducts.js
import React, { useState } from 'react';
import './Basketproducts.css';
import { useStateValue } from './Stateprovider';

function checkStock(instock) {
  return instock ? 'In stock' : 'Out of stock';
}

function getStockColor(instock) {
  return instock ? 'green' : 'red';
}

function Basketproducts({ id, instock, title, img, price, rating }) {
  const [quantity, setQuantity] = useState(1);
  const [{ basket }, dispatch] = useStateValue();

  const handleDeleteFromBasket = () => {
    dispatch({
      type: 'REMOVE_FROM_BASKET',
      id: id,
    });
  };

  return (
    <div className="basket-product">
      <img className="basket-product-img" src={img} alt="Product Item" />
      <div className='basket-product-info'>
        <p className='basket-product-title'>{title}</p>
        <p className='instock' style={{ color: getStockColor(instock) }}>{checkStock(instock)}</p>
        <p className='basket-product-price'>
          <strong>${price}</strong>
        </p>
        <div className="quantity-selector">
          <input
            type="number"
            value={quantity}
            min={1}
            max={100}
            onChange={(event) => setQuantity(parseInt(event.target.value))}
            className="quantity-input"
          />
          <span className="separator">|</span>
          <span className="remove-one" onClick={handleDeleteFromBasket}>Delete</span>
          <span className="separator">|</span>
          <span className="save-for-later">Save for Later</span>
          <span className="separator">|</span>
        </div>
      </div>
    </div>
  );
}

export default Basketproducts;
