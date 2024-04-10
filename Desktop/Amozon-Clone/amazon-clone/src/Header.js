import React from 'react';
import './Header.css';
import ShoppingCartImage from "./Media/shopping-cart-logo1.jpg";
import SearchIcon from '@mui/icons-material/Search';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import { Link } from 'react-router-dom';
import { useStateValue } from './Stateprovider';

function Header() {
  const [{basket}, dispatch] = useStateValue();
  return (
    <div className='header'>
      <Link to="/">
        <img className='header-logo' src={ShoppingCartImage} alt="Shopping Cart" />
      </Link>
      <div className='header-search'>
        <input />
        <SearchIcon className='header-searchicon'/>
      </div>

      <div className='header-nav'></div>

      <div className='header-option'>
        <span className='header-option-one'>Hello User</span>
        <span className='header-option-one'>Sign In</span>
      </div>

      <div className='header-option'>
        <span className='header-option-two'>Return</span>
        <span className='header-option-two'>& Orders</span>
      </div>

      <div className='header-option'>
        <span className='header-option-three'>Your</span>
        <span className='header-option-three'>Prime</span>
      </div>
     
      <Link to='/checkout'>
        <div className='header-optionbasket'>
        <span className='header-basketcount'>{basket?.length}</span>
          <ShoppingCartIcon/>
        </div>
      </Link>
    </div>
  );
}

export default Header;
