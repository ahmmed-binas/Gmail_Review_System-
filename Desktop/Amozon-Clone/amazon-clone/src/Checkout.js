import React from 'react';
import './Checkout.css'; 
import Subtotal from './Subtotal';
import Basketproducts from './Basketproducts'; 
import { useStateValue } from './Stateprovider';
import ProductGuidesSection from './ProductGuidesSection';

function Checkout() {
  const [{ basket }] = useStateValue();
  const totalPrice = basket.reduce((total, item) => total + Number(item.price), 0);

  return (
    <> <div className='checkout'>
      <div className='checkout-left'>
        <div className='checkout-title'>
          <h2>Shopping Cart</h2>
        </div>
        <div className='checkout-price'>
          <p>Price</p>
        </div>
        <hr />
        {basket.length === 0 && (
          <div>
            <hr />
            <p className='empty-cart'>Your Amazon cart is empty</p>
          </div>
        )}
        <div className='basket-products'>
          {basket.map(item => (
            <Basketproducts
              key={item.id}
              instock={item.instock}
              title={item.title}
              img={item.img}
              price={item.price}
            />
          ))}
        </div>
        <div >
          <hr style={{marginTop:"19px"}}/>
          <p className="subtotal-left">Subtotal ({basket.length} items): <span className="subtotal-price">${totalPrice.toFixed(2)}</span></p>
        </div>
      </div>
      <div className='checkout-right'>
        <Subtotal />
      </div>
        </div>    

<div className='last-element'>
<ProductGuidesSection/> 
</div></>
  );
}

export default Checkout;
