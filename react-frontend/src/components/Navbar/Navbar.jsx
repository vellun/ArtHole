import React from "react";
import "./Navbar.css";

function Navbar() {
  return <div className="navbar">
    <a className="logo_a" href="/"><h1 className="logo">Art<span>Hole</span></h1></a>

    <div className="border">
      <ul><li className="nav-link"><a className="nav-link_a" href="/">Галерея</a></li>
          <li className="nav-link"><a className="nav-link_a" href="#">Чат-трансляции</a></li>
          <li className="nav-link"><a className="nav-link_a" href="#">Магазин <i className="fas fa-caret-down"></i></a>
          
          <div className="dropdown">
            <ul>
              <li className="dropdown-link"><a href="#">Персонажи</a></li>
              <li className="dropdown-link"><a href="#">Commisions</a></li>
              <li className="dropdown-link"><a href="#">Манекены(Ych)</a></li>
            </ul>
          </div>
          </li></ul>
    </div>

    <form>
    <div className="search">
      <input className="search-txt" type="text" name="" placeholder="Поиск"/>
        <a className="search-btn" href="#" type="submit"><i class="fa-solid fa-magnifying-glass"></i></a>
    </div>
    </form>

    <div className="sign-in-up">
    <ul>
      <li className="nav-link"><a className="nav-link_a" href="#">Вход</a></li>
      <li className="nav-link"><a className="nav-link_a" href="#">Регистрация</a></li>
    </ul>
    </div>

    

  </div>;
}

export default Navbar;
