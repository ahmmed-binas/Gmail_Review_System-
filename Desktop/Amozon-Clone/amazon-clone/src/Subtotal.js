import React from 'react';
import './Subtotal.css';
import CurrencyFormat from 'react-currency-format';
import { useStateValue } from './Stateprovider';

function Subtotal() {
  const [{ basket }] = useStateValue();


  const totalPrice = basket.reduce((total, item) => total + Number(item.price), 0);

  return (
    <div className="subtotal">
      <CurrencyFormat
        renderText={(value) => (
          <>
            <p>
           <span className='subtotal-title'>  Subtotal</span> ({basket.length} items): <strong>{value}</strong>
            </p>
          </>
        )}
        decimalScale={2}
        value={totalPrice}
        displayType={'text'}
        thousandSeparator={true}
        prefix={'$'}
      />
      <button className='checkout-button'>Proceed to Checkout</button>
    </div>
  );
}

export default Subtotal;
